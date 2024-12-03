import game as m

m.initPlayers()
zoro = m.createNewPlayer("Zoro", damage=20, defensePower=10)
luffy = m.createNewPlayer("Luffy", damage=50, defensePower=20)
pitty = m.createNewPlayer("Pitty", damage=10, defensePower=5)

m.addPlayer(zoro)
m.addPlayer(luffy)
m.addPlayer(pitty)

print("Players that entered the game:", m.PlayerList)

# Simulasi serangan
m.attackPlayer(zoro, luffy)  # Zoro menyerang Luffy

m.setPlayer(pitty, "defense", True)
m.attackPlayer(luffy, pitty)  # Luffy menyerang Pitty

# Tampilkan hasil sementara
m.displayMatchResult()

# Simulasi diskualifikasi
m.removePlayer("Zoro")

# Tampilkan hasil akhir
m.displayMatchResult()
