import math

if __name__ == '__main__':
    result = 0
    file = open("adventofcode2023/zadanie_06/input_example.txt","r")
    list = file.read().split("\n")
    times = []
    distances = []
    
    
    
    times = [int(x) for x in list[0].split()[1:]]
    distances = [int(x) for x in list[1].split()[1:]]
    
    win = 0
    for race in range(len(times)):
        race_win=0
        print()
        print ("race ", race)
        for x in range((math.ceil(times[race]/2)),times[race]): 
            if (x*(times[race]-x) > distances[race]):
                #print ("win: ", x)  
                race_win+=1
            else:
                break
        race_win*=2
        if times[race] % 2 == 0 and race_win > 0:
            race_win-=1
        print ("race win: ", race_win)
        
        if win==0: 
            win=race_win
        else:
            win*=race_win
    print()
    print("result: ", win)
            
                   
          
    
    
    
    

         