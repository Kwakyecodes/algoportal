# AlgoPortal
#### Video Demo: https://youtu.be/Y9EUVrmwvmc
#### Description:
AlgoPortal is a Telegram bot API that's capable of fetching codes from the internet for users in a matter of seconds. It automates the process of googling and looking through several websites to find code and so this bot offers a quicker and less laborious method of fetching code from the internet. AlgoPortal can be useful in several occasions: when preparing for a CS (class?=data structures and algorithm) quiz, when preparing for a software engineering interview, when working on a CS project, etc. 

The steps below state the processes AlgoPortal follows to perform it's primary function:
- User sends a message to AlgoPortal
- AlgoPortal processes the message and extracts the query and programming language
- AlgoPortal perfroms a google search of the query and gets the html code of the search result page in the form of a string
- AlgoPortal looks through the websites in the search results page and finds the first link to GeeksforGeeks. GeeksforGeeks is a website that provides a variety of services for people to learn, thrive and also have fun. They have articles on almost every algorithm or programming problem among others. 
- AlgoPortal then gets the html code of the GeeksforGeeks page in the form of a string, extracts the codes from it (if there are any) and send it to the user as a telegram message

**contants.py**  
This python file contains all the constants that are used in one or more places in the project. These are mostly the different replies of the bot. 

**processor.py**
This python file has only one function: *process*. The function takes the user's input in the form of a string and uses regular expresion to extract the query and programming language from the it. It then returns a dictionary of the query and programming lanuage.

**url.py**
This python file contains two functions: *get_data* and *get_link*. 
*get_data* takes a url in the form of a string and returns a string of the html code of that webpage of that url. 
*get_link* takes a query in the form of a string. It then creates a google search url of the query and gets the hmtl code of the search result page using *get_data*. After that, it uses a library called BeautifulSoup to collect all the links in the html code into a list. Using regular expression, *get_link* finds the GeeksforGeeks link and then returns it in the form of a string.

**generator.py** 
This python files contains four functions: *get_code_lines*, *extract_text* and *generate_code*.
*get_code_lines* basically processes a complete html article and extract html lines containing the code. It does this by getting the chunk of the html article that contains the codes and then splitting it into different divs to get the different lines of code. The fucntion then return a list of strings, which contains each line of code.
*extract_text* extracts actual text from html lines of code. It takes an html containing a line of code in the form of a string, extracts the code text in the form of a string and then returns it.
*generate_code* takes two parameters: url and programming_language, both in the form of strings. The complete html article of the url is got using the *get_data* function in **url.py**. BeautifulSoup, *get_code_lines* and *extract_text* are used to extract the programming languages and chunks of codes from the complete html article. The function then finds a list of the chunks of code that are in the programming_language programming language and return it.

**bot.py**
This is the main file for the program. The file contains the telegram bot api, Telebot. I used AsyncTelebot instead of the regular Telebot because some of processing takes a while and so the bot might need to await a few things. **bot.py** has five functions: *intro*, *help*, *generate_algorithm*, *thanks* and *other_messages*. 
*intro* sends a introduction message to the user when the user starts the bot or sends any message which begins with "hi" or "hello" (case insensitive).
*help* sends a message describing how to use AlgoPortal when a user sends a help command.
*generate_algorithm* accepts any message which is in the correct format for querying AlgoPortal. It then processes the user input using the functions in **generator.py** and send the result (codes) as messages to the user.
*thanks* responds to any message which begins with "thanks".
*other_messages* responds to any other message format which is not described above.
