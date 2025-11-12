# Система вопросов и ответов
import json

def get_question():
    with open("questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)
    return questions[0]  # пока берём первый, можно заменить на случайный

