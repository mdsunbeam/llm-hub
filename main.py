from llms import GPT4Turbo, Claude3, Gemini
import cv2

if __name__ == "__main__":

    logo = cv2.imread("images/llm-hub-logo.jpg")
    system_message = "You are a helpful assistant."
    text = "Describe what you see in this image."

    gpt4turbo = GPT4Turbo(system_message=system_message)
    gpt4turbo.add_user_message(frame=logo, user_msg=text)
    print("GPT4Turbo: ", gpt4turbo.generate_response())

    opus = Claude3(system_message=system_message)
    opus.add_user_message(frame=logo, user_msg=text)
    print("Claude 3 Opus: ", opus.generate_response())

    gemini_1_5_pro = Gemini(system_message=system_message)
    gemini_1_5_pro.add_user_message(frame=logo, user_msg=text)
    print("Gemini 1.5 Pro: ", gemini_1_5_pro.generate_response())