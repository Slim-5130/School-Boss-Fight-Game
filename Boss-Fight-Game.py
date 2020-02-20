#imports
import random 

#class declarations

class Player():
    def __init__(self, name, club, hp, power, speed, intt, dex):
        self.name=name
        self.club=club
        self.maxhp=hp
        self.hp=hp
        self.power=power
        self.maxspeed=speed
        self.speed=speed
        self.intt=intt
        self.dex=dex
        self.evade=False
        self.credit=0
        self.stress=0
        self.stun_counter=1
        self.poison_counter=0
    def is_alive(self):
        return self.hp>0

    def concussion_protocol(self):
        stun_check=random.randint(0,100)
        stun_chance=(.05*self.stun_counter)*100
        if (stun_chance>=stun_check):
            print("Your tackle has concussed your foe, inflicting a stun!")
            if (self.stun_counter<10):
                self.stun_counter+=1
            
        return stun_chance>=stun_check
        
    

class Teacher():
    def __init__(self, name, subject, hp, level):
        self.name=name
        self.subject=subject
        self.hp=hp
        self.level=level
        self.is_stunned=False

    def is_alive(self):
        return self.hp>0
   
    def basic_attack(self, level):
        return 3*level
        

class Smith(Teacher):
    def __init__(self):
        super().__init__(name="Mr. Smith", subject="Language", hp=300, level=3)
        

    def ruler(self):
        print("Mr. Smith strikes with his ruler!")
        damage=(2*self.level)
        if (player.evade==False):
            print("The ruler connects a stinging blow, dealing %s damage!"%(damage))
            return damage
        if (player.evade==True):
            print("You evade and the blow passes harmlessly.")
            return 0

    def poetry_book(self):
        print("Mr.Smith reads a Shakespearian poem from his book!")
        damage=self.level*3
        print("The poem's overly complex language hurts your ears, dealing %s damage!"%(damage))
        return damage


class Brandy(Teacher):
    def __init__(self):
        super().__init__(name="Mr. Brandy", subject="Math", hp=500, level=5)
        self.caffine=10
    


#boss combat behavior
def smith_boss_action(boss):
    boss_action=random.randint(0,2)        
    if (boss_action==2):
        atk_damage=Boss_Smith.poetry_book()
        return atk_damage
    else:
        atk_damage=Boss_Smith.ruler()
        return atk_damage

def brandy_boss_action(player, boss):
    boss_action=random.randint(-1,2)
    
    if (boss.caffine<=0):
        if (boss_action<=0):
            print("Mr. Brandy pulls out his darts, tossing one straight at you!")
            damage=0
            hit_count=0
            while (1==1):
                dart_accuracy=random.randint(0,2)
                if (dart_accuracy==0) or (player.evade==True):
                    print("The throw misses!")
                    break
                else:
                    if (hit_count>0):
                        print("Encouraged by the previous hit, Mr. Brandy throws again!")
                    hit_count+=1
                    hit_damage=round(((hit_count*boss.level)),0)
                    damage+=hit_damage
                    print("The dart lands, dealing %s damage!"%(hit_damage))                
            print("Total damage inflicted: %s"%(damage))
            return damage
        
        if (boss_action<2)and(boss_action>0):
            print("Mr. Brandy assigns a complicated set of math problems, due for a test grade.")
            damage=round(((boss.level*player.stress)*2,0))
            if (player.stress==0):
                print("Your lack of stress allows you to deal with the test without issue. You take no damage!")
            else:
                print("The stressful assignment gives you serious chest pain, inflicting %s damage!")
            player.stress+=3
            print("The test stressed you out! You gain 3 stress.")
            return damage
        
        if (boss_action==2):
            print("Mr. Brandy drinks a fresh Coffee, restoring himself.")
            damage=0
            boss.caffine=5
            boss.hp+=round((.1*(500-boss.hp)),0)
            return damage
    else:
        if (boss_action<=0):
            print("Mr. Brandy makes a sarcastic remark, its severity being related to his lack of coffee.")
            damage=(((boss.level*2)-boss.caffine)+1)
            print("The remark wounds your pride, dealing %s damage"%(damage))
            return damage
        if (boss_action==2):
            print("Mr. Brandy activates his Wax Melter!")
            print("A sickly-sweet scent fills the air. You feel relaxed, but the smell also makes you feel sick.")
            player.poison_counter=3
            if (player.stress>=2):
                player.stress= player.stress-2
            elif (player.stress==1):
                player.stress=player.stress-1
            return 0
        if (boss_action<2)and(boss_action>0):
            print("Mr. Brandy gives a complicated explanation to a simple question, leaving you feeling stressed and confused.")
            damage=round(((boss.level*boss.caffine)/player.intt),0)
            player.stress=player.stress+1
            return damage
            
    
