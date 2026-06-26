"""
   Introduction
Slot machine (American English), informally fruit machine (British English), puggy (Scottish English slang), the slots
(Canadian and American English), poker machine (or pokies in slang) (Australian English and New Zealand English) or simply slot
(American English), is a casino gambling machine with three or more reels which spin when a button is pushed. Slot machines are
also known as one-armed bandits because they were originally operated by one lever on the side of the machine as distinct from a
button on the front panel, and because of their ability to leave the player in debt and impoverished. Many modern machines are still
equipped with a legacy lever in addition to the button. (Source Wikipedia)

Task
You will be given three reels of different images and told at which index the reels stop. From this information your job is to return
the score of the resulted reels.

Rules
1. There are always exactly three reels
2. Each reel has 10 different items.
3. The three reel inputs may be different.
4. The spin array represents the index of where the reels finish.
5. The three spin inputs may be different
6. Three of the same is worth more than two of the same
7. Two of the same plus one "Wild" is double the score.
8. No matching items returns 0.

Item     |  3  same  |  2  same  | 2 same + Wild
----------------------------------------------------
Wild     |    100    |     10    |      N/A
Star     |     90    |      9    |       18
Bell     |     80    |      8    |       16
Shell    |     70    |      7    |       14
Seven    |     60    |      6    |       12
Cherry   |     50    |      5    |       10
Bar      |     40    |      4    |        8
King     |     30    |      3    |        6
Queen    |     20    |      2    |        4
Jack     |     10    |      1    |        2

Returns
Return an integer of the score.

Example

reel1 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
reel2 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
reel3 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
spin = [5,5,5]
result = fruit([reel1,reel2,reel3],spin)
Scoring
reel1[5] == "Cherry"
reel2[5] == "Cherry"
reel3[5] == "Cherry"

Cherry + Cherry + Cherry == 50
Return
result == 50
"""
THREE_SAME = 3
TWO_SAME = 2
TWO_SAME_AND_WILD = 1
WILD = "Wild"

VALUES = {
    "Wild": [100, 10, 0],
    "Star": [90, 9, 18],
    "Bell": [80, 8, 16],
    "Shell": [70, 7, 14],
    "Seven": [60, 6, 12],
    "Cherry": [50, 5, 10],
    "Bar": [40, 4, 8],
    "King": [30, 3, 6],
    "Queen": [20, 2, 4],
    "Jack": [10, 1, 2],
}


def fruit(reels, spin):
    return get_score_result(get_spin_result(reels, spin))

def get_spin_result(reels, spin):
    spin_result = []
    for reel, index in zip(reels, spin):
        spin_result.append(reel[index])
    return spin_result

def wild_score(spin_result):
    return VALUES[WILD][0] if len(spin_result) == 0 else VALUES[WILD][1]

def get_score(spin_result):
    if len(spin_result) == 2:
        return VALUES[spin_result[0]][2] if spin_result[0] == spin_result[1] else 0
    
    if spin_result[0] == spin_result[1] and spin_result[1] == spin_result[2] :
        return VALUES[spin_result[0]][0]
    
    if spin_result[0] == spin_result[1] or spin_result[0] == spin_result[2]:
        return VALUES[spin_result[0]][1]
    
    return VALUES[spin_result[1]][1]
        
def get_score_result(spin_result):
    spin_result = [x for x in spin_result if x != "Wild"]
    return wild_score(spin_result) if len(spin_result) <= 1 else get_score(spin_result)

reel1 = [
    "Wild",
    "Star",
    "Bell",
    "Shell",
    "Seven",
    "Cherry",
    "Bar",
    "King",
    "Queen",
    "Jack",
]
reel2 = [
    "Wild",
    "Star",
    "Bell",
    "Shell",
    "Seven",
    "Cherry",
    "Bar",
    "King",
    "Queen",
    "Jack",
]
reel3 = [
    "Wild",
    "Star",
    "Bell",
    "Shell",
    "Seven",
    "Cherry",
    "Bar",
    "King",
    "Queen",
    "Jack",
]

spin = [0, 5, 5]

result = fruit([reel1, reel2, reel3], spin)

print(result)
