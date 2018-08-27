import random
import time
roomNum = 0

def limit(num, minimum = 1, maximum = 10):
  return max(min(num, maximum), minimum)

def roll(stat):
    return stat + random.randint(1,6)

def randRoom():
    return random.randint(1,6)

def battleMethod(baseATK, baseDEF, HP, enemyStat, enemyHealth):
    while HP > 0 and enemyHealth > 0:
        action = input("You are in battle, would you like to attack, defend, or use a potion? [a/d/p] ")
        if action == "a":
            time.sleep(1)
            damage = roll(baseStat)
            enemyDamage = roll(enemyStat)
            print("You dealt " + str(damage) + " damage to the enemy.")
            enemyHealth -= damage
            print("The enemy dealt " + str(enemyDamage) + " damage to you.")
            time.sleep(1)
            HP -= enemyDamage
            print("Current HP is: " + str(HP))
            print("Current enemy health is: " + str(enemyHealth))
            print("")
        if action == "d":
            time.sleep(1)
            block = roll(baseDEF)
            enemyDamage = roll(enemyStat)
            print("You block " + str(block) + " damage to yourself.")
            time.sleep(1)
            if runesRead and HP < 20:
                print("You also heal 5 HP from your ability.")
                time.sleep(1)
                HP += 5
            if defence >= enemyDamage:
                print("The enemy did no damage.")
                print("Current HP is: " + str(HP))
                print("Current enemy health is: " + str(enemyHealth))
                time.sleep(1)
            else:
                HP += defence
                HP -= enemyDamage
                print("Current HP is: " + str(HP))
                print("Current enemy health is: " + str(enemyHealth))
                time.sleep(1)
            print("")
        if action == "p":
            time.sleep(1)
            if "Health Potion" in inventory:
                print("You used a health potion.")
                time.sleep(1)
                HP += 15
                print("You now have " + str(health) + " health.")
            else:
                print("You don't have any health potions!")
            time.sleep(1)
        if HP <= 0:
            time.sleep(1)
            print("You died.. game over.")
            exit()
        if enemyHealth <= 0:
            time.sleep(1)
            print("You were victorious.")
            print("")
            return HP

def checkInventory(INV):
    print("Opening inventory.")
    time.sleep(1)
    print("You have " + str(coins) + " coins")
    print(INV[1:])
    print("")

def statReadout(CLASS, STR, DEF, DEX, INT, HP):
    print("Class: " + CLASS)
    print("STR: " + str(STR))
    print("DEF: " + str(DEF))
    print("DEX: " + str(DEX))
    print("INT: " + str(INT))
    print("HP: " + str(HP))
    print("")
    return

#Starting Character Info
goblinKingAlive = True
goblinKillNum = 0
chestOpened = False
runesRead = False


name = input("Hello, What is your username? ")
print("Hello " + name + "." )
time.sleep(0.5)

strength = limit(int(input("Enter your strength stat: ")))
print("Strength stat: " + str(strength))
time.sleep(0.5)

defence = limit(int(input("Enter your defence stat: ")))
print("Defence stat: " + str(defence))
time.sleep(0.5)

dexterity = limit(int(input("Enter your dexterity stat: ")))
print("Dexterity stat: " + str(dexterity))
time.sleep(0.5)

magic = limit(int(input("Enter your magic stat: ")))
print("Magic stat: " + str(magic))
time.sleep(0.5)

health = 100
print("Health: " + str(health))
time.sleep(0.5)

coins = 0
inventory = [str(coins)]


baseStat = strength
classtype = input("Are you a Warrior, Mage, or Archer? ")
if classtype == "warrior":
    baseStat = strength
    print("Wielding a sword, you deal " + str(baseStat) + " damage.")
if classtype == "mage":
    baseStat = magic
    print("Wielding a staff, you deal " + str(baseStat) + " damage.")
if classtype == "archer":
    baseStat = dexterity
    print("Wielding a bow, you deal " + str(baseStat) + " damage.")
time.sleep(1)

#Game Start
stoneTrial = input("You come across a cave with a heavy stone sealing the entrance. Would you like to try to move the stone? [Y/N] ")
if stoneTrial.lower() == "y":
    print("You attempt to move the stone")
    time.sleep(1)
    print("Rolling for success...")
    time.sleep(1)
    if roll(strength) > 12:
        print("You move the stone away from the entrance of the cave and feel stronger as a result.")
        time.sleep(1)
        strength += 1
        print("You now have " + str(strength) + " strength.")
        time.sleep(1)
        if classtype == "warrior":
            baseStat += 1
        print("You enter the cave.")
        time.sleep(1)
    else:
        print("As you attempt to move the stone, you trip and scrape your knee against the ground")
        time.sleep(1)
        health -= 5
        print("Your hp is now at: " + str(health))
        time.sleep(1)
        print("You cannot budge the stone and you are forced to find a separate entrance.")
        time.sleep(1)
        print("As you walk around the outside of the cave to investigate, you find a small opening and attempt to slip inside the cave.")
        time.sleep(1)
