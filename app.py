#!usr/bin/env python
# -*-coding:utf-8-*-

import json
import random
from colorama import *
init(autoreset=True)

score = 0
patterns = []
patterns_err = []

def initialize():
    global patterns
    try:
        with open('./patterns.json') as f:
            content = f.read()
        patterns = json.loads(content, encoding='utf-8')
    except Exception as err:
        print 'Load json failed!'
        print err
        exit(1)


def print_definition(rand_index):
    global score
    print (Fore.YELLOW + ' -*- Definition: -*-')
    print (patterns[rand_index]['definition'])
    print (Fore.YELLOW + ' -*- Please input the name of this pattern -*-')
    answer = raw_input()
    if answer.capitalize() == patterns[rand_index]['name'].capitalize():
        print (Fore.GREEN + 'Nice work!')
        score += 1
    else:
        print (Fore.RED + 'Oops! Not correct answer...')
        print (Fore.RED + 'The correct answer is: ' + patterns[rand_index]['name'])
        patterns_err.append(patterns[rand_index]['name'])
    print ''


def game():
    global patterns
    while patterns:
        rand_index = random.randint(0, len(patterns) - 1)
        print_definition(rand_index)
        del patterns[rand_index]
    print (Fore.YELLOW + 'Your final score: ' + str(score) + '/23.')
    if patterns_err:
        patterns_err.sort()
        print 'Please review the definitions of these patterns: '
        for each_err in patterns_err:
            print each_err
    else:
        print 'Fantastic! Keep going!'


if __name__ == '__main__':
    initialize()
    game()