import json
import os
import traceback
from openai import OpenAI
from colorama import init, Fore

init()

# ================= CONFIG =================
API_KEY = ("your_openai_api_key_here")
HISTORY_FILE = "kobie_chat_history.json"
MAX_DETAILED_MESSAGES = 10
# ===========================================

client = OpenAI(api_key=API_KEY)

# ===== Personality Modes =====
PERSONALITIES = {
    "default": "You are Kobie, a witty, knowledgeable AI who explains clearly.",
    "funny": "You are Kobie, a hilarious comedian who answers everything with humor.",
    "serious": "You are Kobie, a highly focused assistant who gives concise answers.",
    "teacher": "You are Kobie, a patient teacher who explains concepts step-by-step."
}


def load_conversation():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return [{"role": "system", "content": PERSONALITIES["default"]}]


def save_conversation(messages):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)


def summarize_old_history(messages):
    if len(messages) <= MAX_DETAILED_MESSAGES + 1:
        return messages
    system_msg = messages[0]
    old_msgs = messages[1:-MAX_DETAILED_MESSAGES]
    recent_msgs = messages[-MAX_DETAILED_MESSAGES:]

    summary_prompt = [
        {"role": "system", "content": "Summarize the conversation briefly for AI memory."},
        {"role": "user", "content": json.dumps(old_msgs, ensure_ascii=False)}
    ]
    summary = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=summary_prompt
    ).choices[0].message.content

    return [system_msg, {"role": "system", "content": f"Summary of earlier conversation: {summary}"}] + recent_msgs


# ===== Plugins =====

def run_python_code(code):
    try:
        safe_locals = {}
        exec(code, {"__builtins__": {}}, safe_locals)
        return f"Output: {safe_locals}"
    except Exception:
        return "Error:\n" + traceback.format_exc()


def chat_with_ai(prompt, messages):
    if prompt.startswith("/run"):
        code = prompt.replace("/run", "").strip()
        return run_python_code(code), messages

    elif prompt.startswith("/mode"):
        mode = prompt.replace("/mode", "").strip().lower()
        if mode in PERSONALITIES:
            messages[0] = {"role": "system", "content": PERSONALITIES[mode]}
            save_conversation(messages)
            return f"Switched personality to: {mode}", messages
        else:
            return f"Available modes: {', '.join(PERSONALITIES.keys())}", messages

    # Normal AI conversation
    messages.append({"role": "user", "content": prompt})
    messages = summarize_old_history(messages)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    reply = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    save_conversation(messages)
    return reply, messages


if __name__ == "__main__":
    messages = load_conversation()
    print(Fore.GREEN + "Kobie ready! Type /run <python>, /mode <type>, or chat normally." + Fore.RESET)

    try:
        while True:
            user_input = input(f"{Fore.YELLOW}You:{Fore.RESET} ")
            if user_input.lower() in ["quit", "exit", "bye"]:
                print(f"{Fore.RED}Goodbye!{Fore.RESET}")
                break

            response, messages = chat_with_ai(user_input, messages)
            print(f"{Fore.CYAN}Kobie:{Fore.RESET} {response}\n")

    except KeyboardInterrupt:
        print(f"{Fore.RED}\nProcess ended!!{Fore.RESET}")

