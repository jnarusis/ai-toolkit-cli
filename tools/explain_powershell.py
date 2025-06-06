from shared.gpt_helper import gpt_chat

def breakdown_powershell_script():
    print("\nPaste the PowerShell script you want explained. Type ':end' on a new line when finished:")
    lines = []
    while True:
        line = input()
        if line.strip() == ":end":
            break
        lines.append(line)
    script = "\n".join(lines)

    messages = [
        {"role": "system", "content": "You are a PowerShell expert. Break down the script line-by-line with clear explanations."},
        {"role": "user", "content": script}
    ]
    response = gpt_chat(messages, model="gpt-4o")

    print("\n=== PowerShell Script Breakdown ===\n")
    print(response)
    return response
