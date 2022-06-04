import json
import random
bj_dict = {"jack" : 10, "queen" : 10, "king" : 10, "8" : 8, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" :7, "9" : 9, "10" : 10 }
with open("money.json", "w") as wf:
    json.dump({'money' : random.randint(100, 10000)}, wf)
def robot():
    pick1 = random.choice([[15, 16, 17], [18, 19, 20, 21]])
    return random.choice(pick1)
def player():
    pick = random.sample(list(bj_dict.keys()), 2)
    final = sum([bj_dict[a] for a in pick])
    return [final, pick]
def blackjack():
    with open("money.json", "r") as rf:
        money = json.load(rf)['money']

    opponent = robot()
    print(f"You have ${money}")
    bet_amount = int(input("Enter how much you would like to bet>"))
    if bet_amount < money:
        me = player()
        final = me[0]
        print(f"Cards : {me[1]}\nTotal is {final}")
        while True:
            des = str(input("Would you like to draw another card <y> or stand <s>?"))
            if des == "y":
                final += random.choice([bj_dict[g] for g in bj_dict.keys()])
                print(f"Your new total is {final}")
                if final > 21:
                    with open("money.json", "w") as wf:
                        json.dump({'money': money - bet_amount}, wf)
                    print(f'YOU LOSE!!! You got more than 21!!!\nYou have {money - bet_amount} money left!')
                    break
                elif final == 21:
                    print("YOU WIN!!!\nYou got 21!!!")
                    break
            elif des == "s":
                if final > 10:
                    if final < opponent:
                        print(f'Jerry had {opponent}')
                        print(f"YOU LOSE!!!\nYou have ${money - bet_amount}")
                        with open("money.json", "w") as wf:
                            json.dump({'money' : money - bet_amount}, wf)
                        break
                    else:
                        print(f"You win!!!\nYou have ${money + bet_amount}")
                        print(f'Jerry had {opponent}')
                        with open("money.json", "w") as wf:
                            json.dump({'money' : money + bet_amount}, wf)
                else:
                    print("You lose!")
                return
    else:
        print("You don't have enough money!!!")
while True:
    blackjack()

