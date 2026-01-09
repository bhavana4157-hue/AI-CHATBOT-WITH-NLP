def get_response(user_text):
    user_text = user_text.lower()

    if "hello" in user_text or "hi" in user_text:
        return "Hello! 🤖 How can I help you today?"
    
    elif "how are you" in user_text:
        return "I'm doing great and ready to chat! 😄"
    
    elif "what is your name" in user_text:
        return "I'm your friendly AI Chatbot! 💡"
    
    elif "who created you" in user_text:
        return "I was created using Python and Flask! 🐍"
    
    elif "time" in user_text:
        from datetime import datetime
        return "Current time ⏰ : " + datetime.now().strftime("%I:%M %p")

    elif "date" in user_text:
        from datetime import datetime
        return "Today's date 📅 : " + datetime.now().strftime("%d-%m-%Y")

    elif "bye" in user_text or "goodbye" in user_text:
        return "Goodbye! 👋 Have a great day!"

    elif "help" in user_text:
        return "You can ask me: time, date, my name, how are you, etc. 😊"

    else:
        return "Oops 😕 I don’t know that answer yet. Try another question!"

