from llms import GPT4Turbo, Claude3, Gemini

if __name__ == "__main__":
    # import google.generativeai as genai
    # # GOOGLE API Key
    # file = open("GOOGLE_API_KEY.txt", "r")
    # api_key = file.read()
    # genai.configure(api_key=api_key)
    # model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", system_instruction="You are a helpful assistant.")
    # message = [{'role': 'user', 'parts': ["What is the capital of Argentina?"]}]
    # response = model.generate_content(message)
    # print(response.text)

    gemini = Gemini()
    user_message = "What is the capital of Argentina?"
    gemini.add_user_message(user_message)
    print(gemini.generate_response())