from typing import AnyStr


def ask(question, defult):

    anwser = "agian"
    
    while anwser == "agian":
        print(question)
        anwser = input(">>>")

        if anwser == "":
            anwser = defult
    
    return anwser.lower()



def aquire():
    global athrmitc, fkterm, rate, kterm, recursive, explict
    athrmitc = ask("Is the sequance arthmatic? Y|N", "y").find("y") != -1

    kterm = int(ask("What term do you know?", "again"))
    fkterm = int(ask(f"What is term {kterm} of the sequence", "agian"))

    if athrmitc:
        rate = ask("Comman differnece", "agian")
        recursive = f"\nf({kterm})={fkterm};f(n) = f(n-1)+{rate}"
        explict = f"\nf(n)= {fkterm} + {rate}(n-{kterm})"
    else:
        rate = ask("Comman ratio", "agian")
        recursive = f"\nf({kterm})={fkterm};f(n) = f(n-1)*{rate}"
        explict = f"\nf(n)= {fkterm} * {rate}^(n-{kterm})"
    
    rate = int(rate)
    
    

def f(n):
    if n == kterm:
        return fkterm
    else:
        if athrmitc:
            return f(n-1) + rate
        else:
            return f(n-1) * rate




aquire()
print(f(int(ask("What term do you want to find?", "agian"))))

print(f"\nRecursive function is:{recursive}")
print(f"\nExplict equation: {explict}\n")