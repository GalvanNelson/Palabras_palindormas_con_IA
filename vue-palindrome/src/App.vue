<template>
  <main class="page">
    <div class="card">
      <!-- Animación del título -->
      <h1 class="title" :class="{ 'animate-title': animate }">Detector de Palabras Palíndromas</h1>
      <h2 class="subtitle" :class="{ 'animate-subtitle': animate }">Expociencia 2025</h2>

      <label class="input-wrap">
        <input v-model="text" placeholder="Escribe una palabra o frase..." />
        <button @click="clear">✕</button>
      </label>

      <div class="result" v-if="status!=='idle'">
        <div v-if="status==='loading'">🔎 Consultando la IA...</div>
        <div v-if="status==='success'">
          <div class="prediction-result">
            <p class="main-result" v-if="response?.prediccion === 1">✅ Es palíndromo</p>
            <p class="main-result" v-else>❌ No es palíndromo</p>
          </div>
          
          <div class="features-section" v-if="response?.features">
            <h3>🧠 Análisis de la IA</h3>
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-label">📏 Longitud:</span>
                <span class="feature-value">{{ response.features[0] }} caracteres</span>
              </div>
              <div class="feature-item">
                <span class="feature-label">🔤 Primera = Última:</span>
                <span class="feature-value">{{ response.features[1] === 1 ? 'Sí ✓' : 'No ✗' }}</span>
              </div>
              <div class="feature-item">
                <span class="feature-label">🅰️ Vocales:</span>
                <span class="feature-value">{{ response.features[2] }}</span>
              </div>
              <div class="feature-item">
                <span class="feature-label">🅱️ Consonantes:</span>
                <span class="feature-value">{{ response.features[3] }}</span>
              </div>
              <div class="feature-item">
                <span class="feature-label">🔢 Letras únicas:</span>
                <span class="feature-value">{{ (response.features[4] * 100).toFixed(0) }}%</span>
              </div>
              <div class="feature-item">
                <span class="feature-label">🪞 Coincidencias espejo:</span>
                <span class="feature-value">{{ (response.features[5] * 100).toFixed(0) }}%</span>
              </div>
              <div class="feature-item">
                <span class="feature-label">⚖️ Simetría de vocales:</span>
                <span class="feature-value">Diferencia: {{ response.features[6] }}</span>
              </div>
            </div>
          </div>
        </div>
        <div v-if="status==='error'">⚠ {{ errorMsg }}</div>
      </div>

      <div class="controls">
        <button @click="callApi" :disabled="!text.trim()">Enviar a IA</button>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      text: '',
      response: null,
      status: 'idle', // idle | loading | success | error
      errorMsg: '',
      animate: false
    }
  },
  mounted() {
    // Activar animaciones al cargar la página
    setTimeout(() => { this.animate = true }, 100)
  },
  methods: {
    async callApi() {
      if (!this.text.trim()) return
      this.status = 'loading'
      this.response = null
      this.errorMsg = ''
      try {
        const res = await fetch('http://localhost:8000/predecir', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ texto: this.text })
        })
        if (!res.ok) throw new Error(`HTTP ${res.status}`)
        const data = await res.json()
        this.response = data
        this.status = 'success'
      } catch (err) {
        this.errorMsg = err.message || 'Error de conexión'
        this.status = 'error'
      }
    },
    clear() {
      this.text = ''
      this.response = null
      this.status = 'idle'
      this.errorMsg = ''
    }
  }
}
</script>

<style>
:root{
  --bg:#f7f8fb;
  --card:#fff;
  --accent:#4f46e5;
  --muted:#6b7280;
}
*{box-sizing:border-box}
html,body,#app{height:100%}
body{font-family:Inter,system-ui,Arial;margin:0;background:linear-gradient(180deg,var(--bg),#fff)}

.page{
  display:flex;
  align-items:center;
  justify-content:center;
  min-height:100vh;
  padding:20px;
}

.card{
  width:100%;
  max-width:560px;
  background: var(--card);
  border-radius:12px;
  padding:22px;
  box-shadow:0 8px 30px rgba(17,24,39,0.06);
  text-align:center;
}

.title{
  font-size:2rem;
  color:#0f172a;
  opacity:0;
  transform: translateY(-20px);
  transition: all 0.8s ease;
}

.subtitle{
  font-size:1.2rem;
  color:var(--muted);
  margin-bottom:20px;
  opacity:0;
  transform: translateY(-10px);
  transition: all 0.8s ease 0.2s;
}

/* Animación activa */
.animate-title{
  opacity:1;
  transform: translateY(0);
}
.animate-subtitle{
  opacity:1;
  transform: translateY(0);
}

.input-wrap{
  display:flex;
  gap:8px;
  background:#f1f5f9;
  padding:8px;
  border-radius:10px;
}
.input-wrap input{
  flex:1;
  border:0;
  background:transparent;
  padding:10px;
  font-size:16px;
  outline:none;
}

.result{
  margin-top:16px;
}

.prediction-result{
  margin-bottom:20px;
}

.main-result{
  font-size:1.5rem;
  font-weight:600;
  margin:10px 0;
}

.features-section{
  background:#f8f9fa;
  border-radius:10px;
  padding:16px;
  margin-top:16px;
  text-align:left;
}

.features-section h3{
  margin:0 0 12px 0;
  font-size:1.1rem;
  color:#0f172a;
  text-align:center;
}

.feature-list{
  display:flex;
  flex-direction:column;
  gap:10px;
}

.feature-item{
  display:flex;
  justify-content:space-between;
  align-items:center;
  padding:8px 12px;
  background:#fff;
  border-radius:6px;
  border-left:3px solid var(--accent);
}

.feature-label{
  font-weight:500;
  color:#4b5563;
  font-size:0.9rem;
}

.feature-value{
  font-weight:600;
  color:#0f172a;
  font-size:0.95rem;
}

.controls{
  margin-top:18px;
  display:flex;
  flex-direction:column;
  gap:8px;
}
button{
  cursor:pointer;
  padding:8px 12px;
  border-radius:8px;
  border:0;
  background:var(--accent);
  color:#fff;
}
button:disabled{
  opacity:0.5;
  cursor:not-allowed;
}
.details{
  color:var(--muted);
  margin-top:6px;
}
code{
  background:#f3f4f6;
  padding:2px 6px;
  border-radius:6px;
}
</style>
