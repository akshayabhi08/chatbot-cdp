from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
import os

# Schema for the index
schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True), path=ID(stored=True))

# Create or open the index
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
    ix = create_in("indexdir", schema)
else:
    ix = open_dir("indexdir")

def search_docs(intent, cdp):
    """
    Search the documentation for relevant sections.
    """
    query_str = f"{intent} {cdp}"
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        results = searcher.search(query, limit=1)
        if results:
            return results[0]['content']
        else:
            return "Sorry, I couldn't find any relevant information."