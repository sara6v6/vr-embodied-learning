"""
analysis.py
VR Embodied Learning — Research Data Analysis
Reads exported JSON from results.html and produces descriptive statistics + plots.

Usage:
    python analysis.py data_experimental.json data_control.json
"""

import json
import sys
import os
import statistics
import datetime

# ── Optional: matplotlib for charts ──────────────────────────
try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("[Warning] matplotlib not installed. Run: pip install matplotlib")
    print("          Statistics will still print to terminal.\n")


# ══════════════════════════════════════════════════════════════
# 1. Load JSON data
# ══════════════════════════════════════════════════════════════

def load_json(filepath):
    """Load a single exported JSON file from results.html."""
    if not os.path.exists(filepath):
        print(f"[Error] File not found: {filepath}")
        sys.exit(1)
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def extract_survey_scores(data):
    """
    Extract post-survey scores (Q3–Q7) from exported JSON.
    Returns a dict: { 'q3': int, 'q4': int, ..., 'q7': int }
    """
    survey = data.get('surveyData', {})
    scores = {}
    for key in ['q3', 'q4', 'q5', 'q6', 'q7']:
        val = survey.get(key)
        if val is not None:
            scores[key] = int(val)
    return scores


def extract_behavior_stats(data):
    """
    Extract behavioral metrics from behavior log.
    Returns: cards_visited (int), session_duration_seconds (int)
    """
    log = data.get('behaviorLog', [])
    cards_visited = data.get('progressData', {})
    cards_count = len(cards_visited)

    # Calculate session duration from log
    start_time = None
    end_time = None
    for event in log:
        t = event.get('timestamp')
        if t:
            dt = datetime.datetime.fromisoformat(t)
            if start_time is None or dt < start_time:
                start_time = dt
            if end_time is None or dt > end_time:
                end_time = dt

    duration = 0
    if start_time and end_time:
        duration = int((end_time - start_time).total_seconds())

    return cards_count, duration


# ══════════════════════════════════════════════════════════════
# 2. Descriptive statistics
# ══════════════════════════════════════════════════════════════

SCALE_LABELS = {
    'q3': 'Spatial Presence (IPQ)',
    'q4': 'Body Ownership (BOI)',
    'q5': 'Cognitive Engagement (AEQ)',
    'q6': 'Emotional Engagement (AEQ)',
    'q7': 'Embodied Interaction',
}

# Subscale groupings
SUBSCALES = {
    'Presence':   ['q3', 'q4'],
    'Engagement': ['q5', 'q6', 'q7'],
}


def describe(scores_list, label=""):
    """Print descriptive stats for a list of numeric values."""
    if not scores_list:
        print(f"  {label}: No data")
        return {}
    n = len(scores_list)
    mean = statistics.mean(scores_list)
    sd = statistics.stdev(scores_list) if n > 1 else 0.0
    minimum = min(scores_list)
    maximum = max(scores_list)
    print(f"  {label}: M={mean:.2f}, SD={sd:.2f}, min={minimum}, max={maximum}, N={n}")
    return {'mean': mean, 'sd': sd, 'min': minimum, 'max': maximum, 'n': n}


def compute_subscale_mean(scores_dict, keys):
    """Average scores across a set of question keys."""
    vals = [scores_dict[k] for k in keys if k in scores_dict]
    return statistics.mean(vals) if vals else None


def analyze_group(label, filepaths):
    """
    Analyze one group (experimental or control).
    filepaths: list of JSON file paths (one per participant).
    Returns aggregated results dict.
    """
    print(f"\n{'='*52}")
    print(f"  GROUP: {label}  (N={len(filepaths)})")
    print(f"{'='*52}")

    all_scores = {k: [] for k in SCALE_LABELS}
    all_presence = []
    all_engagement = []
    all_cards = []
    all_durations = []

    for fp in filepaths:
        data = load_json(fp)
        scores = extract_survey_scores(data)
        cards, duration = extract_behavior_stats(data)

        for k in SCALE_LABELS:
            if k in scores:
                all_scores[k].append(scores[k])

        p_mean = compute_subscale_mean(scores, SUBSCALES['Presence'])
        e_mean = compute_subscale_mean(scores, SUBSCALES['Engagement'])
        if p_mean: all_presence.append(p_mean)
        if e_mean: all_engagement.append(e_mean)

        all_cards.append(cards)
        all_durations.append(duration)

    print("\n  Individual Scale Items (1–7):")
    item_stats = {}
    for k, lbl in SCALE_LABELS.items():
        item_stats[k] = describe(all_scores[k], lbl)

    print("\n  Subscale Composites:")
    presence_stat   = describe(all_presence,   "Presence composite   (Q3+Q4 avg)")
    engagement_stat = describe(all_engagement, "Engagement composite (Q5+Q6+Q7 avg)")

    print("\n  Behavioral Metrics:")
    describe(all_cards,     "Cards visited (0–5)")
    describe(all_durations, "Session duration (seconds)")

    return {
        'label': label,
        'item_stats': item_stats,
        'presence_mean': statistics.mean(all_presence) if all_presence else 0,
        'engagement_mean': statistics.mean(all_engagement) if all_engagement else 0,
        'all_scores': all_scores,
        'all_presence': all_presence,
        'all_engagement': all_engagement,
    }


