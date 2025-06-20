# Swarm Assignment - Multi-Agent with Gemini API

## 📚 Overview

This project demonstrates a simple AI-based multi-agent system using a custom "Swarm" structure integrated with Google's Gemini API. Two agents interact: Agent A handles user input and switches to Agent B when requested. Agent B replies in haiku form using Gemini's generative model.

---

## 👤 Student Name

Sehr Khan

---

## 💻 Source Code Files

### main.py

```python
from dotenv import load_dotenv
from swarm import Agent, Swarm

load_dotenv()

agent_b = Agent(
    name="Agent B",
    instructions="Only speak in Haikus."
)

def transfer_to_agent_b():
    return agent_b

agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b]
)

client = Swarm()
response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to talk to agent B."}]
)

print(response.messages[-1]["content"])
```

### swarm.py

```python
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

class Agent:
    def __init__(self, name, instructions, functions=[]):
        self.name = name
        self.instructions = instructions
        self.functions = functions

    def run(self, messages):
        full_prompt = self.instructions + "\n"
        for m in messages:
            full_prompt += f"{m['role']}: {m['content']}\n"

        for fn in self.functions:
            if callable(fn):
                result = fn()
                if isinstance(result, Agent):
                    return result.run(messages)

        response = model.generate_content(full_prompt)
        return {"messages": messages + [{"role": self.name, "content": response.text}]}

class Swarm:
    def run(self, agent, messages):
        return agent.run(messages)
```

---

## ⚙️ Project Setup

### 🔸 Folder Structure

```
Swarm/
├── main.py
├── swarm.py
├── .env
├── requirements.txt
├── report_romn_english.docx
├── report_english.pdf
```

### 🔸 Requirements

```bash
pip install -r requirements.txt
```

### 🔸 .env

```
GEMINI_API_KEY=your_api_key_here
```

---

## 🧠 How It Works

* `swarm.py` contains the custom Agent and Swarm logic.
* ## `main.py` runs the conversation and switches between agents.
* Agent B uses Gemini to generate creative responses in haiku style.

## 📝 Reports

### 📄 Roman Urdu DOC Report

File: `report_romn_english.docx`
Language: Roman Urdu (for presentation or school assignment)

### 📄 English PDF Report

File: `report_english.pdf`
Language: English (for formal documentation)

---

## 🚀 Sample Output

```
User: I want to talk to Agent B about the sky.
Agent B: 
Clouds drift silently  
Blue sky whispers to the wind  
Nature’s breath above
```

---

## 🧪 How to Test the Project

### ✅ Step 1: Activate Virtual Environment

```bash
.venv\Scripts\activate  # Windows
```

### ✅ Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, manually install:

```bash
pip install python-dotenv google-generativeai
```

---

### ✅ Step 3: Add API Key

Create a `.env` file in your project folder with the following content:

```
GEMINI_API_KEY=your_actual_api_key_here
```

> Replace `your_actual_api_key_here` with your real Gemini API key.

---

### ✅ Step 4: Run the Project

```bash
python main.py
```

You should see output like:

```
Clouds drift silently
Blue sky whispers to the wind
Nature’s breath above
```

---

### ❌ Troubleshooting

| Error                                           | Fix                                       |
| ----------------------------------------------- | ----------------------------------------- |
| `ModuleNotFoundError: No module named 'dotenv'` | Run `pip install python-dotenv`           |
| `ModuleNotFoundError: No module named 'swarm'`  | Ensure `swarm.py` is in the same folder   |
| `API key not found`                             | Check `.env` file and re-run the terminal |

---

### ✅ Output Confirmation

Add this line in `main.py` for a success message:

```python
print("Test Passed ✅")
```
dotenv ka eror solution...
3. .venv Folder Ko Delete Karein (Explorer se)
Windows Explorer mein jaakar C:\Users\computer lab\Desktop\Swarm\.venv folder ko delete karein.
Agar permission error aaye, PC restart karke phir try karein.
4. Naya Virtual Environment Banayein
Terminal mein:
erminal mein:
python -m venv .venv
5. Virtual Environment Activate Karein
.venv\Scripts\activate

6. python-dotenv Install Karein

pip install python-dotenv
---
7. Check Karein python-dotenv Install Hua Ya Nahi
pip list
## ✅ Done by

Sehr Khan
