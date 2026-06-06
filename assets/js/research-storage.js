/**
 * Shared local browser storage utilities for the VR Embodied Learning Prototype.
 * Developer: Xiala Dilimulati
 * Prototype status: undergraduate solo research prototype, 2025
 *
 * Nothing handled here is transmitted to a server. The helper keeps condition-
 * specific behavioral interaction logs separate for transparent comparison.
 */
(function () {
  "use strict";

  const KEYS = {
    survey: "vr-survey-data",
    selectedCondition: "vr-selected-condition",
    embodiedProgress: "vr-learning-progress",
    embodiedLog: "vr-behavior-log",
    controlProgress: "vr-learning-progress-control",
    controlLog: "vr-behavior-log-control"
  };

  const CONDITIONS = {
    embodied: {
      label: "Embodied VR condition",
      progressKey: KEYS.embodiedProgress,
      logKey: KEYS.embodiedLog
    },
    control: {
      label: "Control condition",
      progressKey: KEYS.controlProgress,
      logKey: KEYS.controlLog
    }
  };

  function read(key, fallback) {
    try {
      const value = localStorage.getItem(key);
      return value === null ? fallback : JSON.parse(value);
    } catch (error) {
      console.warn(`[ResearchStorage] Could not read ${key}.`, error);
      return fallback;
    }
  }

  function write(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
      return true;
    } catch (error) {
      console.warn(`[ResearchStorage] Could not write ${key}.`, error);
      return false;
    }
  }

  function normalizeCondition(condition) {
    return Object.prototype.hasOwnProperty.call(CONDITIONS, condition) ? condition : "embodied";
  }

  function getSelectedCondition() {
    return normalizeCondition(localStorage.getItem(KEYS.selectedCondition) || "embodied");
  }

  function setSelectedCondition(condition) {
    const normalized = normalizeCondition(condition);
    localStorage.setItem(KEYS.selectedCondition, normalized);
    return normalized;
  }

  function getConditionData(condition) {
    const normalized = normalizeCondition(condition);
    const config = CONDITIONS[normalized];
    return {
      condition: normalized,
      conditionLabel: config.label,
      progressData: read(config.progressKey, {}),
      behaviorLog: read(config.logKey, [])
    };
  }

  function buildExportPayload(condition) {
    const conditionData = getConditionData(condition || getSelectedCondition());
    return {
      schemaVersion: "1.0",
      exportedAt: new Date().toISOString(),
      privacy: "Local browser storage only; no personally identifiable information requested.",
      condition: conditionData.condition,
      conditionLabel: conditionData.conditionLabel,
      surveyData: read(KEYS.survey, {}),
      progressData: conditionData.progressData,
      behaviorLog: conditionData.behaviorLog
    };
  }

  function resetAll() {
    Object.values(KEYS).forEach((key) => localStorage.removeItem(key));
  }

  window.ResearchStorage = {
    KEYS,
    CONDITIONS,
    read,
    write,
    getSelectedCondition,
    setSelectedCondition,
    getConditionData,
    buildExportPayload,
    resetAll
  };
}());
