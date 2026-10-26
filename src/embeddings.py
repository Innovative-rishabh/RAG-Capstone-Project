
"""
File: embeddings.py

Description:
------------
Google Gemini embedding model setup for the RAG project.

Text chunks are converted into numeric vectors so that documents
can be searched by meaning rather than exact keyword matches.

Workflow:
    Text Chunk → Gemini Embedding Model → Vector
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings


# ---------------------------------------------------------
# Load environment variables from the project's .env file
# ---------------------------------------------------------
load_dotenv()


# ---------------------------------------------------------
# Default Gemini embedding model
# ---------------------------------------------------------
DEFAULT_EMBEDDING_MODEL = "gemini-embedding-001"


# ---------------------------------------------------------
# Create the Gemini embedding model
# ---------------------------------------------------------
def get_embedding_model(
    model_name: str | None = None,
) -> GoogleGenerativeAIEmbeddings:
    """
    Create and return a Google Gemini embedding model.

    Args:
        model_name (str | None):
            Optional embedding model name. If omitted, the function
            reads EMBEDDING_MODEL from the .env file or uses the default.

    Returns:
        GoogleGenerativeAIEmbeddings:
            Configured Gemini embedding client.

    Raises:
        ValueError:
            If GEMINI_API_KEY is missing.
        RuntimeError:
            If the embedding client cannot be initialized.
    """

    # Read Gemini API key
    api_key = os.getenv("GEMINI_API_KEY", "").strip()

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is missing. "
            "Add your Gemini API key to the .env file."
        )

    # Select embedding model
    selected_model = (
        model_name
        or os.getenv(
            "EMBEDDING_MODEL",
            DEFAULT_EMBEDDING_MODEL,
        ).strip()
    )

    if not selected_model:
        selected_model = DEFAULT_EMBEDDING_MODEL

    try:
        # Initialize Gemini embeddings
        embeddings = GoogleGenerativeAIEmbeddings(
            model=selected_model,
            google_api_key=api_key,
        )

        return embeddings

    except Exception as exc:
        raise RuntimeError(
            "Failed to initialize the Gemini embedding model. "
            "Check your GEMINI_API_KEY, EMBEDDING_MODEL, package "
            "installation, internet connection, and API quota."
        ) from exc


# ---------------------------------------------------------
# Get the configured embedding model name for the UI
# ---------------------------------------------------------
def get_embedding_model_name() -> str:
    """
    Return the configured Gemini embedding model name.

    Returns:
        str: The embedding model name configured in .env.
    """

    return (
        os.getenv(
            "EMBEDDING_MODEL",
            DEFAULT_EMBEDDING_MODEL,
        ).strip()
        or DEFAULT_EMBEDDING_MODEL
    )
