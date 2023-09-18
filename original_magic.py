import requests

question = input('Enter your question for the magic 8 ball: ')

magic_8_ball_url = f'https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/{question}'

response = requests.get(magic_8_ball_url).json()

answer = response['answer']

print(f'The magic 8 ball says....  {answer}')



# Part 2 - Magic 8 Ball API
# Why would it be hard to write tests for original_magic.py? It would be hard to write a test for original_magic.py
# because the code is not working: We cannot run a test until we get the code that can be tested.

# Why was it re-written as functions, and why were the functions used chosen?
