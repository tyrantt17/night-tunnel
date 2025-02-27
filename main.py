#night cage inspired maze thing, basic rpg stat loss game

import random
import time

pos = int(0)
demon = False
game = True
hp = int(100)
demonHp = int(10)
pocket1 = int(0)
pocket2 = int(0)
pocket3 = int(0)
parasite = False
oil = False
throatDeath = False
finalBoss = 0
bossSelection = 0
bullets = 0

print("You awake in a long tunnel of pure darkness. All you have is a candle and you feel the darkness crawling on your back.")
print("The walls move around you, breathing heavily. They shift the paths in which you crawl.")
print("Can you survive 100 miles?")
while game == True:
    if throatDeath == True:
        print("The tissues on your throat bleed violently as the parasites fight! The taste of iron overwhelms you.")
        hp = (hp - 5)
        print("Your hp is now "+ str(hp)+".")
    print("On your turn you have 4 possible actions. 1-Crawl, 2-Attack, 3-Inventory, 4-Stats")
    act = int(input("Answer:"))
    if act > 4:
        print("CRITICAL ERROR. END PROGRAM.")
    if act < 1:
        print("CRITICAL ERROR. END PROGRAM.")
    if act == 1:
        if demon == False:
            if oil == False:
                pos = pos+1
            if oil == True:
                pos = pos+2
                oil = False
            print("You crawl through the tunnel.")
            event = random.randint(1,10)
            if event == 1:
                print("As you crawl, you see tentacles whipping the walls, a demon approaches!")
                demon = True
                demonHp = 10
            if event == 2:
                print("A demon drops from the roof, poised to attack!")
                demon = True
                demonHp = 10
            if event == 3:
                print("A strange, hooded man approaches you. He asks to trade an item, but won't show you what he'll give.")
                print("1 - Yes, 2 - No")
                answer = int(input("Answer:"))
                if answer == 1:
                    print("\"Ah! Delightful! What might you have in store for me?\"")
                    print("1 - Oil, 2 - Gun, 3 - Knife, 4 - Bullet")
                    answer = int(input("Answer:"))
                    if pocket1 == answer:
                        print("Thank you. Here is your reward.")
                        pocket1 = 0
                        reward = 1
                    else:
                        if pocket2 == answer:
                            print("Thank you. Here is your reward.")
                            pocket2 = 0
                            reward = 1
                        else:
                            if pocket3 == answer:
                                print("Thank you. Here is your reward.")
                                pocket3 = 0
                            reward = 1
                    if reward == 1:
                        print("The man hands you a box! Ecstaticaly, you open it!")
                        gamble = random.randint(1,5)
                        if gamble == 1:
                            print("But the man was a trickster! It's a hell box! A demon exits!")
                            demon = True
                            demonHp = 10
                        if gamble == 2:
                            print("Inside was a can of \"Mexican Squirt\". You drink it and your soul is happy.")
                            print("Hp increased by 25.")
                            hp = (hp + 25)
                            if hp > 100:
                                hp = 100
                        if gamble == 3:
                            print("It's nothing. bruh.")
                        if gamble == 4:
                            if throatDeath == False:
                                print("Inside is a bottle of \"Anti-Parasite Vodka\". You drink it and all parasites you had die. It tastes disgusting.")
                                parasite = False
                            else:
                                print("You feel the parasites fall down your throat and die. One of them gets stuck and you spit up blood as it claws into your throat. It falls, but you're a bit injured.")
                                hp = hp - 10
                                print("Your HP is now "+str(hp)+".")
                                parasite = False
                                throatDeath = False
                        if gamble == 5:
                            print("You find a satchel of 5 bullets! Wowie!.")
                            bullets = bullets+5
                    else:
                        print("\"You dare try to deceive me!?\"")
                        print("The man speeds past you, stabbing you in the chest.")
                        hp = hp - 10
                        print("Your hp is now "+str(hp)+".")
                else:
                    spooky = random.randint(1,10)
                    if spooky == 1:
                        print("The hood falls off and tentacles fly out at you! The man was a demon!")
                        demon = True
                        demonHp = 10
                    else:
                        print("\"I see. I will leave.\"")
            if event == 4:
                print("You found oil!")
                if pocket1 == 0:
                    pocket1 = 1
                else:
                    if pocket2 == 0:
                        pocket2 = 1
                    else:
                        if pocket3 == 0:
                            pocket3 = 1
                        else:
                            print("Your pockets are full! You move on.")
            if event == 5:
                print("You found a strange liquid on the ground.")
                safe = random.randint(1,2)
                print("Do you drink it? 1 - Yes 2 - No")
                liq = int(input("Answer:"))
                if liq == 1:
                    if safe == 1:
                        if parasite == True:
                            print("You drink the liquid, but the parasite in your throat takes half of it. You regain +5 HP.")
                            hp = hp +5
                            if hp > 100:
                                hp = 100
                        if parasite == False:
                            print("You drink the liquid, and it gives you a warm feeling that reminds you of home. +10 HP.")
                            hp = hp + 10
                            if hp > 100:
                                hp = 100
                    if safe == 2:
                        if parasite == False:
                            print("You drink the liquid, and your throat closes in on itself. Before you die, you feel something stretch it open manually. You've been inflicted with a parasite.")
                            parasite = True
                        else:
                            if parasite == True:
                                print("Another parasite enters your body! The parasites begin violently fighting, shredding your throat!")
                                throatDeath = True
            if event == 6:
                found = random.randint(1,4)
                if found == 1:
                    print("You found a rusty revolver!")
                    if pocket1 == 0:
                        pocket1 = 2
                    else:
                        if pocket2 == 0:
                            pocket2 = 2
                        else:
                            if pocket3 == 0:
                                pocket3 = 2
                            else:
                                print("Your pockets are full! You move on.")
                if found == 2:
                    print("You found a bloody knife!")
                    if pocket1 == 0:
                        pocket1 = 3
                    else:
                        if pocket2 == 0:
                            pocket2 = 3
                        else:
                            if pocket3 == 0:
                                pocket3 = 3
                            else:
                                print("Your pockets are full! You move on.")
                if found == 3:
                    print("You found a bullet!")
                    if pocket1 == 0:
                        pocket1 = 4
                    else:
                        if pocket2 == 0:
                            pocket2 = 4
                        else:
                            if pocket3 == 0:
                                pocket3 = 4
                            else:
                                print("Your pockets are full! You move on.")
                if found == 4:
                    print("Your soul drops to the floor...")
                    time.sleep(1)
                    print("A giant demon of enormous sizes approaches!")
                    time.sleep(1)
                    name = random.randint(1,4)
                    if name == 1:
                        print("It's Azazel!")
                    if name == 2:
                        print("It's Belial!")
                    if name == 3:
                        print("It's Abaddon!")
                    if name == 4:
                        print("It's Leviathan!")
                    demon = True
                    demonHp = 30
        else:
            if bossSelection == 2:
                print("\"YOU CAN'T RUN FROM ME, MORTAL.\"")
                time.sleep(1)
                print("Kalkazor raises his hands to the sky.")
                time.sleep(1)
                verbs = ("incinerates", "voids", "exterminates", "deletes", "inflames", "explodes", "zeroes")
                nouns = ("knee", "soul", "heart", "brain", "lungs", "arms", "legs", "kidney", "forehead", "thigh")
                ranVerb = random.choice(list(verbs))
                ranNoun = random.choice(list(nouns))
                print("Kalkazor "+str(ranVerb)+" your "+str(ranNoun)+"!")
                time.sleep(1)
                dmg = random.randint(5,15)
                print("You took "+str(dmg)+" damage!")
                time.sleep(1)
                hp = hp-dmg
                print("Your health is now "+str(hp)+".")
            else:
                print("You attempt to move forward, and the demon attacks!")
                verbs = ("grips", "whacks", "punches", "kicks", "stabs", "shoots", "removes")
                nouns = ("knee", "soul", "heart", "brain", "lungs", "arms", "legs", "kidney", "forehead", "thigh")
                ranVerb = random.choice(list(verbs))
                ranNoun = random.choice(list(nouns))
                print("The demon "+str(ranVerb)+" your "+str(ranNoun)+"!")
                dmg = random.randint(5,15)
                print("You took "+str(dmg)+" damage!")
                hp = hp-dmg
                print("Your health is now "+str(hp)+".")
    if act == 2:
        print("You reach out to attack!!")
        time.sleep(1)
        verbs = ("eviscerate", "obliterate", "desecrate", "absolve him from", "slit", "smash", "pummel")
        nouns = ("knee", "soul", "heart", "brain", "lungs", "arms", "legs", "kidney", "forehead", "thigh")
        ranVerb = random.choice(list(verbs))
        ranNoun = random.choice(list(nouns))
        print("You "+str(ranVerb)+" his "+str(ranNoun)+"!")
        dmg = random.randint(3,7)
        time.sleep(1)
        if bossSelection == 1:
            print("Vyrkador doesn't even care.")
            time.sleep(1)
        else:
            print("You dealt "+str(dmg)+" damage!")
            demonHp = demonHp-dmg
            time.sleep(1)
            print("His health is now "+str(demonHp)+".")
            time.sleep(1)
        if demonHp < 1:
            print("The demon falls to the ground, dead! Nice!")
            demon = False
        else:
            if bossSelection == 2:
                time.sleep(1)
                print("Kalkazor raises his hands to the sky.")
                time.sleep(1)
                verbs = ("incinerates", "voids", "exterminates", "deletes", "inflames", "explodes", "zeroes")
                nouns = ("knee", "soul", "heart", "brain", "lungs", "arms", "legs", "kidney", "forehead", "thigh")
                ranVerb = random.choice(list(verbs))
                ranNoun = random.choice(list(nouns))
                print("Kalkazor "+str(ranVerb)+" your "+str(ranNoun)+"!")
                time.sleep(1)
                dmg = random.randint(5,15)
                print("You took "+str(dmg)+" damage!")
                time.sleep(1)
                hp = hp-dmg
                print("Your health is now "+str(hp)+".")
            else:
                time.sleep(1)
                print("He fights back!")
                time.sleep(1)
                verbs = ("grips", "whacks", "punches", "kicks", "stabs", "shoots", "removes")
                nouns = ("knee", "soul", "heart", "brain", "lungs", "arms", "legs", "kidney", "forehead", "thigh")
                ranVerb = random.choice(list(verbs))
                ranNoun = random.choice(list(nouns))
                print("The demon "+str(ranVerb)+" your "+str(ranNoun)+"!")
                time.sleep(1)
                dmg = random.randint(5,15)
                print("You took "+str(dmg)+" damage!")
                time.sleep(1)
                hp = hp-dmg
                print("Your health is now "+str(hp)+".")
    if act == 3:
        print("You rummage through your pockets.")
        print("Pocket 1:")
        if pocket1 == 1:
            print("OIL")
        else:
            if pocket1 == 2:
                print("GUN")
            else:
                if pocket1 == 3:
                    print("KNIFE")
                else:
                    if pocket1 == 4:
                        print("BULLET")
                    else:
                        print("NONE")
        print("Pocket 2:")
        if pocket2 == 1:
            print("OIL")
        else:
            if pocket2 == 2:
                print("GUN")
            else:
                if pocket2 == 3:
                    print("KNIFE")
                else:
                    if pocket2 == 4:
                        print("BULLET")
                    else:
                        print("NONE")
        print("Pocket 3:")
        if pocket3 == 1:
            print("OIL")
        else:
            if pocket3 == 2:
                print("GUN")
            else:
                if pocket3 == 3:
                    print("KNIFE")
                else:
                    if pocket3 == 4:
                        print("BULLET")
                    else:
                        print("NONE")
        print("Would you like to use a pocket? 1 2 or 3.")
        usePocket = int(input("Answer:"))
        if usePocket == 1:
            if pocket1 == 1:
                print("You're covered in oil! The next time you move, you'll move two spaces.")
                oil = True
                pocket1 = 0
            if pocket1 == 2:
                print("You pull out your gun!")
                if bullets > 0:
                    if demon == True:
                        aim = random.randint(1,5)
                        if aim != 1:
                            print("And shoot the demon!")
                            demonHp = demonHp - 10
                            print("His health is now "+str(demonHp)+".")
                            time.sleep(1)
                            if demonHp < 1:
                                print("The demon falls to the ground, dead! Nice!")
                                demon = False
                        else:
                            print("The bullet flies off into the abyss... You missed.")
                    else:
                        time.sleep(2)
                        print("Wow. I'm really happy that you pulled your gun out.")
                        time.sleep(3)
                        print("Honestly.")
                        time.sleep(1)
                        print("You're oh so good at pulling the gun out.")
                        time.sleep(1)
                        print("Obviously, there is nothing to shoot at.")
                else:
                    print("Click!")
                    print("\"Out of ammo...\"")
            if pocket1 == 3:
                if demon == True:
                    print("You reach out to attack!!")
                    time.sleep(1)
                    verbs = ("slice", "cut", "shank", "carve", "slit", "pierce", "divide")
                    nouns = ("knee", "soul", "heart", "brain", "lungs", "arms", "legs", "kidney", "forehead", "thigh")
                    ranVerb = random.choice(list(verbs))
                    ranNoun = random.choice(list(nouns))
                    print("You "+str(ranVerb)+" his "+str(ranNoun)+"!")
                    dmg = random.randint(5,9)
                    time.sleep(1)
                    print("You dealt "+str(dmg)+" damage!")
                    demonHp = demonHp-dmg
                    time.sleep(1)
                    print("His health is now "+str(demonHp)+".")
                    time.sleep(1)
                    if demonHp < 1:
                        print("The demon is sliced into oblivion, unrecognizable. It is dead.")
                        demon = False
                    else:
                        time.sleep(1)
                        print("He fights back!")
                        time.sleep(1)
                        verbs = ("grips", "whacks", "punches", "kicks", "stabs", "shoots", "removes")
                        nouns = ("knee", "soul", "heart", "brain", "lungs", "arms", "legs", "kidney", "forehead", "thigh")
                        ranVerb = random.choice(list(verbs))
                        ranNoun = random.choice(list(nouns))
                        print("The demon "+str(ranVerb)+" your "+str(ranNoun)+"!")
                        time.sleep(1)
                        dmg = random.randint(5,15)
                        print("You took "+str(dmg)+" damage!")
                        time.sleep(1)
                        hp = hp-dmg
                        print("Your health is now "+str(hp)+".")
                else:
                    print("Nothing to stab.")
            if pocket1 == 4:
                bullets = bullets +1
                print("You load the bullet into the gun. \"That makes "+str(bullets)+".\"")
                pocket1 = 0
        if usePocket == 2:
            if pocket2 == 1:
                print("You're covered in oil! The next time you move, you'll move two spaces.")
                oil = True
                pocket2 = 0
            if pocket2 == 2:
                print("You pull out your gun!")
                if bullets > 0:
                    if demon == True:
                        aim = random.randint(1,5)
                        if aim != 1:
                            print("And shoot the demon!")
                            demonHp = demonHp - 10
                            print("His health is now "+str(demonHp)+".")
                            time.sleep(1)
                            if demonHp < 1:
                                print("The demon falls to the ground, dead! Nice!")
                                demon = False
                        else:
                            print("The bullet flies off into the abyss... You missed.")
                    else:
                        time.sleep(2)
                        print("Wow. I'm really happy that you pulled your gun out.")
                        time.sleep(3)
                        print("Honestly.")
                        time.sleep(1)
                        print("You're oh so good at pulling the gun out.")
                        time.sleep(1)
                        print("Obviously, there is nothing to shoot at.")
                else:
                    print("Click!")
                    print("\"Out of ammo...\"")
            if pocket2 == 3:
                if demon == True:
                    print("You reach out to attack!!")
                    time.sleep(1)
                    verbs = ("slice", "cut", "shank", "carve", "slit", "pierce", "divide")
                    nouns = ("knee", "soul", "heart", "brain", "lungs", "arms", "legs", "kidney", "forehead", "thigh")
                    ranVerb = random.choice(list(verbs))
                    ranNoun = random.choice(list(nouns))
                    print("You "+str(ranVerb)+" his "+str(ranNoun)+"!")
                    dmg = random.randint(5,9)
                    time.sleep(1)
                    print("You dealt "+str(dmg)+" damage!")
                    demonHp = demonHp-dmg
                    time.sleep(1)
                    print("His health is now "+str(demonHp)+".")
                    time.sleep(1)
                    if demonHp < 1:
                        print("The demon is sliced into oblivion, unrecognizable. It is dead.")
                        demon = False
                    else:
                        time.sleep(1)
                        print("He fights back!")
                        time.sleep(1)
                        verbs = ("grips", "whacks", "punches", "kicks", "stabs", "shoots", "removes")
                        nouns = ("knee", "soul", "heart", "brain", "lungs", "arms", "legs", "kidney", "forehead", "thigh")
                        ranVerb = random.choice(list(verbs))
                        ranNoun = random.choice(list(nouns))
                        print("The demon "+str(ranVerb)+" your "+str(ranNoun)+"!")
                        time.sleep(1)
                        dmg = random.randint(5,15)
                        print("You took "+str(dmg)+" damage!")
                        time.sleep(1)
                        hp = hp-dmg
                        print("Your health is now "+str(hp)+".")
                else:
                    print("Nothing to stab.")
            if pocket2 == 4:
                bullets = bullets +1
                print("You load the bullet into the gun. \"That makes "+str(bullets)+".\"")
                pocket2 = 0
        if usePocket == 3:
            if pocket3 == 1:
                print("You're covered in oil! The next time you move, you'll move two spaces.")
                oil = True
                pocket3 = 0
            if pocket3 == 2:
                print("You pull out your gun!")
                if bullets > 0:
                    if demon == True:
                        aim = random.randint(1,5)
                        if aim != 1:
                            print("And shoot the demon!")
                            demonHp = demonHp - 10
                            print("His health is now "+str(demonHp)+".")
                            time.sleep(1)
                            if demonHp < 1:
                                print("The demon falls to the ground, dead! Nice!")
                                demon = False
                        else:
                            print("The bullet flies off into the abyss... You missed.")
                    else:
                        time.sleep(2)
                        print("Wow. I'm really happy that you pulled your gun out.")
                        time.sleep(3)
                        print("Honestly.")
                        time.sleep(1)
                        print("You're oh so good at pulling the gun out.")
                        time.sleep(1)
                        print("Obviously, there is nothing to shoot at.")
                else:
                    print("Click!")
                    print("\"Out of ammo...\"")
            if pocket3 == 3:
                if demon == True:
                    print("You reach out to attack!!")
                    time.sleep(1)
                    verbs = ("slice", "cut", "shank", "carve", "slit", "pierce", "divide")
                    nouns = ("knee", "soul", "heart", "brain", "lungs", "arms", "legs", "kidney", "forehead", "thigh")
                    ranVerb = random.choice(list(verbs))
                    ranNoun = random.choice(list(nouns))
                    print("You "+str(ranVerb)+" his "+str(ranNoun)+"!")
                    dmg = random.randint(5,9)
                    time.sleep(1)
                    print("You dealt "+str(dmg)+" damage!")
                    demonHp = demonHp-dmg
                    time.sleep(1)
                    print("His health is now "+str(demonHp)+".")
                    time.sleep(1)
                    if demonHp < 1:
                        print("The demon is sliced into oblivion, unrecognizable. It is dead.")
                        demon = False
                    else:
                        time.sleep(1)
                        print("He fights back!")
                        time.sleep(1)
                        verbs = ("grips", "whacks", "punches", "kicks", "stabs", "shoots", "removes")
                        nouns = ("knee", "soul", "heart", "brain", "lungs", "arms", "legs", "kidney", "forehead", "thigh")
                        ranVerb = random.choice(list(verbs))
                        ranNoun = random.choice(list(nouns))
                        print("The demon "+str(ranVerb)+" your "+str(ranNoun)+"!")
                        time.sleep(1)
                        dmg = random.randint(5,15)
                        print("You took "+str(dmg)+" damage!")
                        time.sleep(1)
                        hp = hp-dmg
                        print("Your health is now "+str(hp)+".")
                else:
                    print("Nothing to stab.")
            if pocket3 == 4:
                bullets = bullets +1
                print("You load the bullet into the gun. \"That makes "+str(bullets)+".\"")
                pocket3 = 0
    if act == 4:
        print("Your HP is "+str(hp))
        if throatDeath == True:
            print("You have multiple parasites warring over you.")
        else:
            if parasite == True:
                print("You have a parasite.")
            else:
                print("You don't have a parasite.")
        if demon == True:
            print("There is a demon.")
            print("The demon's health is "+str(demonHp)+".")
        else:
            print("There is no demon.")
        if oil == True:
            print("You are covered in oil.")
        else:
            print("You are not oiled up.")
        print("You've moved "+str(pos)+" miles.")
        print("You have "+str(bullets)+" bullets.")
    if hp < 1:
        print("The walls close in on you.")
        print("You see a chance to escape!")
        time.sleep(1)
        print("...")
        time.sleep(2)
        clutch = random.randint(1,25)
        if clutch == 1:
            print("And you tear through the walls! You're invigorated as you taste life yet again!")
            print("Health increased to 25!")
            hp = 25
        if clutch != 1:
            print("But it's too late. The walls close in on you and you feel your body being digested by the beast.")
            print("GAME OVER")
            game = False
    if pos > 100:
        if finalBoss == 0:
            print("Wait...")
            time.sleep(1)
            print("You see a light!")
            time.sleep(1)
            print("Finally, the exit!")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("But something is blocking the way!")
            time.sleep(1)
            print("Something huge!")
            time.sleep(1)
            finalBoss = 1
            bossSelection = random.randint(1,3)
            if bossSelection == 1:
                print("The sound of metal clanking shakes the earth...")
                time.sleep(1)
                print("It's Vyrkador! The demon of metal!")
                time.sleep(1)
                print("He's impossible to hit with fists! I hope you have tools ready!")
                demon = True
                demonHp = 50
            if bossSelection == 2:
                print("You feel the walls pulling closer...")
                time.sleep(1)
                print("It's Kalkazor! The Demon of Souls!")
                time.sleep(1)
                print("He's got no abilities, but he hits like a truck, and he can take a ton of hits!")
                demon = True
                demonHp = 75
            if bossSelection == 3:
                print("You hear something terrifying slithering towards you...")
                time.sleep(1)
                print("It's Trymus! The Demon of Parasites!")
                time.sleep(1)
                if parasite == True:
                    print("Bad luck...")
                    time.sleep(1)
                    print("Really, really, bad luck..")
                    time.sleep(1)
                    print("You feel something scratching at the inside of your throat.")
                    time.sleep(1)
                    print("A parasite bursts out of your neck!")
                    time.sleep(1)
                    print("You took 50 damage!")
                    time.sleep(1)
                    hp = hp -50
                else:
                    print("You got lucky!")
                    time.sleep(1)
                    print("If you don't have a parasite in you, Trymus can't use his ultimate move!")
                    time.sleep(1)
                    print("Now all that's left is to take him down!")
                    demon = True
                    demonHp = 40
    if finalBoss == 1:
        if demon == False:
            print("You slew the demon!")
            time.sleep(1)
            print("You escaped.")
            game = False
            