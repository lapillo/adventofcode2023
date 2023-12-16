import math


strength_of_cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
results = {"Five": [], "Four": [], "Full":[], "Three":[], "TwoPair":[], "OnePair":[], "High":[]}
cards=[]       



if __name__ == '__main__':
    result = 0
    file = open("adventofcode2023/zadanie_07/input.txt","r")
    list = file.read().split("\n")


    #for item in list:
    cards.extend([(y if x==0 else int(y)) for x,y in enumerate(item.split())] for item in list)
   
    order = dict(zip(strength_of_cards, range(len(strength_of_cards))))
    
    for card in cards:
        number_of_sim_card = [[] for x in range(10)]
        print("card: ", card)

        for strength in strength_of_cards:
            if card[0].count(strength) > 0:           
                number_of_sim_card[card[0].count(strength)].append(strength*card[0].count(strength))          
        
        for i,c in enumerate(number_of_sim_card):
            number_of_sim_card[i] = sorted(c, key=lambda word: [order[c] for c in word])
        print(number_of_sim_card)


        card_sorted=""   
        card[0]=""
        for i in reversed(range(5)):
            card[0] += ''.join(number_of_sim_card[i+1])   
        print("card 0: ",card[0])
        
        print(number_of_sim_card)
        
        if len(number_of_sim_card[5])==1:
            results["Five"].append(card)
        elif len(number_of_sim_card[4])==1:
            results["Four"].append(card)
        elif len(number_of_sim_card[3])==1 and len(number_of_sim_card[2])==1:
            results["Full"].append(card)
        elif len(number_of_sim_card[3])==1:
            results["Three"].append(card)
        elif len(number_of_sim_card[2])==2:
            results["TwoPair"].append(card)
        elif len(number_of_sim_card[2])==1:
            results["OnePair"].append(card) 
        else:
            results["High"].append(card) 
        print(number_of_sim_card)
        
    
    #sort
        
    
    result = 0
    to_win = len(cards)
    
    
    print("result ")
    for type in results:
        results[type] = sorted(results[type], key=lambda word: [order[c] for c in word[0]])
        print (type, " ",results[type])
        for w in results[type]:
            result += to_win*w[1]
            to_win-=1
    print(result)



         