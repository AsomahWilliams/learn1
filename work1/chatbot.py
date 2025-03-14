def customer_support_bot():
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input(":User  ")
        
        if user_input.lower() == "what are your business hours?":
            print("Chatbot: Our business hours are Monday to Friday, 9 AM to 5 PM.")
        elif user_input.lower() == "what is your return policy?":
            print("Chatbot: Our return policy allows returns within 30 days of purchase.")
        elif user_input.lower() == "do you offer international shipping?":
            print("Chatbot: Yes, we offer international shipping to select countries.")
        elif user_input.lower() == "can i track my order?":
            print("Chatbot: Yes, you can track your order using the tracking link sent to your email.")
        elif user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Thank you for reaching out! Have a great day!")
            break
        else:
            print("Chatbot: I'm not sure. Please contact support.")

# Start the chatbot
customer_support_bot()