# ══════════════════════════════════════════════════════════════
# 3. Charts
# ══════════════════════════════════════════════════════════════

COLORS = {
    'experimental': '#4ecdc4',
    'control':      '#ff6b6b',
}


def plot_item_comparison(exp_stats, ctrl_stats):
    """Bar chart: per-item mean scores, experimental vs control."""
    keys = list(SCALE_LABELS.keys())
    short_labels = ['Q3\nPresence', 'Q4\nBody Own.', 'Q5\nCog.Eng.', 'Q6\nEmo.Eng.', 'Q7\nEmbodied']

    exp_means  = [exp_stats['item_stats'].get(k, {}).get('mean', 0) for k in keys]
    ctrl_means = [ctrl_stats['item_stats'].get(k, {}).get('mean', 0) for k in keys]

    x = range(len(keys))
    width = 0.35

    fig, ax = plt.subplots(figsize=(9, 5))
    fig.patch.set_facecolor('#1a1a2e')
    ax.set_facecolor('#16213e')

    bars1 = ax.bar([i - width/2 for i in x], exp_means,  width, label='Experimental', color=COLORS['experimental'], alpha=0.85)
    bars2 = ax.bar([i + width/2 for i in x], ctrl_means, width, label='Control',      color=COLORS['control'],      alpha=0.85)

    ax.set_ylim(0, 7.5)
    ax.set_xticks(list(x))
    ax.set_xticklabels(short_labels, color='#e0e0e0', fontsize=9)
    ax.set_ylabel('Mean Score (1–7)', color='#e0e0e0')
    ax.set_title('Survey Item Scores: Experimental vs Control', color='white', fontsize=13, pad=12)
    ax.tick_params(colors='#a0aec0')
    ax.spines['bottom'].set_color('#2d3748')
    ax.spines['left'].set_color('#2d3748')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.label.set_color('#a0aec0')
    ax.legend(facecolor='#2d3748', labelcolor='white', framealpha=0.8)
    ax.axhline(4, color='#4a5568', linestyle='--', linewidth=0.8, label='Neutral (4)')

    # Value labels on bars
    for bar in bars1:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2, h + 0.1, f'{h:.1f}',
                    ha='center', va='bottom', color='#e0e0e0', fontsize=8)
    for bar in bars2:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2, h + 0.1, f'{h:.1f}',
                    ha='center', va='bottom', color='#e0e0e0', fontsize=8)

    plt.tight_layout()
    plt.savefig('chart_item_comparison.png', dpi=150, bbox_inches='tight')
    print("\n[Saved] chart_item_comparison.png")
    plt.show()


def plot_subscale_comparison(exp_stats, ctrl_stats):
    """Simple grouped bar: Presence composite vs Engagement composite."""
    labels = ['Presence\n(Q3+Q4)', 'Engagement\n(Q5+Q6+Q7)']
    exp_vals  = [exp_stats['presence_mean'],  exp_stats['engagement_mean']]
    ctrl_vals = [ctrl_stats['presence_mean'], ctrl_stats['engagement_mean']]

    x = [0, 1]
    width = 0.3

    fig, ax = plt.subplots(figsize=(6, 5))
    fig.patch.set_facecolor('#1a1a2e')
    ax.set_facecolor('#16213e')

    ax.bar([i - width/2 for i in x], exp_vals,  width, label='Experimental', color=COLORS['experimental'], alpha=0.85)
    ax.bar([i + width/2 for i in x], ctrl_vals, width, label='Control',      color=COLORS['control'],      alpha=0.85)

    ax.set_ylim(0, 7.5)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, color='#e0e0e0')
    ax.set_ylabel('Composite Mean (1–7)', color='#a0aec0')
    ax.set_title('Subscale Composites: Experimental vs Control', color='white', fontsize=12, pad=10)
    ax.tick_params(colors='#a0aec0')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#2d3748')
    ax.spines['left'].set_color('#2d3748')
    ax.axhline(4, color='#4a5568', linestyle='--', linewidth=0.8)
    ax.legend(facecolor='#2d3748', labelcolor='white', framealpha=0.8)

    plt.tight_layout()
    plt.savefig('chart_subscale_comparison.png', dpi=150, bbox_inches='tight')
    print("[Saved] chart_subscale_comparison.png")
    plt.show()


