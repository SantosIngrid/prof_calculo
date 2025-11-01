import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import torch

PDF_PATH = "UERJ.pdf"
DB_PATH = "db_calculo"

def criar_base_vetorial():
    """
    Cria uma base de dados vetorial a partir de um arquivo PDF.
    """
    if not os.path.exists(PDF_PATH):
        print(f" Erro: Arquivo PDF não encontrado em '{PDF_PATH}'")
        return

    print("Carregando PDF...")
    loader = PyPDFLoader(PDF_PATH)
    # Usar lazy_load para otimizar o uso de memória com arquivos grandes
    docs = loader.load()

    print("Dividindo em blocos...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    print("Configurando o dispositivo para embeddings (GPU se disponível)...")
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Usando dispositivo: {device}")
    
    print("Gerando embeddings...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2",
        model_kwargs={'device': device}
    )

    print("Criando e persistindo o banco de conhecimento...")
    Chroma.from_documents(chunks, embeddings, persist_directory=DB_PATH)

    print(f"\n Base criada com sucesso em: '{DB_PATH}'")

if __name__ == "__main__":
    criar_base_vetorial()
