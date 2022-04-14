# Import libraries
from telebot.async_telebot import AsyncTeleBot
import asyncio
from decouple import config
import constants as keys
import processor
import generator
import url

BOT_KEY = config('BOT_KEY') # Replace this with your own BOT_KEY
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
    
    
@bot.message_handler(regexp='“.+” [0-z,+,#]+ implementation') # Support for mobile devices
@bot.message_handler(regexp='".+" [0-z,+,#]+ implementation')
async def generate_algorithm(message: dict) -> None:
    '''Find algorithm and return the code to the user'''
    user_input = message.text.lower()
    
    processed_user_input = processor.process(user_input=user_input)
    query, programming_language = processed_user_input["query"], processed_user_input["programming_language"]
    
    if not query or not programming_language:
        response = keys.WRONG_FORMAT
        
    else:
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
    

@bot.message_handler(regexp='^thanks')
async def thanks(message: dict) -> None:
    '''Reply to a thanks message'''
    response = keys.THANKS
    await bot.send_message(message.chat.id, response)
    
    
@bot.message_handler(content_types=['text'])
async def other_messages(message: dict) -> None:
    '''Respond to unrecognizable messages'''
    response = keys.UNKNOWN_COMMAND
    await bot.send_message(message.chat.id, response)
    
    
asyncio.run(bot.polling())