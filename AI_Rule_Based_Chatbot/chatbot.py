print("🤖 Welcome to Smart AI Chatbot (Type 'exit' to stop)")

# Intent groups
greetings = ["hi", "hello", "hey"]
thanks = ["thank", "thanks", "thank you"]
goodbye = ["bye", "exit", "quit"]

history = []

while True:
    user = input("You: ").lower()

    history.append("User: " + user)

    # Greeting intent
    if any(word in user for word in greetings):
        reply = "Hello 😊 How can I help you today?"

    # Thanks intent
    elif any(word in user for word in thanks):
        reply = "You're welcome 😊 Happy to help!"

    # Goodbye intent
    elif any(word in user for word in goodbye):
        reply = "Goodbye 👋 Have a great day!"
        print("Bot:", reply)
        history.append("Bot: " + reply)
        break

    # Topic: Python
    elif "python" in user:
        reply = "Python is a powerful programming language used in AI, ML, Data Science, and Web Development."

    # Topic: AI
    elif "ai" in user:
        reply = "AI (Artificial Intelligence) makes machines able to think and learn like humans."

    # Topic: chatbot
    elif "chatbot" in user:
        reply = "A chatbot is a program that simulates human conversation using rules or AI."

    # Help
    elif "help" in user:
        reply = "You can ask me about Python, AI, chatbots, or say hello!"

    # Fallback response
    else:
        reply = "I'm still learning 🤖 Try asking about Python, AI, or greetings."

    print("Bot:", reply)
    history.append("Bot: " + reply)

# Optional: save chat history
with open("chat_history.txt", "a") as f:
    for line in history:
        f.write(line + "\n")