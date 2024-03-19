import discord
import random 
import json
import pandas as pd
from typing import Dict, List, Union, Any

def read_money_json() -> Dict[str, int]:
    """
    Reads the money.json file and returns it as a dictionary.
    """
    with open("money.json", "r") as file:
        balance_dictionary = json.load(file)
    return balance_dictionary

def write_money_json(balance_dict: dict) -> None:
    """
    Writes the money.json file with the given dictionary
    """
    with open("money.json", "w") as file:
        json.dump(balance_dict, file, indent = 4, sort_keys=True)

def  get_balance(user_id: int) -> int:
    """
    Gets the balance of a user.
    """
    ensure_user_exists(user_id=user_id)
    balance_dictionary = read_money_json()
    money = balance_dictionary.get(str(user_id))
    return money

def ensure_user_exists(user_id: int) -> Dict[str, int]:
    """
    Ensures that a user exists in the money.json file
    """
    balance_dictionary = read_money_json()
    if str(user_id) not in balance_dictionary:
        balance_dictionary[str(user_id)] = 10_000
        write_money_json(balance_dict=balance_dictionary)
    return balance_dictionary

def give_money(user_id: int, amount: int) -> None:
    """
    Gives a user money.
    """
    balance_dictionary = ensure_user_exists(user_id=user_id)
    balance_dictionary[str(user_id)] += amount
    write_money_json(balance_dict=balance_dictionary)

def take_money(user_id: int, amount: int) -> bool:
    """
    Take money ahhahahahsahahsa
    """
    balance_dictionary = ensure_user_exists(user_id=user_id)
    balance = balance_dictionary.get(str(user_id))
    if balance >= amount:
        balance_dictionary[str(user_id)] -= amount
        write_money_json(balance_dict=balance_dictionary)
        return True
    else:
        return False

def work(user_id: int) -> str:
    with open("work.json", "r") as file:
        work_dictionary = json.load(file)
    if str(user_id) not in work_dictionary:
        work_dictionary[str(user_id)] = "1970-01-01 00:00:00-00:00"
    current_time = pd.Timestamp.now(tz="US/Pacific")
    last_worked = pd.Timestamp(work_dictionary[str(user_id)])
    print(current_time, last_worked)
    if current_time - last_worked > pd.Timedelta(hours=12):
        work_dictionary[str(user_id)] = str(current_time)
        with open("work.json", "w") as file:
            json.dump(work_dictionary, file, indent=4, sort_keys=True)
        money = random.randint(1500, 2000)
        give_money(user_id, money)
        return f"got {money} moneys"
    else:
        return "worked too soon"
    

slot_symbols = ["🍒", "🍊", "🍋", "🍇", "🍓", "💰"]

prize_map = {
    "🍒": 3,
    "🍊": 5,
    "🍋": 7,
    "🍇": 10,
    "🍓": 15,
    "💰": 55,
}
probabilities = [
    0.4,
    0.15,
    0.25,
    0.1,
    0.05,
    0.05
]


def slot_machine(user_id: int, rolls: int):
    user_balance = get_balance(user_id=user_id)
    money_spent = rolls * 25
    if user_balance < money_spent:
        return "User is  too poor."

    if rolls <= 1000 and rolls > 0:
        total_value = 0
        value = 0
        take_money(user_id=user_id, amount=money_spent)
        for i in range(rolls):
            picks = random.choices(slot_symbols, weights=probabilities, k=3)
            for thing in picks:
                value += prize_map[thing]

            if picks[0] == picks[1] and picks[1] == picks[2]:
                value = value * 2
            
            total_value += value
            value = 0
        give_money(user_id=user_id, amount=total_value)

        return f" You got: \n {picks} \n worth {total_value} dollars. \n Spent {money_spent} dollars. \n Net gain/loss is {total_value - money_spent}"
    return "Number of rolls must be 1-1000."



if __name__ == "__main__":
    print(work(111))