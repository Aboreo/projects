
def ask(question,defualt):
    print(question)
    anwser = input('>>>')
    if anwser == '':
        anwser = defualt
    if anwser == 'exit':
        quit()
    return anwser


def paildrome(word):
    word = list(word)

    reverseCopy = word.copy()
    reverseCopy.reverse()

    fact = word == reverseCopy


    return fact

    



while True:
    anwser = ask('What is the word?','exit')

    fact = paildrome(anwser.lower())

    if fact:
        print("The word is a paildrome!")
    else:
        print("The word is not a paildrome")
    