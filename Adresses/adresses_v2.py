import pickle   

class Adresses():
    def __init__(self,name, location, number, note) -> None:
        self.name = name.capitalize()
        self.location = location.capitalize()
        self.number = number.capitalize()
        self.note = note

    def show(self):
        print(f"Name: {self.name} \nHouse: {self.location} \nPhone Number: {self.number} \nnote: {self.note}\n")
    
    def deleate(self):
        index = indexOfadress.index(self.name)
        del(indexOfadress[index])
        del(all_address[index])
    
    def edit(self,ifname=False,iflocation=False,ifnumber=False,ifnote=False):

        if ifname:
            currentName = self.name
            self.name = ask(f"What is the new name for {self.name}?",self.name)
            indexOfadress[indexOfadress.index(currentName)] = self.name.capitalize()
        
        if iflocation:
            self.location = ask(f"What is the new location for {self.name}?",self.location)
        
        if ifnumber:
            self.number = ask(f"What is the new number for {self.name}?",self.number)
        
        if ifnote:
            self.note = ask(f"What is the new note for {self.name}?",self.note,False)
    
def ask(question, defult, iflower=True):
    print(question)  
    anwser = input(">>>")

    if anwser == '':
        anwser = defult

    elif anwser == 'exit':
        file = open(FILENAME,'wb')
        pickle.dump(all_address,file)
        file.close()
        quit()

    if iflower:
        return anwser.lower()
    else:
        return anwser

def setup():
    global all_address,indexOfadress
    file = open(FILENAME,'rb')

    try:  #tries to open the data fomr the database if failed or file is not there, it will delete the file and/or make the file and store an empty list in it.
        data = pickle.load(file)
    except:
        file.close()
        reset()
        file = open(FILENAME,'rb')
        data = pickle.load(file)

    all_address = list(data)
    file.close()

    #setting up the names of all the people
    indexOfadress = []
    for address in all_address:
        indexOfadress.append(address.name.capitalize())

def reset():
    file = open(FILENAME, 'wb')
    reset = []
    pickle.dump(reset, file)
    file.close()

def finding(spefication,list):
    retrunValue = -1
    
    for item in list:
        if item == spefication:
            retrunValue += 1

    return retrunValue  

FILENAME = 'D:\\Aryan\\Coding\\Python\\projects\\Adresses\\address_data_V2.txt'
setup()

while True:
    anwser = ask(f"What do you want to do? Options: 'new', 'clear', 'exit', \nor you can type a name from this list: {indexOfadress}", 'new')

    if anwser == 'new':
        name = ask("What is the name of the person",'N/A').capitalize()

        all_address.append(Adresses(name,ask(f"Where does {name} live?",'N/A'),ask(f"What is the phone number of {name}",'N/A'),ask(f"What is a note for {name}?",'N/A',False)))
        indexOfadress.append(all_address[len(all_address)-1].name)
    
    elif anwser == 'clear':
        if ask("Are you sure? Y|N",'n')[0] == 'y':
            all_address.clear()
            indexOfadress.clear()

            print("Done")
        else:
            print("Canceled")

    elif anwser == 'debug':
        print(all_address)
        print(indexOfadress)

    elif anwser == 'debug.clear':
        reset()
        all_address.clear()
        indexOfadress.clear()

        print(f"Done")
    
    elif anwser == 'debug.save':
        debugSaveList = []

        for person in all_address:
            person_metadata = f"Name: {person.name}, Location: {person.location}, Phone Number: {person.number}, Note: {person.note}"
            debugSaveList.append(person_metadata)

        print(f"\n{debugSaveList}\n")

    elif finding(anwser.capitalize(),indexOfadress) != -1:
        action = ask(f"What do you want to do with {anwser.capitalize()}? Options: 'details', 'del', 'edit'",'detils')
        index = indexOfadress.index(anwser.capitalize())

        if action == 'details':
            all_address[index].show()
            
        elif action == 'del':
            all_address[index].deleate()

        elif action == 'edit':
            whatToedit = ask(f"What do you want to edit? Options: 'name', 'location', 'Phone number', 'note' ",'note')
            all_address[index].edit(whatToedit.find("name")!=-1, whatToedit.find("location")!=-1, whatToedit.find("phone number")!=-1, whatToedit.find("note")!=-1)