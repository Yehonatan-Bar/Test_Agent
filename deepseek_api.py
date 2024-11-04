import os
from openai import OpenAI
import time  # Add this import at the top of the file

def get_deepseek_response(prompt, isChat=False):
    # Try to get the API key from environment variable
    api_key = os.environ.get("DEEPSEEK_API_KEY")

    # Initialize the OpenAI client with DeepSeek's base URL and your API key
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )
    # Ensure the prompt is in the correct format
    if isinstance(prompt, list):
        messages = prompt
    elif isinstance(prompt, str):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    else:
        raise ValueError("Invalid prompt format. Expected string or list of messages.")
    
    if isChat:
        model = "deepseek-chat"
        temperature = 1.0
    else:
        model = "deepseek-coder"
        temperature = 0.0
    try:
        time.sleep(1)
        # Make the API call
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=False,
            temperature=temperature,
        )
        
        print(f"response.choices[0].message.content: {response.choices[0].message.content}")
        # Return the model's response
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    result = get_deepseek_response(user_prompt)
    print("DeepSeek's response:")
    print(result)