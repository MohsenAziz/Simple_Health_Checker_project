def welcome_message():
    print('''Hi there, thanks for visiting  health centre today:)
first let's start by checking your weight:-''')

def getting_data():
    gender=int(input('Enter your gender please 1 for male 0 for woman: '))
    height_cm=int(input('Now enter your height in cm please, (at least 150cm): '))
    return gender,height_cm


def weight(gender, height_cm):
    while (1):
        if height_cm < 150:
            print('please enter value higher than 150')
            height_cm = int(input('Now enter your height in cm please, (at least 150cm): '))
        elif gender == 1:
            result = round(52 + 1.9 * (height_cm - 150) / 2.54, 2)
            break
        else:
            result = round(49 + 1.7 * ((height_cm - 150) / 2.54), 2)
            break
    print(f'your ideal weight should be around: {result}')


def general_tips_questionnaire():
    print('Want to check Some general tips for healthier body?')
    answer = int(input('Enter 1 if yes , 0 otherwise: '))
    return answer


def general_healthy_tips(answer):
    while (1):

        if answer == 1:
            print('Great choice, daily checking on your health is really important.')
            print('Here are some tips to stay healthy every day:-')
            print("""
                 1) Eat a healthy diet.
                 2) Consume less salt and sugar.
                 3) Reduce intake of harmful fats.
                 4) Avoid harmful use of alcohol.
                 5) Don’t smoke.
                 6) Be active.
                 7) Check your blood pressure regularly.
                 8) Get tested.
                 9) Cover your mouth when coughing or sneezing.
                 10) Prevent mosquito bites.
                 11) Follow traffic laws.
                 12) Drink only safe water.
                 13) Clean your hands properly.
                 14) Prepare your food correctly.
                 15) Have regular check-ups.""")
            break
        elif answer == 0:
            print("Other time then, but don't forget to check later")

            break
        else:
            print('Please enter a valid option')
            answer = int(input('Enter 1 if yes , 0 otherwise: '))


def food_tips_questionnaire():
    print('Want to check Some food concerning tips?')
    answer=int(input('Enter 1 if yes , 0 otherwise: '))
    return answer


def food_concerning_tips(answer):
    while (1):

        if answer == 1:
            print('Great choice, daily checking on your health is really important.')
            print('Here are some tips to stay healthy every day:-')
            print("""
1)Choose whole foods instead of processed. ...
2)Say no to sugary drinks. ...
3)Keep healthy food readily available. ...
4)Try the “Outer Ring” technique while buying food. ...
5)Go nuts for nuts (and seeds). ...
6)Eat more fish. ...
7)Use whole grain flour in baking recipes. ...
8)Eat in smaller plates.""")
            break
        elif answer == 0:
            print("Other time then, but don't forget to check later")

            break
        else:
            print('Please enter a valid option')
            answer = int(input('Enter 1 if yes , 0 otherwise: '))




def conclude():
    print('Have a great day')