# swarm.py

import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  

class Agent:
    def __init__(self, name, instructions, functions=None):
        self.name = name
        self.instructions = instructions
        self.functions = functions or []

class Swarm:
    def run(self, agent, messages):
        for message in messages:
            content = message["content"].lower()
            if "agent b" in content:
                for func in agent.functions:
                    new_agent = func()
                    return type("Response", (), {
                        "messages": [{"role": "agent", "content": f"{new_agent.name} says: {new_agent.instructions}"}]
                    })()
        return type("Response", (), {
            "messages": [{"role": "agent", "content": f"{agent.name} says: {agent.instructions}"}]
        })()
