import random
def sort(arry):
    
    testingInt = 0
    while True:
        done = True
        for number in range(len(arry)-1):
            testingInt = number
            if arry[testingInt] > arry[testingInt+1]:
                arry.insert(testingInt+2,arry[testingInt])
                del(arry[testingInt])
                done = False
           # testingInt += 1
        if done:
            break    
    return arry    


tst = [1,3,4,2,6,5]

random.shuffle(tst)

print(tst)

print(f"\n{sort(tst)}")




# def insertSort(arry):
#     testingInt = 0
    
#     while True:
#         done = True

#         for number in range(len(arry)-1):
#             #none
#             test = True
#             tester = number-1
#             while test:
#                 if arry[number] < arry[tester]:

#                     arry.insert(testingInt+2,arry[number])
#                     del(arry[testingInt])
#                 done = False

#         if done:
#             break    
#     return arry    