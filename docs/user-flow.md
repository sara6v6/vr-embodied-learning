# User Flow

## Intended Reviewer or Pilot Flow

1. Read the project overview in `README.md`.
2. Open `survey.html`.
3. Select the embodied VR condition or control condition.
4. Complete the pre-survey.
5. Explore the selected virtual learning environment.
6. Return to `survey.html` and complete the post-survey.
7. Open `results.html` to review the selected condition, behavioral interaction log, and self-report values.
8. Export anonymous JSON for offline descriptive analysis.
9. Reset local data before beginning another clean session.

## Condition Interaction

### Embodied VR Condition

- Drag the mouse to look around on desktop.
- Use WASD for precise movement through the classroom.
- Hold the center gaze cursor on a labeled sphere for two seconds to open a knowledge card.
- Click the floor for quick teleportation.
- Camera-attached first-person avatar hands remain in the lower field of view.
- Gaze dwell produces subtle reach feedback before card activation.
- Card activation and teleportation produce brief hand feedback to reinforce body-action causality.

These affordances are designed as minimal body ownership and agency cues; they do not prove that a body ownership illusion occurs.

### Control Condition

- Click colored cubes to open or close knowledge cards.
- Use WASD to move on desktop.
- Avatar hands, gaze activation, and teleportation are omitted.

Both conditions present the same five core learning topics. The control condition is intended as a credible comparison condition.

## Local-Only Flow

The browser stores the selected condition, self-report responses, progress, and behavioral interaction log in localStorage. No account, backend, tracking service, or server transmission is used.
