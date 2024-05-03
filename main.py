from llms import GPT4Turbo, Claude3, Gemini
import cv2

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

    img = cv2.imread("meme.jpg")
    # img = cv2.resize(img, (100, 100))
    print(img.shape)

    # gpt4 = GPT4Turbo()
    # gpt4.add_user_message(frame=img)
    # print(gpt4.generate_response())

    # opus = Claude3()
    # opus.add_user_message_vision(img)
    # print(opus.generate_response())
    gemini = Gemini()
    gemini.add_user_message(img, "What is the main object of interest in this image?")
    print(gemini.generate_response())

    # gemini = Gemini()
    # user_message = "What is the capital of Argentina?"
    # gemini.add_user_message(user_message)
    # print(gemini.generate_response())