def plot_score_distribution(exp_stats, ctrl_stats):
    """Box plots: distribution of Presence and Engagement composites."""
    fig, axes = plt.subplots(1, 2, figsize=(8, 5))
    fig.patch.set_facecolor('#1a1a2e')

    pairs = [
        ('Presence Composite', exp_stats['all_presence'],   ctrl_stats['all_presence']),
        ('Engagement Composite', exp_stats['all_engagement'], ctrl_stats['all_engagement']),
    ]

    for ax, (title, exp_vals, ctrl_vals) in zip(axes, pairs):
        ax.set_facecolor('#16213e')
        data_to_plot = []
        tick_labels = []
        colors = []
        if exp_vals:
            data_to_plot.append(exp_vals)
            tick_labels.append('Experimental')
            colors.append(COLORS['experimental'])
        if ctrl_vals:
            data_to_plot.append(ctrl_vals)
            tick_labels.append('Control')
            colors.append(COLORS['control'])

        if data_to_plot:
            bp = ax.boxplot(data_to_plot, patch_artist=True, widths=0.4)
            for patch, color in zip(bp['boxes'], colors):
                patch.set_facecolor(color)
                patch.set_alpha(0.7)
            for element in ['whiskers', 'caps', 'medians']:
                for item in bp[element]:
                    item.set_color('white')
            for flier in bp['fliers']:
                flier.set_marker('o')
                flier.set_color('#a0aec0')

        ax.set_ylim(0, 7.5)
        ax.set_xticklabels(tick_labels, color='#e0e0e0', fontsize=9)
        ax.set_title(title, color='white', fontsize=10)
        ax.tick_params(colors='#a0aec0')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_color('#2d3748')
        ax.spines['left'].set_color('#2d3748')
        ax.yaxis.label.set_color('#a0aec0')

    fig.suptitle('Score Distributions by Condition', color='white', fontsize=13)
    plt.tight_layout()
    plt.savefig('chart_distributions.png', dpi=150, bbox_inches='tight')
    print("[Saved] chart_distributions.png")
    plt.show()


# ══════════════════════════════════════════════════════════════
# 4. Main
# ══════════════════════════════════════════════════════════════

def main():
    print("=" * 52)
    print("  VR Embodied Learning — Data Analysis")
    print("=" * 52)

    # Accept file arguments: experimental files first, then control
    # Example: python analysis.py exp1.json exp2.json -- ctrl1.json ctrl2.json
    # Simple mode: python analysis.py exp.json ctrl.json
    args = sys.argv[1:]

    if '--' in args:
        sep = args.index('--')
        exp_files  = args[:sep]
        ctrl_files = args[sep+1:]
    elif len(args) == 2:
        exp_files  = [args[0]]
        ctrl_files = [args[1]]
    elif len(args) == 1:
        # Single file mode: just analyze one file
        exp_files  = [args[0]]
        ctrl_files = []
    else:
        print("Usage:")
        print("  python analysis.py experimental.json control.json")
        print("  python analysis.py exp1.json exp2.json -- ctrl1.json ctrl2.json")
        print("  python analysis.py single_file.json")
        sys.exit(0)

    exp_results  = analyze_group("Experimental (Embodied Interaction)", exp_files)

    if ctrl_files:
        ctrl_results = analyze_group("Control (Text Reading Only)", ctrl_files)

        print("\n" + "="*52)
        print("  BETWEEN-GROUP COMPARISON")
        print("="*52)
        print(f"  Presence  — Experimental: {exp_results['presence_mean']:.2f}  |  Control: {ctrl_results['presence_mean']:.2f}  |  Δ={exp_results['presence_mean']-ctrl_results['presence_mean']:+.2f}")
        print(f"  Engagement — Experimental: {exp_results['engagement_mean']:.2f}  |  Control: {ctrl_results['engagement_mean']:.2f}  |  Δ={exp_results['engagement_mean']-ctrl_results['engagement_mean']:+.2f}")
        print("\n  Note: Formal significance testing (t-test) requires N≥10 per group.")
        print("        Current output is descriptive only.")

        if HAS_MATPLOTLIB:
            print("\n  Generating charts...")
            plot_item_comparison(exp_results, ctrl_results)
            plot_subscale_comparison(exp_results, ctrl_results)
            plot_score_distribution(exp_results, ctrl_results)
    else:
        print("\n  Single-group mode: no comparison chart generated.")
        if HAS_MATPLOTLIB and exp_results['all_scores']:
            # Just plot this group's item means
            keys = list(SCALE_LABELS.keys())
            means = [statistics.mean(exp_results['all_scores'][k]) if exp_results['all_scores'][k] else 0 for k in keys]
            fig, ax = plt.subplots(figsize=(8, 4))
            fig.patch.set_facecolor('#1a1a2e')
            ax.set_facecolor('#16213e')
            bars = ax.bar(range(len(keys)), means, color=COLORS['experimental'], alpha=0.85)
            ax.set_ylim(0, 7.5)
            ax.set_xticks(range(len(keys)))
            ax.set_xticklabels([SCALE_LABELS[k] for k in keys], rotation=15, ha='right', color='#e0e0e0', fontsize=8)
            ax.set_ylabel('Mean Score (1–7)', color='#a0aec0')
            ax.set_title('Survey Item Scores', color='white')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.axhline(4, color='#4a5568', linestyle='--', linewidth=0.8)
            ax.tick_params(colors='#a0aec0')
            plt.tight_layout()
            plt.savefig('chart_single_group.png', dpi=150, bbox_inches='tight')
            print("[Saved] chart_single_group.png")
            plt.show()

    print("\n  Analysis complete.")


if __name__ == '__main__':
    main()
