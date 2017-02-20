import random
from functools import reduce

print("Atk Speed e Duração do Engage Devem Ser Informadas em Segundos")

def weapon_damage(damage_min, damage_max, atk_speed, engage_duration):

    total_hits = engage_duration/atk_speed
    hit_arr = range(0, int(total_hits+1))
    hits_damage_storage = []

    for x in hit_arr:
        hit_damage = float(random.randint(damage_min, damage_max+1))
        hits_damage_storage.append(hit_damage)

    damage_per_second = reduce((lambda a, b: a + b), hits_damage_storage)
    print("Total damage:",damage_per_second)
    print("DPS:", damage_per_second/engage_duration)

player_min_input = int(input("Digite o Dano Mínimo de Sua Arma"))
player_max_input = int(input("Digite o Dano Máximo de Sua Arma"))
player_atk_speed_input = float(input("Digite a AtkSpeed de Sua Arma"))
player_engage_duration_input = float(input("Digite a Duração da Luta"))
weapon_damage(player_min_input, player_max_input, player_atk_speed_input, player_engage_duration_input)