import requests

from config import (
    DEEPSEEK_API_KEY,
    DEEPSEEK_API_URL,
    MODEL_NAME,
    EXPERIMENT_A,
    EXPERIMENT_B
)


def call_llm(
    code,
    problem,
    variant="A"
):

    if variant == "A":

        prompt = f"""
You are a software engineer.

Fix the bug.

Problem:
{problem}

Code:
{code}

Return ONLY the full corrected code.
"""

        temperature = EXPERIMENT_A["temperature"]

    else:

        prompt = f"""
You are a senior debugging engineer.

Before fixing:

1. Identify root cause.
2. Consider edge cases.
3. Avoid side effects.
4. Apply the minimal correct patch.

Problem:
{problem}

Code:
{code}

Return ONLY the full corrected code.
"""

        temperature = EXPERIMENT_B["temperature"]

    response = requests.post(
        DEEPSEEK_API_URL,
        headers={
            "Authorization":
                f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type":
                "application/json"
        },
        json={
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": temperature
        }
    )

    response.raise_for_status()

    output = response.json()[
        "choices"
    ][0]["message"]["content"]

    if "```" in output:

        parts = output.split("```")

        if len(parts) >= 2:

            output = parts[1]

            if output.startswith("python"):
                output = output[6:]

    return output.strip()