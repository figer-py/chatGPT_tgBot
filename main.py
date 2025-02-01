import config
from openai import OpenAI

client = OpenAI(api_key=config.KEY)


stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say this is a test"}],
)
