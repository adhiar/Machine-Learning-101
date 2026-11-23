import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.knowledge.embedder.sentence_transformer import SentenceTransformerEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.models.groq import Groq
load_dotenv()
# Must match the values used when the PDF/CSV data was ingested.
knowledge = Knowledge(
    vector_db=LanceDb(
        table_name="layanan",
        uri="token/lancedb",
        search_type=SearchType.vector,
        embedder=SentenceTransformerEmbedder())
)

agent = Agent(
    model=Groq(id="qwen/qwen3.8-27b"),
    knowledge=knowledge,
    search_knowledge=True,
    markdown=True,
)

agent.print_response(
    "Mau Ukur resistansi internal baterai",
    stream=True,
)