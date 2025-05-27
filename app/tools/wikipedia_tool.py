from langchain_community.utilities import WikipediaAPIWrapper

wikipedia = WikipediaAPIWrapper(top_k_results=2, lang="es")
