from base import *

from functools import cmp_to_key


labels = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def isFiveOfKind(string, jokers):
	if jokers >= 4:
		return True

	first = string[0]
	if string.count(first) + jokers == 5:
		return True

def isFourOfKind(string, jokers):
	if jokers >= 3:
		return True
   
	first = string[0]
	second = string[1]
	if string.count(first) + jokers == 4 or string.count(second) + jokers == 4:
		return True
	return False

def isFullHouse(string, jokers):
	if string.count(string[0]) + jokers == 3 and string.count(string[-1]) == 2:
		return True
	return False

def isThreeOfAKind(string, jokers):
	if jokers == 2:
		return True

	if string.count(string[0]) + jokers == 3:
		return True
	return False

def isTwoPair(string, jokers):
	if string.count(string[0]) == 2 and string.count(string[2]) == 2:
		return True
	return False

def isOnePair(string, jokers):
	if jokers == 1:
		return True
	if string.count(string[0]) == 2:
		return True

def findType(string):
	jokers = string.count("J")
	string = string.replace("J", "")

	if isFiveOfKind(string, jokers):
		return 6
	elif isFourOfKind(string, jokers):
		return 5
	elif isFullHouse(string, jokers):
		return 4
	elif isThreeOfAKind(string, jokers):
		return 3
	elif isTwoPair(string, jokers):
		return 2
	elif isOnePair(string, jokers):
		return 1
	return 0

def reorder_string(s):
    jokers = s.count("J")
    s = s.replace("J", "")

    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    sorted_chars = sorted(counts, key=lambda x: counts[x], reverse=True)
    reordered_str = ''.join([c * counts[c] for c in sorted_chars])
    
    return reordered_str + ("J" * jokers)

def _sort(a,b):
	aType = findType(reorder_string(a[0]))
	bType = findType(reorder_string(b[0]))
	if(aType > bType):
		return 1
	elif (bType > aType):
		return -1

	for i in range(0, 5):
		aIdx = labels.index(a[0][i])
		bIdx = labels.index(b[0][i])
		if(aIdx < bIdx):
			return 1
		elif (aIdx > bIdx):
			return -1

	return 0

def process(i, line):
  cards, bid = line.split()
  bid = int(bid)
  return cards, bid

def final(results: list):
    cmp_items = cmp_to_key(_sort)
    results.sort(key = cmp_items)

    sum = 0
    for i, card_bid in enumerate(results):
        sum += (i + 1) * card_bid[1]
        
    return sum


print(
    do_func_for_each_line_in_file(
        f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
        process,
        final,
    )
)
