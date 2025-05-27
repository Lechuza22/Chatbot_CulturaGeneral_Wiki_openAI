# 🤖 Chatbot Cultura General - Streamlit + LangChain + OpenAI

Este es un proyecto didáctico de chatbot desarrollado con **Streamlit**, **LangChain** y **OpenAI**, capaz de responder preguntas de cultura general, filosofía, economía, sociología, matemáticas y más. Usa **Wikipedia como fuente externa de conocimiento** y **memoria conversacional** para mantener el contexto. Está preparado para ser desplegado en **Streamlit Cloud**.

---

## 🚀 Funcionalidades

- 🧠 Integra un modelo LLM (OpenAI GPT / Gemini)
- 📚 Consulta datos directamente desde Wikipedia
- 💬 Soporte de memoria conversacional
- 🛠️ Arquitectura modular usando agentes de LangChain
- 🌐 Interfaz simple y responsiva con Streamlit
- ☁️ Desplegable en la nube de [Streamlit Cloud](https://share.streamlit.io)

---

## 📁 Estructura del proyecto

```
chatbot_culturageneral_wiki_openai/
├── chatbot_ui.py              # Interfaz principal de Streamlit
├── requirements.txt           # Librerías necesarias
├── .env.example               # Variables de entorno de ejemplo
├── app/
│   ├── __init__.py
│   ├── config.py              # Lectura de API keys
│   ├── chatbot.py             # Agente con memoria y herramientas
│   └── tools/
│       ├── __init__.py
│       └── wikipedia_tool.py  # Tool de Wikipedia para LangChain
```

---

## 🧪 Requisitos

- Python 3.10 o superior
- Cuenta con API Key de [OpenAI](https://platform.openai.com/account/api-keys)
- Opcional: API Key de [Google Gemini](https://makersuite.google.com/app) si preferís usar Gemini

---

## 🔧 Configuración local

1. Cloná el repositorio:

```bash
git clone https://github.com/tu-usuario/chatbot_culturageneral_wiki_openai.git
cd chatbot_culturageneral_wiki_openai
```

2. Crea el entorno virtual y activalo:

```bash
python -m venv .venv
.venv\Scripts\activate      # En Windows
source .venv/bin/activate  # En Linux/macOS
```

3. Instalá las dependencias:

```bash
pip install -r requirements.txt
```

4. Crea un archivo `.env` con tu clave de API:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx
```

5. Ejecutá la app:

```bash
streamlit run chatbot_ui.py
```

---

## ☁️ Despliegue en Streamlit Cloud

1. Subí el repositorio a GitHub
2. Iniciá sesión en [Streamlit Cloud](https://share.streamlit.io)
3. Seleccioná tu repo y como archivo principal indicá: `chatbot_ui.py`
4. Configurá las **secrets** desde el menú → _Manage App_ → _Secrets_:

```ini
OPENAI_API_KEY = "tu_clave"
```

---

## 🧠 Aprendizajes

Este proyecto está orientado al aprendizaje de:

- Integración de LLMs con herramientas externas (Wikipedia)
- Uso de memoria en LangChain
- Despliegue de apps en la nube con Streamlit
- Uso modular y escalable de agentes conversacionales

---

## 📜 Licencia

Este proyecto es de uso educativo y libre bajo la licencia MIT.

---

Desarrollado con 💻 por [Jerónimo Martínez](https://github.com/jeronimomartinez)
