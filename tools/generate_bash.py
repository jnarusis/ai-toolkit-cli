from shared.gpt_helper import gpt_chat

def generate_bash_script():
    task = input("\nDescribe the Bash script you want: ")
    messages = [
        {"role": "system", "content": "You are a Linux shell expert. Return only the script code."},
        {"role": "user", "content": task}
    ]
    response = gpt_chat(messages, model="gpt-4o")
    print("\n=== Bash Script Output ===\n")
    print(response)
    return response