#Combat Loops
def brandy_boss_fight(player,Boss_Brandy):
    print("You have entered class with Mr. Brandy!")
    print("----------------------------")
    print("")
    print("Mr. Brandy stands before you, a full cup of coffee in his hand.")
    i=1
    drink_effect_timer=0
    while (Boss_Brandy.is_alive()==True) and (player.is_alive()==True):
        playerturn=True
        Boss_Brandy.is_stunned==False            
        #player turn
        while (playerturn==True):
            fight_action=input(">>>What will you do?   ").lower()
                    
            print("")
                        
                            
            if (fight_action=="guidance"):
                print("You can 'attack', 'use skill', 'dodge' or 'flee'.")

            elif (fight_action=="attack"):
                damage = player_attack(player)
                Boss_Brandy.hp=Boss_Brandy.hp-damage
                if (player.club=='football'):
                    boss_stun=player.concussion_protocol()
                    Boss_Brandy.is_stunned=boss_stun
                playerturn=False

            elif (fight_action=="use skill"):
                damage = use_skill(player)
                Boss_Brandy.hp=Boss_Brandy.hp-damage
                if (player.club=='football'):
                    drink_effect_timer=3
                playerturn=False

            elif (fight_action=="dodge"):
                evade_check=random.randint(0,100)
                player.evade=bool(evade_check<=(10*player.speed))
                if (player.evade==True):
                    print("You will evade any physical attacks for this turn.")
                else:
                    print("Your evade fails!")
                playerturn=False

            elif (fight_action=="flee"):
                print("You turn and run, escaping narrowly.")
                playerturn=False
                        
            else:
                print("You can't do that.")
                            

        if (fight_action=="flee"):
            break

        #boss action
        print("")
        if (Boss_Brandy.is_alive()==True):
            if (Boss_Brandy.is_stunned==False):
                damage = brandy_boss_action(player,Boss_Brandy)
                damage=playerdamage(player,damage)
                player.hp=player.hp-damage
            else:
                print("Mr. Brandy is stunned, and cannot act!")
                Boss_Brandy.is_stunned=False
        else:
            break
        
        if (player.poison_counter>0):
            print("")
            print("You are poisoned!")
            poison_damage= round(((player.poison_counter*3)-(player.power/2)),0)
            damage=playerdamage(player,poison_damage)
            print("The poison inflicts %s damage!"%(damage))
            player.hp=player.hp-damage
            print("You now have %s health!"%(player.hp))
            player.poison_counter-=1
            if (player.poison_counter>0):
                print("You will be poisoned for %s more turns!"%(player.poison_counter))
            elif (player.poison_counter==0):
                print("The poison has worn off!")
        #drink checkup
        print('')
        if (drink_effect_timer>0):
            print("")
            playerheal(player,10)
            print("Your sports drink restores some health. Now have %s health."%player.hp)                       
            drink_effect_timer=drink_effect_timer-1
            if (drink_effect_timer==0):
                print("The effects of your drink have worn off!")
        print("")


        #round reset
        print("Round %s over! %s has %s health remaining! Mr. Brandy has %s health remaining!"%(i,player.name, player.hp, Boss_Brandy.hp))
        if (player.club=='nhs')or(player.stress>0):
            print("Your current stress level is %s."%(player.stress))
            if (player.stress>3):
                print("Your high stress begins to take its toll. You are stressed out!")
                stress_damage=round(((player.stress*(.05*player.maxhp))/2),0)
                #Stress-baseed damage resistance was too strong when applied to stressed out
                player.hp=player.hp-stress_damage
                print("You take %s damage from the stress!"%(stress_damage))
                print("You now have %s HP remaining."%(player.hp))
        i+=1
        if (Boss_Brandy.caffine>0):
            Boss_Brandy.caffine=Boss_Brandy.caffine-1
            print("Mr. Brandy's coffee runs lower. His caffine level is now %s."%(Boss_Brandy.caffine))
            if (Boss_Brandy.caffine==0):
                print("Mr. Brandy has run out of coffee!")
        print("")


    print("----------------------------")
    print("")
    print("The fight is over!")
    player.stress=0
    player.stun_counter=0
                
    if (Boss_Brandy.is_alive()==False):
        print("You defeated Mr. Brandy!")
        player.credit=player.credit+1
        print("You have earned 1 credit!")
    else:
        Boss_Brandy.hp=500

    
    return 0

