import math


strength_of_cards       = {"A":0, "K":1, "Q":2, "J":3, "T":4, "9":5, "8":6, "7":7, "6":8, "5":9, "4":10, "3":11, "2":12}
patterns = [[5],[4,1],[3,2],[3,1,1],[2,2,1],[2,1,1,1],[1,1,1,1,1]]

cards=[]     
winners=[]

def search_cards_for_key(cards):

    winners=[]
    cards_to_skip = [] 
   
    max_size = 0
    for pattern in patterns:
        card_data = [""]*len(cards)
        card_found_keys = [0]*len(cards)
        cards_copy = [x[0] for x in cards]
        for key in pattern:
            max_size+=key
            for strength in strength_of_cards:
                for i,card in enumerate(cards_copy):
                    if card.count(strength) == key and card_found_keys[i] < len(pattern) and i not in cards_to_skip:
                        cards_copy[i]=cards_copy[i].replace(strength,"",key)
                        card_data[i]+= strength*key###
                        card_found_keys[i]+=1
        win_cards_data=[]
        for i,card in enumerate(cards):
            if len(card_data[i]) == 5:# len(pattern):
                data = [card_data[i], cards[i][1],cards[i][0]]
                win_cards_data.append(data)
                cards_to_skip.append(i)
        winners.append(win_cards_data)
    return (winners)

        
def sort_cards(str):
    print(str)

if __name__ == '__main__':
    
    file = open("adventofcode2023/zadanie_07/input.txt","r")
    list = file.read().split("\n")

    #for item in list:
    cards.extend([(y if x==0 else int(y)) for x,y in enumerate(item.split())] for item in list)

    winners=search_cards_for_key(cards)
    
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


    
    

    
        
 
    
    # for winner in winners:
    #     for w in winner:
    #         for i in range(len(w[0])):
    #             index = strength_of_cards.index(w[0][i])
    #             w[0]=w[0][:i]+strength_of_cards_alpha[index]+w[0][i+1:]  
    #     #print(winner)
    #     winner.sort()
    #     #print(winner) 
    
     
                
                
                
                
    # for winner in winners:
    #     for w in winner:
    #         for i in range(len(w[0])):
    #             index = strength_of_cards_alpha.index(w[0][i])
    #             w[0]=w[0][:i]+strength_of_cards[index]+w[0][i+1:]  
    #     #print(winner)


    
    
    #walidate input
    
    # x=0
    # for winner in winners:  
    #     for w in winner:
    #         for card in cards:
    #             if card[0] == w[2]:
    #                 x+=1
    #             if card[1] == w[1]:
    #                 x+=1
    #             if 
    # print(x)
        