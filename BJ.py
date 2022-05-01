import random
def bet():
    x = 0
    while x<5 or x>player[1]:
        try:
            x = int(input(f'You have {player[1]} coins. How much money do you bet? '))
            if x>player[1]:
                x=int(input(f'How much money do you bet? You only have {player[1]} coin(s) left. '))
            elif x<5:
                x = int(input(f'How much money do you bet? You must bet at least 5 coins. '))
        except:
            print(f'Your bet must be a postive interger')
            x = 0

    return x

def value(card,val=0):
    if ['0','K','J','Q'].count(card) != 0:
        return 10
    elif card == 'A':
        if  val> 10:
            return 1
        else:
            return 11
    else:
        return int(card)

def handval(hand):
    val = 0
    a = 0
    for i in hand:
        if i[1] == 'A':
            a+=1
        else:
            val += value(i[1])
    for i in range(a):
        val += value('A',val)
    return val

def lose(reason):
    player[1] = player[1]-player[3]
    print(f'\nYou lost becasue {reason}! You lost {player[3]} coins. ')
    gameover()

def win(reason):
    player[1] = player[1]+(2*player[3])
    print(f'\nYou won because {reason} You earned {player[3]*2} coins. ')
    player[2] += 1
    gameover()

def draw(reason):
    print(f"\nYou drawed because {reason} Don't worry you will keep your money! ")
    gameover()


def gameover():
    global done,deck, discard
    print(f"This was the dealers hand {dealer[0]}({dealer[1]}) and this was your hand {player[0]}({player[4]})")
    discard += player[0]
    discard += dealer[0]
    if len(discard) >=40:
        deck += discard
        print("The discard cards are being added to the deck")
        discard = []
    player[0],dealer[0] = [], []
    player[4], dealer[1] = 0, 0
    player[5] += 1
    try:
        x = input('\nDo you still want to play? ').lower()[0]
        if x[0] == 'n':
            done = False
        elif x[0] == 'y':
            print('YAY!')
        else:
           print("Let's assume you do!") 
    except:
        print("Let's assume you do!")
    

#player = cards, money left, how many wins, bet placed, value of cards, how many games played
player = [[],1000,0,0,0,0]

dealer= [[],0]

done = True
discard = []
deck = ['DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D0', 'DJ', 'DQ', 'DK', 
        'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H0', 'HJ', 'HQ', 'HK', 
        'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S0', 'SJ', 'SQ', 'SK', 
        'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C0', 'CJ', 'CQ', 'CK']

while player[1]>4 and done:
    

    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)



    print(f'\n\n')

    for i in range(2):
        dealer[0].append(deck.pop(0))
        player[0].append(deck.pop(0))

    player[4] = handval(player[0])
    dealer[1] = handval(dealer[0])
    player[3] = bet()
    pmove = ''

    if dealer[1] ==21:
        lose('the dealer got a blackjack')
        continue
    elif player[4] == 21:
        win('you were dealt a blackjack')
        continue
    elif player[4] == 21 and dealer[1] == 21:
        draw('you and the dealer got a blackjack')
        continue


    while player[4] < 21 and pmove != 's':
        print(f'\nThese are your cards {player[0]} value is {player[4]}.\nThis is the dealers first card, {dealer[0][0]} value is {value(dealer[0][0][1])}')
        try:
            pmove = input('Make your move. Do you want to HIT or STAND. ')[0].lower()
        except:
            pmove = 'bruh do better'
        if pmove == 'h':
            player[0].append(deck.pop(0))
        player[4] = handval(player[0])



    if player[4] > 21:
        lose(f'you busted')
        continue
    else:
        while dealer[1] < 17:
            dealer[0].append(deck.pop())
            dealer[1] = handval(dealer[0])

    if player[4] == dealer[1]:
        draw('you both had the same value')  
    elif dealer[1] == 21:
        lose(f'the dealer got to 21')
        continue
    elif player[4] == 21:
        win(f'you got to 21')
        continue
    elif dealer[1] > 21:
        win('the dealer busted')
    elif dealer[1] > player[4]:
        lose('the dealer got a higher value than you')
    elif player[4] > dealer[1]:
        win('your cards are a higher value than the dealers.')

if player[1] < 5:
    print('Ah shucks you ran out of all your money')
print(f'Hope you play again soon! You ended with {player[2]} wins out of {player[5]} games and {player[1]} coins.\n\n')
