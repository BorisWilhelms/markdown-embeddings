from langchain.embeddings.base import Embeddings
from langchain.vectorstores.base import VectorStore

def query(query: str, store: VectorStore, e: Embeddings):
    results = store.similarity_search(query)

    for r in results:
        print("-----")
        print("Source: {}".format(r.metadata["source"]))
        print("Summary: {}".format(r.summary))

