
# Online Python - IDE, Editor, Compiler, Interpreter
bag = {"red":12,"green":13,"blue":14}


def get_game_number(game):
    game_number = game.split(":")[0].split(" ")[1]
    return game_number
# end def

def validate_game_is_possible(bag, game):
    game_number = int(get_game_number(game))
    
    game_data = game.split(":")[1].split(";")
    print("")
    print(game_data)
    for draw in game_data:
        draw = draw.split(",")
        print(draw)
        cubes = {"red":0,"green":0,"blue":0}
        for color in draw:
            cube_count_color = color.strip().split(" ")
            if cube_count_color[1] not in cubes.keys():
                cubes[cube_count_color[1]]=0
            cubes[cube_count_color[1]] = cubes[cube_count_color[1]] + int(cube_count_color[0])
        print(cubes)
        if cubes["red"] > bag["red"] or cubes["green"] > bag["green"] or cubes["blue"] > bag["blue"]:
            print("fail!")
            return 0
    print("success all!")
    return game_number
    
    
def miltiple_min_for_game(game):
    game_data = game.split(":")[1].split(";")
    print("")
    print(game_data)
    cubes = {}
    for draw in game_data:
        draw_cubes={}
        draw = draw.split(",")
        #print(draw)
        for color in draw:
            cube_count_color = color.strip().split(" ")
            if cube_count_color[1] not in draw_cubes.keys():
                draw_cubes[cube_count_color[1]]=0
            draw_cubes[cube_count_color[1]] = draw_cubes[cube_count_color[1]] + int(cube_count_color[0])
        #print(draw_cubes)
        for color in draw_cubes:
            if color not in cubes.keys():
                cubes[color]=[]
            cubes[color].append(draw_cubes[color])
    print(cubes)
    result = 0
    for color in cubes:
        if result == 0:
            result = max(cubes[color])
        else:
            result = result *  max(cubes[color])
    return result

# end def

if __name__ == '__main__':
    result = 0
    with open("/config/workspace/adventofcode/zadanie_02/input.txt") as file:
        for game in file:
            game = game.strip()
            #result = result + validate_game_is_possible(bag, game)
            result = result + miltiple_min_for_game(game)
            
    print(result) 