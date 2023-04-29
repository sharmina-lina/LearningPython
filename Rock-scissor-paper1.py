import random
print("Welcome")
chars = "RPS"
def rps(player1,player2):
    if (player1 == "R" and player2 == "P"):
        return "Computer Won"
    elif (player1 == "P" and player2 == "R"):
        return "you won"
    elif (player1 == "P" and player2 == "S"):
        return "Computer won"
    elif player1 == "S" and player2 == "P":
        return "you won"
    elif player1 == "R" and player2 == "S":
        return "you won "
    elif player1 == "S" and player2 == "R":
        return "Computer won"
    elif player1 not in chars:
        return "wrong input"
    elif player1 == player2:
        return "Match tie"
run = True
while run:
    player1 = input("R for Rock, P for paper and S for Scissor: \n" )
    player2 = random.choice(chars)
    print(rps(player1, player2))