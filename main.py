# import openai
# My Test Key
from openai import OpenAI
from colorama import init, Fore

init()

def chat_with_ai(prompt):
    client = OpenAI(
        api_key="Generate your Chatgpt api key"
    )

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error during API request: {e}")
        return "Sorry, I encountered an error while processing your request."


try:
    if __name__ == "__main__":
        while True:
            user_input = input(f"{Fore.YELLOW}You:{Fore.RESET} ")
            if user_input.lower() in ["quit", "exit", "bye"]:
                print(f"{Fore.RED}Goodbye!{Fore.RESET}")
                break

            response = chat_with_ai(user_input)
            print("\n" + "-" * 50)
            print(f"{Fore.GREEN}User:{Fore.RESET} {user_input}\n")
            print("-" * 50)
            print(f"{Fore.CYAN}Kobie:{Fore.RESET} {response}\n")
            print("-" * 50)

    from openai import OpenAI

except KeyboardInterrupt:
    print(f"{Fore.RED}\nProcess ended!!{Fore.RESET}")






