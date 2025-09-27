import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def main():
    """
    This function creates the main Streamlit application for the medical chatbot.
    It sets up the UI, initializes the language model, and handles user interaction.
    """
    st.set_page_config(page_title="Medical Symptom Checker", page_icon="🩺", layout="centered")

    st.title("🩺 Medical Symptom Checker Chatbot")

    # --- Sidebar for API Key Input ---
    with st.sidebar:
        st.header("Configuration")
        api_key = st.text_input("Enter your Google API Key", type="password", key="api_key_input")
        if api_key:
            st.success("API Key provided!")
        else:
            st.warning("Please enter your Google API Key.")

    st.markdown("""
    Welcome! Describe your symptoms, and I'll provide you with potential insights.
    **Disclaimer:** This chatbot is for informational purposes only and is not a substitute for professional medical advice. Please consult a doctor for any health concerns.
    """)

    # --- Check for API Key before proceeding ---
    if not api_key:
        st.info("Please enter your Google API Key in the sidebar to start the chatbot.")
        st.stop()  # Stop the app from running further

    # Set the environment variable once we have the key
    os.environ["GOOGLE_API_KEY"] = api_key

    # --- Initialize Chat Model and Chain ---
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

        # Enhanced prompt template for better medical context
        prompt_template = """
        You are an advanced AI medical assistant. Your role is to analyze user-described symptoms
        and provide a concise, clear, and informative response.

        **Instructions for the AI:**
        1.  **Analyze Symptoms:** Carefully read the user's query to understand the symptoms they are experiencing.
        2.  **Provide Potential Causes:** Based on the symptoms, list potential, common medical conditions that could be related. Do not provide a definitive diagnosis.
        3.  **Suggest Next Steps:** Recommend general next steps, such as monitoring symptoms, home care tips (if applicable), or when it's crucial to see a doctor.
        4.  **Crucial Disclaimer:** ALWAYS end your response with a clear and prominent disclaimer: "This is not a medical diagnosis. Please consult a healthcare professional for an accurate diagnosis and treatment plan."
        5.  **Tone:** Maintain a helpful, empathetic, and professional tone.
        6.  **Safety First:** If the user describes symptoms that could indicate a medical emergency (e.g., chest pain, difficulty breathing, severe bleeding), your primary and immediate advice should be to seek emergency medical help (e.g., "call 911" or "go to the nearest emergency room immediately").

        **User's Query:**
        {query}

        **Your Response:**
        """

        prompt = PromptTemplate(
            input_variables=["query"],
            template=prompt_template
        )

        # Using LangChain Expression Language (LCEL) for the chain
        # This is the modern way and avoids the deprecation warnings.
        output_parser = StrOutputParser()
        llm_chain = prompt | llm | output_parser

    except Exception as e:
        st.error(f"Error initializing the language model: {e}")
        st.info("Please check your Google API key and ensure it is correct.")
        return  # Stop execution if the model fails to load

    # --- User Input and Chat History ---
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Get new user input
    user_query = st.chat_input("Describe your symptoms...")

    if user_query:
        # Add user message to session state and display it
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)

        # Generate and display bot response
        with st.chat_message("assistant"):
            with st.spinner("Analyzing your symptoms..."):
                try:
                    # Using .invoke() instead of the deprecated .run()
                    response = llm_chain.invoke({"query": user_query})
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"An error occurred while generating a response: {e}")


if __name__ == "__main__":
    main()

