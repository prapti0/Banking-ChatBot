import tkinter as tk
import random

# Define some responses
greetings = ["hello", "hi", "hey", "greetings", "howdy","hy"]
thank_you = ["thank you", "thanks", "much appreciated"]
goodbyes = ["goodbye", "bye", "see you later", "take care","no"]
check_account = ["check account", "account balance", "balance"]
withdrawal = ["withdrawal", "withdraw", "cash"]
details = ["details", "information", "more"]
r=[500, 200, 1000, 100, 2000]


# Define a function to generate a response to the user's input
def generate_response(user_input):
    # Convert input to lowercase
    user_input = user_input.lower()


    # Check if user input matches a greeting
    for word in user_input.split():
        if word in greetings:
            return "Hello! How can I assist you with your banking needs?"

    # Check if user wants to check their account balance
    for word in user_input.split():
        if word in check_account:
            return "Your account balance is 5000. Is there anything else I can help you with?"

    # Check if user wants to make a withdrawal
    for word in user_input.split():
         if word in withdrawal:
             return "Sure, how much would you like to withdraw,500,200,1000,100,2000?"
    for word in user_input.split():
        if word in r:
            return "Money has been successfully withdrawal"
    # Check if user wants to know some details or information
    for word in user_input.split():
        if word in details:
            return "What kind of information are you looking for? You can ask about our interest rates, loan options, or credit card benefits."
        if "loan" in user_input:
            return "We offer personal loans, home loans, and car loans. Please visit our website or contact us for more details."

        if "credit card" in user_input:
            return "We offer several credit card options with various rewards and benefits. Please visit our website or contact us for more details."

        if "cheque book" in user_input:
            return "Every new account holder is provided with a complimentary cheque book. If you need additional cheque books, please visit our nearest branch or contact us."




    # Check if user input matches a thank you
    for word in user_input.split():
        if word in thank_you:
            return "You're welcome! Is there anything else I can help you with?"

    # Check if user input matches a goodbye
    for word in user_input.split():
        if word in goodbyes:
            return "Goodbye! Have a great day!"

    # If none of the above match, generate a generic response
    return "I'm sorry, I don't understand. Could you please rephrase your question?"


# Define a function to handle the user's input and generate a response
def handle_user_input():
    user_input = entry.get()
    response = generate_response(user_input)
    chat_history.insert(tk.END, "You: " + user_input + "\n", "user")
    chat_history.insert(tk.END, "Bot: " + response + "\n", "bot")
    entry.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("AI Banking Chatbot")
root.geometry("600x500")
root.configure(bg="#FDF5E6")

# Create the chat history text widget
chat_history = tk.Text(root, height=15, width=70, bg="#8FBC8F", fg="#000000", font=("Comic Sans MS", 12))



# Create the entry field for the user's input
entry = tk.Entry(root, width=60, bg="#ffffff", fg="#000000", font=("Comic Sans MS", 12))
entry.bind("<Return>", lambda event: handle_user_input())

# Create the send button
send_button = tk.Button(root, text="Send", command=handle_user_input, bg="#007bff", fg="#ffffff", font=("Comic Sans MS", 11))

# Pack the widgets into the main window
chat_history.tag_config("user", foreground="#000080", font=("Comic Sans MS", 11, "bold"))
chat_history.tag_config("bot", foreground="#dc3545", font=("Comic Sans MS", 11, "bold"))
chat_history.pack( padx=10, pady=10)
entry.pack(padx=5,pady=5)
#entry.pack(fill=tk.BOTH)

# Start the main loop
root.mainloop()