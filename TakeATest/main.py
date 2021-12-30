import pickle, os
def ask(question,defult):
    if question != "": print(question)
    anwser = "agian"
    while anwser == "agian":
        anwser = input(">>>")

        if (anwser == ""):
            anwser = defult
            if anwser == "agian":
                print("Can't be empty, please try agian.")
    
    return anwser.lower()

def load():
    global testNames
    name = "TestNames.txt"
    with open(name,"rb") as file:
        testNames = pickle.load(file)

def save():
    name = "TestNames.txt"
    with open(name,"wb") as file:
        pickle.dump(testNames,file)


def testfunctions(mode="add"):

    if mode == "add": questionName = "What is the name for the test?"
    elif mode == "find": questionName = f"What is the name of the test?\nThese are the options {testNames}"
    elif mode == "del": questionName = f"Please pick a test to delate from the list below:\n{testNames}"

    while True:
        requstedname = ask(questionName, None)
        if requstedname in testNames or requstedname == None:
            if mode == "add":
                print("Has to be a name not used.")
            elif (mode == "find" or mode == "del") and requstedname != None:
                return requstedname
        else:
            if mode == "add":
                testNames.append(requstedname)
                return requstedname
            elif mode == "find" or mode == "del":
                print(f"{requstedname} is not a test yet")
    
        

class test():
    def __init__(self,name) -> None:
        self.test = []
        self.name = name

    def add(self,question,anwsers):
        self.test.append([question,anwsers])

    def save(self):
        filename = f"D:\\Aryan\\Coding\\Python\\projects\\Test\\SaveFolder\\{self.name}.txt"
        with open(filename,"wb") as txtfile: 
            pickle.dump(workingOnTest,txtfile)


load()

option = ask(f"New test or existing or do you want to delate one?\nNew|test|del", "new")
if (option == "new"):
    workingOnTest = test(testfunctions())

    for i in range(1,int(ask("How many questions do you want? (defult is 3).","3"))+1):
        question = ask(f"What is the {i} question?","agian")
        anwsers = []
        for i in range(int(ask("How many differnt anwsers do you have?","1"))):
            anwsers.append(ask("What is this anwser?", "agian"))
    
        workingOnTest.add(question,anwsers)
    workingOnTest.save()
    print("Done!")
    save()

elif option == "test":
    whichTest = testfunctions("find")

    with open(f"D:\\Aryan\\Coding\\Python\\projects\\Test\\SaveFolder\\{whichTest}.txt","rb") as file:
        fullTest = pickle.load(file)

    i = 1
    correct = 0
    for question in fullTest.test:
        print(f"Question {i}:")
        print(question[0])
        anwser = ask("",":N:O:N:E:")

        if anwser in question[1]:
            print(f"Correct! :)")
            correct += 1
        elif anwser == ":N:O:N:E:":
            print("Sorry, guessing won't count correct.")
        else:
            print(f"Wrong :(")
        i += 1
    
    print(f"\nYour final score was: {correct}/{i-1}\n")

elif option == "del":
    testToDel = testfunctions("del")
    if ask("Are you sure?", "n").find("y") != -1:
        os.remove(f"D:\\Aryan\\Coding\\Python\\projects\\Test\\SaveFolder\\{testToDel}.txt")
        testNames.remove(testToDel)
        save()
    else:
        print("Ok!")

else:
    print("Ok bye!")
        


    


print("Thank you!")
