

# Loops
def main():
    
    # For___________________________________________________________________________

    def rangeLoop(number):
        for num in range(number):
            print(num)
            
    # rangeLoop(4)
            
    def listForLoop(listGiven):
        for item in listGiven:
            print(item)
    
    studentNames = ["Daniel", "Jayden", "Ashley", "Cecelia", "Jordan", "Aidan"]
    # listForLoop(studentNames)

    studentIdNumbers = [25972365, 21379835, 56402378, 7623953, 27356353]
    # listForLoop(studentIdNumbers)
    
    def continueInLoop(listGiven):
        for item in listGiven:
            if item == "Jayden" or item == "Cecelia":
                continue
            else:
                print(item)

    # continueInLoop(studentNames)

    def breakInLoop(listGiven):
        for item in listGiven:
            if item == "Ashley":
                break
            else:
                print(item)
    
    # breakInLoop(studentNames)

    # While___________________________________________________________________________
    def whileIntLoop(var):
        while var <= 5:
            print(var)
            var += 1
    
    # whileIntLoop(2)

    # whileIntLoop(10)
    
    def whileContLoop(num):
        while num < 5:
            num += 1
            if num == 3:
                continue
            else:
                print(num)
    
    # whileContLoop(0)

if __name__ == "__main__":
    main()