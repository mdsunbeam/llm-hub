from llms import GPT4Turbo, Claude3

if __name__ == "__main__":
    claude = Claude3()
    claude.add_user_message("How many moons does Jupiter have?")
    response = claude.generate_response()