def smith_boss_fight(player,Boss_Smith):
    print("You have entered class with Mr. Smith!")
    print("----------------------------")
    print("")
    print("Mr. Smith stands before you, brandishing a hardened ruler and a dictionary.")
    i=1
    drink_effect_timer=0
    while (Boss_Smith.is_alive()==True) and (player.is_alive()==True):
        playerturn=True
        Boss_Smith.is_stunned==False            
        #player turn
        while (playerturn==True):
            fight_action=input(">>>What will you do?   ").lower()
                    
            print("")
                        
                            
            if (fight_action=="guidance"):
                print("You can 'attack', 'use skill', 'dodge' or 'flee'.")

            elif (fight_action=="attack"):
                damage = player_attack(player)
                Boss_Smith.hp=Boss_Smith.hp-damage
                if (player.club=='football'):
                    boss_stun=player.concussion_protocol()
                    Boss_Smith.is_stunned=boss_stun
                playerturn=False

            elif (fight_action=="use skill"):
                damage = use_skill(player)
                Boss_Smith.hp=Boss_Smith.hp-damage
                if (player.club=='football'):
                    drink_effect_timer=3
                playerturn=False

            elif (fight_action=="dodge"):
                evade_check=random.randint(0,100)
                player.evade=bool(evade_check<=(10*player.speed))
                if (player.evade==True):
                    print("You will evade any physical attacks for this turn.")
                else:
                    print("Your evade fails!")
                playerturn=False

            elif (fight_action=="flee"):
                print("You turn and run, escaping narrowly.")
                playerturn=False
                        
            else:
                print("You can't do that.")
                            

        if (fight_action=="flee"):
            break

        #boss action
        print("")
        if (Boss_Smith.is_alive()==True):
            if (Boss_Smith.is_stunned==False):
                damage = smith_boss_action(Boss_Smith)
                damage=playerdamage(player,damage)
                player.hp=player.hp-damage
            else:
                print("Mr. Smith is stunned, and cannot act!")
        else:
            break
                    
        #drink checkup
        print('')
        if (drink_effect_timer>0):
            print("")
            playerheal(player,10)
            print("Your sports drink restores some health. Now have %s health."%player.hp)                       
            drink_effect_timer=drink_effect_timer-1
            if (drink_effect_timer==0):
                print("The effects of your drink have worn off!")
        print("")


        #round reset
        print("Round %s over! %s has %s health remaining! Mr. Smith has %s health remaining!"%(i,player.name, player.hp, Boss_Smith.hp))
        if (player.club=='nhs'):
            print("Your current stress level is %s."%(player.stress))
            if (player.stress>3):
                print("Your high stress begins to take its toll. You are stressed out!")
                stress_damage=round(((player.stress*(.05*player.maxhp))/2),0)
                #Stress-baseed damage resistance was too strong when applied to stressed out
                player.hp=player.hp-stress_damage
                print("You take %s damage from the stress!"%(stress_damage))
                print("You now have %s HP remaining."%(player.hp))
        i+=1
                    
                        
        print("")


    print("----------------------------")
    print("")
    print("The fight is over!")
    player.stress=0
    player.stun_counter=0
                
    if (Boss_Smith.is_alive()==False):
        print("You defeated Mr. Smith!")
        player.credit=player.credit+1
        print("You have earned 1 credit!")
    else:
        Boss_Smith.hp=300

    
    return 0
