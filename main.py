# Логика команд и обработки
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from quiz import get_question
from database import get_user_score, add_score

app = Client("quiz_bot", bot_token="YOUR_BOT_TOKEN", api_id=12345, api_hash="your_api_hash")

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("Привет! Я квиз-бот. Напиши /quiz, чтобы начать игру.")

@app.on_message(filters.command("quiz"))
async def quiz_handler(client, message):
    question = get_question()
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(opt, callback_data=opt)] for opt in question["options"]
    ])
    await message.reply(question["question"], reply_markup=keyboard)

@app.on_callback_query()
async def answer_handler(client, callback_query):
    correct = "Париж"  # заглушка
    if callback_query.data == correct:
        add_score(callback_query.from_user.username, 1)
        await callback_query.answer("✅ Верно!")
    else:
        await callback_query.answer("❌ Неверно!")

@app.on_message(filters.command("score"))
async def score_handler(client, message):
    score = get_user_score(message.from_user.username)
    await message.reply(f"У тебя {score} очков!")

app.run()

