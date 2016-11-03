# Project Euler Problem 54: Poker Hands
# Author: Kavin Subramanyam
# Notes: Fuck this problem.

import collections

suitmap = {
	'C': 0,
	'D': 1,
	'H': 2,
	'S': 3
}

valuemap = {
	'2': 0,
	'3': 1,
	'4': 2,
	'5': 3,
	'6': 4,
	'7': 5,
	'8': 6,
	'9': 7,
	'T': 8,
	'J': 9,
	'Q': 10,
	'K': 11,
	'A': 12
}

handmap = {
	'HC': 0,
	'OP': 1,
	'TP': 2,
	'TOF': 3,
	'S': 4,
	'F': 5,
	'FH': 6,
	'FOF': 7,
	'SF': 8,
	'RF': 9
}

def enumerate(card):
	return valuemap[card[:-1]] + suitmap[card[-1]] * 13

def enumerate_hand(hand):
	return sorted([enumerate(card) for card in hand])

def get_suit(card):
	return card//13

def get_value(card):
	return card % 13

def get_suits(cards):
	return sorted([get_suit(card) for card in cards])

def get_values(cards):
	return sorted([get_value(card) for card in cards])

def is_royal_flush(hand):
	cards = enumerate_hand(hand)
	if get_value(cards[0]) == 8:
		expected_suits = [get_suit(cards[0]) for i in range(5)]
		expected_values = [8, 9, 10, 11, 12]
		return get_suits(cards) == expected_suits and get_values(cards) == expected_values
	else:
		return False

def is_straight_flush(hand):
	cards = enumerate_hand(hand)
	suit_count = len(set(get_suits(cards)))
	for i in range(4):
		if get_value(cards[i]) + 1 != get_value(cards[i + 1]):
			return False
	return suit_count == 1

# Returns boolean, card value
def is_four_of_kind(hand):
	cards = enumerate_hand(hand)
	values = get_values(cards)

	counter = collections.Counter(values)
	most_common = counter.most_common(1)
	if most_common[0][1] == 4:
		return (True, most_common[0][0])
	else:
		return (False, -1)

# Returns boolean, three of kind value, pair value
def is_full_house(hand):
	cards = enumerate_hand(hand)
	values = get_values(cards)

	counter = collections.Counter(values)
	most_common = counter.most_common(2)
	if most_common[0][1] == 3 and most_common[1][1] == 2:
		return (True, most_common[0][0], most_common[1][0])
	else:
		return (False, -1, -1)

def is_flush(hand):
	cards = enumerate_hand(hand)
	return len(set(get_suits(cards))) == 1

def is_straight(hand):
	cards = enumerate_hand(hand)
	values = get_values(cards)
	for i in range(4):
		if values[i] + 1 != values[i + 1]:
			return False
	return True

# Return boolean, card value
def is_three_of_kind(hand):
	cards = enumerate_hand(hand)
	values = get_values(cards)

	counter = collections.Counter(values)
	most_common = counter.most_common(1)
	if most_common[0][1] == 3:
		return (True, most_common[0][0])
	else:
		return (False, -1)

# Return boolean, first pair card value, second pair card value
def is_two_pairs(hand):
	cards = enumerate_hand(hand)
	values = get_values(cards)

	counter = collections.Counter(values)
	most_common = counter.most_common(2)
	if most_common[0][1] == 2 and most_common[1][1] == 2:
		pairs = sorted([most_common[0][0], most_common[1][0]])
		return (True, pairs[0], pairs[1])
		return True
	else:
		return (False, -1, -1)

# Return boolean, pair value
def is_pair(hand):
	cards = enumerate_hand(hand)
	values = get_values(cards)

	counter = collections.Counter(values)
	most_common = counter.most_common(1)
	if most_common[0][1] == 2:
		return (True, most_common[0][0])
	else:
		return (False, -1)

def highest_card(hand):
	cards = enumerate_hand(hand)
	values = get_values(cards)
	return values[-1]

