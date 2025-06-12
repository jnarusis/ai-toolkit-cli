import openai
import os

def interactive_tutor():
    print("\n=== AI Sysadmin Tutor Mode ===\n")
    print("You can ask any question about Windows Server, Ubuntu/Linux, networking, scripting, or general sysadmin tasks.")
    print("Type 'exit' to return to the main menu.\n")

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ['exit', 'quit']:
            print("\nReturning to main menu...\n")
            break

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful, experienced system administrator. "
                            "Your job is to assist the user with technical tasks related to homelabs, "
                            "Windows Server, Linux systems, scripting, networking, and infrastructure configuration. "
                            "Always give direct, accurate, step-by-step answers where appropriate."
                        )
                    },
                    {"role": "user", "content": user_input}
                ]
            )
            reply = response.choices[0].message.content
            print(f"\nAssistant:\n{reply}\n")
        except Exception as e:
            print(f"\nError communicating with OpenAI: {e}\n")
