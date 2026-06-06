#!/usr/bin/env python3
"""
Offline descriptive analysis for exported VR Embodied Learning sessions.

Developer: Xiala Dilimulati
Prototype status: undergraduate solo research prototype, 2025

Expected input:
    JSON files exported from results.html. Missing survey values and behavioral
    fields are allowed. The script does not perform inferential statistics.

Usage:
    python analysis.py exported_session.json
    python analysis.py data/*.json
    python analysis.py --plot data/*.json

When --plot is requested and matplotlib is available, a descriptive condition
summary is saved to assets/figures/descriptive-condition-summary.png.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


CONSTRUCTS = {
    "q1": "VR familiarity",
    "q2": "Baseline cognitive interest",
    "q3": "Spatial presence",
    "q4": "Body ownership illusion",
    "q5": "Agency",
    "q6": "Cognitive engagement",
    "q7": "Emotional engagement",
    "q8": "Perceived learning",
    "q9": "Embodied interaction",
}


def load_session(path: Path) -> dict[str, Any] | None:
    """Load one exported session, reporting readable errors without aborting."""
    try:
        with path.open(encoding="utf-8") as file:
            payload = json.load(file)
    except (OSError, json.JSONDecodeError) as error:
        print(f"[skip] {path}: {error}", file=sys.stderr)
        return None
    if not isinstance(payload, dict):
        print(f"[skip] {path}: top-level JSON value must be an object", file=sys.stderr)
        return None
    payload["_source_file"] = str(path)
    return payload


def numeric(value: Any) -> float | None:
    """Return a finite numeric value or None."""
    if isinstance(value, bool):
        return None
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if result == result and abs(result) != float("inf") else None


def event_elapsed(event: dict[str, Any]) -> float:
    """Read current or legacy elapsed-time fields."""
    return numeric(event.get("elapsed_time", event.get("elapsed"))) or 0.0


def event_card_id(event: dict[str, Any]) -> str | None:
    """Read current or legacy card identifier fields."""
    value = event.get("card_id", event.get("cardId"))
    return str(value) if value else None


def infer_condition(session: dict[str, Any]) -> str:
    """Infer condition from export metadata, survey, or event log."""
    survey = session.get("surveyData") or {}
    explicit = session.get("condition") or survey.get("condition")
    if explicit in {"embodied", "control"}:
        return explicit
    for event in session.get("behaviorLog") or []:
        if event.get("condition") in {"embodied", "control"}:
            return event["condition"]
    return "unspecified"


def summarize_session(session: dict[str, Any]) -> dict[str, Any]:
    """Extract descriptive survey and behavioral metrics from one session."""
    survey = session.get("surveyData") or {}
    progress = session.get("progressData") or {}
    events = session.get("behaviorLog") or []
    card_opens = [event_card_id(event) for event in events if event.get("type") == "card_open"]
    card_opens = [card_id for card_id in card_opens if card_id]
    elapsed_values = [event_elapsed(event) for event in events]
    ended = [event for event in events if event.get("type") == "session_end"]
    explicit_duration = numeric(ended[-1].get("session_duration")) if ended else None

    return {
        "source": session.get("_source_file", "unknown"),
        "condition": infer_condition(session),
        "survey": {key: numeric(survey.get(key)) for key in CONSTRUCTS if numeric(survey.get(key)) is not None},
        "unique_cards": len(progress) if isinstance(progress, dict) else len(set(card_opens)),
        "card_open_count": len(card_opens),
        "teleport_count": sum(event.get("type") == "teleport" for event in events),
        "event_count": len(events),
        "duration_seconds": explicit_duration if explicit_duration is not None else max(elapsed_values, default=0),
        "exploration_sequence": card_opens,
    }


def describe(values: Iterable[float]) -> str:
    """Format descriptive statistics while handling empty and single-value sets."""
    clean = list(values)
    if not clean:
        return "no values"
    mean = statistics.mean(clean)
    standard_deviation = statistics.stdev(clean) if len(clean) > 1 else 0.0
    return f"N={len(clean)}, mean={mean:.2f}, SD={standard_deviation:.2f}, range={min(clean):.2f}-{max(clean):.2f}"


def print_session(summary: dict[str, Any]) -> None:
    """Print one readable session summary."""
    print(f"\nSession: {summary['source']}")
    print(f"  Condition: {summary['condition']}")
    print(f"  Duration: {summary['duration_seconds']:.0f} seconds")
    print(f"  Unique cards visited: {summary['unique_cards']}")
    print(f"  Card-open events: {summary['card_open_count']}")
    print(f"  Teleportation events: {summary['teleport_count']}")
    sequence = " -> ".join(summary["exploration_sequence"]) or "none"
    print(f"  Exploration sequence: {sequence}")
    print("  Self-report values:")
    if not summary["survey"]:
        print("    no values")
    for key, value in summary["survey"].items():
        print(f"    {CONSTRUCTS[key]}: {value:g} / 7")


def print_condition_summary(summaries: list[dict[str, Any]]) -> None:
    """Print descriptive summaries grouped by condition."""
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for summary in summaries:
        groups[summary["condition"]].append(summary)

    print("\nCondition-level descriptive summary")
    print("This output is exploratory and does not establish statistical significance.")
    for condition, group in sorted(groups.items()):
        print(f"\n{condition} ({len(group)} session(s))")
        for metric in ["duration_seconds", "unique_cards", "card_open_count", "teleport_count", "event_count"]:
            print(f"  {metric.replace('_', ' ')}: {describe(item[metric] for item in group)}")
        for key, label in CONSTRUCTS.items():
            values = [item["survey"][key] for item in group if key in item["survey"]]
            if values:
                print(f"  {label}: {describe(values)}")
        sequences = Counter(tuple(item["exploration_sequence"]) for item in group if item["exploration_sequence"])
        if sequences:
            common, count = sequences.most_common(1)[0]
            print(f"  Most common exploration sequence ({count}): {' -> '.join(common)}")


def save_plot(summaries: list[dict[str, Any]]) -> None:
    """Optionally save a compact descriptive plot when matplotlib is available."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("\n[plot skipped] matplotlib is not installed. Descriptive text output is complete.")
        return

    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for summary in summaries:
        groups[summary["condition"]].append(summary)

    labels = sorted(groups)
    cards = [statistics.mean(item["unique_cards"] for item in groups[label]) for label in labels]
    duration = [statistics.mean(item["duration_seconds"] for item in groups[label]) for label in labels]

    figure, axes = plt.subplots(1, 2, figsize=(9, 4))
    axes[0].bar(labels, cards, color="#1d4ed8")
    axes[0].set_title("Mean unique cards visited")
    axes[0].set_ylim(0, 5)
    axes[1].bar(labels, duration, color="#555555")
    axes[1].set_title("Mean session duration")
    axes[1].set_ylabel("Seconds")
    figure.suptitle("Exploratory descriptive condition summary")
    figure.tight_layout()

    output = Path("assets/figures/descriptive-condition-summary.png")
    output.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output, dpi=160)
    plt.close(figure)
    print(f"\n[plot saved] {output}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Describe exported VR Embodied Learning JSON sessions.")
    parser.add_argument("files", nargs="+", type=Path, help="One or more exported JSON files")
    parser.add_argument("--plot", action="store_true", help="Save an optional descriptive plot")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    sessions = [session for path in args.files if (session := load_session(path)) is not None]
    if not sessions:
        print("No readable exported sessions were provided.", file=sys.stderr)
        return 1

    summaries = [summarize_session(session) for session in sessions]
    print("VR Embodied Learning Prototype: offline descriptive analysis")
    print("No inferential or validated-result claims are produced.")
    for summary in summaries:
        print_session(summary)
    print_condition_summary(summaries)
    if args.plot:
        save_plot(summaries)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
