
def modify_elements(pokemon_list, index, value):
    for i in range(len(pokemon_list)):
        curr_pokemon = pokemon_list[i]
        if index < 0:
            pokemon_list[0] = pokemon_list[-1]
            curr_pokemon += value
            pokemon_list[i] = curr_pokemon
        elif index >= len(pokemon_list):
            pokemon_list[-1] = pokemon_list[0]
            curr_pokemon += value
            pokemon_list[i] = curr_pokemon

        else:
            if curr_pokemon <= value:
                curr_pokemon += value
                pokemon_list[i] = curr_pokemon
            else:
                curr_pokemon -= value
                pokemon_list[i] = curr_pokemon
    return pokemon_list

# def bigger_index(poke_list, index, value):




pokemons = list(map(int, input().split()))
command = int(input())
score = 0
while True:
    if command >= len(pokemons):
        pokemons = modify_elements(pokemons, command, pokemons[-1])
        command = int(input())
        continue
    elif command < 0:
        pokemons = modify_elements(pokemons, command, pokemons[0])
        command = int(input())
        continue
    else:
        value_of_pokemon = pokemons.pop(command)
    if pokemons:
        pokemons = modify_elements(pokemons, command, value_of_pokemon)
    else:
        score += value_of_pokemon
        break
    score += value_of_pokemon
    command = int(input())

print(score)