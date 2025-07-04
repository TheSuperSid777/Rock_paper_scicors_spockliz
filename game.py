import random
cpu = random.randint(1,3)
print("1 is for 📄 paper")
print("2 is for 🪨 rock")
print("3 is for  ✂️ scissors")
player = int(input("Enter the value"))
print(cpu)
if cpu == 1 and player == 1:
    print("Tie")
elif cpu == 1 and player == 2:
    print("cpu wins")
elif cpu == 1 and player == 3:
    print("player wins")
elif cpu == 2 and player == 2:
    print("Tie")
elif cpu == 2 and player == 1:
    print("Player wins")
elif cpu == 2 and player == 3:
    print("cpu wins")
elif cpu == 3 and player == 3:
    print("tie")
elif cpu == 3 and player == 2:
    print("Player wins")
elif cpu == 3 and player == 1:
    print("cpu wins")