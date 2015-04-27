#!usr/bin/env python
# -*-coding:utf-8-*-

import json
import random
import os

score = 0
patterns = []


def initialize():
    global patterns
    try:
        with open('./patterns.json') as f:
            content = f.read()
        patterns = json.loads(content)
    except Exception as err:
        print 'Load json failed!'
        print err
        exit(1)



def print_definition(rand_index):
    global score
    print ' -*- Definition: -*-'
    print patterns[rand_index]['definition']
    print ' -*- Please input the name of this pattern -*-'
    answer = raw_input()
    if answer.capitalize() == patterns[rand_index]['name'].capitalize():
        print ('Nice work!')
        score += 1
    else:
        print ('Oops! Not correct answer...')
        print ('The correct answer is: ' + patterns[rand_index]['name'])
    print ''


def game():
    global patterns
    while patterns:
        rand_index = random.randint(0, len(patterns) - 1)
        print_definition(rand_index)
        del patterns[rand_index]
    print 'Your final score: ' + str(score) + '/23.'


if __name__ == '__main__':
    initialize()
    game()
    os.system("pause")