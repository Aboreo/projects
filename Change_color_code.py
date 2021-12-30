
def error(messege):
    print(f"Error: {messege}")


def take_input(question):
    print(question)
    anwser = input('>>>')
    if anwser.find('exit') != -1:
        quit()
    return anwser


def contains(parmeter, string):

    index = string.find(parmeter)
    return index


def scan_messeage(message):
    cleared = True
    if len(message) < 7 or len(message) > 7:
        error("Input is too short or too long")
        cleared = False
    
    if contains('#', message) ==-1 :
        error("Hex code needs to inculde #")
        cleared = False

    for charater in ['A','B','C','D','E','F']:

        if contains(charater, message) != -1:
            error(f"{charater} must be in lowercase")
            cleared = False
    
    for noncharater in ['G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 
    '[', ']', ',', '.', '<', '>', '/', '?', ':', ';', "'", '"', '|', '-', '_', '=', '+', '`', '~', '!', '@', '$', '%', '^', '&', '*' , '(' ,')']:
        if contains(noncharater, message) != -1:
            error(f"{noncharater} is not a vaild digit")
            cleared = False     

    return cleared

def hexIndex(hexLetter):
    storage = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')
    return storage.index(hexLetter)

def HexToNumbers(hexletters):
    return hexMath(hexIndex(hexletters[0]),hexIndex(hexletters[1]))

def hexMath(a,b):
    anwser = (a*16)+b
    return anwser

def hexToRGB(hexademicl):

    hexademicl = hexademicl[1:]

    R = HexToNumbers(hexademicl[0:2])
    G = HexToNumbers(hexademicl[2:4])
    B = HexToNumbers(hexademicl[4]+hexademicl[5])

    return R,G,B





def rgbToHSV(R,G,B):
    r = float(R/255)
    g = float(G/255)
    b = float(B/255)

    colorMax,colorMin = max(r,g,b), min(r,g,b)
    colordiff = colorMax-colorMin

    # If Debugging needed later:
    # print(f'max,min,diff {colorMax, colorMin, colordiff}')

    # print(f"if r {(60*((g-b)/colordiff)+360)%360}, if g: {(60*((b-r)/colordiff)+120)%360}, if b: {(60*((r-g)/colordiff)+240)%360}")


    if colordiff == 0:
        h = 0
    
    elif colorMax == r:
        h = (60*((g-b)/colordiff)+360)%360

    elif colorMax == g:
        h = (60*((b-r)/colordiff)+120)%360
    
    elif colorMax == b:
        h = (60*((r-g)/colordiff)+240)%360
    
    h = round(h,0)

    if colorMax == 0:
        s = 0
    else:
        s = round(colordiff/colorMax *100,0)
    
    v = colorMax*100
    
    print(f'HSV {int(h),int(s),int(v)}')
    return hsvToCsb(h,s,v)

def hsvToCsb(h,s,v):
    c = (h/360) *100


    return int(c),int(s),int(v)






while True:
    done = False
    while not done:
        anwser = take_input('What is the hex?')
        
        done = scan_messeage(anwser)

    R,G,B = hexToRGB(anwser)
    print(f"RGB: {R,G,B}")

    Color, Satruation, Brightness = rgbToHSV(R,G,B)
    print(f'CSB: {Color,Satruation,Brightness}')




