import pickle   

def ask(question, defult):
    print(question)  
    anwser = input(">>>")
    if anwser == '':
        anwser = defult
    elif anwser == 'exit':
        file = open('D:\\Aryan\\Coding\\Python\\projects\\Adresses\\address_data.txt','wb')
        pickle.dump(all_address,file)
        file.close()
        quit()

    return anwser.lower()


def setup():
    global all_address,indexOfadress
    file = open('D:\\Aryan\\Coding\\Python\\projects\\Adresses\\address_data.txt','rb')
    try:  #tries to open the data fomr the database if failed or file is not there, it will delete the file and/or make the file and store an empty list in it.
        data = pickle.load(file)
    except:
        file.close()
        reset()
        file = open('D:\\Aryan\\Coding\\Python\\projects\\Adresses\\address_data.txt','rb')
        data = pickle.load(file)

    all_address = list(data)
    file.close()
    #setting up the names of all the people
    indexOfadress = []
    for address in all_address: indexOfadress.append(address.name)

def reset():
    file = open('D:\\Aryan\\Coding\\Python\\projects\\Adresses\\address_data.txt', 'wb')
    reset = []
    pickle.dump(reset, file)
    file.close()

class Adresses():
    def __init__(self,name, location, number, relation) -> None:
        self.name = name.capitalize()
        self.location = location.capitalize()
        self.number = number.capitalize()
        self.relation = relation.capitalize()

    def show(self):
        print(f"Name: {self.name} \nHouse: {self.location} \nPhone Number: {self.number} \Relation: {self.relation}")
    



setup()

while True:
    anwser = ask("What do you want to do? Options: 'new', 'find', 'clear', 'del', 'exit'", 'new')

    if anwser == 'new':

        name = ask("What is the name of the person",'N/A')
        all_address.append(Adresses(name,ask(f"Where does {name} live?",'N/A'),ask(f"What is the phone number of {name}",'N/A'),ask(f"What is your relationship with {name.capitalize()}?",'N/A',False)))
        indexOfadress.append(all_address[len(all_address)-1].name)

    elif anwser.find('find') != -1:
        whichPerson = ask(f"Who would you like to find? The list of people is below: \n{indexOfadress}", 'none').capitalize()

        try:
            whichPerson = indexOfadress.index(whichPerson)
            all_address[int(whichPerson)].show()

        except:
            print(f"Not vaild option or user not registered")

    elif anwser == 'del':
        personsName = ask(f"Who would you like to remove? The list of people is below: \n{indexOfadress}", 'none').capitalize()

        try: 
            whichPerson = indexOfadress.index(personsName)
            
            if ask("Are you sure? Y or N", 'n')[0] == 'y':
                del(all_address[whichPerson])
                del(indexOfadress[whichPerson])
                print(f"{personsName} has been deleted.")
            else:
                print(f"{personsName} was not deleted.")
     
        except:
            print("Not vaild option")
    
    elif anwser == 'reset':
        all_address.clear()
        indexOfadress.clear()

    elif anwser == 'debug':
        print(all_address)
        print(indexOfadress)

    elif anwser == 'debug.clear':

        reset()
        all_address.clear()
        indexOfadress.clear()

        print("Done")