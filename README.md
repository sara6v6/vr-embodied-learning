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
%%{init: {"theme": "base", "themeVariables": {"fontFamily": "Inter, Arial, sans-serif", "background": "#ffffff", "primaryColor": "#f8fafc", "primaryTextColor": "#0f172a", "lineColor": "#64748b"}}}%%

flowchart TD
    T["RESEARCH FRAMEWORK<br/>Embodied Cognition × VR Learning Engagement"]

    subgraph P1["01  Theoretical Foundation"]
        A["📚 Embodied Cognition Theory<br/>Wilson 2002 · Varela 1991"]
    end

    subgraph P2["02  VR Learning Environment"]
        B["🏫 VR Scene Design<br/>Immersive Classroom<br/>A-Frame WebVR"]
    end

    subgraph P3["03  Embodied Interaction"]
        C["👁️ Gaze Interaction<br/>Teleportation<br/>Avatar Hands"]
    end

    subgraph P4["04  Engagement Measurement"]
        D["📊 Learning Engagement<br/>Likert Survey<br/>LocalStorage Tracking"]
    end

    subgraph P5["05  Results Interpretation"]
        E["📈 Data Visualization<br/>Results Dashboard<br/>Presence · Engagement"]
    end

    T --> A
    A --> B
    B --> C
    C --> D
    D --> E

    classDef title fill:#020617,color:#f8fafc,stroke:#020617,stroke-width:2px;
    classDef theory fill:#dbeafe,color:#1e3a8a,stroke:#2563eb,stroke-width:2px;
    classDef design fill:#dcfce7,color:#14532d,stroke:#16a34a,stroke-width:2px;
    classDef interaction fill:#ede9fe,color:#4c1d95,stroke:#7c3aed,stroke-width:2px;
    classDef assessment fill:#fef3c7,color:#78350f,stroke:#d97706,stroke-width:2px;
    classDef result fill:#fee2e2,color:#7f1d1d,stroke:#dc2626,stroke-width:2px;

    class T title;
    class A theory;
    class B design;
    class C interaction;
    class D assessment;
    class E result;

    style P1 fill:#f8fafc,stroke:#cbd5e1,stroke-width:1px
    style P2 fill:#f8fafc,stroke:#cbd5e1,stroke-width:1px
    style P3 fill:#f8fafc,stroke:#cbd5e1,stroke-width:1px
    style P4 fill:#f8fafc,stroke:#cbd5e1,stroke-width:1px
    style P5 fill:#f8fafc,stroke:#cbd5e1,stroke-width:1px

    linkStyle 0 stroke:#0f172a,stroke-width:3px
    linkStyle 1 stroke:#2563eb,stroke-width:3px
    linkStyle 2 stroke:#16a34a,stroke-width:3px
    linkStyle 3 stroke:#7c3aed,stroke-width:3px
    linkStyle 4 stroke:#d97706,stroke-width:3px
```

---

## User Flow

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontFamily": "Inter, Arial, sans-serif", "background": "#ffffff", "primaryColor": "#f8fafc", "primaryTextColor": "#0f172a", "lineColor": "#64748b"}}}%%

flowchart TD
    H["USER FLOW<br/>Survey → VR Learning → Results Dashboard"]

    subgraph S1["Survey Stage"]
        U1["🧑 User<br/>Starts the learning task"]
        U2["📝 survey.html<br/>Complete pre-survey<br/>2 items"]
    end

    subgraph S2["VR Learning Stage"]
        V1["🕶️ VR Scene<br/>Enter immersive classroom"]
        V2["👁️ Gaze Interaction<br/>Unlock knowledge cards"]
        V3["🧭 Teleportation<br/>Explore the classroom"]
        V4["🙌 Avatar Hands<br/>Embodied interaction cues"]
    end

    subgraph S3["Post-Learning Stage"]
        P1["📝 survey.html<br/>Complete post-survey<br/>5 items"]
        P2["📤 Submit<br/>Auto redirect"]
    end

    subgraph S4["Results Stage"]
        R1["📊 results.html<br/>Display progress charts"]
        R2["📈 Dashboard<br/>Presence · Engagement · Score"]
    end

    H --> U1
    U1 --> U2
    U2 --> V1
    V1 --> V2
    V2 --> V3
    V3 --> V4
    V4 --> P1
    P1 --> P2
    P2 --> R1
    R1 --> R2

    classDef title fill:#020617,color:#f8fafc,stroke:#020617,stroke-width:2px;
    classDef survey fill:#dbeafe,color:#1e3a8a,stroke:#2563eb,stroke-width:2px;
    classDef vr fill:#ede9fe,color:#4c1d95,stroke:#7c3aed,stroke-width:2px;
    classDef post fill:#fef3c7,color:#78350f,stroke:#d97706,stroke-width:2px;
    classDef result fill:#dcfce7,color:#14532d,stroke:#16a34a,stroke-width:2px;

    class H title;
    class U1,U2 survey;
    class V1,V2,V3,V4 vr;
    class P1,P2 post;
    class R1,R2 result;

    style S1 fill:#f8fafc,stroke:#bfdbfe,stroke-width:2px
    style S2 fill:#faf5ff,stroke:#ddd6fe,stroke-width:2px
    style S3 fill:#fffbeb,stroke:#fde68a,stroke-width:2px
    style S4 fill:#f0fdf4,stroke:#bbf7d0,stroke-width:2px

    linkStyle 0 stroke:#0f172a,stroke-width:3px
    linkStyle 1 stroke:#2563eb,stroke-width:3px
    linkStyle 2 stroke:#2563eb,stroke-width:3px
    linkStyle 3 stroke:#7c3aed,stroke-width:3px
    linkStyle 4 stroke:#7c3aed,stroke-width:3px
    linkStyle 5 stroke:#7c3aed,stroke-width:3px
    linkStyle 6 stroke:#7c3aed,stroke-width:3px
    linkStyle 7 stroke:#d97706,stroke-width:3px
    linkStyle 8 stroke:#d97706,stroke-width:3px
    linkStyle 9 stroke:#16a34a,stroke-width:3px
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
