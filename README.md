<!DOCTYPE html>  
<html lang="en">  
<head>  
  <meta charset="utf-8">  
  <title>Learning Experience Survey | VR Embodied Learning</title>  
  <meta name="viewport" content="width=device-width, initial-scale=1.0">  
  <style>  
    * { box-sizing: border-box; margin: 0; padding: 0; }  

    body {  
      font-family: 'Helvetica Neue', Arial, sans-serif;  
      background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);  
      min-height: 100vh;  
      color: #e0e0e0;  
      padding: 40px 20px;  
    }  

    .container {  
      max-width: 720px;  
      margin: 0 auto;  
    }  

    .header {  
      text-align: center;  
      margin-bottom: 48px;  
    }  

    .header h1 {  
      font-size: 1.8rem;  
      color: #ffffff;  
      margin-bottom: 10px;  
    }  

    .header p {  
      color: #a0aec0;  
      font-size: 0.95rem;  
      line-height: 1.6;  
    }  

    .section-label {  
      font-size: 0.75rem;  
      letter-spacing: 0.12em;  
      text-transform: uppercase;  
      color: #63b3ed;  
      margin-bottom: 20px;  
      padding-bottom: 8px;  
      border-bottom: 1px solid #2d3748;  
    }  

    .card {  
      background: rgba(255,255,255,0.05);  
      border: 1px solid rgba(255,255,255,0.08);  
      border-radius: 12px;  
      padding: 28px;  
      margin-bottom: 20px;  
      transition: border-color 0.2s;  
    }  

    .card:hover {  
      border-color: rgba(99,179,237,0.3);  
    }  

    .question-num {  
      font-size: 0.72rem;  
      color: #63b3ed;  
      text-transform: uppercase;  
      letter-spacing: 0.1em;  
      margin-bottom: 8px;  
    }  

    .question-text {  
      font-size: 1.0rem;  
      color: #e2e8f0;  
      line-height: 1.5;  
      margin-bottom: 6px;  
    }  

    .question-sub {  
      font-size: 0.82rem;  
      color: #718096;  
      margin-bottom: 20px;  
      font-style: italic;  
    }  

    .likert-scale {  
      display: flex;  
      gap: 8px;  
      align-items: center;  
      flex-wrap: wrap;  
    }  

    .scale-labels {  
      display: flex;  
      justify-content: space-between;  
      width: 100%;  
      margin-bottom: 10px;  
    }  

    .scale-labels span {  
      font-size: 0.75rem;  
      color: #718096;  
    }  

    .likert-options {  
      display: flex;  
      gap: 8px;  
      width: 100%;  
    }  

    .likert-options label {  
      flex: 1;  
      display: flex;  
      flex-direction: column;  
      align-items: center;  
      gap: 6px;  
      cursor: pointer;  
    }  

    .likert-options input[type="radio"] {  
      display: none;  
    }  

    .likert-btn {  
      width: 100%;  
      padding: 10px 4px;  
      border-radius: 8px;  
      border: 2px solid #2d3748;  
      background: #1a202c;  
      color: #a0aec0;  
      font-size: 0.9rem;  
      font-weight: 600;  
      text-align: center;  
      transition: all 0.15s;  
      cursor: pointer;  
    }  

    .likert-options input[type="radio"]:checked + .likert-btn {  
      border-color: #63b3ed;  
      background: rgba(99,179,237,0.15);  
      color: #63b3ed;  
      transform: scale(1.05);  
    }  

    .likert-options label:hover .likert-btn {  
      border-color: #4a5568;  
      background: #2d3748;  
    }  

    .tab-bar {  
      display: flex;  
      gap: 0;  
      margin-bottom: 36px;  
      border-radius: 10px;  
      overflow: hidden;  
      border: 1px solid #2d3748;  
    }  

    .tab-btn {  
      flex: 1;  
      padding: 14px;  
      background: #1a202c;  
      color: #718096;  
      border: none;  
      cursor: pointer;  
      font-size: 0.9rem;  
      font-weight: 600;  
      transition: all 0.2s;  
    }  

    .tab-btn.active {  
      background: rgba(99,179,237,0.15);  
      color: #63b3ed;  
    }  

    .vr-link-section {  
      text-align: center;  
      margin: 28px 0;  
      padding: 20px;  
      background: rgba(99,179,237,0.08);  
      border-radius: 12px;  
      border: 1px dashed rgba(99,179,237,0.3);  
    }  

    .vr-link-section p {  
      color: #a0aec0;  
      font-size: 0.88rem;  
      margin-bottom: 12px;  
    }  

    .btn-vr {  
      display: inline-block;  
      padding: 10px 24px;  
      background: linear-gradient(135deg, #3182ce, #2b6cb0);  
      color: white;  
      text-decoration: none;  
      border-radius: 8px;  
      font-size: 0.9rem;  
      font-weight: 600;  
      transition: opacity 0.2s;  
    }  

    .btn-vr:hover { opacity: 0.85; }  

    .submit-section {  
      text-align: center;  
      margin-top: 36px;  
    }  

    .btn-submit {  
      padding: 14px 48px;  
      background: linear-gradient(135deg, #38a169, #2f855a);  
      color: white;  
      border: none;  
      border-radius: 10px;  
      font-size: 1rem;  
      font-weight: 700;  
      cursor: pointer;  
      transition: opacity 0.2s, transform 0.15s;  
    }  

    .btn-submit:hover {  
      opacity: 0.9;  
      transform: translateY(-1px);  
    }  

    .toast {  
      position: fixed;  
      top: 30px;  
      left: 50%;  
      transform: translateX(-50%) translateY(-80px);  
      background: #38a169;  
      color: white;  
      padding: 14px 28px;  
      border-radius: 10px;  
      font-weight: 600;  
      transition: transform 0.35s ease;  
      z-index: 1000;  
    }  

    .toast.show {  
      transform: translateX(-50%) translateY(0);  
    }  

    .nav-links {  
      text-align: center;  
      margin-top: 32px;  
    }  

    .nav-links a {  
      color: #63b3ed;  
      text-decoration: none;  
      margin: 0 16px;  
      font-size: 0.88rem;  
    }  

    .nav-links a:hover { text-decoration: underline; }  

    .phase-hidden { display: none; }  
  </style>  
</head>  
<body>  

<div class="container">  

  <div class="header">  
    <h1>Learning Experience Survey</h1>  
    <p>This survey measures your <strong>sense of presence</strong> and <strong>learning engagement</strong> in the VR environment.<br>  
    7-point Likert scale (1 = Strongly Disagree, 7 = Strongly Agree)<br>  
    <span style="font-size:0.8rem;color:#4a5568">Items adapted from IPQ (Schubert et al., 2001), BOI Scale (Longo et al., 2008) &amp; AEQ (Fredricks et al., 2004)</span></p>  
  </div>  

  <div class="tab-bar">  
    <button class="tab-btn active" id="tab-pre" onclick="switchPhase('pre')">  
      Pre-Survey  
    </button>  
    <button class="tab-btn" id="tab-post" onclick="switchPhase('post')">  
      Post-Survey  
    </button>  
  </div>  

  <form id="survey-form">  

    <!-- ── 前测阶段 ── -->  
    <div id="phase-pre">  

      <p class="section-label">Section A · Baseline Measures (Before VR)</p>  

      <!-- Q1 -->  
      <div class="card">  
        <div class="question-num">Question 1 · Technology Familiarity</div>  
        <div class="question-text">I am familiar with VR (virtual reality) technology.</div>  
        <div class="question-sub">Rate your prior experience with VR headsets or applications.</div>  
        <div class="scale-labels">  
          <span>Strongly Disagree</span><span>Strongly Agree</span>  
        </div>  
        <div class="likert-options" id="q1">  
          <label><input type="radio" name="q1" value="1"><span class="likert-btn">1</span></label>  
          <label><input type="radio" name="q1" value="2"><span class="likert-btn">2</span></label>  
          <label><input type="radio" name="q1" value="3"><span class="likert-btn">3</span></label>  
          <label><input type="radio" name="q1" value="4"><span class="likert-btn">4</span></label>  
          <label><input type="radio" name="q1" value="5"><span class="likert-btn">5</span></label>  
          <label><input type="radio" name="q1" value="6"><span class="likert-btn">6</span></label>  
          <label><input type="radio" name="q1" value="7"><span class="likert-btn">7</span></label>  
        </div>  
      </div>  

      <!-- Q2 -->  
      <div class="card">  
        <div class="question-num">Question 2 · Learning Motivation</div>  
        <div class="question-text">I feel motivated and curious about today's learning content.</div>  
        <div class="question-sub">Rate your interest level before entering the VR scene.</div>  
        <div class="scale-labels">  
          <span>Strongly Disagree</span><span>Strongly Agree</span>  
        </div>  
        <div class="likert-options">  
          <label><input type="radio" name="q2" value="1"><span class="likert-btn">1</span></label>  
          <label><input type="radio" name="q2" value="2"><span class="likert-btn">2</span></label>  
          <label><input type="radio" name="q2" value="3"><span class="likert-btn">3</span></label>  
          <label><input type="radio" name="q2" value="4"><span class="likert-btn">4</span></label>  
          <label><input type="radio" name="q2" value="5"><span class="likert-btn">5</span></label>  
          <label><input type="radio" name="q2" value="6"><span class="likert-btn">6</span></label>  
          <label><input type="radio" name="q2" value="7"><span class="likert-btn">7</span></label>  
        </div>  
      </div>  

      <div class="vr-link-section">  
        <p>After completing the pre-survey, enter the VR learning scene. Return here to complete the post-survey when finished.</p>  
        <a href="index.html" class="btn-vr" target="_blank">▶ Enter VR Learning Scene</a>  
      </div>  

    </div>  

    <!-- ── 后测阶段 ── -->  
    <div id="phase-post" class="phase-hidden">  

      <p class="section-label">Section B · Presence &amp; Engagement Scales (IPQ · BOI · AEQ)</p>  

      <!-- Q3 -->  
      <div class="card">  
        <div class="question-num">Question 3 · Spatial Presence — IPQ (Schubert et al., 2001)</div>  
        <div class="question-text">During the VR experience, I felt as if I was really present in the virtual classroom.</div>  
        <div class="question-sub">I felt a sense of being present in the virtual classroom. [IPQ-SP]</div>  
        <div class="scale-labels">  
          <span>Strongly Disagree</span><span>Strongly Agree</span>  
        </div>  
        <div class="likert-options">  
          <label><input type="radio" name="q3" value="1"><span class="likert-btn">1</span></label>  
          <label><input type="radio" name="q3" value="2"><span class="likert-btn">2</span></label>  
          <label><input type="radio" name="q3" value="3"><span class="likert-btn">3</span></label>  
          <label><input type="radio" name="q3" value="4"><span class="likert-btn">4</span></label>  
          <label><input type="radio" name="q3" value="5"><span class="likert-btn">5</span></label>  
          <label><input type="radio" name="q3" value="6"><span class="likert-btn">6</span></label>  
          <label><input type="radio" name="q3" value="7"><span class="likert-btn">7</span></label>  
        </div>  
      </div>  

      <!-- Q4 -->  
      <div class="card">  
        <div class="question-num">Question 4 · Body Ownership — BOI Scale (Longo et al., 2008)</div>  
        <div class="question-text">The virtual hands felt like my own real hands.</div>  
        <div class="question-sub">The virtual hands felt like my own real hands. [BOI-adapted]</div>  
        <div class="scale-labels">  
          <span>Strongly Disagree</span><span>Strongly Agree</span>  
        </div>  
        <div class="likert-options">  
          <label><input type="radio" name="q4" value="1"><span class="likert-btn">1</span></label>  
          <label><input type="radio" name="q4" value="2"><span class="likert-btn">2</span></label>  
          <label><input type="radio" name="q4" value="3"><span class="likert-btn">3</span></label>  
          <label><input type="radio" name="q4" value="4"><span class="likert-btn">4</span></label>  
          <label><input type="radio" name="q4" value="5"><span class="likert-btn">5</span></label>  
          <label><input type="radio" name="q4" value="6"><span class="likert-btn">6</span></label>  
          <label><input type="radio" name="q4" value="7"><span class="likert-btn">7</span></label>  
        </div>  
      </div>  

      <!-- Q5 -->  
      <div class="card">  
        <div class="question-num">Question 5 · Cognitive Engagement — AEQ (Fredricks et al., 2004)</div>  
        <div class="question-text">I actively thought about the knowledge presented in the learning cards.</div>  
        <div class="question-sub">I actively thought about the knowledge presented in the learning cards. [AEQ-CE]</div>  
        <div class="scale-labels">  
          <span>Strongly Disagree</span><span>Strongly Agree</span>  
        </div>  
        <div class="likert-options">  
          <label><input type="radio" name="q5" value="1"><span class="likert-btn">1</span></label>  
          <label><input type="radio" name="q5" value="2"><span class="likert-btn">2</span></label>  
          <label><input type="radio" name="q5" value="3"><span class="likert-btn">3</span></label>  
          <label><input type="radio" name="q5" value="4"><span class="likert-btn">4</span></label>  
          <label><input type="radio" name="q5" value="5"><span class="likert-btn">5</span></label>  
          <label><input type="radio" name="q5" value="6"><span class="likert-btn">6</span></label>  
          <label><input type="radio" name="q5" value="7"><span class="likert-btn">7</span></label>  
        </div>  
      </div>  

      <!-- Q6 -->  
      <div class="card">  
        <div class="question-num">Question 6 · Emotional Engagement — AEQ (Fredricks et al., 2004)</div>  
        <div class="question-text">Compared to traditional learning, the VR environment made me feel more engaged and interested.</div>  
        <div class="question-sub">Compared to traditional learning, the VR environment made me more engaged and interested. [AEQ-EE]</div>  
        <div class="scale-labels">  
          <span>Strongly Disagree</span><span>Strongly Agree</span>  
        </div>  
        <div class="likert-options">  
          <label><input type="radio" name="q6" value="1"><span class="likert-btn">1</span></label>  
          <label><input type="radio" name="q6" value="2"><span class="likert-btn">2</span></label>  
          <label><input type="radio" name="q6" value="3"><span class="likert-btn">3</span></label>  
          <label><input type="radio" name="q6" value="4"><span class="likert-btn">4</span></label>  
          <label><input type="radio" name="q6" value="5"><span class="likert-btn">5</span></label>  
          <label><input type="radio" name="q6" value="6"><span class="likert-btn">6</span></label>  
          <label><input type="radio" name="q6" value="7"><span class="likert-btn">7</span></label>  
        </div>  
      </div>  

      <!-- Q7 -->  
      <div class="card">  
        <div class="question-num">Question 7 · Embodied Interaction</div>  
        <div class="question-text">Spatial movement and gaze interaction helped me better understand the concept of embodied cognition.</div>  
        <div class="question-sub">Spatial movement and gaze interaction helped me better understand embodied cognition.</div>  
        <div class="scale-labels">  
          <span>Strongly Disagree</span><span>Strongly Agree</span>  
        </div>  
        <div class="likert-options">  
          <label><input type="radio" name="q7" value="1"><span class="likert-btn">1</span></label>  
          <label><input type="radio" name="q7" value="2"><span class="likert-btn">2</span></label>  
          <label><input type="radio" name="q7" value="3"><span class="likert-btn">3</span></label>  
          <label><input type="radio" name="q7" value="4"><span class="likert-btn">4</span></label>  
          <label><input type="radio" name="q7" value="5"><span class="likert-btn">5</span></label>  
          <label><input type="radio" name="q7" value="6"><span class="likert-btn">6</span></label>  
          <label><input type="radio" name="q7" value="7"><span class="likert-btn">7</span></label>  
        </div>  
      </div>  

    </div>  

    <p style="text-align:center;font-size:0.75rem;color:#4a5568;margin-top:24px;font-style:italic">  
      Schubert T., Friedmann F., Regenbrecht H. (2001). The experience of presence: Factor analytic insights. <em>Presence</em>, 10(3).<br>  
      Fredricks J.A., Blumenfeld P.C., Paris A.H. (2004). School engagement. <em>Review of Educational Research</em>, 74(1).<br>  
      Longo M.R. et al. (2008). What is embodiment? <em>Neuropsychologia</em>, 46(6).  
    </p>  

    <div class="submit-section">  
      <button type="button" class="btn-submit" onclick="submitSurvey()">  
        Submit Survey  
      </button>  
    </div>  

  </form>  

  <div class="nav-links">  
    <a href="index.html">← VR Scene</a>  
    <a href="results.html">View Results →</a>  
  </div>  

</div>  

<div class="toast" id="toast">✓ Data saved. Redirecting to results...</div>  

<script>  
  let currentPhase = 'pre';  

  function switchPhase(phase) {  
    currentPhase = phase;  
    document.getElementById('phase-pre').classList.toggle('phase-hidden', phase !== 'pre');  
    document.getElementById('phase-post').classList.toggle('phase-hidden', phase !== 'post');  
    document.getElementById('tab-pre').classList.toggle('active', phase === 'pre');  
    document.getElementById('tab-post').classList.toggle('active', phase === 'post');  
  }  

  function submitSurvey() {  
    const form = document.getElementById('survey-form');  
    const data = {};  
    const questions = currentPhase === 'pre' ? ['q1','q2'] : ['q3','q4','q5','q6','q7'];  

    let allAnswered = true;  
    questions.forEach(q => {  
      const val = form.querySelector(`input[name="${q}"]:checked`);  
      if (!val) { allAnswered = false; }  
      else { data[q] = parseInt(val.value); }  
    });  

    if (!allAnswered) {  
      alert('Please answer all questions before submitting.');  
      return;  
    }  

    const existing = JSON.parse(localStorage.getItem('vr-survey-data') || '{}');  
    const merged = Object.assign(existing, data);  
    merged[`${currentPhase}-timestamp`] = new Date().toISOString();  
    localStorage.setItem('vr-survey-data', JSON.stringify(merged));  

    const toast = document.getElementById('toast');  
    toast.classList.add('show');  

    setTimeout(() => {  
      if (currentPhase === 'pre') {  
        switchPhase('post');  
        toast.classList.remove('show');  
      } else {  
        window.location.href = 'results.html';  
      }  
    }, 1800);  
  }  
</script>  

</body>  
</html>
