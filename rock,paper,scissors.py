import random as randomChoice

newDict = {'rock':'1', 'paper':'2','scissors':'3'}
compDict = {'1':'rock', '2':'paper','3':'scissors'}
# paper beats rock
# scissors beats paper
# rock beats scissors

def Results(userResponse, computerResponse):
        diff = int(userResponse) - computerResponse
        if diff in [1,-2]:
            return 'you win'
        if diff in [-1,2]:
            return 'Computer won'
        else:
            return 'It\'s a Tie'
def CheckRepeat(again):
    if again =='Y':
        return True
    elif again == 'N':
        return False
    else:
        print('I\'m not sure what that means so we are playing again')
        return True

repeat = True

while repeat:   
    Name = input('Whats your name?')
    response = input(' let\'s play a game!\nRock = 1, Paper = 2, Scissors = 3.\n Which option do you choose?')
    computer = randomChoice.randint(1,3)
    score = Results(response,computer)
    print('Computer chose: '+ compDict.get(str(computer)))
    print(score)
    again = input('Do you wanna play again?(Y/N)')
    repeat = CheckRepeat(again)