if stoneTrial.lower() == "n":
    print("You decide to ignore the stone and find a separate entrance.")
    time.sleep(1)
    print("As you walk around the outside of the cave to investigate, you find a small opening and manage to slip inside the cave.")
    time.sleep(1)
print("Now inside the cave, you light a torch and examine your surroundings.")
time.sleep(1)
print("The path ahead seems to stretch on endlessly, and you hear various critters running about.")
time.sleep(1)
print("You decide to carefully tread forward and keep a steady hand on your weapon.")
print("")
time.sleep(1)

#Optional Monster Encounter
print("Deeper inside the cave your hear an unsettling growl and stop in your tracks. As you look carefully, you see a goblin lumbering ahead.")
time.sleep(1)
monsterTrial = input("Do you decide to fight or try to hide and avoid the encounter? [fight/flee] ")
time.sleep(1)
if monsterTrial == "fight":
    time.sleep(1)
    print("You ambush the goblin.")
    time.sleep(1)
    health = battleMethod(baseStat, defence, health, 0, 25)
    goblinKillNum += 1
if monsterTrial == "flee":
    time.sleep(1)
    print("You quickly duck behind a nearby rock and try to wait out the goblin.")
    time.sleep(1)
    print("Rolling for success...")
    time.sleep(1)
    if roll(dexterity) > 12:
        print("The goblin seems to not have noticed your presence and continues onward unaware.")
        time.sleep(1)
        print("You feel like your ability to sneak around has improved.")
        time.sleep(1)
        dexterity += 1
        print("You now have " + str(dexterity) + " dexterity.")
        time.sleep(1)
        if classtype == "archer":
            baseStat += 1
    else:
        print("The goblin spots your hiding spot and fires off an arrow towards you.")
        time.sleep(1)
        print("Rolling for defence...")
        time.sleep(1)
        if roll(defence) > 12:
            print("You manage to deflect the arrow but the goblin continues to walk towards you, looks like you'll have to fight.")
            time.sleep(1)
            health = battleMethod(baseStat, defence, health, 0, 25)
            goblinKillNum += 1
        else:
            print("The arrow grazes your arm and you wince in pain.")
            time.sleep(1)
            health -= 5
            print("Looks like you can't avoid this fight.")
            time.sleep(1)
            health = battleMethod(baseStat, defence, health, 0, 25)
            goblinKillNum += 1
print("You press onward into the cave.")
print("")
time.sleep(1)

