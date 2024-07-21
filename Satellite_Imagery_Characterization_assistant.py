import os
import json
import base64
import urllib.request
import streamlit as st
import boto3
from botocore.exceptions import ClientError
from PIL import Image

# Constants
MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"
AWS_REGION = "us-east-1"
IMAGE_FILE = "logo.png"

# Function to download the image
def download_image(url, file_name):
    urllib.request.urlretrieve(url, file_name)

# Function to load and encode the image data
def load_and_encode_image(file_name):
    with open(file_name, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")
    return image_data

# Function to format the request payload
def format_request_payload(image_data, question):
    return {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "temperature": 0.5,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": image_data
                        }
                    },
                    {
                        "type": "text",
                        "text": question
                    }
                ]
            }
        ],
    }

# Function to invoke the model and get the response
def invoke_model(model_id, request_payload):
    client = boto3.client("bedrock-runtime", region_name=AWS_REGION)
    request = json.dumps(request_payload)

    try:
        response = client.invoke_model(modelId=model_id, body=request.encode('utf-8'))
        response_body = response["body"].read()
        model_response = json.loads(response_body)
        return model_response["content"][0]["text"]
    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
        return None

# Main function
def main():
    image_url = st.text_input("Enter the image URL:")

    if image_url:
        try:
            download_image(image_url, IMAGE_FILE)
            image_data = load_and_encode_image(IMAGE_FILE)
            question = "What is in this image?"
            request_payload = format_request_payload(image_data, question)
            response_text = invoke_model(MODEL_ID, request_payload)

            if response_text:
                st.write(response_text)
            else:
                st.error("Failed to get a response from the model.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid image URL.")

if __name__ == "__main__":
    main()
