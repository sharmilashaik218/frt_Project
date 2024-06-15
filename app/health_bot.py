from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a ChatBot instance
health_bot = ChatBot('HealthBot')

# Create a new trainer for the ChatBot
trainer = ChatterBotCorpusTrainer(health_bot)

# Train the chat bot based on the english corpus
trainer.train('chatterbot.corpus.english')

# Function to interact with the user
def chat_with_user():
    print("Hello! I am HealthBot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("HealthBot: Goodbye!")
            break
        else:
            response = health_bot.get_response(user_input)
            print("HealthBot:", response)

# Start the conversation
if __name__ == "__main__":
    chat_with_user()
