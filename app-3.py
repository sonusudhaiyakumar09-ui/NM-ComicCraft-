import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

try:
    from google import genai
except ImportError:
    genai = None

load_dotenv()

app = Flask(__name__)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def generate_story(topic, genre, characters, panels):
    """Generate a comic story using Google's Gemini model."""
    if not GEMINI_API_KEY or genai is None:
        return demo_story(topic, genre, characters, panels)

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)

        prompt = f"""
Create a short, creative comic story.

Title/topic: {topic}
Genre: {genre}
Characters: {characters}
Number of panels: {panels}

Return exactly {panels} panels. For each panel provide:
Panel number
Scene description
Dialogue
Narration

Keep the story suitable for students and easy to convert into a comic.
"""
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as error:
        return f"Gemini API error: {error}\n\n" + demo_story(topic, genre, characters, panels)

def demo_story(topic, genre, characters, panels):
    result = [
        f"COMIC TITLE: {topic}",
        f"GENRE: {genre}",
        f"CHARACTERS: {characters}",
        "",
        "DEMO MODE",
        "Add your Gemini API key in the .env file to generate AI-powered stories.",
        ""
    ]

    for number in range(1, panels + 1):
        result.append(f"PANEL {number}")
        result.append(f"Scene: The characters begin their {genre.lower()} adventure.")
        result.append(f"Dialogue: The team says, 'Let's solve this together!'")
        result.append(f"Narration: The story continues with a new challenge.")
        result.append("")

    return "\n".join(result)

@app.route("/", methods=["GET", "POST"])
def home():
    story = None
    form_data = {
        "topic": "",
        "genre": "Adventure",
        "characters": "",
        "panels": 4
    }

    if request.method == "POST":
        form_data["topic"] = request.form.get("topic", "").strip()
        form_data["genre"] = request.form.get("genre", "Adventure")
        form_data["characters"] = request.form.get("characters", "").strip()

        try:
            form_data["panels"] = max(1, min(10, int(request.form.get("panels", 4))))
        except ValueError:
            form_data["panels"] = 4

        if form_data["topic"] and form_data["characters"]:
            story = generate_story(
                form_data["topic"],
                form_data["genre"],
                form_data["characters"],
                form_data["panels"]
            )
        else:
            story = "Please enter a comic topic and at least one character."

    return render_template("index.html", story=story, form_data=form_data)

if __name__ == "__main__":
    app.run(debug=True)
