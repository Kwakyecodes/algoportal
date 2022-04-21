# Import libraries
from telebot.async_telebot import AsyncTeleBot
import asyncio
import os
import constants as keys
import processor
import generator
import url

BOT_KEY = os.environ.get("BOT_KEY") # Replace this with your own BOT_KEY
bot = AsyncTeleBot(BOT_KEY)

print("Bot started...")


@bot.message_handler(commands=['start'])
@bot.message_handler(regexp='^hi')
@bot.message_handler(regexp='^hello')
async def intro(message: dict) -> None:
    '''Introduce bot'''
    await bot.send_message(message.chat.id, keys.INTRODUCTION)
    
    
@bot.message_handler(commands=['help'])
async def help(message: dict) -> None:
    '''Show user how to use bot'''
    await bot.send_message(message.chat.id, keys.HELP_INFO)
    

@bot.message_handler(regexp='^thanks')
@bot.message_handler(regexp='^thank')
async def thanks(message: dict) -> None:
    '''Reply to a thanks message'''
    response = keys.THANKS
    await bot.send_message(message.chat.id, response)
    
    
@bot.message_handler(content_types=['text'])
async def generate_algorithm(message: dict) -> None:
    '''Find algorithm and return the code to the user'''
    user_input = message.text.lower()
    
    processed_user_input = processor.process(user_input=user_input)
    query, programming_language = processed_user_input["query"], processed_user_input["programming_language"]
    
    # Get geeks for geeks url from url.py
    link = url.get_link(query=query)
    
    # Check if link is empty
    if not link:
        response = keys.ALGORITHM_NOT_FOUND
        await bot.send_message(message.chat.id, response)
        return
    
    response = generator.generate_code(url=link, programming_language=programming_language)

    if type(response) == list:
        for code in response:
            await bot.send_message(message.chat.id, code)
    else:
        await bot.send_message(message.chat.id, response['error'])
    
asyncio.run(bot.polling())