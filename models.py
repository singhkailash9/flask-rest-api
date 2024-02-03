import json

def load_data(file):
    with open(file, 'r') as f:
        return json.load(f)

def save_cards(cards):
    with open('cards.json', 'w') as f:
        json.dump(cards, f)
