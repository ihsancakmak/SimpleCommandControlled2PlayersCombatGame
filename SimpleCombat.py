import random

def startgame():
    firstHero = ""
    secondHero = ""

    print("----- First Hero -----")
    firstHero += input("Please type your hero's name: ")
    while firstHero.isspace() or firstHero == "":
        print("Names cannot be empty.")
        firstHero = ""
        firstHero += input("Please type your hero's name: ")

    while True:
        print("----- Second Hero -----")
        secondHero = input("Please type your hero's name: ")
        while secondHero.isspace() or secondHero == "":
            print("Names cannot be empty.")
            secondHero = ""
            secondHero = input("Please type your hero's name: ")

        if nameError(firstHero, secondHero):
            continue
        break
    restart(firstHero, secondHero)

def restart(firstHero, secondHero):
    player1 = ""
    player2 = ""

    health1 = 100
    health2 = 100

    HP1 = f"HP[{health1}]:{int(health1/2)*'|'}"
    HP2 = f"HP[{health2}]:{int(health2/2)*'|'}"

    if choose(firstHero, secondHero) == firstHero:
        player1 += firstHero
        player2 += secondHero
    else:
        player1 += secondHero
        player2 += firstHero

    printHero(HP1, HP2, player1, player2)
    attack(player1, player2,health1, health2, HP1, HP2, firstHero, secondHero)


def nameError(firstHero, secondHero):
    while firstHero == secondHero:
        print("Names cannot be the same, please choose another name!")
        return True
    return False


def choose(firstHero, secondHero):
    names = [firstHero, secondHero]
    player1 = random.choice(names)
    print(f"Coin toss result: {player1} starts first!")
    return player1


def printHero(HP1, HP2, firstHero, secondHero, size=70, space=0):
    while firstHero or secondHero:
        print(firstHero[:size].ljust(size) + " " * space + secondHero[:size])
        firstHero = firstHero[size:]
        secondHero = secondHero[size:]

    while HP1 or HP2:
        print(HP1[:size].ljust(size) + " " * space + HP2[:size])
        HP1 = HP1[size:]
        HP2 = HP2[size:]


def attack(player1, player2, health1, health2, HP1, HP2, firstHero, secondHero):
    i = 0
    while health1 and health2 > 0:

        if i < 1:
            print(f"----------{player1} Attacks!!----------")

            power = int(input("Choose your attack magnitude between 1 and 50:"))

            while 1 > power or power > 50:
                print("The attack magnitude must be between 1 and 50.")
                power = int(input("Choose your attack magnitude between 1 and 50:"))

            i += 1
            damage = hitchance(power)
            if damage > 0:
                health2 = health2 - damage

                HP2 = f"HP[{health2}]:{int(health2 / 2) * '|'}"
                printHero(HP1, HP2, player1, player2)
                if health2 <= 0:
                    finish(player1, firstHero, secondHero)
            else:
                print(f"Oooops! {player1} missed the attack!")
                health2 = health2 - damage

                HP2 = f"HP[{health2}]:{int(health2 / 2) * '|'}"
                printHero(HP1, HP2, player1, player2)

        else:
            print(f"----------{player2} Attacks!!----------")

            power = int(input("Choose your attack magnitude between 1 and 50:"))

            while 1 > power or power > 50:
                print("The attack magnitude must be between 1 and 50.")
                power = int(input("Choose your attack magnitude between 1 and 50:"))

            i -= 1
            damage = hitchance(power)
            if damage > 0:

                health1 = health1 - damage

                HP1 = f"HP[{health1}]:{int(health1 / 2) * '|'}"
                printHero(HP1, HP2, player1, player2)
                if health1 <= 0:
                    finish(player2, firstHero, secondHero)
            else:

                print(f"Oooops! {player2} missed the attack!")
                health1 = health1 - damage
                HP1 = f"HP[{health1}]:{int(health1 / 2) * '|'}"
                printHero(HP1, HP2, player1, player2)


def hitchance(power):
    chance = random.randint(1,52)
    if chance > power:
        return power
    else:
        return 0


def finish(winner, firstHero, secondHero):
    star = "*" * 100
    writtenStar = int((100 - (len(winner) + 9))/2) * "*"
    print(star)
    print(f"{writtenStar} {winner} Wins!!! {writtenStar}")
    print(star)

    answer = input("Do you want to play again?(yes/no): ")
    if answer == "yes":
        return restart(firstHero, secondHero)
    else:

        exit()


startgame()
