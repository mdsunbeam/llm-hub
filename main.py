from llms import GPT4Turbo, Claude3, Gemini, Llama3
import cv2

if __name__ == "__main__":

    MODELS = {
    "OpenAI": ["gpt-4-turbo", "gpt-4o", "gpt-3.5-turbo"], 
    "Anthropic": ["claude-3-opus-20240229", "claude-3-sonnet-20240229", "claude-3-haiku-20240307"], 
    "Google": ["gemini-1.5-pro-latest", "gemini-pro", "gemini-pro-vision"], 
    "Meta": ["llama3-70b-8192", "llama3-8b-8192"]
    }

    # example inputs
    logo = cv2.imread("images/llm-hub-logo.jpg")
    system_message = "You are a helpful assistant."
    text = "Describe what you see in this image."
    text2 = "When was George Washington born?"

    # model instantiation and response generation
    llama3_70b = Llama3(model_name=MODELS["Meta"][0], system_message=system_message)
    llama3_70b.add_user_message(frame=None, user_msg=text2)
    print("Llama3 70B: ", llama3_70b.generate_response())

    gpt4turbo = GPT4Turbo(model_name=MODELS["OpenAI"][0], system_message=system_message)
    gpt4turbo.add_user_message(frame=logo, user_msg=text)
    print("GPT4Turbo: ", gpt4turbo.generate_response())

    opus = Claude3(model_name=MODELS["Anthropic"][0], system_message=system_message)
    opus.add_user_message(frame=logo, user_msg=text)
    print("Claude 3 Opus: ", opus.generate_response())

    gemini_1_5_pro = Gemini(model_name=MODELS["Google"][0], system_message=system_message)
    gemini_1_5_pro.add_user_message(frame=logo, user_msg=text)
    print("Gemini 1.5 Pro: ", gemini_1_5_pro.generate_response())
