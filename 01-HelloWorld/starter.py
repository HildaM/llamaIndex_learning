from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.embeddings import resolve_embed_model

# Don't Import "from openai import OpenAI". It will panic
from llama_index.llms import OpenAI

# load data
documents = SimpleDirectoryReader("data").load_data()

# bge-m3 embedding model
embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")

# set LM Studio
llm = OpenAI(api_base="http://localhost:1234/v1", api_key="not-needed")

# Index the data
service_context = ServiceContext.from_defaults(
    embed_model=embed_model, llm=llm,
)
index = VectorStoreIndex.from_documents(
    documents, service_context=service_context
)

# query
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)