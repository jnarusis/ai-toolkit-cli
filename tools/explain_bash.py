from shared.gpt_helper import gpt_chat

def breakdown_bash_script():
    print("\nPaste the Bash script you want explained. Type ':end' on a new line when finished:")
    lines = []
    while True:
        line = input()
        if line.strip() == ":end":
            break
        lines.append(line)
    script = "\n".join(lines)

    messages = [
        {"role": "system", "content": "You are a Bash expert who explains each line of a script in detail."},
        {"role": "user", "content": script}
    ]
    response = gpt_chat(messages, model="gpt-4o")
    print("\n=== Script Breakdown ===\n")
    print(response)
    return response
