import pyautogui

k = input("all pokemon cards (code) wanted searched? sep by comma >> ").split(',')

n = len(k)

pyautogui.hotkey('alt','tab')


for i in range(n):

    j = k[i].split('/')
    pyautogui.hotkey('ctrl','t')
    pyautogui.hotkey('ctrl','e')

    pyautogui.write(f'pokemon {j[0]}/{j[1]} worth')
    pyautogui.hotkey('enter')

pyautogui.hotkey('ctrl','2') 
    
    

    



