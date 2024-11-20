from flask import Flask
import random

app = Flask(__name__)

jokes = [
    "Relationship status? I'll leave the relations to the database.",
    "Why was the function sad after a successful first call? It didn't get a callback.",
    "Whats the object-oriented way to become wealthy? Inheritance",
    "!false -> It's funny 'cause it's true.",
    "I never tell the same joke twice, I have a DRY sense of humor.",
    "Why don't bachelors like Git? Because they are afraid to commit.",
    "A SQL query goes into a bar, walks up to two tables and asks: Can I JOIN you?",
    "How many developers does it take to change a light bulb? None. It's a hardware issue",
]


@app.get("/")
def tell_joke():
    joke = random.choice(jokes)
    return f"<p>{joke}</p>"
