from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()  # reads ANTHROPIC_API_KEY from the .env file

MODEL = "claude-haiku-5-5"

client = Anthropic()  # finds ANTHROPIC_API_KEY in the environment automatically

response = client.messages.create(
    model=MODEL,
    max_tokens=300,
    messages=[
        {"role": "user", "content": "Say hello and explain what an API is in two sentences."}
    ],
)

print(response.content[0].text)
print("Tokens used:", response.usage.input_tokens, "in,", response.usage.output_tokens, "out")