

🚀 Step-by-Step Installation
🛠 1. Install UV
Linux/macOS:

curl -LsSf https://astral.sh/uv/install.sh | sh
Windows (PowerShell):

If you get a TLS error, first run this:

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Then install:

irm https://astral.sh/uv/install.ps1 | iex
✅ Verify installation:

uv --version
📁 2. Initialize Your Project
uv init my-first-agent
cd my-first-agent
This will set up a new Python project with UV's virtual environment.

📦 3. Install Required Packages
uv add openai-agents python-dotenv
This installs the OpenAI Agents SDK and dotenv for environment variables.

🧪 4. Activate the Environment
Windows:

.venv\Scripts\activate
Linux/macOS:

source .venv/bin/activate
