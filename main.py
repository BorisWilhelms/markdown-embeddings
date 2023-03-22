#!/usr/bin/env python3

import os
import sys
from typing import List

from mde.db import initialize
from mde.indexer import index
from mde.query import query

from qdrant_client import QdrantClient
from langchain.vectorstores import Qdrant
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings import OpenAIEmbeddings

def main(args: List[str]):
    collection = "tt-readme-hf"
    e = HuggingFaceEmbeddings()
    dim = 768

    # collection = "tt-readme-hf-3"
    # e = HuggingFaceEmbeddings(model_name="distiluse-base-multilingual-cased-v2")
    # dim = 512

    # collection = "tt-readme-oi"
    # e = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    # dim = 1536

    client = QdrantClient("localhost", port=6333)
    qdrant = Qdrant(client, collection, embedding_function=e.embed_query)

    command = args[1]
    match command:
        case "init-db":
            initialize(collection, client, dim)
        case "index":
            if len(args) <= 2:
                help(args[0])
            index(args[2], qdrant, e)
        case "query":
            if len(args) <= 2:
                help(args[0])
            query(args[2], qdrant, e)
        case _:
            help

def help(executable: str):
    print("{} COMMAND [arguments]".format(executable))
    print("Available commands")
    print("  init-db   Initializes the database. No argument")
    print("  index     Indexes a path. Argument is a path")
    print("  query     Runs a query. Argument is the query")
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help(sys.argv[0])
    main(sys.argv)
