# 🤖 Simple Agent Setup Guide

A lightweight AI agent built using **Python**, **UV**, **OpenAI Agents SDK**, and **Gemini API**.

---

## 🚀 Step-by-Step Installation

### 🛠 1. Install UV

**Linux/macOS:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

If you get a TLS error, first run this:

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
```

Then install:

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

✅ **Verify installation:**

```bash
uv --version
```

---

### 📁 2. Initialize Your Project

```bash
uv init my-first-agent
cd my-first-agent
```

This will set up a new Python project with UV's virtual environment.

---

### 📦 3. Install Required Packages

```bash
uv add openai-agents python-dotenv
```

This installs the OpenAI Agents SDK and dotenv for environment variables.

---

### 🧪 4. Activate the Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

---

### 🔐 5. Add Your Gemini API Key

Create a `.env` file in the root directory and add:

```env
GEMINI_API_KEY=your_gemini_api_key
```

📌 Get your Gemini API key from:
[https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

### ▶️ 6. Run the Agent

Make sure your script is named `main.py`, then run:

```bash
uv run main.py
```

💬 Type a message like `hi` or `bye` in the terminal and interact with your agent.

---

## 🎉 You’re All Set!

Your **Simple Agent** is now up and running. Customize it, connect more APIs, and explore what’s possible 🚀
