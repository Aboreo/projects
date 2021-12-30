
def value(n):
    if n == "0":
        if total > 88:
            return 1
        else:
            return 11
    elif n == "4":
        return -10
    elif n == "9":
        return 0
    else:
        return int(n)


data = input("").split(",")

total = int(data[0])

player = data[1:4]

dealer = data[4:]



while True:
    total += value(player[0])
    player.append(dealer[0])
    del dealer[0]
    del player[0]
    if total > 99:
        print(f"{total}, Dealer")
        break
    
    total += value(dealer[0])
    del dealer[0]
    if total > 99:
        print(f"{total}, Player")
        break
