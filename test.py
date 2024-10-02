import boto3
import json

#testing..

# Initialize the Bedrock Runtime client
bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')

# Set the model ID for Claude 3
model_id = "anthropic.claude-3-haiku-20240307-v1:0"

# Define the system message (context)
system_message = """You are an AI assistant specialized in programming humor. 
Your jokes should be clever, related to coding concepts, and suitable for all audiences."""

# Define the user message
user_message = "Tell me a short joke about Python."

# Prepare the request with additional context
request = {
    "modelId": model_id,
    "messages": [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": system_message
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_message
                }
            ]
        }
    ],

    "inferenceConfiguration": {
        "temperature": 0.7,
        "maxTokens": 200
    }
}

try:
    response = bedrock_runtime.converse(**request)
    
    # Extract and print the response
    if 'output' in response:
        output = json.loads(response['output'])
        if 'messages' in output and len(output['messages']) > 0:
            assistant_message = output['messages'][0]['content'][0]['text']
            print("Claude's response:")
            print(assistant_message)
            
            # Extract token usage from the response
            if 'usage' in output:
                
                # Print token usage
                print(f"\nToken usage:")
                print(f"Input tokens: {input_tokens}")
                print(f"Output tokens: {output_tokens}")
                print(f"Total tokens: {input_tokens + output_tokens}")
            else:
                print("\nToken usage information not available in the response.")
        else:
            print("No message content found in the response.")
    else:
        print("Unexpected response format.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
