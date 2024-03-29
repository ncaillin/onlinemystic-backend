import random
import json

def get_reading():
    
    with open('files/major_arcana_readings.json') as file:
        data = json.load(file)
    
    card_list = list(data["readings"])

    readings_list = random.sample(card_list, 3)
    output = []
    for card in readings_list:
        reversed = random.randint(0, 1)
        if reversed == 1:
            output.append({"name": card, "reversed": True, "meaning": data["readings"][card]["reversed"]})
        elif reversed == 0:
            output.append({"name": card, "reversed": False, "meaning": data["readings"][card]["normal"]})
    
    return(str(output))


def get_reading_cards(request): 
    with open('files/major_arcana_readings.json') as file:
        data = json.load(file)
    
    card_list = list(data["readings"])

    if request.method == "POST":
        cards = json.loads(request.body)['data']
        output = []
        for card in cards:
            if card["reversed"] == True:
                output.append({"name": card["name"], "reversed": True, "meaning": data["readings"][card["name"]]["reversed"]})
            elif card["reversed"] == False:
                output.append({"name": card["name"], "reversed": False, "meaning": data["readings"][card["name"]]["normal"]})

        return(str(output))