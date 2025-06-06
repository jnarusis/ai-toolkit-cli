from shared.gpt_helper import gpt_chat

def generate_powershell_script():
    task = input("\nDescribe the PowerShell script you want: ")
    response = gpt_chat(
        [
            {"role": "system", "content": "You are a Windows PowerShell expert. Generate only the PowerShell script. Only output code — no explanation or extra text."},
            {"role": "user", "content": task}
        ],
        model="gpt-4o"
    )
    print("\n=== PowerShell Script Output ===\n")
    print(response)
    return response
