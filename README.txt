
INSTRUCTIONS TO RUN THE CHATBOT LOCALLY:

1. Install Ollama (only once):
   curl -fsSL https://ollama.com/install.sh | sh

2. Download the llama3 model (automatically done when running):
   ollama run llama3

3. Open a new terminal and start the backend server:
   cd backend
   pip install -r requirements.txt
   python app.py

4. Open frontend/index.html in a browser.( python -m http.server 8000 )


Start chatting with your AI!
