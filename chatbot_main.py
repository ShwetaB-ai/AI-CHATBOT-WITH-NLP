import nltk
import random
from nltk.stem import WordNetLemmatizer



lemmatizer = WordNetLemmatizer()

corpus = """
Hello! I am your AI chatbot.
I can answer questions about programming, weather, and general topics.
Python is a programming language used for web development, AI, and data science.
Artificial intelligence enables machines to think and learn.
Machine learning is a subset of artificial intelligence.
Weather describes atmospheric conditions like temperature and humidity.
India is a country in Asia.
Pune is a city in Maharashtra.
"""

sent_tokens = nltk.sent_tokenize(corpus.lower())

greeting_inputs = ["hello", "hi", "hey", "greetings"]
greeting_responses = ["Hello!", "Hi there!", "Hey!", "Greetings!"]

def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in greeting_inputs:
            return random.choice(greeting_responses)
    return None

def get_response(user_input):
    user_tokens = preprocess(user_input)
    
    best_match = None
    best_score = 0

    for sentence in sent_tokens:
        sent_tokens_list = preprocess(sentence)
        
        common_words = set(user_tokens).intersection(set(sent_tokens_list))
        score = len(common_words)
        
        if score > best_score:
            best_score = score
            best_match = sentence

    if best_score == 0:
        return "Sorry, I didn't understand that."
    else:
        return best_match

print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("🤖 Chatbot: Goodbye! 👋")
        break

    greet = greeting(user_input)
    if greet:
        print("🤖 Chatbot:", greet)
    else:
        response = get_response(user_input)
        print("🤖 Chatbot:", response)