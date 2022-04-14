# Import libraries
import re

def process(user_input: str) -> dict:
    '''Process user_input and extract query and programming language'''
    query = re.findall('".+"', user_input)
    if not query: # Support for mobile devices
        query = re.findall('“.+”', user_input)
        
    query = query[0][1:-1]
    
    programming_language = user_input.split(" ")[-2]
    
    result = {"query": query, "programming_language": programming_language}
    return result
