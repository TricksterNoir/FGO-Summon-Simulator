import secrets
import json  

def sort_rarity(amount):
    summon_list = []
    if amount == 1:
        summon_list.append(secrets.randbelow(100))
    else:
        for i in range(1, 11):
            summon_list.append(secrets.randbelow(100)+1)
    
    return summon_list

def sort_summon_one(rarity):
    rarity_sorted = sort_rarity(1)
    selected_summon = ""

    if rarity == 1:
        five_star_servant_list = '5s_Servants.json'
        with open(five_star_servant_list, 'r') as five_star_list:
            five_star = json.load(five_star_list)

        sort_servant = secrets.randbelow(len(five_star))
        selected_servant = five_star[sort_servant]['Name']

        selected_summon = selected_servant

    elif rarity in range(2,6):
        five_star_ce_list = '5s_ce.json'
        with open(five_star_ce_list, 'r') as five_star_list:
            five_star = json.load(five_star_list)
        
        sort_ce = secrets.randbelow(len(five_star))
        selected_ce = five_star[sort_ce]['Name']
        selected_summon = selected_ce

    elif rarity in range(6,9):
        four_star_servant_list = '4s_Servants.json'
        with open(four_star_servant_list, 'r') as four_star_list:
            four_star = json.load(four_star_list)
        
        sort_servant = secrets.randbelow(len(four_star))
        selected_servant = four_star[sort_servant]['Name']
        selected_summon = selected_servant

    elif rarity in range(9,21):
        four_star_ce_list = '4s_ce.json'
        with open(four_star_ce_list, 'r') as four_star_list:
            four_star = json.load(four_star_list)
        
        sort_ce = secrets.randbelow(len(four_star))
        selected_ce = four_star[sort_ce]['Name']
        selected_summon = selected_ce
        
    elif rarity > 20 and rarity % 2 == 1 and rarity < 101:
        three_star_servant_list = '3s_Servants.json'
        with open(three_star_servant_list, 'r') as three_star_list:
            three_star = json.load(three_star_list)
        
        sort_servant = secrets.randbelow(len(three_star))
        selected_servant = three_star[sort_servant]['Name']
        selected_summon = selected_servant

    elif rarity > 20 and rarity % 2 == 0 and rarity < 101:
        three_star_ce_list = '3s_ce.json'
        with open(three_star_ce_list, 'r') as three_star_list:
            three_star = json.load(three_star_list)
        
        sort_ce = secrets.randbelow(len(three_star))
        selected_ce = three_star[sort_ce]['Name']
        selected_summon = selected_ce

    return selected_summon

teste = sort_summon_one(22)