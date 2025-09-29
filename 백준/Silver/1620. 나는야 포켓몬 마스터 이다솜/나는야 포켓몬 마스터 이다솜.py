import sys

# 도감에 수록된 포켓몬 개수 N, 내가 맞춰야 하는 문제 개수 M
N, M = map(int, sys.stdin.readline().split())

# 입력받은 내용을 바탕으로, 포켓몬 도감 list 생성
pokedex = [sys.stdin.readline().strip() for _ in range(N)]

# 포켓몬 도감 list를 바탕으로, 포켓몬 도감 dictionay 생성
pokemon_dict = {i+1: pokemon for i, pokemon in enumerate(pokedex)}
reverse_pokemon_dict = {value: key for key, value in pokemon_dict.items()}

# 찾아야 하는 포켓몬 번호 or 이름 입력
pokemon_list = [sys.stdin.readline().strip() for _ in range(M)]

for pokemon in pokemon_list:
    if pokemon.isdigit():
        print(pokemon_dict[int(pokemon)])
    else:
        print(reverse_pokemon_dict[pokemon])
