from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
Your job is to answer questions using ONLY the restaurant reviews
provided below.

If the reviews do not contain enough information to answer the question,
say that you don't have enough information.

Do not make up information.

Relevant restaurant reviews:

{reviews}

Question:

{question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def format_documents(documents):
    formatted_reviews = []

    for document in documents:
        rating = document.metadata.get("rating", "Unknown")
        date = document.metadata.get("date", "Unknown")

        formatted_reviews.append(
            f"""
Review:
{document.page_content}

Rating: {rating}
Date: {date}
"""
        )

    return "\n---\n".join(formatted_reviews)

while True:
    print("\n" + "-" * 50)

    question = input("Ask your question: ").strip()

    if question.lower() == "q":
        print("Goodbye!")
        break

    if not question:
        print("Please enter a question.")
        continue

    try:
        documents = retriever.invoke(question)

        if not documents:
            print("I couldn't find any relevant reviews.")
            continue

        reviews = format_documents(documents)

        result = chain.invoke(
            {
                "reviews": reviews,
                "question": question,
            }
        )

        print("\nAnswer:")
        print(result)

    except Exception as e:
        print(f"\nError: {e}")