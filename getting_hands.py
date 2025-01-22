import random
colors = [1,2,3,4]
numbers = list(range(2,15))
ac = []
for i in colors:
    for u in numbers:
        ac.append(int(f"{i}{u}"))
    

def is_straight(cards):
    cds = {}
    for ca in cards:
        if ca < 100:
            co = int(ca/10)
            nu = str(ca/10).split(".")[1]
        else:
            co = int(ca/100)
            nu = str(ca/100).split(".")[1]
        
        if nu == "1":
                nu = 10 
        cds[ca] = (co,int(nu))
    cols = []
    vals = []
    for i in cds:
        cols.append(cds[i][0])
        vals.append(cds[i][1])
    res = []
    for val in vals:
        if val not in res:
            res.append(val)
    sorted_v = sorted(res)
    vals = sorted_v
    print("t",vals)
    current_streak = 1
    streak_length = 5
    for i in vals:
        if i == vals[vals.index(i)-1]+1:
            current_streak += 1
            if current_streak >= streak_length:
                return True
        else:
            current_streak = 1
    return False
def is_flush(cards):
    pass
def random_c():
    return ac.pop(random.randint(0,len(ac)-1))

def readable_c(ca):
    if ca < 100:
        co = int(ca/10)
        nu = str(ca/10).split(".")[1]
    else:
        co = int(ca/100)
        nu = str(ca/100).split(".")[1]
    
    if nu == "1":
            nu = "10"
    rc = ""
    if co == 1:
        rc += "💎"
    if co == 2:
        rc += "❤️"
    if co == 3:
        rc += "🍁"
    if co == 4:
        rc += "☘️"
    rc += f" {str(nu)}"
    return rc


karten = []
for i in range(0,7):
    karten.append(random_c())
for i in karten:
    print(f"{i}:{readable_c(i)}")
print(is_straight(karten))