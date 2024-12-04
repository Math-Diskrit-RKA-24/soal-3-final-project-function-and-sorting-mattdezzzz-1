import game as m

# serangan raja terakhir
def almagestAttack(target, score=0, damage=0, health=16, defensePower=0, defense=False):
    m.setPlayer(target, 'score', score)
    m.setPlayer(target, 'damage', damage)
    m.setPlayer(target, 'health', health)
    m.setPlayer(target, 'defensePower', defensePower)
    m.setPlayer(target, 'defense', defense)
    m.attackPlayer(gamma_almagest, target)

# eliminasi player yang mati
def mokad():
    for i in m.PlayerList:
        if i['health'] <= 0:
            m.removePlayer(i['name'])

# saling serang bergantian
def war(enemy):
    while enemy['health'] > 0:
        for i in teams:
            if enemy['health'] > 0:
                m.attackPlayer(i, enemy)
            if enemy['health'] > 0:
                m.attackPlayer(enemy, i)

end = False # untuk mengakhiri game nantinya

# Intro
print('Welcome to Galactic Empire Battleship')
empire = input("Name your Galactical Empire : ")

print(f"You must protect {empire} Galaxy against Gamma galactical empire.")
fighterType = input('Pick your warrior. Short range fighter or long range fighter? (short/long) : ')

m.initPlayers()

# Our team
alpha_lexion = m.createNewPlayer("Alpha Lexion", damage=35, defensePower=15) # raja
bellatrix = m.createNewPlayer("Bellatrix", damage=25, defensePower=10) # commander
minion = m.createNewPlayer("Centaurus", damage=15, defensePower=20) # centaur
if fighterType == 'long':
    minion = m.createNewPlayer("Sagittarius", damage=20, defensePower=15) # pemanah

# Enemies
gamma_almagest = m.createNewPlayer("Gamma Almagest", damage=50, defensePower=34) # raja terakhir
perseus = m.createNewPlayer("Perseus", damage=25, defensePower=10) # commander musuh
altair = m.createNewPlayer("Altair", damage=23, defensePower=10) # preman
cygnus = m.createNewPlayer("Cygnus", damage=20, defensePower=10) # preman
zenith = m.createNewPlayer("Zenith", damage=10, defensePower=5) # kroco musuh

# Add players
for i in [alpha_lexion, bellatrix, minion, gamma_almagest, perseus, altair, cygnus, zenith]:
    m.addPlayer(i)

m.setPlayer(alpha_lexion, 'health', 120)
m.setPlayer(gamma_almagest, 'health', 130)

teams = m.PlayerList[:3]
enemies = m.PlayerList[4:]

# Level 1 lawan prajurit musuh
print('\nLevel 1: Andromeda Epic Battle')
print('Galaxy : Adromeda')
input('Are you ready? (Enter to continue)')

war(zenith) # saling serang tim dengan zenith
mokad() # lihat siapa yang mokad dan eliminasi

# Level 2 lawan pejabat musuh
print('\nLevel 2 : Triangulum Tripple Battle')
print('Galaxy : Triangulum')
input('Are you ready? (Enter to continue)')

for i in [cygnus, altair, perseus]:
    war(i)
    mokad()

# Pulihkan health jadi 80, jika < 20 set defense jadi True
print('\nWelcome to Povidone-Iodine Waterfall')
print('Galaxy : Healaxy')
input('Relax, you must enhance your team. Enjoy the waterfall (enter to continue)')

for i in teams:
    if i['health'] < 30:
        m.setPlayer(i, 'defense', True)
    m.setPlayer(i, 'health', 80)
    print(i)

# Level 3 labirin galaksi
print('\nLevel 3: Whirlpool Gargantua Maze')
print('Galaxy : Whirlpool')
input('Are you ready? (Enter to continue)')
print('\nGamma Almagest, the king of Gamma empire, uses Gargantua, a blazar powered weapon in this maze galaxy as a catasthrophic mine.\nChoose the best path to solve the maze and go to Gamma Galaxy to beat the Gamma Almagest!\n')
print("zxc*v **\nz**x\n z*xcvz x**c\n  **zxc ****\n*zxc* ** zxc") # vxc**
path = input("\nChoose one character each row to represents your escape way.\nGargantua could be anywhere between z,x,c,v,or supernova(*). but if you're lucky, passing through supernova could be a pandora's box instead.\nHint : Bellatrix found that xc* at the last row may be safe and the supernova never be ambigous.\nYour path (ex: z*c**v) : ")

if path == 'vxc**':
    print("Strike, you survived the vortex! Now let's go to the Gamma Galaxy.")
    m.setPlayer(bellatrix, 'damage', bellatrix['damage']*1.2)
    m.setPlayer(alpha_lexion, 'defense', True)
else:
    for i in teams:
        m.setPlayer(i, 'health', 0)
        mokad()
    print("Kiwkiw! that's the sound of blazar blast. Game over :(")
    end = True

if end == False:
    # Level 4 lawan raja terakhir
    print('\nFinal Round: Dark Lactose Exotic Battle')
    print('Galaxy : Gamma')
    input('Are you ready for the last battle? (Enter to continue)')

    almagestAttack(minion, health=0) # one hit minion mati
    mokad()

    for i in [alpha_lexion, bellatrix]:
        m.attackPlayer(i, gamma_almagest) # team menyerang almagest

    almagestAttack(alpha_lexion, score = 0, damage=6, health=56)
    almagestAttack(bellatrix, damage=5, health=51)
    almagestAttack(gamma_almagest, score=1000, damage=999, health=304, defensePower=999, defense=True)

    # kerja sama dan kerja keras pantang menyerah
    while gamma_almagest['health'] > 1:
        m.attackPlayer(alpha_lexion, gamma_almagest)
        if gamma_almagest['health'] > 1:
            m.attackPlayer(bellatrix, gamma_almagest)

    almagestAttack(alpha_lexion)
    mokad()

    m.attackPlayer(bellatrix, gamma_almagest)
    mokad()

    SkorTim = []
    SkorLawan = []

    for i in teams:
        SkorTim.append(i['score'])
    for j in enemies:
        SkorLawan.append(j['score'])

    if sum(SkorTim) > sum(SkorLawan):
        print(f'Aweswome, {empire} Galaxy win the game! :)))')
    elif sum(SkorLawan) > sum(SkorTim):
        print(f"Gamma empire win the game :(")
    else:
        print("draw")

    m.displayMatchResult()
else:
    m.displayMatchResult()
