import streamlit as st
from app.chatbot import agente_memoria

st.set_page_config(page_title="Chatbot Gemini + Wikipedia", layout="centered")

st.title("🤖 Chatbot con Gemini + Wikipedia")
st.markdown("Hazme una pregunta sobre filosofía, ciencia, economía, sociología, etc.")

# Inicializar historial en sesión
if "historial" not in st.session_state:
    st.session_state.historial = []

# Entrada del usuario
pregunta = st.text_input("Tu pregunta:", "")

if st.button("Enviar") and pregunta.strip():
    respuesta = agente_memoria.run(pregunta)
    st.session_state.historial.append(("🧑‍🎓 Tú", pregunta))
    st.session_state.historial.append(("🤖 Bot", respuesta))

# Mostrar el historial
for autor, mensaje in reversed(st.session_state.historial):
    st.markdown(f"**{autor}:** {mensaje}")
