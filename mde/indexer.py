import fnmatch
import os
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.vectorstores.base import VectorStore
from langchain.embeddings.base import Embeddings
from langchain.text_splitter import NLTKTextSplitter

from qdrant_client import QdrantClient


def index(directory_path: str, store: VectorStore, e: Embeddings):
    
    text_splitter = NLTKTextSplitter(chunk_size=1000)  
    files = find_markdown_files(directory_path)
    for f in files:
        print("Processing {}".format(f))
        loader = UnstructuredMarkdownLoader(f)
        doc = loader.load_and_split(text_splitter)
        store.add_documents(doc)


def find_markdown_files(directory):
    markdown_files = []
    
    for root, _, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, '*.md'):
            markdown_files.append(os.path.join(root, filename))

    return markdown_files