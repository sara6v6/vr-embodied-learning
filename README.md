# VR Embodied Learning Prototype

![Status: Prototype](https://img.shields.io/badge/status-prototype-555555)
![Platform: Browser / WebVR](https://img.shields.io/badge/platform-browser%20%2F%20WebVR-1d4ed8)
![Framework: A-Frame](https://img.shields.io/badge/framework-A--Frame-ef2d5e)
![Data: LocalStorage only](https://img.shields.io/badge/data-localStorage%20only-16794a)
![License: MIT](https://img.shields.io/badge/license-MIT-black)

## Abstract

This project is a browser-based WebVR research prototype investigating how embodied interaction and virtual presence may shape cognitive engagement and perceived learning. It compares an embodied VR condition with a control condition and records self-report responses and behavioral interaction logs for exploratory analysis. The prototype is intended as a proof of concept for future HCI and VR learning research, not as a completed empirical study.

The prototype is a solo-developed research practice artifact. It does not claim statistically valid findings, validated outcomes, or completed human-subjects research. Its purpose is to make a future pilot study or controlled evaluation concrete, inspectable, and browser-accessible.

## Live Demo

- GitHub Pages demo: https://sara6v6.github.io/vr-embodied-learning/
- Embodied VR condition: https://sara6v6.github.io/vr-embodied-learning/index.html
- Control condition: https://sara6v6.github.io/vr-embodied-learning/index-control.html
- Self-report instrument: https://sara6v6.github.io/vr-embodied-learning/survey.html
- Local results dashboard: https://sara6v6.github.io/vr-embodied-learning/results.html

To deploy: open repository **Settings → Pages**, select the `main` branch and root folder, then access each HTML file directly.

## Research Positioning

The prototype sits at the intersection of HCI, immersive learning, embodied cognition, and human augmentation. It explores how spatial presence, body ownership illusion, agency, and embodied interaction may relate to cognitive engagement and perceived learning in a virtual learning environment.

The embodied VR condition includes first-person avatar hands attached to the camera, gaze-directed reach feedback, and a brief hand response during teleportation. These affordances are designed to provide minimal body ownership and agency cues; they do not demonstrate that a body ownership illusion occurs. The control condition preserves the virtual classroom and core learning topics while removing those embodied affordances. This supports an exploratory between-condition comparison without intentionally degrading the control experience.

### Exploratory Research Questions

- **RQ1:** Does embodied avatar interaction increase exploratory behavior in a VR learning environment compared with a control condition without embodied affordances?
- **RQ2:** Do spatial presence and body ownership illusion correlate with self-reported cognitive engagement and perceived learning?
- **RQ3:** What behavioral interaction patterns emerge during embodied versus non-embodied VR exploration?

These are exploratory research questions. The prototype is designed for small-scale pilot testing and design reflection, not for statistically powered empirical claims.

## Reviewer Flow

1. Read the project overview.
2. Complete the pre-survey and choose a condition.
3. Explore either the embodied VR condition or control condition.
4. Return to the self-report instrument and complete the post-survey.
5. View the local results dashboard.
6. Export anonymous JSON for offline descriptive analysis.

## Prototype Components

| Component | Research purpose |
| --- | --- |
| Embodied VR condition | Uses camera-attached first-person hands, gaze-directed reach feedback, and teleport hand feedback as minimal body ownership and agency cues |
| Control condition | Presents the same core topics without avatar hands, gaze activation, or teleportation |
| Self-report instrument | Records adapted exploratory ratings for presence, body ownership, agency, engagement, and perceived learning |
| Behavioral interaction log | Records condition, timestamps, elapsed time, card events, and teleportation events |
| Local results dashboard | Summarizes one locally stored session without making inferential claims |
| `analysis.py` | Loads exported JSON and reports descriptive statistics; plots are optional |

## Measures and Variables

| Construct or measure | Type | Prototype representation |
| --- | --- | --- |
| Condition | Independent/context | Embodied VR condition or control condition |
| Spatial presence | Self-report | Adapted single exploratory item |
| Body ownership illusion | Self-report | Adapted single exploratory item |
| Agency | Self-report | Adapted single exploratory item |
| Cognitive engagement | Self-report | Adapted single exploratory item |
| Emotional engagement | Self-report | Adapted single exploratory item |
| Perceived learning | Self-report | Adapted single exploratory item |
| Exploratory behavior | Behavioral | Card visits, sequence, duration, and teleportation count |

The self-report instrument is adapted for exploratory prototype evaluation and is not a full validated psychometric instrument.

## Local Data and Analysis

All responses and behavioral interaction logs remain in local browser storage. Nothing is transmitted to a server, and no personally identifiable information is requested. The results dashboard exports a JSON file that can be inspected or analyzed offline.

```bash
python analysis.py exported_session.json
python analysis.py data/*.json
```

`analysis.py` handles missing values, groups sessions by condition, and prints descriptive statistics. If `matplotlib` is installed, it can also save a simple descriptive plot. See [docs/data-schema.md](docs/data-schema.md) for the expected structure and localStorage keys.

## Technology

- A-Frame 1.5.0
- JavaScript and browser localStorage
- Chart.js 4.4.0
- Python standard library, with optional matplotlib
- Static HTML/CSS suitable for GitHub Pages

No backend, login, tracking, or server-side data collection is used.

## Privacy and Ethics

- No personally identifiable information is collected.
- Survey responses and behavioral interaction logs are stored locally in the browser.
- No data is transmitted to a server.
- Exported JSON should be anonymized and handled responsibly before analysis.
- This is not a formal human-subjects study.
- Future formal studies would require appropriate consent procedures and institutional review where applicable.
- The prototype is suitable for design exploration and pilot testing, not generalizable conclusions.

See [docs/ethics-and-limitations.md](docs/ethics-and-limitations.md) for additional detail.

## Limitations

- A small sample size is expected during pilot use.
- Browser-based WebVR may produce lower presence than standalone head-mounted displays.
- Measures are self-report items only; no physiological data is collected.
- The experience is single-session and has no longitudinal component.
- Demand characteristics and self-selection bias are possible.
- No formal ethics review has been conducted at this stage.
- localStorage content can be lost when browser data is cleared.
- Survey items are adapted and do not form a complete validated psychometric instrument.

These limitations are stated as research transparency. They define what a future controlled study would need to improve.

## Documentation

- [Research design](docs/research-design.md)
- [User flow](docs/user-flow.md)
- [Local data schema](docs/data-schema.md)
- [Ethics and limitations](docs/ethics-and-limitations.md)

## Screenshots

Real screenshots have not yet been added.

- **VR scene:** placeholder for a real capture of the embodied VR condition
- **Survey flow:** placeholder for a real capture of the pre/post self-report instrument
- **Results dashboard:** placeholder for a real capture using an actual local session

Empty screenshot and figure directories are retained at `assets/screenshots/` and `assets/figures/`.

## Repository Structure

```text
vr-embodied-learning/
├── index.html
├── index-control.html
├── survey.html
├── results.html
├── analysis.py
├── assets/
│   ├── css/research-ui.css
│   ├── js/research-storage.js
│   ├── screenshots/
│   └── figures/
└── docs/
```

## Author Note

- **Developer:** Xiala Dilimulati
- **Background:** B.S. Educational Technology, Shanghai Normal University
- **Research interest:** VR presence, embodied cognition, human augmentation, HCI, and learning technology
- **Status:** undergraduate solo research prototype, 2025

## Portfolio Summary

**Title:** VR Embodied Learning Prototype

**One-sentence summary:** A browser-based WebVR research prototype exploring how embodied interaction, spatial presence, and body ownership may shape cognitive engagement and perceived learning.

**My contribution:** Concept design, WebVR implementation, survey flow, behavioral logging, results dashboard, and exploratory analysis script.

**Technologies:** A-Frame, JavaScript, localStorage, Chart.js, Python

**Status:** Exploratory prototype for graduate research preparation.

## References

The design is theoretically grounded by foundational work including:

- Botvinick, M., & Cohen, J. (1998). Rubber hand illusion and body ownership.
- Witmer, B. G., & Singer, M. J. (1998). Presence in virtual environments.
- Wilson, M. (2002). Embodied cognition.
- Dede, C. (2009). Immersive interfaces for engagement and learning.
- Slater, M. (2009). Place illusion and plausibility illusion in immersive virtual environments.

These references provide foundational context rather than a complete literature review. Recent literature on VR learning, embodiment, and human augmentation should be reviewed and added before formal research submission.
