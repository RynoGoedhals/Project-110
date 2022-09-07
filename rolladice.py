import random

response = input("Do you want to roll a dice y/n: ")

while response == "y":
    no = random.randint(1, 6)

    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        response = input("Do you want to roll a dice y/n: ")
        

    if no == 2:
        print("[-----]")
        print("[0    ]")
        print("[     ]")
        print("[    0]")
        print("[-----]")
        response = input("Do you want to roll a dice y/n: ")

    if no == 3:
        print("[-----]")
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
        print("[-----]")
        response = input("Do you want to roll a dice y/n: ")

    if no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
        response = input("Do you want to roll a dice y/n: ")

    if no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
        response = input("Do you want to roll a dice y/n: ")

    if no == 6:
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")
        response = input("Do you want to roll a dice y/n: ")