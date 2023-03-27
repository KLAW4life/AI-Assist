# AI-Assist

This is my fist project to try and create an AI assistant in Ubuntu.

How to run this program:

Start virtual environment:
```bash
python3 -m venv venv (you may need to use python instead if you are using python)
source venv/bin/activate (or .\venv\Scripts\activate on Windows)
pip install -r requirements.txt
```

Then run the following command in the terminal:
```bash
sudo apt install libespeak-dev
```

First we need to install the Text to Speech (TTS) library for Python 2 and 3 for Linux Users

```bash
pip install pyttsx3
```
