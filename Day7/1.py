input_file = open('1.txt', 'r')

hands = []

FIVE_KIND = 7
FOUR_KIND = 6
FULL_HOUSE = 5
THREE_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
ONE = 1

CARDS_VALUES = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def get_hand_type(hand_dic:dict):
    card_types = len(hand_dic.keys())
    if card_types == 1:
        return FIVE_KIND
    elif card_types == 2:
        v1, v2 = hand_dic.values()
        if v1 == 4 or v2 == 4:
            return FOUR_KIND
        else:
            return FULL_HOUSE
    elif card_types == 3:
        v1, v2, v3 = hand_dic.values()
        if v1 == 3 or v2 == 3 or v3 == 3:
            return THREE_KIND
        else:
            return TWO_PAIR
    elif card_types == 4:
        return ONE_PAIR    
    else:
        return ONE

def hand_to_dic(hand):
    hand_dic = {}
    for c in list(hand):
        hand_dic[c] = hand_dic.get(c,0)+1
    return hand_dic

def key_hand(hand1):
    cards1_type = get_hand_type(hand_to_dic(hand1[0]))
    map(lambda c: c, list(hand1[0]))
    return (cards1_type, list(map(lambda c: CARDS_VALUES.index(c), list(hand1[0]))))
    

while True:
    line = input_file.readline().strip()
    if not line:
        break
    cards, bid = line.split()
    hands.append((cards, int(bid)))


hands.sort(key=key_hand)
print(hands)

bid_sum = 0
for rank,h in enumerate(hands,1):
    bid_sum += h[1]* rank
print(bid_sum)
