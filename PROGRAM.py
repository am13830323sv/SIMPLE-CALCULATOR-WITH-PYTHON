print("Welcome To Python Calculator : ")

while True:
    NumberOne = int()

    while True:
        try:
            NumberOne = int(input("Please Enter Number One : "))

            break

        except(ValueError):
            print("Error : Please Enter Just A Number.")

            continue

    NumberTwo = int()

    while True:
        try:
            NumberTwo = int(input("Please Enter Number Two : "))

            break

        except(ValueError):
            print("Error : Please Enter Just A Number.")

            continue

    Operation = int()

    while True:
        print("1) Sum")
        print("2) Subtraction")
        print("3) Multiplication")
        print("4) Divide")

        try:
            Operation = int(input("Please Enter Operation's Nummber : "))

            if Operation < 1 or Operation > 4:
                print("Error : Your Operation Not Exist.")

                continue

            break

        except(ValueError):
            print("Error : Please Enter Just A Number.")

            continue

    if Operation == 1:
        Sum = NumberOne + NumberTwo

        print(f"Number One + Number Two = {Sum}")

    elif Operation == 2:
        Subtraction = NumberOne - NumberTwo

        print(f"Number One - Number Two = {Subtraction}")

    elif Operation == 3:
        Multiplication = NumberOne * NumberTwo

        print(f"Number One * Number Two = {Multiplication}")

    elif Operation == 4:
        try:
            Divide = NumberOne / NumberTwo

            print(f"Number One / Number Two = {Divide}")

        except(ZeroDivisionError):
            print("Error : Division To Zero.")

    Status = int()

    while True :
        print("1) New")
        print("2) Exit")

        try:
            Status = int(input("Please Enter Status's Number : "))

            if Status < 1 or Status > 2 :
                print("Error : Your Status Not Exist.")

                continue

            break

        except(ValueError):
            print("Error : Please Enter Just A Number.")

            continue

    if Status == 1 :
        continue
    
    elif Status == 2:
        print("Thank You For Select Us.")

        break
