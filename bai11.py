import random

while True:
    human = input("Nhap ky tu (b-d-k), ky tu khac de thoat: ")

    if human not in ["b", "d", "k"]:
        break

    computer = random.choice(["b","d","k"])

    print("Computer:", computer)

    if human == computer:
        print("Ty so human - computer: 0 - 0")

    elif (human == "b" and computer == "k") or \
         (human == "k" and computer == "d") or \
         (human == "d" and computer == "b"):
        print("Ty so human - computer: 1 - 0")

    else:
        print("Ty so human - computer: 0 - 1")
