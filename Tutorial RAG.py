from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.csv_reader import CSVReader
from agno.knowledge.embedder.sentence_transformer import SentenceTransformerEmbedder
from agno.vectordb.lancedb import LanceDb

knowledge = Knowledge(
    vector_db=LanceDb(
        table_name="layanan",
        uri="token/lancedb",
        embedder=SentenceTransformerEmbedder()
    )
)

knowledge.insert(
    name="Layanan-1",
    path="Dummy.csv",
    reader=CSVReader(),
    upsert=True,
)
