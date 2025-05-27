from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool, initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory

from app.config import OPENAI_API_KEY
from app.tools.wikipedia_tool import wikipedia

# Modelo de OpenAI
llm = ChatOpenAI(
    model="gpt-3.5-turbo",  # o "gpt-4" si tenés acceso
    openai_api_key=OPENAI_API_KEY,
    temperature=0.7
)

herramientas = [
    Tool(
        name="Buscar en Wikipedia",
        func=wikipedia.run,
        description="Usa esta herramienta para buscar información en Wikipedia sobre temas generales."
    )
]

memoria = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

agente_memoria = initialize_agent(
    tools=herramientas,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memoria,
    verbose=True
)
