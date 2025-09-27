# 🩺 Medical Symptom Checker Chatbot

A conversational **AI-powered chatbot** designed to provide users with informational insights into their health symptoms.  
Users can describe their symptoms in a simple chat interface, and the application leverages the power of **Google's Gemini model** to offer potential causes, suggest next steps, and provide clear disclaimers about seeking professional medical advice.

---

## ✨ Features

- **Interactive Chat Interface**: A clean and user-friendly chat window for a seamless conversational experience.  
- **AI-Powered Symptom Analysis**: Utilizes Google's `gemini-1.5-flash` model to understand and analyze user-described symptoms.  
- **Secure API Key Input**: A sidebar for users to securely enter their Google API Key.  
- **Built-in Safety Protocols**: The AI is guided by a carefully engineered prompt that prioritizes user safety, provides responsible information, and recognizes potential emergencies.  
- **Session-Based Chat History**: Remembers the conversation within a single session, allowing for conversational context.  

---

## 🛠️ Technology Stack

- **Python**: Core programming language.  
- **Streamlit**: For building the interactive web user interface.  
- **LangChain**: Framework to structure and manage the interaction with the language model.  
- **Google Gemini**: Large Language Model (LLM) used for generating responses.  

---

## 🚀 Setup and Installation

Follow these steps to set up and run the project on your local machine.

### 1. Prerequisites
Ensure you have **Python 3.8+** installed.

### 2. Create a Virtual Environment (Recommended)

**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate

```
**For macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3.Install Dependencies
**Create a requirements.txt file and add:**
```bash
streamlit
langchain-google-genai
```
**Then install dependencies:**
```bash
pip install -r requirements.txt
```
## ▶️ How to Run the Application

### 1. Get a Google API Key
- Obtain an API key from [Google AI Studio](https://aistudio.google.com).

### 2. Run the Streamlit App
In your terminal, run:
```bash
streamlit run app.py
```
3. Use the Chatbot
Enter your Google API Key in the left sidebar.

Start typing your symptoms into the chat box to interact with the bot.

⚠️ Important Disclaimer
This chatbot is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.
Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

