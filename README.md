# Norman Sicily Historical Chatbot

This project is a natural language chatbot designed to analyze historical relationships between people and places in Norman Sicily using structured data and vectorized documents.

**Features**

1. Uses Azure OpenAI GPT-4o to generate pandas queries from natural language.

2. Supports two main dataframes: people_to_places_df and places_to_places_df.

3. Includes document search with semantic retrieval (RAG).

4. Streamlit-based user interface for interaction.

**Setup Instructions**

Install Required Dependencies

pip install openai
pip install langchain
pip install langchain_openai
pip install -U langchain-community
pip install chromadb
pip install streamlit
pip install sentence-transformers

**Environment Variables**

Replace the following with your credentials: 

- AZURE_OPENAI_API_KEY=your_api_key_here
- AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
- AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
- AZURE_OPENAI_API_VERSION=2024-12-01-preview

**Running the Chatbot**

Streamlit Web Interface:

streamlit run streamlit_app.py

This will open a web-based chat interface in your browser.

**Data Files**

Ensure the following files are in the same directory:

people_to_places.csv

places_to_places.csv

combined_output.txt

These are loaded at runtime by the chatbot.
