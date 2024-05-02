from openai import OpenAI
import anthropic
import google.generativeai as genai

import base64
import cv2
import json
import re


class GPT4Turbo:
    def __init__(self, model_name: str = "gpt-4-turbo"):
        self.model_name = model_name
        self.messages = []

        # OPENAI API Key
        file = open("OPENAI_API_KEY.txt", "r")
        api_key = file.read()
        self.client = OpenAI(api_key=api_key)

    def encode_image(self, cv_image):
        _, buffer = cv2.imencode(".jpg", cv_image)
        return base64.b64encode(buffer).decode("utf-8")

    def add_system_message(self, sys_msg):
        system_prompt_msg = [sys_msg]
        system_prompt = {"role": "system", "content": system_prompt_msg}
        self.messages.append(system_prompt)
        
    def query_LLM(self):
        self.response = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.messages,
            temperature=0,
            n=1,
            max_tokens=500,
        )
        return self.response

    def generate_response(self) -> str:     
        response = self.query_LLM()
        print(response)
        response_text = response.choices[0].message.content
        print(len(self.messages))
        return response_text

    def add_user_message(self, frame, user_msg):
        msg = user_msg
        self.messages.append(
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": msg},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{self.encode_image(frame)}",
                            "detail": "low",
                        },
                    },
                ],
            }
        )

    def add_assistant_message(self):
        self.messages.append({"role": "assistant", "content": self.response})

class Claude3:
    def __init__(self, model_name: str = "claude-3-opus-20240229"):
        self.model_name = model_name
        self.system_message = "I am a helpful assistant."
        self.messages = []

        # ANTHROPIC API Key
        file = open("ANTHROPIC_API_KEY.txt", "r")
        api_key = file.read()
        self.client = anthropic.Anthropic(api_key=api_key)

    def query_LLM(self):
        self.response = self.client.messages.create(
            model=self.model_name,
            max_tokens=500,
            temperature=0,
            system=self.system_message,
            messages=self.messages,
        )
        return self.response

    def generate_response(self) -> str:     
        response = self.query_LLM()
        print(response)

        print(len(self.messages))
        return response
    
    def add_user_message(self, user_msg):
        self.messages.append(
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_msg},
                ]
            }
        )

class Gemini:
    def __init__(self, model_name: str = "gemini-pro"):
        self.model_name = model_name
        self.system_message = "I am a helpful assistant."
        self.messages = []

        # GOOGLE API Key
        file = open("GOOGLE_API_KEY.txt", "r")
        api_key = file.read()
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name = self.model_name, system_instruction=self.system_message)

    def query_LLM(self):
        self.response = self.model.generate_content(self.messages)
        return self.response

    def generate_response(self) -> str:     
        response = self.query_LLM()
        print(response)

        print(len(self.messages))
        return response.text
    
    def add_user_message(self, user_msg):
        self.messages.append(
            {
                "role": "user",
                "parts": [user_msg]
            }
        )
    
    def add_assistant_message(self, assistant_msg):
        self.messages.append(
            {
                "role": "model",
                "parts": [assistant_msg]
            }
        )