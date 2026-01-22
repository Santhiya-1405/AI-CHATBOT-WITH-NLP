import nltk
from nltk.chat.util import Chat, reflections

pairs = [

    (r"hi|hello|hey|hai", 
     ["Hello!", "Hi there!", "Hey! How can I help you?"]),
    (r"good (morning|afternoon|evening)", 
     ["Good %1! How can I help you today?"]),

    (r"how are you", 
     ["I'm doing great! How about you?", "I'm fine, thank you!"]),
    (r"what.*doing", 
     ["I'm chatting with you and answering your questions."]),
    (r"tell me something", 
     ["Sure! AI is changing the future of technology."]),
    (r"tell me something interesting", 
     ["Did you know? AI can recognize faces better than humans in some cases."]),
    (r"are you busy", 
     ["Never! I'm always here to help you."]),
    (r"what is your work|what do you do", 
     ["My job is to assist users by answering questions."]),

    (r"what.*your name", 
     ["I am an AI Chatbot built using NLP."]),
    (r"who.*created you|who made you", 
     ["I was created using Python and the NLTK library."]),
    (r"what.*can you do", 
     ["I can chat with you and answer questions about AI, NLP, and programming."]),

    (r"what is ai", 
     ["AI stands for Artificial Intelligence."]),
    (r"what is nlp", 
     ["NLP stands for Natural Language Processing."]),
    (r"difference.*ai.*ml", 
     ["AI is a broad concept, while Machine Learning is a subset of AI."]),
    (r"what is machine learning", 
     ["Machine Learning enables systems to learn from data."]),

    (r"what is python", 
     ["Python is a popular programming language used in AI."]),
    (r"why.*python", 
     ["Python is easy to learn and has powerful libraries."]),
    (r"what is nltk", 
     ["NLTK is a Natural Language Processing library in Python."]),


    (r"where.*from", 
     ["I live inside your computer."]),
    (r"what time.*", 
     ["I can't check time, but your system can."]),


    (r"bye|exit|quit|goodbye", 
     ["Goodbye! Have a nice day 😊", "See you later!"])
]

default_responses = [
    "I'm not sure I understand. Can you rephrase?",
    "Interesting! Tell me more.",
    "Sorry, I don't have an answer for that yet."
]

class SmartChat(Chat):
    def respond(self, str):
        response = super().respond(str)
        return response if response else nltk.random.choice(default_responses)

def chatbot():
    print("=" * 55)
    print("🤖 SMART AI CHATBOT USING NLP (NLTK)")
    print("Type 'bye' or 'exit' to quit")
    print("=" * 55)

    chat = SmartChat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
