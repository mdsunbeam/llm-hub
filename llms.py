from openai import OpenAI
import anthropic
import google.generativeai as genai

import base64
import cv2
import json
import re

# TODO: Add handling for text or image only and image with text
class GPT4Turbo:
    def __init__(self, model_name="gpt-4-turbo", system_message=None):
        self.model_name = model_name
        self.messages = []
        self.system_message = system_message
        # OPENAI API Key
        file = open("OPENAI_API_KEY.txt", "r")
        api_key = file.read()
        self.client = OpenAI(api_key=api_key)

        if system_message is not None:
            system_prompt = {"role": "system", "content": [system_message]}
            self.messages.append(system_prompt)

    def encode_image(self, cv_image):
        _, buffer = cv2.imencode(".jpg", cv_image)
        return base64.b64encode(buffer).decode("utf-8")
        
    def query_LLM(self):
        self.response = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.messages,
            temperature=1,
            n=1,
            max_tokens=500,
        )
        return self.response

    def generate_response(self) -> str:     
        response = self.query_LLM()
        # print(response)
        response_text = response.choices[0].message.content
        # print(len(self.messages))
        return response_text

    def add_user_message(self, frame=None, user_msg=None):
        if user_msg is not None and frame is not None:
            self.messages.append(
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_msg},
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
        elif user_msg is not None and frame is None:
            self.messages.append(
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_msg},
                    ],
                }
            )
        elif user_msg is None and frame is not None:
            self.messages.append(
                {
                    "role": "user",
                    "content": [
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
        else:
            pass

    def add_assistant_message(self):
        if self.response is not None:
            self.messages.append({"role": "assistant", "content": self.response})

class Claude3:
    def __init__(self, model_name="claude-3-opus-20240229", system_message=None):
        self.model_name = model_name
        self.system_message = system_message
        self.messages = []

        # ANTHROPIC API Key
        file = open("ANTHROPIC_API_KEY.txt", "r")
        api_key = file.read()
        self.client = anthropic.Anthropic(api_key=api_key)

    def encode_image(self, cv_image):
        _, buffer = cv2.imencode(".jpg", cv_image)
        return base64.b64encode(buffer).decode("utf-8")

    def query_LLM(self):
        if self.system_message is not None:
            self.response = self.client.messages.create(
                model=self.model_name,
                max_tokens=500,
                temperature=1,
                system=self.system_message,
                messages=self.messages,
            )
        else:
            self.response = self.client.messages.create(
                model=self.model_name,
                max_tokens=500,
                temperature=1,
                messages=self.messages,
            )
        return self.response

    def generate_response(self) -> str:     
        response = self.query_LLM()
        # print(response)

        # print(len(self.messages))
        return response
    
    def add_user_message(self, frame=None, user_msg=None):
        if frame is not None and user_msg is not None:
            image_data = self.encode_image(frame)
            self.messages.append(
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/jpeg",
                                "data": image_data
                            }
                        },
                        {"type": "text", "text": user_msg}
                    ]
                }
            )
        elif frame is not None and user_msg is None:
            image_data = self.encode_image(frame)
            self.messages.append(
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/jpeg",
                                "data": image_data
                            }
                        }
                    ]
                }
            )
        elif frame is None and user_msg is not None:
            self.messages.append(
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_msg},
                    ]
                }
            )
        else:
            pass
    

class Gemini:
    def __init__(self, model_name="gemini-1.5-pro-latest", system_message=None):
        self.model_name = model_name
        self.system_message = system_message
        self.messages = []

        # GOOGLE API Key
        file = open("GOOGLE_API_KEY.txt", "r")
        api_key = file.read()
        genai.configure(api_key=api_key)
        generation_config = genai.GenerationConfig(temperature = 1, top_p = 0, top_k = 1)
        if self.system_message is not None:
            self.model = genai.GenerativeModel(model_name = self.model_name, system_instruction=self.system_message, generation_config=generation_config)
        else:
            self.model = genai.GenerativeModel(model_name = self.model_name, generation_config=generation_config)

    def encode_image(self, cv_image):
        _, buffer = cv2.imencode(".jpg", cv_image)
        return base64.b64encode(buffer).decode("utf-8")

    def query_LLM(self):
        self.response = self.model.generate_content(self.messages)
        # print(response)
        return self.response

    def generate_response(self) -> str:     
        response = self.query_LLM()
        # print(response)

        # print(len(self.messages))
        return response.text
    
    def add_user_message(self, frame, user_msg):

        if frame is not None and user_msg is not None:
            image_data = self.encode_image(frame)
            self.messages.append(
                {
                    "role": "user",
                    "parts": [
                        {
                            "mime_type": "image/jpeg",
                            "data": image_data
                        },
                        {
                            "text": user_msg
                        }
                    ]
                }
            )
        elif frame is not None and user_msg is None:
            image_data = self.encode_image(frame)
            self.messages.append(
                {
                    "role": "user",
                    "parts": [
                        {
                            "mime_type": "image/jpeg",
                            "data": image_data
                        }
                    ]
                }
            )
        elif frame is None and user_msg is not None:
            self.messages.append(
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": user_msg
                        }
                    ]
                }
            )
        else:
            pass
    
    def add_assistant_message(self, assistant_msg):
        self.messages.append(
            {
                "role": "model",
                "parts": assistant_msg
            }
        )
    
    def add_user_message_vision(self, frame):
        image_data = self.encode_image(frame)
        self.messages.append(
            {
                "role": "user",
                "parts": [
                    {
                        "mime_type": "image/jpeg",
                        "data": image_data
                    },
                    {
                        "text": "Describe this image."
                    }
                ]
            }
        )