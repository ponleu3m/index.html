

def chatbot(user_input):
    user = user_input.lower().strip()

    if user == "hello":
        return "Hi there! "
    elif user == "how are you":
        return "I'm just a bunch of code, but I'm doing great! "
    elif user == "what's your name":
        return "I'm ChatBot. Nice to meet you!"
    elif user == "bye":
        return "Goodbye! "
    else:
        return "Sorry, I don't understand that. "

user_inputs = ["hello", "how are you", "what's your name", "what is 2 + 2", "bye"]

for msg in user_inputs:
    print("You:", msg)
    print("Bot:", chatbot(msg))
    print()


