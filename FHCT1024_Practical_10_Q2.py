capitals = { #key (state), value (capital)
    'Johor': 'Johor Bahru',
    'Kedah': 'Alor Setar',
    'Kelantan': 'Kota Bharu',
    'Melaka': 'Melaka',
    'Negeri Sembilan': 'Seremban',
    'Pahang': 'Kuantan',
    'Penang': 'Georgetown',
    'Perak': 'Ipoh',
    'Perlis': 'Kangar' ,
    'Sabah': 'Kota Kinabalu',
    'Sarawak': 'Kuching',
    'Selangor': 'Shah Alam',
    'Terengganu': 'Kuala Terengganu'
}

import random

# print(capitals.keys()) # left side data
# print(capitals.values()) # right side data

for quiz in range(2):
    quiz_file = open(f"quiz_{str(quiz+1)}.txt", "w")

    quiz_file.write("Name : \n")
    quiz_file.write("ID   : \n")
    quiz_file.write("\n\n")

    states = list(capitals.keys()) #prepare the list of states
    random.shuffle(states) #randomise the states
    # print(states)

    for question in range(2):
        correct = capitals[states[question]] # get the correct answer
        # print(f"correct answer: {correct}")
        wrong = list(capitals.values())
        wrong.remove(correct) # remove the correct answers from the list
        wrong = random.sample(wrong, 3)
        options = wrong + [correct]
        random.shuffle(options)
        # print("Options :")
        # print(options)
        quiz_file.write(f"{str(question+1)}. What is the capital of {states[question]}?\n")

        for option in range(4):
            quiz_file.write(f"{'ABCD'[option]}. {options[option]}\n")

        quiz_file.write("\n") # space between question

    quiz_file.close()