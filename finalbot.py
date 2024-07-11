import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class ChatbotApp(QMainWindow):
    def __init__(self):
        super().__init__()


        self.chatbot = ChatBot('Buddha')
        self.trainer = ListTrainer(self.chatbot)
        self.train_chatbot()


        self.setWindowTitle("Chat with Buddha")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.layout.addWidget(self.chat_display)

        self.user_input = QLineEdit()
        self.layout.addWidget(self.user_input)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

    def train_chatbot(self):
        FILE_PATH = "processed_chat.txt"
        ADDITIONAL_FILE_PATH = "additional_chat.txt"
        cleaned_lines = self.clean_file(FILE_PATH)
        additional_lines = self.clean_file(ADDITIONAL_FILE_PATH)
        cleaned_lines.extend(additional_lines)
        self.trainer.train(cleaned_lines)

    def clean_file(self, file_path):
        cleaned_lines = []
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for line in lines:
                line = line.replace("'", "").replace('"', "").strip()
                if line:
                    cleaned_lines.append(line)
        except Exception as e:
            print(f"An error occurred while cleaning the file: {e}")
        return cleaned_lines

    def send_message(self):
        message = self.user_input.text()
        if message.strip():
            self.chat_display.append(f"You: {message}")
            self.user_input.clear()
            response = self.chatbot.get_response(message)
            self.chat_display.append(f"Buddha: {response}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatbotApp()
    window.show()
    sys.exit(app.exec_())