#player gameplay functions
def playerheal(player, heal):
    player.hp+=heal
    if player.hp>player.maxhp:
        player.hp=player.maxhp
    return 0

def playerdamage(player, damage):
    if (player.club=='nhs')and(player.stress>0):
        print("Your stress numbs you, reducing damage.")
        damage_reduction= damage*(.1*player.stress)
        damage=round(damage-damage_reduction,0)
        return damage
    else:
        return damage
        

def player_attack(player):
    if (player.club=='football'):
        print("You hit your foe with a heavy tackle!")
        damage = round(2*player.power,0)
        print("Your attack hit for %s damage!"%(damage))
        print("")
        return damage
        
    if (player.club=='track'):
        print("You hurl a discus at your foe!")
        damage = round(2.5*player.dex,0)
        print("The discus connects, dealing %s damage!"%(damage))
        print("")
        return damage
        
    if (player.club=='nhs'):
        print("You procrastinate, and the act causes chest pain in your foe.")
        damage = round(1.75*player.intt,0)
        player.stress+=1
        print("The chest pain inflicts %s damage, and your stress level has increased to %s."%(damage,player.stress))
        print("")
        return damage
    

def use_skill(player):
    if (player.club=='nhs'):
        while (1==1):
            nhs_skill_select=input("Do you want to use 'Time Management' or 'Burn Out'?  ").lower()
            
            
            if (nhs_skill_select=='time management'):
                print("You have employed 'Time management' and begin to feel relieved.")
                print("")
                missing_health=player.maxhp-player.hp
                heal=round(((.2*missing_health)*player.stress),0)
                playerheal(player,heal)
                print("With the effective use of your time, you have recovered to %s hp, and have relieved all stress!"%(player.hp))
                print("")
                player.stress=0
                return 0
                

            elif (nhs_skill_select=='burn out'):
                if (player.stress<3):
                    print("You aren't stressed enough for this yet.")
                    print("")
                    print("You have procrastinated instead.")
                    print("")
                    damage = player_attack(player)
                    return damage
                else:
                    print("Your stress overwhelms you, and you burn out in a fiery blast!")
                    damage=round((player.intt*(1.75**player.stress)),0)
                    print("The blast inflicts %s damage, and releases all of your stress."%(damage))
                    print("")
                    player.stress=0
                    return damage
            
            else:
                print('That is not an available skill.')

    elif (player.club=='football'):
        print("You have used the 'Energy Drink' skill!")
        print("")
        print("You drink a bottle of Croc-Aid, restoring your body.")
        print("")
        heal=10
        playerheal(player,heal)
        print("You gain %s health!"%(heal))
        print("")
        print("Your drink's effects will last for 3 more turns.")
        print("")
        return 0


    elif (player.club=='track'):
        print("You have used the 'Call Trainer' skill!")
        print("")
        print("The school trainer Rob comes and patches you up.")
        print("")
        missing_health=player.maxhp-player.hp
        heal=round((.75*missing_health),0)
        player.hp+=heal
        print("Rob heals you by %s hp, putting your current health at %s!"%(heal,player.hp))
        print("")
        return 0


        
#startup text/club selection
print("Welcome to the Gelbirt School!")
print("Today, we're going on an adventure!")
print("Before we begin, you'll have to answer a few questions for me.")

while (1==1):

    print("What is your name?")
    pname=input("My name is: ")

    print("You should sign up for a club. It'll help you out, trust me. You can join 'Football', 'Track', or 'NHS'.")
    pclub=input("I am going to join: ").lower()

    print("Your name is %s and you're going to join %s? Is this correct?"%(pname,pclub))
    intro_ask=input("Type 'yes' to proceed, or 'no' to go back:  ").lower()
    if (pclub=='nhs')or(pclub=='football')or(pclub=='track'):
        if (intro_ask=='yes'):
            break
    else:
        print("Invalid input. Please try again.")
    
