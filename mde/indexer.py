from langchain.document_loaders import DirectoryLoader
from langchain.vectorstores.base import VectorStore
from langchain.embeddings.base import Embeddings
from langchain.text_splitter import NLTKTextSplitter

def index(directory_path: str, store: VectorStore, e: Embeddings):
    loader = DirectoryLoader(directory_path, glob="**/*.md")
    docs = loader.load_and_split(NLTKTextSplitter(chunk_size=1000))
    store.add_documents(docs)
