def myhelper():
    print("myhelper: I am your helper bot...WELCOME!!!\n")
    
    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ["hello", "hi", "hey"]:
            print("myhelper: Hi! How can I help you today?")
        elif user_input in ["how are you", "how are you?", "how are u"]:
            print("myhelper: I'm fine, thanks for asking!")
        elif user_input in ["what is codealpha", "tell me about codealpha", "codealpha"]:
            print("myhelper: CodeAlpha is a tech platform providing virtual internships and hands-on learning experiences for students!")
        elif user_input in ["what domain is this internship", "which domain"]:
            print("myhelper: This is the Python Programming Internship at CodeAlpha.")
        elif user_input in ["what is your name", "what's your name", "who are you"]:
            print("myhelper: I am a Python rule-based chatbot created for the CodeAlpha internship task!")
        elif user_input in ["what can you do", "help", "what do you do"]:
            print("myhelper: I can answer questions about greetings, myself, and the CodeAlpha internship platform.")

        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            print("myhelper: Goodbye! Best of luck with your CodeAlpha internship!")
            break
        else:
            print("myhelper: Sorry, I don't understand that. Try asking 'what is codealpha'.")
if __name__ == "__main__":
    myhelper()