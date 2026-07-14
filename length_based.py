from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Load PDF
loader = PyPDFLoader("9.langchain-text-splitters/dl-curriculum.pdf")

docs = loader.load()

# Create text splitter
splitter = CharacterTextSplitter(
    separator="",
    chunk_size=200,
    chunk_overlap=0
)

# Split the PDF into chunks
result = splitter.split_documents(docs)

print("Total Pages:", len(docs))
print("Total Chunks:", len(result))
print("-" * 50)

print(result[1].page_content)
print("-" * 50)

print(result[1].metadata)