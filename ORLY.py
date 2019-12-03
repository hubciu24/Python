import random

def welcome():
    print(
        """
             |-----------------------------------------------|
             |               WITAJ W GRZE                    |
             |              ORZEL VS RESZKA                  | 
             |-----------------------------------------------|
        """
    )
def computer():
    result = random.randint(1, 2)
    return result

def player():
    choice = input("Wybierz orła (O) lub Reszkę (R)")
    while choice not in ("O", "R"):
        choice = input("Wybierz orła (O) lub Reszkę (R)")

    if choice == "O":
        choice = 1
    elif choice == "R":
        choice = 2
    else:
        print("Wybierz O lub R!")
    return choice

#main

welcome()
play = player()
comp = computer()

if comp == 1:
    print("ORZEŁ!")
elif comp == 2:
    print("RESZKA!")

if play == comp:
    print("WYGRAŁEŚ!")
else:
    print("Przegrałeś!")

input("\nNaciśnij Enter aby wyjść!")

