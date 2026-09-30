# ComicRaft – AI Comic Story Creator Using Gemini Models

ComicRaft is a beginner-friendly Python web application that creates comic story scripts with the help of Google's Gemini AI models.

## Features

- Create an AI-generated comic story
- Enter comic topic
- Select genre
- Add characters
- Choose number of panels
- Generate scene descriptions, dialogue and narration
- Gemini API integration
- Demo mode when an API key is not configured
- Simple Flask web interface

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Google Gemini API
- python-dotenv

## Project Structure

```text
ComicRaft_AI_Comic_Story_Creator/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## How to Run

### 1. Install Python

Make sure Python 3.10 or later is installed.

### 2. Open the project folder

Open Command Prompt or Terminal inside this folder.

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate it

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 5. Install packages

```bash
pip install -r requirements.txt
```

### 6. Configure Gemini API

Rename:

```text
.env.example
```

to:

```text
.env
```

Then add your Gemini API key:

```text
GEMINI_API_KEY=your_actual_api_key
```

Do not upload `.env` to GitHub.

### 7. Run the application

```bash
python app.py
```

Open the local URL shown by Flask, normally:

```text
http://127.0.0.1:5000
```

## How ComicRaft Works

1. User enters a comic topic.
2. User selects a genre.
3. User enters character names.
4. User selects the number of comic panels.
5. Flask sends the prompt to Gemini.
6. Gemini generates the comic story.
7. The generated story is displayed on the webpage.

## Important

Never publish your Gemini API key in GitHub. Keep it inside `.env`, which is already included in `.gitignore`.

## Future Enhancements

- AI-generated comic images
- Download comic as PDF
- User accounts
- Save previous stories
- Multiple comic templates
- Text-to-speech narration
- Character image generation
- Database integration
