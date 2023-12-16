import math

if __name__ == '__main__':
    result = 0
    file = open("adventofcode2023/zadanie_06/input.txt","r")
    list = file.read().split("\n")
    times = []
    distances = []
    
    
    
    list[0].replace(" ","")
    list[1].replace(" ","")
    
    print (list[0])
    times = [int(x) for x in list[0].replace(" ","").split(":")[1:]]
    distances = [int(x) for x in list[1].replace(" ","").split(":")[1:]]
    
    win = 0
    
    
    for race in range(len(times)):
        race_win=0
        print()
        print ("race ", race)
        step=2
        mid = math.ceil(times[race]/2)
        dist = mid*(times[race]-mid)
        while dist > distances[race]:
            dist-=step
            step+=2
            race_win+=1
        race_win*=2
        if times[race] % 2 == 0 and race_win > 0:
            race_win-=1    
        win = race_win if win==0 else win * race_win

        
    print()
    print("result: ", win)
            
                   
          
    
    
    
    

         