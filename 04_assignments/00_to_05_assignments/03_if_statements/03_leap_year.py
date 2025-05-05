def leap_year():
    year:int = int(input("Enter as year : "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is a not leap year.")
        else:
            print(f"{year} is a not leap year.")
    else:
        print(f"{year} is a not leap year.")

if __name__ == "__main__":
    leap_year()
