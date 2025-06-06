# AI Toolkit CLI

This is a modular command-line toolkit for Linux and DevOps automation tasks. It uses the OpenAI API to generate scripts, explain technical concepts, and break down command-line operations. Designed to assist with hands-on system administration and scripting work.

## Features

- Generate Bash scripts from plain-language prompts  
- Break down existing Bash scripts line by line  
- Explain Linux and DevOps concepts on demand  
- Generate PowerShell scripts from plain-language prompts  
- Break down existing PowerShell scripts line by line  
- Explain Windows/PowerShell concepts on demand  
- Save output to files for later use  
- Modular structure for future expansion  

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/jnarusis/ai-toolkit-cli.git
   cd ai-toolkit-cli
   ```

2. Create and activate a virtual environment:

   **Windows:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

   **Linux/macOS:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install requirements:

   ```bash
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key:

   - Copy `.env.example` to `.env`
   - Paste your `OPENAI_API_KEY=your-key-here`

5. Run the CLI tool:

   ```bash
   python main.py
   ```

## Project Structure

```
ai-toolkit-cli/
├── tools/                        # CLI modules
│   ├── generate_bash.py
│   ├── explain_bash.py
│   ├── explain_linux.py
│   ├── generate_powershell.py
│   ├── explain_powershell.py
│   └── explain_windows.py
│
├── shared/                       # Utility modules
│   └── gpt_helper.py
│
├── .env.example
├── requirements.txt
├── main.py
└── README.md
```

## License

This project is licensed under the MIT License.