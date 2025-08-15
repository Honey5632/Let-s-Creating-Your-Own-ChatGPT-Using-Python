# 🤖 Kobie AI Chatbot

Kobie is your personal AI assistant built in Python — with **persistent memory**, **custom personality modes**, **plugins** (weather, Python code execution, etc.), **voice capabilities**, and **real-time web search integration**.  
It’s like having your own local ChatGPT, but fully customizable and with saved conversations across sessions.

---

## ✨ Features

- 💬 **Persistent conversation memory** — Kobie remembers your past chats even after closing the program.
- 🧠 **Memory optimization** — old chats are summarized to keep performance high.
- 🎭 **Custom personality modes** — switch between `Friendly`, `Professional`, or `Funny`.
- 🖥 **Python code executor** — run Python code directly inside the chat.
- 🌐 **Web search plugin** — fetch real-time data from the internet (Google/DuckDuckGo).
- ⏱ **Typing effect** for more natural responses.
- ⚡ **Performance improvements** — keeps last N messages, async-ready structure.

---

## 📂 Project Structure

kobie_chatbot/
├── kobie.py # Main chatbot script
├── kobie_chat_history.json # Saved conversation history
├── weather_api_key.txt # (Optional) Weather API key storage
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 🔧 Installation

### 1️⃣ Clone the Repository
Make sure you have Python 3.8+ installed.
```bash
git clone https://github.com/yourusername/kobie-chatbot.git
cd kobie-chatbot
```

### 2️⃣ Install required libraries
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Your OpenAI API Key

You’ll need an OpenAI API key for Kobie to work.
Get it here: https://platform.openai.com

### Edit the API_KEY variable in kobie.py:
API_KEY = "your_openai_api_key_here"

## 🚀 Usage

Run the chatbot:
```python
python kobie.py
```

## You can now:
- Chat normally — just type messages.
- Quit — type quit, exit, or bye.
- Change personality — /personality friendly, /personality professional, /personality funny
- Python execution — /py print(2+2)
- Web search — /search latest AI news

## 🧠 Memory Management

- Kobie stores all conversations in kobie_chat_history.json.
- If the file grows too large, old conversations are summarized automatically.
- This keeps responses fast and relevant.

## 🛠 Future Ideas

- Web dashboard with Flask or FastAPI
- Plugin marketplace
- Support for multiple AI models
- Telegram/Discord integration

## ⚠️ Disclaimer
- You are responsible for your own OpenAI usage and costs.
- Python code execution is sandboxed but still execute with caution.
