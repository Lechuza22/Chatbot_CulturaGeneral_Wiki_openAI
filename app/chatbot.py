from langchain_community.chat_models import ChatOpenAI
from langchain.agents import Tool, initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage, HumanMessage

from app.config import OPENAI_API_KEY
from app.tools.wikipedia_tool import wikipedia

# Mensaje del sistema para establecer el estilo de las respuestas
sistema = SystemMessage(
    content=(
        "Respondé de manera clara, estructurada y atractiva. "
        "Usá títulos, emojis y viñetas cuando sea útil. "
        "Organizá la información en secciones si es posible."
    )
)

# Modelo de OpenAI
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    openai_api_key=OPENAI_API_KEY,
    temperature=0.7
)

# Herramientas
herramientas = [
    Tool(
        name="Buscar en Wikipedia",
        func=wikipedia.run,
        description="Usa esta herramienta para buscar información en Wikipedia sobre temas generales."
    )
]

# Memoria conversacional
memoria = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Agente con memoria y estilo guiado
agente_memoria = initialize_agent(
    tools=herramientas,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memoria,
    verbose=True,
    agent_kwargs={
        "system_message": sistema
    }
)  
