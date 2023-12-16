strength_of_cards       = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cards=[]     


def search_cards_for_key(cards, pattern):
    card_data = [""]*len(cards)
    cards_copy = [x[0] for x in cards]
    
    for key in pattern:
        for i,card in enumerate(cards_copy):
            for strength in strength_of_cards:
                if card.count(strength) == key:
                    cards_copy[i]=cards_copy[i].replace(strength,'')
                    card_data[i]+= strength*key
                    break

    win_cards_data=[]
    for i,card in enumerate(cards):
        if len(card_data[i]) == 5:# len(pattern):
            data = [card_data[i], cards[i][1],cards[i][0]]
            win_cards_data.append(data)
    return (win_cards_data)
                       
        
if __name__ == '__main__':
    
    file = open("adventofcode2023/zadanie_07/input.txt","r")
    list = file.read().split("\n")

    #for item in list:
    cards.extend([(y if x==0 else int(y)) for x,y in enumerate(item.split())] for item in list)

    
    
    patterns = [[5],[4,1],[3,2],[3,1,1],[2,2,1],[2,1,1,1],[1,1,1,1,1]]
    #patterns = [[1,1,1,1,1]]
    
    winners=[]
    for pattern in patterns:
        win_cards_data = search_cards_for_key(cards,pattern)
        winners.append(win_cards_data)
    
    
    order = dict(zip(strength_of_cards, range(len(strength_of_cards))))
    for i,winner in enumerate(winners):
        winners[i] = sorted(winner, key=lambda word: [order[c] for c in word[0]])
        print(i,winner)



    to_win = len(cards)
    result = 0
    count=0
    for winner in winners:  
        for w in winner:
            result += to_win*w[1]
            to_win-=1
            count+=1
    print(result)
    print(count)
        