import os
import google.generativeai as genai

# Set up the API key and model configuration
genai.configure(api_key="")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="You are an advanced marketing model that analyzes promotional and service messages to predict their performance scores. Your task is to evaluate the content of a given message and provide a score between 0 and 100, where a higher score indicates better expected performance based on factors like engagement potential, clarity, and persuasive power. Consider various aspects such as the tone, content, emotional appeal, call to action, and relevance to the target audience.",
)

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "hello",
            ],
        },
        {
            "role": "model",
            "parts": [
                "I need more information to evaluate the performance of a message! Please provide me with the actual message you want me to analyze. \n\nFor example, tell me:\n\n* **What is the message about?** (e.g., a product launch, a sale, a blog post, a social media post, etc.)\n* **Who is the target audience?** (e.g., young adults, professionals, parents, etc.)\n* **What is the goal of the message?** (e.g., drive sales, increase brand awareness, generate leads, etc.)\n* **What is the actual message text?**\n\nOnce I have this information, I can analyze the message and provide you with a performance score. \n",
            ],
        },
    ]
)

def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break

        # Send the message
        response = chat_session.send_message(user_input)
        # Print the response
        print(f"Model: {response.text}")

# Start the chat
chat()
