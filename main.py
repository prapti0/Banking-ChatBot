import tkinter as tk

# Define some responses
greetings = ["hello", "hi", "hey", "greetings", "howdy", "hy"]
thank_you = ["thank you", "thanks", "much appreciated"]
goodbyes = ["goodbye", "bye", "see you later", "take care", "no"]
check_account = ["check account", "account balance", "balance"]
withdrawal_keywords = ["withdrawal", "withdraw", "cash"]
details = ["details", "information", "more"]
withdrawal_amounts = {500, 200, 1000, 100, 2000}  # Set for quick lookup

# Define a function to generate a response
def generate_response(user_input):
    user_input = user_input.lower().strip()  # Normalize input

    # Check for greetings
    if any(word in user_input for word in greetings):
        return "Hello! How can I assist you with your banking needs?"

    # Check account balance
    if any(word in user_input for word in check_account):
        return "Your account balance is ₹5000. Is there anything else I can help you with?"

    # Check for withdrawal request
    if any(word in user_input for word in withdrawal_keywords):
        return "Sure, how much would you like to withdraw? Options: ₹500, ₹200, ₹1000, ₹100, ₹2000."

    # Process withdrawal amount
    try:
        amount = int(user_input)
        if amount in withdrawal_amounts:
            return f"₹{amount} has been successfully withdrawn. Anything else I can help with?"
        else:
            return "Invalid amount. Please choose from ₹500, ₹200, ₹1000, ₹100, or ₹2000."
    except ValueError:
        pass  # Continue checking other responses

    # Provide banking details
    if any(word in user_input for word in details):
        return "What kind of information do you need? You can ask about loans, credit cards, or cheque books."

    if "loan" in user_input:
        return "We offer personal loans, home loans, and car loans. Visit our website or contact us for details."

    if "credit card" in user_input:
        return "We offer various credit card options with rewards. Visit our website for more details."

    if "cheque book" in user_input:
        return "Every new account holder gets a complimentary cheque book. For additional ones, visit our branch."

    # Check for thank you
    if any(word in user_input for word in thank_you):
        return "You're welcome! Is there anything else I can help you with?"

    # Check for goodbyes
    if any(word in user_input for word in goodbyes):
        return "Goodbye! Have a great day!"

    # Default response
    return "I'm sorry, I don't understand. Could you please rephrase your question?"

# Function to handle user input
def handle_user_input():
    user_input = entry.get().strip()
    if not user_input:
        return  # Ignore empty input

    response = generate_response(user_input)
    
    chat_history.config(state=tk.NORMAL)  # Enable editing
    chat_history.insert(tk.END, f"You: {user_input}\n", "user")
    chat_history.insert(tk.END, f"Bot: {response}\n\n", "bot")
    chat_history.config(state=tk.DISABLED)  # Disable editing
    chat_history.yview(tk.END)  # Auto-scroll to the latest message
    entry.delete(0, tk.END)

# Create the main UI window
root = tk.Tk()
root.title("AI Banking Chatbot")
root.geometry("600x500")
root.configure(bg="#FDF5E6")

# Create the chat history text widget
chat_history = tk.Text(root, height=15, width=70, bg="#8FBC8F", fg="#000000", font=("Comic Sans MS", 12))
chat_history.tag_config("user", foreground="#000080", font=("Comic Sans MS", 11, "bold"))
chat_history.tag_config("bot", foreground="#dc3545", font=("Comic Sans MS", 11, "bold"))
chat_history.pack(padx=10, pady=10)
chat_history.config(state=tk.DISABLED)  # Prevent manual typing in chat history

# Create input field and send button
entry = tk.Entry(root, width=60, bg="#ffffff", fg="#000000", font=("Comic Sans MS", 12))
entry.pack(padx=5, pady=5)
entry.bind("<Return>", lambda event: handle_user_input())

send_button = tk.Button(root, text="Send", command=handle_user_input, bg="#007bff", fg="#ffffff", font=("Comic Sans MS", 11))
send_button.pack(pady=5)

# Run the chatbot UI
root.mainloop()