# Returns True if player one wins
def compare_hands(game):
	cards = game.split(' ')
	p1_hand = cards[:5]
	p2_hand = cards[5:]

	hands = []

	for hand in p1_hand, p2_hand:
		if is_royal_flush(hand):
			hands.append('RF')
		elif is_straight_flush(hand):
			hands.append('SF')
		elif is_four_of_kind(hand)[0]:
			hands.append('FOF')
		elif is_full_house(hand)[0]:
			hands.append('FH')
		elif is_flush(hand):
			hands.append('F')
		elif is_straight(hand):
			hands.append('S')
		elif is_three_of_kind(hand)[0]:
			hands.append('TOF')
		elif is_two_pairs(hand)[0]:
			hands.append('TP')
		elif is_pair(hand)[0]:
			hands.append('OP')
		else:
			hands.append('HC')
	
	if hands[0] == hands[1]:
		# Royal Flush ties not possible? Since suit is not accounted for
		# Straight Flush, Straight Tie, just check each card is highest for player 1
		if hands[0] == 'SF' or hands[0] == 'S':
			return get_values(enumerate_hand(p1_hand)) > get_values(enumerate_hand(p2_hand))
		elif hands[0] == 'FOF': # Four of a kind tie, just check that player 1 has the larger card of count 4
			p1_card = is_four_of_kind(p1_hand)[1]
			p2_card = is_four_of_kind(p2_hand)[1]
			return p1_card > p2_card
		elif hands[0] == 'FH': # Check three of kind values
			p1_cards = is_full_house(p1_hand)
			p2_cards = is_full_house(p2_hand)
			return p1_cards[1] > p2_cards[1]
		elif hands[0] == 'F': # Flush tie, just compare off highest cards
			p1_cards = get_values(enumerate_hand(p1_hand))
			p2_cards = get_values(enumerate_hand(p2_hand))
			return p1_cards > p2_cards
		elif hands[0] == 'TOF':
			p1_card = is_three_of_kind(p1_hand)[1]
			p2_card = is_three_of_kind(p2_hand)[1]
			return p1_card > p2_card
		elif hands[0] == 'TP':
			p1_cards = sorted(is_two_pairs(p1_hand)[1:], reverse=True)
			p2_cards = sorted(is_two_pairs(p2_hand)[1:], reverse=True)
			if p1_cards[0] == p2_cards[0]:
				if p1_cards[1] == p2_cards[1]:
					return highest_card(p1_hand) > highest_card(p2_hand)
				else:
					return p1_cards[1] > p2_cards[1]
			else:
				return p1_cards[0] > p2_cards[0]
		elif hands[0] == 'OP':
			p1_card = is_pair(p1_hand)[1]
			p2_card = is_pair(p2_hand)[1]
			if p1_card == p2_card:
				return sorted(get_values(enumerate_hand(p1_hand)), reverse=True) > sorted(get_values(enumerate_hand(p2_hand)), reverse=True)
			else:
				return p1_card > p2_card
		else:
			return sorted(get_values(enumerate_hand(p1_hand)), reverse=True) > sorted(get_values(enumerate_hand(p2_hand)), reverse=True)
	else:
		return handmap[hands[0]] > handmap[hands[1]]

if __name__ == '__main__':
	# royal_flush = ['TC', 'JC', 'QC', 'KC', 'AC']
	# straight_flush = ['2S', '3S', '4S', '5S', '6S']
	# four_of_kind = ['2C', '2D', '2H', '2S', '4D']
	# full_house = ['2H', '2D', '4C', '4D', '4S']
	# flush = ['3D', '6D', '7D', 'TD', 'QD']
	# straight = ['4D', '5S', '6C', '7C', '8S']
	# three_of_kind = ['3C', '3D', '3H', '5S', '6C']
	# two_pairs = ['3C', '3D', '4D', '4S', 'AC']
	# pair = ['3C', '3D', '4S', '5S', '6S']
	filename = 'poker.txt'
	wincount = 0
	with open(filename, 'r') as games:
		while True:
			game = games.readline()
			if game == '':
				break
			result = compare_hands(game.strip())
			if result:
				wincount += 1
	print(wincount)
