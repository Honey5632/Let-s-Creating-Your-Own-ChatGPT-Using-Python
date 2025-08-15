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
```bash
git clone https://github.com/yourusername/kobie-chatbot.git
cd kobie-chatbot
```
### Install required libraries
```bash
pip install -r requirements.txt
```
