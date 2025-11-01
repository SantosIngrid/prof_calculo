import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate

DB_PATH = "db_calculo"
EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"
LLM_MODEL = "llama3.2:1b"   

def inicializar_professor():
    """
    Inicializa e retorna a cadeia de QA (RetrievalQA) do professor de cálculo.
    """

    if not os.path.isdir(DB_PATH):
        print(f"Erro: Base '{DB_PATH}' não encontrada.")
        print("Execute primeiro: python criar_base.py")
        return None

    print("Carregando base de conhecimento...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    db = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)

    retriever = db.as_retriever(search_kwargs={"k": 3})
    llm = Ollama(model=LLM_MODEL)

    prompt_template = """
Você é um professor de Cálculo I com didática clara e progressiva, semelhante à do Guidorizzi.
Siga as instruções:

1. Explique passo a passo, sem pular etapas.
2. Use linguagem simples, mas precisa.
3. Se necessário, reexplique em outras palavras.
4. No final, proponha um exercício simples relacionado ao conteúdo.

CONTEXTO (retirado do livro):
{context}

PERGUNTA DO ALUNO:
{question}

RESPOSTA DO PROFESSOR:
"""

    PROMPT = PromptTemplate(
        input_variables=["context", "question"],
        template=prompt_template
    )

    print("Inicializando cadeia RAG...")
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": PROMPT},
        return_source_documents=True
    )

    return chain


def iniciar_chat(professor_chain):
    """
    Inicia o chat com o professor.
    """
    print("\n🎓 Professor de Cálculo I iniciado!")
    print("Digite sua pergunta (ou 'sair'):\n")

    while True:
        pergunta = input("Você: ")

        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Até a próxima")
            break

        
        resposta = professor_chain.invoke({"query": pergunta})

        print("\n Professor:\n")
        print(resposta["result"], "\n")

        # Para ver de onde veio a resposta:
        # print("Fontes:", [doc.metadata['page'] for doc in resposta['source_documents']])


if __name__ == "__main__":
    professor = inicializar_professor()
    if professor:
        iniciar_chat(professor)
