from ingestion.loadder import youtube_load
from chunking.chunker import split_docs
from embeddings.embed import get_embedding
from vector_store.faiss_store import create_embeddings
from retrieval.retriever import get_retriever
from prompt.prompt_temp import get_prompt
from llm.model import get_llm


def main():

    print("Loading YouTube Transcript...")

    # Step 1: Load transcript
    documents = youtube_load("o126p1QN_RI")

    # Step 2: Split into chunks
    chunks = split_docs(documents)

    # Step 3: Load embedding model
    embedding_model = get_embedding()

    # Step 4: Create FAISS vector store
    vector_store = create_embeddings(
        chunks,
        embedding_model
    )

    # Step 5: Create retriever
    retriever = get_retriever(vector_store)

    # Step 6: Load prompt
    prompt = get_prompt()

    # Step 7: Load LLM
    llm = get_llm()

    print("\nRAG is Ready!")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("Question: ")

        if question.lower() == "exit":
            break

        # Retrieve relevant chunks
        retrieved_docs = retriever.invoke(question)

        # Build context
        context = "\n\n".join(
            doc.page_content for doc in retrieved_docs
        )

        # Create final prompt
        final_prompt = prompt.invoke(
            {
                "context": context,
                "question": question
            }
        )

        # Generate answer
        response = llm.invoke(final_prompt)

        print("\nAnswer:\n")
        print(response.content)
        print("-" * 60)


if __name__ == "__main__":
    main()