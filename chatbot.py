import datetime
import random

# Date, time and day
def get_datetime():
    now = datetime.datetime.now()
    return now.strftime("%d-%m-%Y"), now.strftime("%H:%M"), now.strftime("%A")

# Calculator
def calculate(expression):
    try:
        return eval(expression)
    except:
        return "Invalid calculation 😅"

# Quotes list
def get_quote():
    quotes = [
        "Believe in yourself and keep learning.",
        "Consistency beats talent when talent doesn’t work hard.",
        "Small progress every day leads to big success.",
        "Learning never exhausts the mind."
    ]
    return random.choice(quotes)

# Chatbot logic
def chatbot_reply(user_input):
    user_input = user_input.lower()
    date, time, day = get_datetime()

    greetings = ["hello", "hi", "hey", "hii", "good morning", "good evening"]

    if user_input in greetings:
        return "Hello! 👋 I'm here to chat and help you."

    elif user_input == "how are you":
        return "I'm doing great 🤖 Always ready to talk!"

    elif user_input.startswith("i am"):
        mood = user_input.replace("i am", "").strip()
        return f"I see 👍 Feeling {mood} is totally okay."

    elif user_input == "time":
        return f"Current time is {time}"

    elif user_input == "date":
        return f"Today's date is {date}"

    elif user_input == "day":
        return f"Today is {day}"

    elif user_input.startswith("calc"):
        expression = user_input.replace("calc", "").strip()
        return f"Result: {calculate(expression)}"

    elif user_input == "python":
        return (
            "Python is a beginner-friendly language used in web development, "
            "automation, data science, AI, and software development."
        )

    elif user_input == "c language":
        return (
            "C is a powerful programming language used for system programming, "
            "operating systems, and embedded systems."
        )

    elif user_input == "dsa":
        return (
            "DSA stands for Data Structures and Algorithms. "
            "It helps in writing efficient and optimized code."
        )

    elif user_input == "ai":
        return (
            "Artificial Intelligence enables machines to think, learn, "
            "and make decisions like humans."
        )

    elif user_input == "internship":
        return (
            "Internships help you gain real-world experience, improve skills, "
            "and increase job opportunities."
        )

    elif user_input == "skills":
        return (
            "Important skills:\n"
            "- Programming\n"
            "- Problem solving\n"
            "- Communication\n"
            "- Time management\n"
            "- Logical thinking"
        )

    elif user_input == "study tips":
        return (
            "Study Tips:\n"
            "1. Set clear goals\n"
            "2. Practice daily\n"
            "3. Revise regularly\n"
            "4. Take breaks\n"
            "5. Stay consistent"
        )

    elif user_input == "food":
        return "Food keeps us energized 😄 What's your favorite dish?"

    elif user_input == "hobby":
        return "Hobbies reduce stress and increase creativity 🎨🎵"

    elif user_input == "motivation":
        return "Keep going 💪 Every step forward counts."

    elif user_input == "quote":
        return get_quote()

    elif user_input == "joke":
        return "Why did the programmer quit his job? Because he didn't get arrays 😂"

    elif user_input == "weather":
        return "I can't check live weather 🌦️ but I hope it's good where you are!"

    elif user_input == "help":
        return (
            "You can talk to me using these commands:\n"
            "- hello / hi\n"
            "- how are you\n"
            "- i am happy/sad\n"
            "- time / date / day\n"
            "- calc 8*5\n"
            "- python / c language / dsa / ai\n"
            "- internship / skills\n"
            "- study tips\n"
            "- food / hobby\n"
            "- motivation / quote / joke\n"
            "- weather\n"
            "- bye"
        )

    elif user_input == "bye":
        return "Goodbye 👋 Take care and keep learning!"

    else:
        return "Hmm 🤔 I didn't understand that. Type 'help' to see options."

# Main loop
def run_chatbot():
    print("🤖 Interactive Rule-Based Chatbot Started")
    print("Type 'help' to explore what I can do\n")

    while True:
        user_input = input("You: ")
        response = chatbot_reply(user_input)
        print("Bot:", response)

        if user_input.lower() == "bye":
            break

    print("🤖 Chatbot Session Ended")

# Run chatbot
run_chatbot()