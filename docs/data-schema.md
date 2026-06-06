# Local Data Schema

All records are stored locally in the browser. No records are transmitted to a server.

## localStorage Keys

| Key | Purpose |
| --- | --- |
| `vr-selected-condition` | Current condition: `embodied` or `control` |
| `vr-survey-data` | Pre/post self-report instrument values, condition, and phase timestamps |
| `vr-learning-progress` | Unique cards visited in the embodied VR condition |
| `vr-behavior-log` | Behavioral interaction log for the embodied VR condition |
| `vr-learning-progress-control` | Unique cards visited in the control condition |
| `vr-behavior-log-control` | Behavioral interaction log for the control condition |

## Behavioral Event

New events use the following fields:

```json
{
  "type": "card_open",
  "condition": "embodied",
  "card_id": "card-1",
  "timestamp": "2025-01-01T00:00:00.000Z",
  "elapsed_time": 12,
  "user_action": "card_open"
}
```

Supported event types are `session_start`, `card_open`, `card_close`, `teleport`, and `session_end`. Teleport events may include a rounded `position`. Session-end events may include `session_duration` and `cards_visited`.

## Survey Values

| Field | Construct |
| --- | --- |
| `q1` | VR familiarity |
| `q2` | Baseline cognitive interest |
| `q3` | Spatial presence |
| `q4` | Body ownership illusion |
| `q5` | Agency |
| `q6` | Cognitive engagement |
| `q7` | Emotional engagement |
| `q8` | Perceived learning |
| `q9` | Embodied interaction |
| `condition` | Selected comparison condition |
| `pre_timestamp`, `post_timestamp` | Local ISO timestamps |

## Exported JSON

The results dashboard exports:

```json
{
  "schemaVersion": "1.0",
  "exportedAt": "ISO timestamp",
  "privacy": "Local browser storage only...",
  "condition": "embodied",
  "conditionLabel": "Embodied VR condition",
  "surveyData": {},
  "progressData": {},
  "behaviorLog": []
}
```

No participant identifier is generated. Exported files should remain anonymized before any analysis or sharing.
