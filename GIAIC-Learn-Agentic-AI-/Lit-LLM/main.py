from litellm import completion
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get GEMINI_API_KEY from environment
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Set API key in environment so LiteLLM can access it
os.environ["GEMINI_API_KEY"] = gemini_api_key

try:
    # Call Gemini model using LiteLLM
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{"role": "user", "content": "Hello, how are you?"}],
    )

    # Display the response
    print("\n" + "=" * 50)
    print(f"Content: {response.choices[0].message.content}")
    print(f"Model: {response.model}")
    print("Usage:")
    print(f"  Prompt Tokens: {response.usage.prompt_tokens}")
    print(f"  Completion Tokens: {response.usage.completion_tokens}")
    print(f"  Total Tokens: {response.usage.total_tokens}")
    print("=" * 50 + "\n")

except Exception as e:
    print(f"Error occurred: {str(e)}")

