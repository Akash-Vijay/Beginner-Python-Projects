"""

*   File                  :       03_treasure_island.py
*   Description           :       Program to create a simple treasure island game
*   Creator               :       Akash Vijay
*   Date                  :       December 6, 2021

"""

print("!! Welcome to Treasure Island !! \n")
print("Your mission is to find the treasure\n")

choice = input("\nYou are in a crossroad. Where do you want to go? Left or Right: ").lower()
if choice == "right":
    print("Game Over. You have been killed by a lion.")
elif choice == "left":
    choice = input("You have now reached a lake. What do you want to do? Swim or Wait: ").lower()
    if choice == "swim":
        print("Game Over. You have been eaten by a crocodile.")
    elif choice == "wait":
        choice = input("You have now reached near 3 closed doors. Which one do you want to open? Red, Blue or Yellow: ").lower()
        if choice == "red":
            print("Game Over. You stepped into fire.")
        elif choice == "blue":
            print("Game Over. You stepped into fire.")
        elif choice == "yellow":
            print("Hurray. You found the Treasure.")
