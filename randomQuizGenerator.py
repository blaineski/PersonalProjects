#! python3#
# this programme will run a random quiz generator

import random

# The quiz data. Keys are states and values are the capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
     'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
     'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
     'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
     'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
     'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
     'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
     'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
     'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
     'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
     'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
     'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
     'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
     'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
     'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
     'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
     'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# generate 35 quiz files
for quizNum in range(35):

    # create the quiz and answer files
    quizFile = open("capitalsquiz%s.txt" % (quizNum + 1), "w")
    answerKeyFile = open("capitalsquiz_answers%s.txt" % (quizNum + 1), "w")

    # write out the header for the quiz
    quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quizFile.write((" " * 20) + "State Capitals QUiz (Form %s)" % (quizNum + 1)
    quizFile.write("\n\n")

    # TODO: shuffle the order of the states

    # TODO: loop through all 50 states, making a question for each

