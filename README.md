AI Toolkit CLI
==============

This is a modular, GPT-powered command-line toolkit for scripting, system administration, and IT learning. It supports both Linux and Windows environments, and includes an interactive tutor mode to guide users through homelab builds and troubleshooting tasks.

Designed for self-directed IT learners, homelab builders, and sysadmin professionals who want rapid, explainable help at the command line.

Features
--------

- Generate Bash scripts from plain-language prompts  
- Break down existing Bash scripts line by line  
- Explain Linux and DevOps concepts  
- Generate PowerShell scripts from natural language  
- Break down PowerShell scripts line by line  
- Explain Windows sysadmin concepts (GPO, services, registry, etc.)  
- NEW: AI Tutor Mode – ask any sysadmin question in natural language  
- Modular and documented – easily extensible with new tools or workflows  

Real-World Use
--------------

I used this assistant to help build my full Windows Server Homelab, step by step. The AI Tutor helped me understand and implement Active Directory, Group Policy, DHCP, WSUS, and more.

It can also guide users through setting up a Linux lab, managing scripts, or debugging tasks interactively.

Setup
-----

1. Clone the repository:

       git clone https://github.com/jnarusis/ai-toolkit-cli.git
       cd ai-toolkit-cli

2. Create and activate a virtual environment:

   **Windows:**

       python -m venv venv
       .\venv\Scripts\activate

   **Linux/macOS:**

       python3 -m venv venv
       source venv/bin/activate

3. Install requirements:

       pip install -r requirements.txt

4. Set your OpenAI API key:

   - Copy `.env.example` to `.env`
   - Replace with your key:

         OPENAI_API_KEY=your-key-here

5. Run the CLI tool:

       python main.py

Menu Overview
-------------

       === AI CLI Toolkit ===
       1. Generate a Bash script
       2. Break down a Bash script
       3. Explain a Linux/DevOps concept
       4. Generate a PowerShell script
       5. Break down a PowerShell script
       6. Explain a Windows/PowerShell concept
       7. AI Tutor Mode (Ask GPT)
       8. Exit

Project Structure
-----------------

    ai-toolkit-cli/
    ├── tools/
    │   ├── generate_bash.py
    │   ├── explain_bash.py
    │   ├── explain_linux.py
    │   ├── generate_powershell.py
    │   ├── explain_powershell.py
    │   ├── explain_windows.py
    │   ├── tutor_mode.py          # GPT-powered AI tutor
    │   └── tutorial_mode.py       # Static walkthrough (Windows Homelab)
    │
    ├── shared/
    │   └── gpt_helper.py          # Shared API call logic (optional)
    │
    ├── .env.example
    ├── requirements.txt
    ├── main.py
    └── README.md

License
-------

This project is licensed under the MIT License.