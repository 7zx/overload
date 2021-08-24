import json
import random


# Procura um IP aleatório
def random_IP():
    ip = []
    for _ in range(0, 4):
        ip.append(str(random.randint(1, 255)))
    return ".".join(ip)


# Procura uma referência aleatória
def random_referer():
    with open("tools/L7/referers.txt", "r") as referers:
        referers = referers.readlines()
    return random.choice(referers)


# Procura um user agent aleatório
def random_useragent():
    with open("tools/L7/user_agents.json", "r") as agents:
        user_agents = json.load(agents)["agents"]
    return random.choice(user_agents)
