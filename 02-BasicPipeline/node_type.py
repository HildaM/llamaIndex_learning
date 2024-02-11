# https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/root.html
from llama_index import SimpleDirectoryReader
from llama_index.node_parser import SentenceSplitter

# load data from file
document = SimpleDirectoryReader(
    input_files=["./data/king.dreamspeech.excerpts.pdf"]
).load_data()

# get nodes from document
parser = SentenceSplitter(
    chunk_size=100,
    chunk_overlap=10,
)
nodes = parser.get_nodes_from_documents(document)

# Look into the type of "Node"
print(type(nodes), '\n')
print(len(nodes), '\n')
print(type(nodes[0]), '\n')
print(nodes[0])

for i in range(len(nodes)):
    print(nodes[i], '\n')