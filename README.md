# VR Embodied Learning Scene
**A WebVR prototype exploring embodied cognition and presence in immersive learning environments**

🔗 **Live Demo:** https://sara6v6.github.io/vr-embodied-learning/  
📋 **Survey:** https://sara6v6.github.io/vr-embodied-learning/survey.html  
📊 **Results:** https://sara6v6.github.io/vr-embodied-learning/results.html  

---

## Overview

This prototype is an exploratory research practice investigating how **body ownership illusion** and **sense of presence** in virtual reality may influence learner engagement and cognitive investment.

The design is informed by research on VR presence and embodied cognition, particularly work related to:
- Presence and immersion in virtual environments
- Embodied cognition and its role in knowledge construction
- Interactive affordances in VR learning spaces

---
## Research Framework

```mermaid  
flowchart LR  
    A["📚 Theory\nEmbodied Cognition\nWilson 2002 · Varela 1991"]  
    B["🏫 VR Environment\nImmersive Classroom\nA-Frame WebVR"]  
    C["👁️ Interaction\nGaze · Teleport · Avatar"]  
    D["📊 Measure\nLikert Survey · Log"]  
    E["📈 Results\nPresence · Engagement"]  

    A -->|Concept| B  
    B -->|Context| C  
    C -->|Behavior| D  
    D -->|Data| E  

    classDef theory fill:#eff6ff,color:#1e3a8a,stroke:#2563eb,stroke-width:2px  
    classDef design fill:#dcfce7,color:#065f46,stroke:#16a34a,stroke-width:2px  
    classDef interact fill:#ede9fe,color:#4c1d95,stroke:#7c3aed,stroke-width:2px  
    classDef assess fill:#fffbeb,color:#78350f,stroke:#d97706,stroke-width:2px  
    classDef output fill:#fee2e2,color:#7f1d1d,stroke:#dc2626,stroke-width:2px  

    class A theory  
    class B design  
    class C interact  
    class D assess  
    class E output  
```
---
## User Flow

```mermaid  
sequenceDiagram  
    autonumber  
    participant U as User  
    participant S as survey.html  
    participant V as VR Scene  
    participant R as results.html  

    Note over U,S: Pre-learning measurement  
    U->>S: Complete pre-survey (2 items)  

    Note over S,V: Transition to immersive learning  
    S->>V: Enter VR classroom  

    Note over V: Embodied interaction phase  
    V->>V: Gaze interaction — unlock knowledge cards  
    V->>V: Teleportation — explore classroom space  
    V->>V: Avatar hands — support embodied presence  

    Note over V,S: Post-learning measurement  
    V-->>S: Return to survey  
    S->>S: Complete post-survey (5 items)  

    Note over S,R: Data processing and visualization  
    S->>R: Submit responses — auto redirect  
    R->>R: Render progress and score charts  
```
---

## Demo Features

| Feature | Description |
|---------|-------------|
| Immersive Classroom | Virtual classroom with blackboard, desks, chairs, and windows |
| Gaze Interaction | Look at a colored sphere for 2 seconds to reveal a knowledge card |
| Teleportation | Click anywhere on the floor to move to that position |
| Avatar Hands | Virtual hands visible in first-person view (body ownership) |
| 5 Knowledge Cards | Embodied Cognition · Presence · Body Ownership · Engagement · Research Design |
| Ambient Audio | Background audio loop to enhance sense of presence |
| Learning Progress | localStorage-based tracking of visited cards, displayed on HUD |
| Pre/Post Survey | 7-point Likert scale measuring presence and learning engagement |
| Results Dashboard | Chart.js visualization of survey scores and exploration data |
| Control Condition | Separate scene (index-control.html) with click-based card reading and no avatar hands |

---

## Research Background

The prototype is inspired by studies on **tele-existence**, **pseudo-embodiment**, and **presence engineering** in XR environments. The central question guiding this exploration:

> *How does the sense of "being there" and bodily presence in a virtual space alter the quality of cognitive engagement during learning tasks?*

This question connects educational technology with affective computing and human augmentation — the core intersection I aim to investigate at the graduate level.

---

## Methodology

### Research Questions
1. Does immersive VR presence (measured by IPQ) correlate with increased learning engagement (measured by AEQ)?
2. Does body ownership illusion (avatar hands) contribute to the sense of spatial presence?

### Variables
| Variable | Type | Measurement |
|----------|------|-------------|
| Spatial Presence | Dependent | IPQ items (Q3) — 7-point Likert |
| Body Ownership | Dependent | BOI-adapted (Q4) — 7-point Likert |
| Cognitive Engagement | Dependent | AEQ (Q5) — 7-point Likert |
| Emotional Engagement | Dependent | AEQ (Q6) — 7-point Likert |
| VR Familiarity | Control | Self-report (Q1) — 7-point Likert |
| Card Exploration | Behavioral | Count of cards visited (0–5) |
| Exploration Sequence | Behavioral | Timestamp log per card_open event |
| Session Duration | Behavioral | Total time in VR scene (seconds) |
| Teleportation Count | Behavioral | Number of floor-click teleports |

### Data Collection
- **Survey data**: Pre/post Likert responses stored in `localStorage` (`vr-survey-data`)
- **Behavioral data**: Timestamped event log stored in `localStorage` (`vr-behavior-log`)
  - Event types: `session_start`, `card_open`, `card_close`, `teleport`, `session_end`
- **Export**: All data exportable as structured JSON from results.html

### Validated Scales Used
- **IPQ** — Igroup Presence Questionnaire (Schubert et al., 2001)
- **BOI Scale** — Body Ownership Illusion (Longo et al., 2008, adapted)
- **AEQ** — Academic Engagement Questionnaire (Fredricks et al., 2004)

### Quasi-Experimental Design
Two-condition quasi-experimental design. Participants are assigned to either the Experimental condition (index.html: gaze interaction, teleportation, avatar hands) or the Control condition (index-control.html: click-to-read, no embodied affordances). Both groups complete identical pre/post surveys. Behavioral data is logged throughout each session and exportable as JSON for offline analysis via analysis.py.

---

## Technology

- **[A-Frame](https://aframe.io/)** (WebVR framework, v1.5.0)
- **Chart.js** (data visualization)
- **Python / matplotlib** (offline statistical analysis)
- localStorage API (client-side progress and survey data)
- Runs directly in browser — no installation required
- Mobile compatible (Google Cardboard supported)

---

## How to Experience

1. Open **survey.html** and complete the pre-survey
2. Click the link to enter the VR scene
3. Use **WASD** to move, **mouse** to look around
4. **Gaze** at colored spheres for 2 seconds to open knowledge cards
5. **Click** on the floor to teleport
6. Return to survey.html and complete the post-survey
7. View your results in **results.html**

---

## Repository Structure

```  
vr-embodied-learning/  
├── index.html          — Experimental condition: embodied VR scene  
├── index-control.html  — Control condition: text-based VR scene  
├── survey.html         — Pre/post Likert survey (shared)  
├── results.html        — Data visualization dashboard  
├── analysis.py         — Offline statistical analysis (Python)  
└── README.md  
```


---

## Author

**Xiala Dilimulati**
B.S. Educational Technology, Shanghai Normal University
Research interest: VR presence, embodied learning, human-computer interaction

---

## Acknowledgements

Built with [A-Frame](https://aframe.io/) by Mozilla and [Chart.js](https://www.chartjs.org/). Concept developed as part of graduate school application research exploration.
