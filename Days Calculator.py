from datetime import datetime


def main():
    today = datetime.today()
    birth_date = input("Enter date in YYYY-MM-DD format : ")
    
    try:
        date = datetime.strptime(birth_date, "%Y-%m-%d")

        if date.month > today.month:
            print(f"\nYou will turn {today.year - date.year} this year 🎂 !")
        else:
            print(f"\nYou had {today.year - date.year} birthdays 🎁 !")

        print(f"\nYou are "
          f"\n{(today - date).days} days "
          f"\n{(today.hour - date.hour)} hours "
          f"\n{(today.minute - date.minute)} minutes and"
          f"\n{(today.second - date.second)} seconds "
          f"\nold !")

    except:
        print("Invalid date")


if __name__ == "__main__":
    main()
