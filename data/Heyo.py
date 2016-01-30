def mainsi():
    user=input("Would you like a list or a specific person? List or Specific? ")
    if user=='List':
        filen=open('dataside','r')
        line=filen.readline().rstrip()
        while line!="":
            print(line, end="\n")
            line=filen.readline().rstrip()
    elif user=='Specific':
        speci()
    else:
        print("Please enter 'List' or 'Specific'.")
        mainsi()
def speci():
    user1=input("What class are you having trouble in? Please enter the CRN number: ")
    if user1=='1170':
        filen=open('1170tutors','r')
        line=filen.readline().rstrip()
        while line!="":
            print(line, end="\n")
            line=filen.readline().rstrip()
    elif user1=='2170':
        filen=open('2170tutors','r')
        line=filen.readline().rstrip()
        while line!="":
            print(line, end="\n")
            line=filen.readline().rstrip()
    elif user1=='3130':
        filen=open('3130tutors','r')
        line=filen.readline().rstrip()
        while line!="":
            print(line, end="\n")
            line=filen.readline().rstrip()
    elif user1=='3222':
        filen=open('3222tutors', 'r')
        line=filen.readline().rstrip()
        while line!="":
            print(line, end="\n")
            line=filen.readline().rstrip()
    elif user1=='3250':
        filen=open('3250tutors','r')
        line=filen.readline().rstrip()
        while line!="":
            print(line, end="\n")
            line=filen.readline().rstrip()
    elif user1=='4410':
        filen=open('4410tutors','r')
        line=filen.readline().rstrip()
        while line!="":
            print(line, end="\n")
            line=filen.readline().rstrip()
    elif user1=='4700':
        filen=open('4700tutors','r')
        line=filen.readline().rstrip()
        while line!="":
            print(line, end="\n")
            line=filen.readline().rstrip()
    else:
        print("Could not find the CRN you inputed. Please try again.")
        speci()
mainsi()