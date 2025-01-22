from collections import Counter
import random

# Karten-Farben und Werte definieren
SUITS = {1: "Herz", 2: "Karo", 3: "Pik", 4: "Kreuz"}
VALUES = {2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11: "Bube", 12: "Dame", 13: "König", 14: "Ass"}

# Funktion, um zu prüfen, ob eine Hand eine Straight enthält
def is_straight(values):
    sorted_values = sorted(values)

    

# Funktion, um zu prüfen, ob eine Hand eine Flush enthält
def is_flush(suits):
    suit_counts = Counter(suits)
    return any(count >= 5 for count in suit_counts.values())

# Funktion, um Kartenwerte zu analysieren
def analyze_hand(cards):
    suits = [card // 100 for card in cards]
    values = [card % 100 for card in cards]

    # Prüfen auf Paare, Drillinge und Vierlinge
    value_counts = Counter(values)
    counts = list(value_counts.values())

    # Flush prüfen
    if is_flush(suits):
        return "Flush"

    # Straight prüfen
    if is_straight(values):
        return "Straight"

    # Full House prüfen
    if 3 in counts and 2 in counts:
        return "Full House"

    # Vierling prüfen
    if 4 in counts:
        return "Vierling"

    # Drilling prüfen
    if 3 in counts:
        return "Drilling"

    # Zwei Paare prüfen
    if counts.count(2) >= 2:
        return "Zwei Paare"

    # Ein Paar prüfen
    if 2 in counts:
        return "Ein Paar"

    return "Hohe Karte"

def random_c():
    card1 = int(f"{random.choice(list(SUITS))}{random.choice(list(VALUES))}")
    return card1
# Beispielkarten (Herz Bube, Pik 10, Karo 8, Herz Dame, Kreuz Ass, Herz 7, Pik 9)
karten = []
for i in range(0,6):
    karten.append(random_c())
print(karten)
ergebnis = analyze_hand(karten)
print(f"Die Pokerhand ist: {ergebnis}")
