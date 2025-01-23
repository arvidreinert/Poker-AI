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
    cols = []
    for ca in cards:
        if ca < 100:
            co = int(ca/10)
        else:
            co = int(ca/100)
        cols.append(co)
    counters = {1:0,2:0,3:0,4:0}
    for i in cols:
        counters[i] += 1
    for i in counters:
        if counters[i] >= 5:
            return True
    return False
def get_matching(cards):
    cds = {}
    tre = 0
    pairs = 0
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
    vals_dict = {}
    for i in vals:
        vals_dict[i]=0
    for i in vals:
        vals_dict[i] += 1
    for i in vals_dict:
        if vals_dict[i] == 2:
            pairs += 1
        if vals_dict[i] == 3:
            tre += 1
    print(pairs,tre)
    if pairs >= 1 and tre >= 1:
        return "fullhouse"
    if tre == 1:
        return "three"
    if pairs == 1:
        return "1pair"
    if pairs == 2:
        return "2pair"
    return "highcard"
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

def check_hands(cards):
    pass

karten = []
for i in range(0,7):
    karten.append(random_c())
for i in karten:
    print(f"{i}:{readable_c(i)}")
print(get_matching(karten))