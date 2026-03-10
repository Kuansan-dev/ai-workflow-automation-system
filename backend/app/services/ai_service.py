import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_summary(text: str) -> str:
    response = client.responses.create(
        model="gpt-5.4",
        input=f"Summarize this text clearly in 2-4 sentences:\n\n{text}"
    )
    return response.output_text.strip()


def extract_action_items(text: str) -> str:
    response = client.responses.create(
        model="gpt-5.4",
        input=(
            "Extract action items from the following text. "
            "Return them as a short bullet list.\n\n"
            f"{text}"
        )
    )
    return response.output_text.strip()