from shared.gpt_helper import gpt_chat

def explain_windows_concept():
    concept = input("\nWhat Windows or PowerShell concept do you want explained? ")

    messages = [
        {"role": "system", "content": "You are a Windows systems expert who explains clearly and simply."},
        {"role": "user", "content": concept}
    ]
    response = gpt_chat(messages, model="gpt-3.5-turbo")

    print("\n=== Windows/PowerShell Concept Explanation ===\n")
    print(response)
    return response