#Random Dungeon
while health > 0:
    print("You stop for a second to take a breather. You can access your inventory, look at your stats, or continue onwards.")
    action = input("What would you like to do? [inv/stat/con] ")
    if action == "inv":
        time.sleep(1)
        checkInventory(inventory)
        roomNum = 0
    if action == "stat":
        time.sleep(1)
        statReadout(classtype, strength, defence, dexterity, magic, health)
        roomNum = 0
    if action == "con":
        print("You decide to keep moving.")
        print("")
        time.sleep(1)
        if goblinKingAlive == False:
            print("Looks like you've cleared this dungeon, but there might be a bit more to explore.")
            action = input("Do you want to stay or leave? ")
            if action == "leave":
                print("You return to town.")
                roomNum = 99
            if action == "stay":
                print("You decide to stay a while.")
        roomNum = randRoom()
            
    #Room 1 - Forced Monster Encounter
    if roomNum == 1 and goblinKingAlive:
        print("You see a goblin ahead in the distance but there's no time to hide.")
        print("Looks like you'll have to fight.")
        health = battleMethod(baseStat, defence, health, 0, 25)
        goblinKillNum += 1
        if goblinKillNum > 4 and goblinKingAlive:
            print("As you take a breather after slaying the goblin, you suddenly feel the ground begin to tremble.")
            time.sleep(1)
            print("Suddenly, a giant goblin wielding a giant club rushes from out of the darkness towards you.")
            print("Looks like you've angered the Goblin King by slaying too many goblins.")
            time.sleep(1)
            print("You take a second to prepare yourself and ready your fighting stance, this fight might be a tough one.")
            print("")
            health = battleMethod(baseStat, defence, health, 5, 75)
            print("You manage to kill the Goblin King.")
            time.sleep(1)
            print("You feel a little more experienced in adventuring and find coins as well as a health potion on his corpse.")
            time.sleep(1)
            print("You take his gold crown as a symbol of his defeat and put it in your pouch.")
            time.sleep(1)
            strength += 1
            dexterity += 1
            magic += 1
            defence += 1
            baseStat += 1
            inventory.append("Health Potion")
            coins += 100
            print("Plus 1 to all stats!.")
            goblinKingAlive = False
            print("")
        print("You press onward into the cave.")
        print("")
        time.sleep(1)
    elif goblinKingAlive == False:
        print("The news of your victory over the Goblin King has spread quickly.")
        time.sleep(1)
        print("A goblin in the distance spots you and scurries away hastily.")

    #Room 2 - Treasure Chest
    if roomNum == 2:
        print("You step into a room that has a treasure chest in the middle.")
        time.sleep(1)
        print("This almost looks too suspicious, but you might find some good loot if you try to open the chest.")
        time.sleep(1)
        chestTrial = input("Do you try to open the chest? [y/n] ")
        if chestTrial == "y":
            time.sleep(1)
            print("You check for traps and attempt to open the chest.")
            time.sleep(1)
            print("Rolling for success...")
            time.sleep(1)
            if roll(dexterity) > 12:
                if chestOpened == False:
                    print("You find an obvious trap and disarm the chest, gaining some lockpicking experience in the process.")
                    time.sleep(1)
                    dexterity += 1
                    print("You now have " + str(dexterity) + " dexterity.")
                    time.sleep(1)
                    if classtype == "archer":
                        baseStat += 1
                    chestOpened = True
                print("You open the chest to discover some coins and a health potion which restores you for 15 health.")
                time.sleep(1)
                inventory.append("Health Potion")
                coins += 15
            else:
                print("You attempt to open the chest and accidentally trigger a trap, causing you to lose 15 HP.")
                time.sleep(1)
                print("You fail to open the chest for now.")
                time.sleep(1)
                health -= 15
                print("You now have " + str(health) + " health.")
            print("You press onward into the cave.")
        if chestTrial == "n":
            print("You decide to ignore the chest and press onwards.")
        print("")
        time.sleep(1)

    #Room 3 - Magic Runes
    if roomNum == 3 and runesRead == False:
        print("You notice an unnatural blueish glow emanating from some rocks.")
        time.sleep(1)
        print("As you step closer to investigate, you discover that the glow is caused by magical runes that you can't quite make out.")
        time.sleep(1)
        print("Do you try to read the runes out loud?")
        time.sleep(1)
        print("This could result in learning a new ability, or it could backfire if you haven't brushed up on your ancient runes in a while.")
        time.sleep(1)
        action = input("[y/n] ")
        if action == "y":
            time.sleep(1)
            print("You begin reciting the runes aloud.")
            time.sleep(1)
            print("Rolling for success...")
            time.sleep(1)
            if roll(magic) > 12:
                print("You manage to recite the verse without error and learn a new ability.")
                time.sleep(1)
                print("You now heal a small amount when defending with low health (HP < 20).")
                print("You also gained some magic experience from the runes.")
                time.sleep(1)
                magic += 1
                print("You now have " + str(magic) + " magic.")
                time.sleep(1)
                if classtype == "mage":
                    baseStat += 1
                runesRead = True
                print("You leave the runes behind and continue onward.")
                print("")
                time.sleep(1)
            else:
                print("You accidentally stumble over a few of the words and begin to feel weakened.")
                print("Looks like you accidentally drained 10 health from yourself.")
                print("")
                time.sleep(1)
                health -= 10
                print("You now have " + str(health) + " health.")
                time.sleep(1)
                print("You decide to continue onward for now and leave the runes behind.")
                print("")
    elif roomNum == 3 and runesRead == True:
        print("You come across the same runes for the healing spell, but there's nothing more to learn here.")
        print("You decide to continue onward.")
        print("")
        time.sleep(1)

    #Room 4 - Rusty Sword
    if roomNum == 4 and "rusty sword" not in inventory:
        print("As you scan your surroundings, you see a glint of metal gleam in your torchlight.")
        time.sleep(1)
        print("You step closer to take a look and discover a worn, rusty sword jutting out of a rock.")
        time.sleep(1)
        print("You might be able to pull it out with a little bit of strength and finesse.")
        time.sleep(1)
        action = input("Would you like to try to pull it out? [y/n] ")
        if action == "y":
            print("Rolling for success...")
            time.sleep(1)
            if roll(strength) > 12 and roll(dexterity) > 12:
                print("You manage to pull the sword out.")
                time.sleep(1)
                print("You put the sword in your inventory.")
                inventory.append("rusty sword")
                time.sleep(1)
                print("The sword cannot be used in its current state, looks like you'll need to take it back to the town to clean it up.")
                time.sleep(1)
            else:
                print("You try to pull the sword out, but it refuses to budge.")
                time.sleep(1)
                print("You decide to move on for now.")
                time.sleep(1)
            print("You continue deeper into the cave.")
            print("")
            time.sleep(1)
        if action == "n":
            print("You ignore the sword and continue onward.")
            print("")
            time.sleep(1)

    #Filler rooms
    if roomNum == 5 or roomNum == 6:
        print("You find nothing of interest here.")
        time.sleep(1)
