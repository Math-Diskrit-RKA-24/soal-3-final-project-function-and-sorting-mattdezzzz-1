def initPlayers():
    # inisialisasi daftar pemain
    global PlayerList
    PlayerList = []


def createNewPlayer(name, damage=0, defensePower=0):
    # membuat dictionary pemain baru
    return dict(
        name=name,
        score=0,
        damage=damage,
        health=100,
        defensePower=defensePower,
        defense=False,
    )


def addPlayer(player):
    global PlayerList
    # menambahkan pemain ke variabel global PlayerList
    PlayerList.append(player)


def removePlayer(name):
    global PlayerList
    for player in PlayerList:
        if player["name"] == name:
            # hapus pemain dari variabel global PlayerList
            PlayerList.remove(player)
            print(f"{player['name']} Disqualified")
            return
        print("There is no player with that name!")


def setPlayer(player, key, value):
    if key in player:
        # mengupdate atribut pemain
        player[key] = value
    else:
        print(f"Pemain tidak memiliki atribut {key} !")


def attackPlayer(attacker, target):
    # mengkalkulasi damage yang diterima target berdasarkan defense dan defensePower yang dimiliki target
    if target["defense"]:
        attacker_damage = max(attacker["damage"] - target["defensePower"], 0)
        print(
            f"{attacker['name']} attacking {target['name']}, {target['name']} being Defensive"
        )
    else:
        attacker_damage = attacker["damage"]
        print(
            f"{attacker['name']} attacking {target['name']}, without {target['name']} being Defensive"
        )

    # mengkalkulasi health yang tersisa setelah serangan
    new_health = max(target["health"] - attacker_damage, 0)

    # mengupdate score penyerang
    setPlayer(attacker, "score", attacker["score"] + (0.8 if target["defense"] else 1))

    # mengupdate health target dan defense target
    setPlayer(target, "health", new_health)
    setPlayer(target, "defense", False)

    print(
        f"{attacker['name']}'s Score {attacker['score']} x {target['name']}'s Health {target['health']}"
    )


def displayMatchResult():
    global PlayerList

    # mengurutkan pemain berdasarkan score dan health
    sorted_players = sorted(
        PlayerList, key=lambda player: (-player["score"], -player["health"])
    )

    for i, player in enumerate(sorted_players, 1):
        print(
            f"Rank {i}: {player['name']} | Score: {player['score']} | Health: {player['health']}"
        )
