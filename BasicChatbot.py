def chatbot():
    print("CHATBOT: Hi, I'm ChatBot! Type 'bye' to exit.")
    
    while True:
        user_input = input("YOU: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("CHATBOT: Hello there! How can I help you today?")
        elif user_input in ["how are you", "how are you doing"]:
            print("CHATBOT:I'm doing great! Thanks for asking.")
        elif user_input in ["what is your name", "who are you"]:
            print("CHATBOT: I'm a simple chatbot-PYBOT (created using Python)!")
        elif user_input in ["bye", "goodbye", "exit"]:
            print("CHATBOT: Goodbye! Have a great day.")
            break
        elif user_input in ["thank you", "thanks"]:
            print("CHATBOT: You're welcome!")
        else:
            print("CHATBOT: Sorry, I didn't understand that.")

chatbot()
