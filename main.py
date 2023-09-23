import csv

def getIceCreamValues(fileName):
    tempDict = {} # temporary dictionary that we are storing values in and returning at the end of the function
    with open(fileName, newline='') as csvfile: #opening the csv file
        csvreader = csv.reader(csvfile) # gives a list of each row
        next(csvreader) # skips the header (name,price,description)
        for row in csvreader: # reads every row in the ice cream csv
            tempDict[row[0]] = [row[1], row[2]] # 0 = name, 1 = price, 2 = description
    return tempDict

def getToppingValues(fileName):
    tempDict = {}
    with open(fileName, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            tempDict[row[0]] = row[1]
    return tempDict

def getConeValues(fileName):
    tempDict = {}
    with open(fileName, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            tempDict[row[0]] = row[1]
    return tempDict

def getIceCreamSelection(values):
    tempCounter = 1
    maxLength = max(len(value) for value in values) # Ezekiel - Gives the value of the largest string in the keys
    for value in values:
        print(f"{tempCounter}: {value.ljust(maxLength)}  -  ${values[value][0]}  -  {values[value][1]}")
        tempCounter+=1
    while True:
        try:
            userInput = int(input("Enter the number of the Ice Cream you would like: "))
            if userInput < len(values) or userInput > 0:
                return list(values)[userInput-1]
            else:
                raise ValueError
        except:
            print("Please enter a valid input.")


def getToppingSelection(values):
    maxLength = max(len(value) for value in values)
    for value in values:
        print(f"{list(values).index(value)+1}: {value.ljust(maxLength)} - ${values[value]}")
    while True:
        try:
            userInput = int(input("Enter the number of the Topping you would like: "))
            if userInput < len(values) or userInput > 0:
                return list(values)[userInput-1]
            else:
                raise ValueError
        except:
            print("Please enter a valid input.")


def getConeSelection(values):
    maxLength = max(len(value) for value in values)
    for value in values:
        print(f"{list(values).index(value)+1}: {value.ljust(maxLength)} - ${values[value]}")
    while True:
        try:
            userInput = int(input("Enter the number of the Cone you would like: "))
            if userInput < len(values) or userInput > 0:
                return list(values)[userInput-1]
            else:
                raise ValueError
        except:
            print("Please enter a valid input.")


def main() -> None:
    icecreamValues = getIceCreamValues("icecreams.csv")
    toppingValues = getToppingValues("toppings.csv")
    coneValues = getConeValues("cones.csv")

    print("Welcome to Zeke 'n' Heather's Gelato Grotto!\n--------------------------------------------\n")
    print("--- Choose your Ice Cream ---")
    icecreamChoice = getIceCreamSelection(icecreamValues)
    print("\n--- Choose your Topping ---")
    toppingChoice = getToppingSelection(toppingValues)
    print("\n--- Choose your Cone ---")
    coneChoice = getConeSelection(coneValues)

    icecreamPrice = float(icecreamValues[icecreamChoice][0])
    toppingPrice = float(toppingValues[toppingChoice])
    conePrice = float(coneValues[coneChoice])

    total = icecreamPrice + toppingPrice + conePrice

    print(f"\nItems chosen:\n- Ice Cream: ${'{:.2f}'.format(icecreamPrice)} {icecreamChoice}\n- Topping: ${'{:.2f}'.format(toppingPrice)} {toppingChoice}\n- Cone: ${'{:.2f}'.format(conePrice)} {coneChoice}\nTotal: ${'{:.2f}'.format(total)}")
    

if __name__ == "__main__":
    main()
