def fatcorial(number):

    anwser = 1

    for i in range(1,number+1,1):
        anwser = anwser*i

    return anwser 

print(fatcorial(int(input("number: "))))


def FirstFactorial(num): 
    if num == 1:
      return 1
    else:
      return num * FirstFactorial(num-1)
 

 
print(FirstFactorial(int(input("fd "))))

