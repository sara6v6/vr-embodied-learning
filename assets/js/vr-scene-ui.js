/**
 * Shared screen-space UI for both VR conditions.
 * Detailed learning content is presented in HTML so it remains readable and
 * does not become oversized world-space text inside the A-Frame scene.
 */
(function () {
  "use strict";

  const CARDS = {
    "card-1": {
      title: "Embodied Cognition & Learning",
      body: "Embodied cognition proposes that thinking is shaped by bodily action and sensorimotor experience.",
      points: ["Gestures can support concept formation.", "Spatial interaction may reinforce memory cues.", "Learning design can connect action with reflection."]
    },
    "card-2": {
      title: "Spatial Presence",
      body: "Spatial presence describes the subjective sense of being located within a mediated environment.",
      points: ["Environmental coherence supports orientation.", "Interaction feedback can strengthen a sense of being there.", "Presence is an experience to measure, not an assumed outcome."]
    },
    "card-3": {
      title: "Body Ownership Illusion",
      body: "Body ownership illusion refers to the feeling that a seen virtual body or body part may belong to oneself.",
      points: ["First-person alignment can provide a minimal ownership cue.", "Visual and action feedback may affect self-location.", "This prototype does not claim that ownership is established."]
    },
    "card-4": {
      title: "Learning Engagement",
      body: "Learning engagement can include behavioral participation, cognitive effort, and emotional interest.",
      points: ["Behavioral logs describe interaction patterns.", "Self-report items capture perceived cognitive engagement.", "Engagement should not be equated automatically with learning."]
    },
    "card-5": {
      title: "Research Design",
      body: "The prototype supports an exploratory between-condition comparison using local-only records.",
      points: ["Embodied VR and control conditions present the same topics.", "Behavioral interaction logs describe exploration.", "Adapted self-report items support design reflection."]
    }
  };

  let currentCardId = null;
  let instructionTimer = null;

  function updateProgress(count) {
    const progress = document.getElementById("scene-progress");
    if (progress) progress.textContent = `Progress ${count}/5`;
  }

  function openCard(cardId) {
    const card = CARDS[cardId];
    const panel = document.getElementById("knowledge-panel");
    if (!card || !panel) return;
    if (currentCardId && currentCardId !== cardId && typeof window.onKnowledgeCardClose === "function") {
      window.onKnowledgeCardClose(currentCardId);
    }
    currentCardId = cardId;
    panel.querySelector(".knowledge-panel__index").textContent = `Knowledge card ${cardId.split("-")[1]} of 5`;
    panel.querySelector("h2").textContent = card.title;
    panel.querySelector("p").textContent = card.body;
    panel.querySelector("ul").innerHTML = card.points.map((point) => `<li>${point}</li>`).join("");
    panel.classList.add("open");
    panel.setAttribute("aria-hidden", "false");
  }

  function closeCard() {
    const panel = document.getElementById("knowledge-panel");
    if (!panel || !panel.classList.contains("open")) return;
    const closingCardId = currentCardId;
    panel.classList.remove("open");
    panel.setAttribute("aria-hidden", "true");
    currentCardId = null;
    if (closingCardId && typeof window.onKnowledgeCardClose === "function") {
      window.onKnowledgeCardClose(closingCardId);
    }
  }

  function showInstructions() {
    const toast = document.getElementById("instruction-toast");
    if (!toast) return;
    toast.classList.remove("hidden");
    clearTimeout(instructionTimer);
    instructionTimer = setTimeout(() => toast.classList.add("hidden"), 7000);
  }

  function initialize() {
    document.getElementById("knowledge-panel-close")?.addEventListener("click", closeCard);
    showInstructions();
  }

  window.VRSceneUI = { initialize, updateProgress, openCard, closeCard, showInstructions };
}());
