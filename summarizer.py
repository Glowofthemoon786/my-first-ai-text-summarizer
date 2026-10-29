
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the secret API key
load_dotenv()

# Connect to OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Welcome to my AI Text Summarizer!")

# Ask the user to enter text
text = input("\nPaste the text you want to summarize:\n")

if text.strip():
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            instructions="Summarize the user's text clearly and simply. Keep the main ideas and important details.",
            input=text
        )

        print("\nHere is your summary:\n")
        print(response.output_text)

    except Exception as error:
        print("\nSomething went wrong:", error)
else:
    print("You did not enter any text.")