print("----------------------------")
print("")
print("Welcome to your first day at Gelbirt, %s!"%(pname))
print("All you need to do to earn a diploma is defeat a teacher in each subject and earn their class credit!")
start=input("Are you ready? Good Luck!")

#boss initialization
Boss_Smith=Smith()
Boss_Brandy=Brandy()
#initializing player 
if (pclub=='football'):
    player=Player(name=pname,club='football',hp=100,power=7,speed=3,intt=2,dex=5)
if (pclub=='track'):
    player=Player(name=pname,club='track',hp=80,power=5,speed=8,intt=6,dex=7)
if (pclub=='nhs'):
    player=Player(name=pname,club='nhs',hp=60,power=2,speed=6,intt=9,dex=4)
#for guidance action
guidance_list={'go to the nurse':"Restore your health to max.",'go to class':"Enter combat with a teacher to earn credit",'inventory':"Prints out character details",'end game':"Stops the game.",'guidance':"Prints out available actions.",'explain stats':"Explains how each stat affects the game.",'check credit':"Shows how much credit you have. If you can graduate, you will be given the option to do so."}

#game loop
print("Type 'guidance' if you don't know what to do")
while player.is_alive():
    if (player.is_alive()==False):
        print("You have been defeated!")
        break
    print("----------------------------")
    print("")
    current_action=input("What do you want to do?   ").lower()


    if (current_action=="go to class"):

        class_select=str(input("""Which class would you like to attend?
        P1:English
        P2:Math
        Enter the period number of the class you would like to attend:  """)).lower()
        if (class_select=='1') or (class_select=='p1'):
            if (Boss_Smith.is_alive()==True):
                print("You enter your first period english class, taught by Mr. Smith.")

                enter_fight=input("Do you want to fight Mr. Smith for 1 credit?    ").lower()

                if (enter_fight=='yes'):
                    smith_boss_fight(player,Boss_Smith)
                else:
                    print("You return to the halls.")

            else:
                print("You have passed this class, no more credit can be earned.")

        if (class_select=='2') or (class_select=='p2'):
            if (Boss_Brandy.is_alive()==True):
                print("You enter your second period math class, taught by Mr. Brandy.")

                enter_fight=input("Do you want to fight Mr. Brandy for 1 credit?    ").lower()

                if (enter_fight=='yes'):
                    brandy_boss_fight(player,Boss_Brandy)
                else:
                    print("You return to the halls.")

            else:
                print("You have passed this class, no more credit can be earned.")

            
    elif (current_action=="inventory"):
        print("Your current health is %s out of a total health of %s"%(player.hp,player.maxhp))
        print("You are a member of %s"%(player.club))
        print("Your stats are:")
        print("Power:%s"%(player.power))
        print("Speed:%s"%(player.speed))
        print("Intellegence:%s"%(player.intt))
        print("Dexterity:%s"%(player.dex))
        
            

    elif (current_action=="end game"):
        break

    elif (current_action=='guidance'):
        print("Action: explanation")
        print("")
        for key, value in guidance_list.items():
            print("%s: %s"%(key,value))
    

    elif (current_action=="explain stats"):
        print("Stat explanation:")
        print("Power affects how much damage your physical attacks can do.")
        print("Speed affects your ability to dodge attacks.")
        print("Intelligence affects how much damage spells deal.")
        print("Dexterity affects the capablility of ranged attacks.")


    elif (current_action=="check credit"):
        print("You have %s credits."%(player.credit))
        if (player.credit>1):
            graduation_check=input("You have enough credit to graduate. Are you ready to graduate?   ").lower()
            if (graduation_check=='yes'):
                break

    elif (current_action=="go to the nurse"):
        print("")
        print("The school nurse gives you a cup of water, and it heals all of your wounds.")
        player.hp=player.maxhp

    else:
        print("That is not an available action.")

if (player.is_alive()==False):
    
    print("GAME OVER")

if (player.credit>1):
    print("Congratulations! You win!")

