# main.py
from dotenv import load_dotenv
# Make sure swarm.py exists in the same directory or is installed as a package
from swarm import Agent, Swarm

load_dotenv()

# Define second agent
agent_b = Agent(
    name="Agent B",
    instructions="Only speak in Haikus."
)
# Register agent_b with the swarm if needed, or just define it here for transfer
# Function to switch to agent B
def transfer_to_agent_b(*args, **kwargs):
    return agent_b

# Define first agent
agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b]
)

# Run swarm
client = Swarm()
response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to talk to agent B."}]
)

print(response.messages[-1]["content"])
