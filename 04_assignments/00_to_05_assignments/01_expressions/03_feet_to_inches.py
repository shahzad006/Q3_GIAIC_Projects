inch : int = 12

def foot():
    feet:int = int(input("Enter feet and I well convert into inches.  "))
    print(f"There are {inch * feet} inches in {feet} feet.")


if __name__ == "__main__":
    foot()