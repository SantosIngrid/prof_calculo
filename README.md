###Professor de Cálculo I Offline (LLaMA + Apostila Cálculo UERJ)

Este projeto cria um **professor virtual de Cálculo I**, capaz de explicar conceitos, resolver exercícios passo a passo e tirar dúvidas — **tudo rodando localmente**, sem depender de internet ou APIs externas.

A base de conhecimento utilizada é a apostila **"UERJ.pdf"** disponível através do link **https://www.ime.unicamp.br/~deleo/MS123/UERJ.pdf**, processado em trechos com embeddings e armazenado em um banco vetorial ChromaDB.  
O modelo de linguagem é executado via **Ollama** com **LLaMA**, garantindo privacidade e liberdade para estudo.

---

##Objetivo do Projeto

- Permitir estudar **Cálculo I** com um professor personalizado.
- Responder dúvidas com base no conteúdo da apostila da Universidade Estadual do Rio de Janeiro.
- Gerar explicações passo a passo, exemplos e exercícios.
- Funcionar **completamente offline**, ideal para ambientes sem internet.
- Servir como base para evolução futura (ex.: interface web, chatbot, telegram bot etc).

---

## Arquitetura do Sistema

| Componente | Função |
|-----------|--------|
| **Ollama** | Executa o modelo LLaMA localmente. |
| **LangChain** | Orquestra prompts e pipeline de perguntas. |
| **Sentence Transformers** | Gera embeddings dos trechos do livro. |
| **ChromaDB** | Armazena a base vetorial para busca semântica. |
| **Python** | Código principal. |

---

## Requisitos

- Linux (Ubuntu recomendado)
- Python 3.10+
- Conda (opcional, mas recomendado)
- 8GB de RAM (16GB recomendado)
- **Ollama instalado**
- Modelo LLaMA baixado via Ollama

---

## Instalação

### 1) Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/professor-calculo.git
cd professor-calculo
```
### 2) Crie o ambiente:
```bash
conda create -n prof_calculo python=3.11 -y
conda activate prof_calculo
```
### 3) Instale as depêndencias:
```bash
pip install -r requirements.txt
```
### 4) Instale o Ollama:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
### 5)Baixe o modelo LlaMa:
```bash
ollama pull llama3.2:1b
```
### 6) Criando as bases (inserindo o arquivo PDF na pasta)
```bash
python criar_base.py
```

### 7) Executando o professor:
```bash
python professor.py
```

Exemplo de pergunta:  "Explique o que é limite com exemplos simples."

Personalização do Estilo de Ensino

O professor pode ser configurado para:

Estilo	Descrição
1	Didático e paciente
2	Direto ao ponto
3	Com foco em exercícios
4	Estilo militar / ITA (sem dó 😅)

Edite no arquivo professor.py o prompt inicial para ajustar o estilo.

Próximos Passos (Roadmap)
Criar interface web com Streamlit / Gradio
Adicionar módulo de resolução de exercícios automatizada
Criar versão chatbot Telegram

Contribuições

Contribuições são bem-vindas!
Se quiser sugerir melhorias, abra uma issue ou envie um pull request.

Observação Legal

Este projeto é apenas para fins de estudo pessoal.
Se você possui o livro (outra fonte de dados como um livro do Guidorizzi por exemplo) , respeite os direitos autorais e não distribua o PDF.
