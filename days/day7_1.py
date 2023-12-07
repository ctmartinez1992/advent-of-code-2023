from base import *

from functools import cmp_to_key


labels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def isFiveOfKind(string):
  first = string[0]
  if string.count(first) == 5:
    return True

def isFourOfKind(string):
  first = string[0]
  second = string[1]
  if string.count(first) == 4 or string.count(second) == 4:
    return True
  return False

def isFullHouse(string):
  if string.count(string[0]) == 3 and string.count(string[3]) == 2:
    return True
  return False

def isThreeOfAKind(string):
  if string.count(string[0]) == 3: return True
  return False

def isTwoPair(string):
  if string.count(string[0]) == 2 and string.count(string[2]) == 2:
    return True
  return False

def isOnePair(string):
  if string.count(string[0]) == 2:
    return True

def findType(string):
  if isFiveOfKind(string):
    return 6
  elif isFourOfKind(string):
    return 5
  elif isFullHouse(string):
    return 4
  elif isThreeOfAKind(string):
    return 3
  elif isTwoPair(string):
    return 2
  elif isOnePair(string):
    return 1
  return 0

def reorder_string(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
        sorted_chars = sorted(counts, key=lambda x: counts[x], reverse=True)
        reordered_str = ''.join([c * counts[c] for c in sorted_chars])
    return reordered_str

def _sort(a,b):
  aType = findType(reorder_string(a[0]))
  bType = findType(reorder_string(b[0]))
  if(aType > bType):
    return 1
  elif (bType > aType): return -1

  for i in range(0, 5):
    aIdx = labels.index(a[0][i])
    bIdx = labels.index(b[0][i])
    if(aIdx < bIdx):
      return 1
    elif (aIdx > bIdx): return -1

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
