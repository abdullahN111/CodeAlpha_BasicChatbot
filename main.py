def main():

    print("\nWelcome to the Chatbot!\n")
    print("Please begin to chat by selecting a number.")

    list_of_responses = [
        "Hello, How are you?",
        "What can I do for you?",
        "Yes I can",
        "Goodbye!",
        "I'm here to help you with anything you need."
    ]
    
    list_of_inputs = [
        "Hi",
        "Hello",
        "Hey",
        "Goodbye",
        "See you later",
        "Can you help me?",
        "What can you do?"
    ]
    
    for index, inputs in enumerate(list_of_inputs):
        print(f"{index+1}. {inputs}")
        
    while True:
        user_input = input("\nYou: ")
        if user_input == "1":
            user_input = list_of_inputs[0]
            print(f"Chatbot: {list_of_responses[0]}")
        elif user_input == "2":
            user_input = list_of_inputs[1]
            print(f"Chatbot: {list_of_responses[0]}")
        elif user_input == "3":
            user_input = list_of_inputs[2]
            print(f"Chatbot: {list_of_responses[0]}")
        elif user_input == "4":
            user_input = list_of_inputs[3]
            print(f"Chatbot: {list_of_responses[3]}")
        elif user_input == "5":
            user_input = list_of_inputs[4]
            print(f"Chatbot: {list_of_responses[3]}")
        elif user_input == "6":
            user_input = list_of_inputs[5]
            print(f"Chatbot: {list_of_responses[2]}")
            
        elif user_input == "7":
            user_input = list_of_inputs[6]
            print(f"Chatbot: {list_of_responses[4]}")
            
        elif user_input.lower() in ["exit", "quit", "bye"]:
            print("Exiting the chatbot. Goodbye!")
            break
        else:
            print("Invalid input. Please select a number from the list.")
            

main()