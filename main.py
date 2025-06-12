from tools import (
    generate_bash,
    explain_bash,
    explain_linux,
    generate_powershell,
    explain_powershell,
    explain_windows,
    tutor_mode
)

def main():
    last_output = ""

    while True:
        print("\n=== AI CLI Toolkit ===")
        print("1. Generate a Bash script")
        print("2. Break down a Bash script")
        print("3. Explain a Linux/DevOps concept")
        print("4. Generate a PowerShell script")
        print("5. Break down a PowerShell script")
        print("6. Explain a Windows/PowerShell concept")
        print("7. AI Tutor Mode (Ask GPT)")
        print("8. Exit")
        choice = input("Choose an option (1–8): ")

        if choice == "1":
            last_output = generate_bash.generate_bash_script()
        elif choice == "2":
            last_output = explain_bash.breakdown_bash_script()
        elif choice == "3":
            last_output = explain_linux.explain_linux_concept()
        elif choice == "4":
            last_output = generate_powershell.generate_powershell_script()
        elif choice == "5":
            last_output = explain_powershell.breakdown_powershell_script()
        elif choice == "6":
            last_output = explain_windows.explain_windows_concept()
        elif choice == "7":
            tutor_mode.interactive_tutor()
        elif choice == "8":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
