# https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/root.html
# Document is the important type in the LLaMaIndex

from llama_index import SimpleDirectoryReader

# load data from file
document = SimpleDirectoryReader(
    input_files=["./data/king.dreamspeech.excerpts.pdf"]
).load_data()

# Look into the type of "Document"
print(type(document), '\n')
print(len(document), '\n')
print(type(document[0]), '\n')
print(document[0])