# ==========================================
# Project: Rule-Based AI Chatbot
# Language: Python
# ==========================================

print("=" * 45)
print("       WELCOME TO RULEBOT 🤖")
print("=" * 45)

print("Bot: Hello! I'm RuleBot, your chatbot.")
print("Bot: Type 'help' to see what I can do.")
print("Bot: Type 'bye' to end our conversation.\n")


# Continuous conversation loop
while True:

    # Get user input
    user_input = input("You: ").lower().strip()

    # Handle empty input
    if user_input == "":
        print("Bot: Please type something!")

    # Handle exit commands
    elif user_input in ["bye", "exit", "quit", "goodbye"]:
        print("Bot: Goodbye! Have a great day! 😊")
        break

    # Handle greetings
    elif user_input in ["hi", "hello", "hey", "hii"]:
        print("Bot: Hello! 👋 How can I help you?")

    # Handle help command
    elif user_input == "help":
        print("\nBot: Here is what you can ask me:")
        print("- Say hello")
        print("- Ask how I am")
        print("- Ask who I am")
        print("- Ask what AI is")
        print("- Ask what Python is")
        print("- Say thank you")
        print("- Type bye to exit")

    # Handle introduction
    elif user_input in ["who are you", "what is your name"]:
        print("Bot: I'm RuleBot, a simple chatbot created using Python!")

    # Handle how-are-you questions
    elif user_input in ["how are you", "how are you doing"]:
        print("Bot: I'm doing great! Thanks for asking. 😊")

    # Handle AI questions
    elif user_input in ["what is ai", "define ai"]:
        print(
            "Bot: Artificial Intelligence (AI) enables "
            "machines to perform tasks that usually require "
            "human intelligence."
        )

    # Handle Python questions
    elif user_input in ["what is python", "define python"]:
        print(
            "Bot: Python is a popular programming language "
            "used in AI, machine learning, and data science."
        )

    # Handle thank-you messages
    elif user_input in ["thanks", "thank you", "thank u"]:
        print("Bot: You're welcome! Happy to help. 😊")

    # Handle unknown messages
    else:
        print(
            "Bot: Sorry, I don't understand that yet. "
            "Type 'help' to see what you can ask me."
        )

    print()