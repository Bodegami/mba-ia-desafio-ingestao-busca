import os
from dotenv import load_dotenv
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

for k in ("OPENAI_API_KEY", "DATABASE_URL", "PG_VECTOR_COLLECTION_NAME", "PDF_PATH"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

PDF_PATH = os.getenv("PDF_PATH", "document.pdf")

pdf = os.getenv("PDF_PATH", "document.pdf")


def ingest_pdf():
    current_dir = Path(__file__).parent

    candidate = Path(PDF_PATH)
    if not candidate.is_absolute():
        pdf_path = current_dir / candidate
    else:
        pdf_path = candidate

    if not pdf_path.exists():
        raise FileNotFoundError(
            f"PDF not found at: {pdf_path} (env PDF_PATH={PDF_PATH})"
        )

    docs = PyPDFLoader(str(pdf_path)).load()
    splits = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=150, add_start_index=False
    ).split_documents(docs)

    if not splits:
        raise SystemExit(0)

    enriched = []
    for d in splits:
        meta = {k: v for k, v in d.metadata.items() if v not in ("", None)}
        new_doc = Document(page_content=d.page_content, metadata=meta)
        enriched.append(new_doc)

    ids = [f"doc-{i}" for i in range(len(enriched))]

    embeddings = OpenAIEmbeddings(
        model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
    )

    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True,
    )

    store.add_documents(documents=enriched, ids=ids)


if __name__ == "__main__":
    ingest_pdf()
