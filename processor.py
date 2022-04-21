# Import libraries
import constants as keys

def process(user_input: str) -> dict:
    '''Process user_input and extract query and programming language'''
    # Remove full stop from user input
    if user_input[-1] == '.':
        user_input = user_input[0:-1]
        
    languages = keys.LANGUAGES
    programming_language = ''
    
    for word in user_input.split(" "):
        if word in languages:
            programming_language = word
            break

    result = {"query": user_input, "programming_language": programming_language}
    
    return result
