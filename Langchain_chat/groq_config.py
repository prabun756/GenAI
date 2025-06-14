from langchain_groq import ChatGroq

def get_grqu_llm():
    return ChatGroq(
        model_name = "llama3-8b-8192",
        groq_api_key = "XYZ",
        temperature=0.5
    )
