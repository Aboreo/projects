from random import randint

def ask(question,defult):
    print(question)
    anwser = input('>>>')
    if anwser == '':
        anwser = defult
    elif anwser == 'exit':
        quit()
    return anwser

def alphabet():
    global numbers,lowercaseLetters,specialCharaters

    generlCharaters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    lowercasecharaters = 'qwertyuiopasdfghjklzxcvbm'
    numberCharaters = '1234567890'
    specialCharatersString = '!@#$%^&*()-_{}[]'

    if numbers:
        generlCharaters = generlCharaters + numberCharaters
    if specialCharaters:
        generlCharaters = generlCharaters + specialCharatersString
    if lowercaseLetters:
        generlCharaters= generlCharaters + lowercasecharaters
    return list(generlCharaters)        

length = int(ask("How long do you want the password to be?",'12'))
numbers = ask("Do you want to inculde numbers in the password? Y|N ",'y').lower() == 'y'
lowercaseLetters = ask("Do you want to inculde lowercase letters in the password? Y|N ",'y').lower() == 'y'
specialCharaters = ask("Do you want to inculde special charaters in the password? Y|N ",'y').lower() == 'y'

lettersAllowed = alphabet()
badPassword = True

while badPassword:
    password = ''
    for i in range(length):
        password = password + lettersAllowed[randint(0,len(lettersAllowed)-1)]

    print('Your password is:')
    print(password)
    badPassword = ask("Are you content with the password? Y|N ",'n').lower() == 'n'