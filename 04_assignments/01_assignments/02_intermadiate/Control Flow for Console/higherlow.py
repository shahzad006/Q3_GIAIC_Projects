import random

round = 5

def main():
    print("********************** Wellcome to the High Low Game **********************")
    

    your_score = 0

    for i in range(round):
        print("Round" , i+1)

        computer_number:int =  random.randint(1,100)
        your_number : int = random.randint(1,100)

        print("Your number is :",your_number)

        choice :str = input("Do you think your number is higher or lower than the computer's number ? ")
        higher_and_correct : bool = choice == "higher" and your_number > computer_number
        lower_and_correct : bool = choice == "lower" and your_number < computer_number


        if higher_and_correct or lower_and_correct:
            print("You are right the computer number was" , computer_number)
            your_score +=1
        else:
            print("That's is correct . the computer's number was",computer_number)

        print("Your score is now",your_score)
        print()
    print("********************** Thanks for playing **********************")



if __name__ == "__main__":
    main()