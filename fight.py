from gladiator import Gladiator
import time
import random

name = input("What is your gladiator's name?\n").capitalize()
time.sleep(1)
weapons = input("""
Choose your weapon:
Sword (damage: 10-12)
Dagger (damage: 5-8)
Spear (damage: 2-4)
Bow and Arrow (damage: 10-15)
""")
if weapons == 'Sword':
    low = 10
    high = 12
elif weapons == 'Dagger':
    low = 5
    high = 8
elif weapons == 'Spear':
    low = 2
    high = 4
elif weapons == 'Bow and Arrow':
    low = 10
    high = 15
time.sleep(2)
glad = Gladiator(name, 100, 0, low, high)

opponents = ['Dustin', 'Ricky', 'Addey', 'James H', 'Onna', 'Martin', 'Keegan',
             'James S', 'Adam', 'Jacob', 'Eddrick', 'Nicole', 'Nate', 'Sean']
opponent = opponents[random.choice(range(len(opponents) - 1))]
print('Your opponent is', opponent)
time.sleep(1)
weapon = [['Sword', 'low = 10', 'high = 12'],
          ['Dagger', 'low = 5', 'high = 8'], ['Spear', 'low = 2', 'high = 4'],
          ['Bow and Arrow', 'low = 10', 'high = 15']]
weapon2 = weapon[random.choice(range(len(weapon)))]
print('Your opponents weapon is', weapon2)
time.sleep(2)
print('This is a battle to the death!')
time.sleep(2)
print('May the best gladiator win!')
time.sleep(2)
print('Battle begins in....')
time.sleep(2)
print(""">===>>=====> >=>    >=> >======>     >=======> >=======>
     >=>     >=>    >=> >=>    >=>   >=>       >=>
     >=>     >=>    >=> >=>    >=>   >=>       >=>
     >=>     >=====>>=> >> >==>      >=====>   >=====>
     >=>     >=>    >=> >=>  >=>     >=>       >=>
     >=>     >=>    >=> >=>    >=>   >=>       >=>
     >=>     >=>    >=> >=>      >=> >=======> >=======> """)
time.sleep(2)
print(""">===>>=====> >=>        >=>     >===>
     >=>     >=>        >=>   >=>    >=>
     >=>     >=>   >>   >=> >=>        >=>
     >=>     >=>  >=>   >=> >=>        >=>
     >=>     >=> >> >=> >=> >=>        >=>
     >=>     >> >>    >===>   >=>     >=>
     >=>     >=>        >=>     >===>      """)
time.sleep(2)
print("""    >===>      >==>    >=> >=======>
  >=>    >=>   >> >=>  >=> >=>
>=>        >=> >=> >=> >=> >=>
>=>        >=> >=>  >=>>=> >=====>
>=>        >=> >=>   > >=> >=>
  >=>     >=>  >=>    >>=> >=>
    >===>      >=>     >=> >=======>""")
print(""" (     (                )
 )\ )  )\ )  (       ( /(   *   )
(()/( (()/(  )\ )    )\())` )  /(
 /(_)) /(_))(()/(   ((_)\  ( )(_))
(_))_|(_))   /(_))_  _((_)(_(_())
| |_  |_ _| (_)) __|| || ||_   _|
| __|  | |    | (_ || __ |  | |
|_|   |___|    \___||_||_|  |_|  """)
time.sleep(2)
glad2 = Gladiator(opponent, 100, 0, low, high)


def fight(glad, glad2):
    """ (Gladiator) -> int
    """

    while True:
        option = input('Would you like to attack or heal?\n')
        dead = glad.is_dead(glad2)
        time.sleep(1)
        if dead == 'You are dead...':
            status = 'LOST'
            opp_stat = 'WON'
            break
        elif dead == 'Opponent is dead...':
            status = 'WON'
            opp_stat = 'LOST'
            break
        if option == 'attack':
            print(glad2.attack(glad))
            print(glad.attack(glad2))
        elif option == 'heal':
            glad.heal()
        print(repr(glad), repr(glad2))


fight(glad, glad2)
dead = glad.is_dead(glad2)
if dead == 'You are dead...':
    print(dead)
    status = 'LOST'
    opp_stat = 'WON'
elif dead == 'Opponent is dead...':
    print(dead)
    status = 'WON'
    opp_stat = 'LOST'

print('''
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░
░ ░   ░   ░   ▒   ░      ░      ░
      ░       ░  ░       ░      ░  ░
 ▒█████   ██▒   █▓▓█████  ██▀███   ▐██▌
▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒ ▐██▌
▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒ ▐██▌
▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄   ▓██▒
░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒ ▒▄▄
░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░ ░▀▀▒
  ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░ ░  ░
░ ░ ░ ▒       ░░     ░     ░░   ░     ░
    ░ ░        ░     ░  ░   ░      ░
              ░                       ''')

print('Player 1:', name, status)
print('Player 2:', opponent, opp_stat)
