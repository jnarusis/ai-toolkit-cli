from shared.gpt_helper import gpt_chat

def explain_linux_concept():
    topic = input("\nWhat concept do you want explained? ")
    messages = [
        {"role": "system", "content": "You are a Linux tutor who explains clearly and simply."},
        {"role": "user", "content": topic}
    ]
    response = gpt_chat(messages, model="gpt-3.5-turbo")
    print("\n=== Explanation ===\n")
    print(response)
    return response
