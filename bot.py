from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import random

def clean_file(file_path):
    cleaned_lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            line = line.replace("'", "").replace('"', "").strip()
            if line:  # Check if the line is not empty
                cleaned_lines.append(line)
    except Exception as e:
        print(f"An error occurred while cleaning the file: {e}")
    return cleaned_lines

FILE_PATH = "processed_chat.txt"
ADDITIONAL_FILE_PATH = "additional_chat.txt"

# Clean the existing data file
cleaned_lines = clean_file(FILE_PATH)

# Optionally, append additional training data
additional_lines = clean_file(ADDITIONAL_FILE_PATH)
cleaned_lines.extend(additional_lines)

# Create a new chat bot named 'CoolBot'
chatbot = ChatBot('Buddha')

trainer = ListTrainer(chatbot)
trainer.train(cleaned_lines)
exit_conditions = ("quit", "exit")



while True:
    query = input("YOU > ")
    if query.lower() in exit_conditions:
        print("Buddha > See you later!")
        break
    else:
        response = chatbot.get_response(query)
        print(f"Buddha  > {response}")
