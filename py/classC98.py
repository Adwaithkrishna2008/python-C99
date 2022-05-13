def CountWordFromFile():
    fileName=input("Enter the file name")
    NoOfWords=0
    file=open(fileName,'r')
    for line in file:
        words=line.split(",")
        print(len(words))
        NoOfWords=NoOfWords+len(words)
    print("No of words",NoOfWords)


CountWordFromFile()