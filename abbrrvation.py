
def ask(question,defualt):
    print(question)
    anwser = input('>>>')
    if anwser == '':
        anwser = defualt
    if anwser == 'exit':
        quit()
    return anwser

def abbrivete(phrase):

    listOfWords = phrase.split()

    for word in listOfWords:
        listOfWords[listOfWords.index(word)] = word[0].upper()
    return listOfWords

while True:
    words = ask('What do you want to abbreviate?','exit')
    abbrevation = abbrivete(words)
    print(*abbrevation,sep='')

