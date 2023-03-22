from qdrant_client import QdrantClient
from qdrant_client.http import models

def initialize(collection_name: str, client: QdrantClient, size: int):
    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(size=size, distance=models.Distance.COSINE),
    )

