import random

print('Welcome to the magic eight ball!')

print('please type your question for me')
while True:
    question = input('> ')

    answers = ['yes.','no.', 'maybe.','of course.','likey.','am i corect.',
               
              'sure.','definitly.','very possible.','sorry try again later.',
               'better not tell you now.','dont count on it.','very doutful.',
               'signs point yes.','ask again later.','it is certain.',
               'out look good.',]
    
    answer = random. choice(answers)
    print(answer)




      
