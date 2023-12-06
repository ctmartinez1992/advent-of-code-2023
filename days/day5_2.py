from base import *

class GenericMap:
    def __init__(self, dst, src, loop):
        self.dst = dst
        self.src = src
        self.loop = loop

    def convert(self, val: int):
        for i in range(len(self.src)):
            srs = self.src[i]
            if val >= srs and val < srs + self.loop[i]:
                return (val - srs) + self.dst[i]
        return val
    
    def trace(self, val: int):
        for i in range(len(self.src)):
            srs = self.src[i]
            if val >= srs and val < srs + self.loop[i]:
                return i
        return -1

class Almanac:
    def __init__(self, seed2soil, soil2fert, fert2water, water2light, light2temp, temp2humid, humid2loc):
        self.seed2soil = seed2soil
        self.soil2fert = soil2fert
        self.fert2water = fert2water
        self.water2light = water2light
        self.light2temp = light2temp
        self.temp2humid = temp2humid
        self.humid2loc = humid2loc
        self.maps = (seed2soil, soil2fert, fert2water, water2light, light2temp, temp2humid, humid2loc)

    def trace(self, seed):
        t = []
        val = seed
        for m in self.maps:
            t.append(m.trace(val))
            val = m.convert(val)
        return t
    
    def seed_to_loc(self, seed: int):
        val = seed
        for m in self.maps:
            val = m.convert(val)
        return val
    
def parse_generic_map(f):
    dst, src, loop = [], [], []
    for line in f:
        line = line.strip()
        if line == '':
            return GenericMap(dst, src, loop)
        drs, srs, rl = [int(part) for part in line.split (' ') if part != '']
        dst.append(drs)
        src.append(srs)
        loop.append(rl)
    return GenericMap(dst, src, loop)

def parse_almanac(f):
    seed2soil = parse_generic_map(f)
    f.readline()
    soil2fert = parse_generic_map(f)
    f.readline()
    fert2water = parse_generic_map(f)
    f.readline()
    water2light = parse_generic_map(f)
    f.readline()
    light2temp = parse_generic_map(f)
    f.readline()
    temp2humid = parse_generic_map(f)
    f.readline()
    humid2loc = parse_generic_map(f)
    return Almanac(seed2soil, soil2fert, fert2water, water2light, light2temp, temp2humid, humid2loc)

def reduce_seed_groups(seed_groups, almanac):
    if len(seed_groups) == 0:
        return []
    
    new_groups = []
    for sg in seed_groups:
        if type(sg) == int:
            new_groups.append(sg)
        elif sg[0] == sg[1] or almanac.trace(sg[0]) == almanac.trace(sg[1]):
            new_groups.append(sg[0])
            new_groups.append(sg[0])
        elif sg[0] == sg[1] - 1:
            new_groups += [sg[0], sg[1]]
        else:
            length = 1 + (sg[1] - sg[0])
            preg = (sg[0], sg[0] + length // 2)
            postg = (sg[0] + length // 2 + 1, sg[1])
            new_groups += reduce_seed_groups((preg, postg), almanac)
    return new_groups

with open("inputs/day5_2.txt", 'r') as f:
    seed_pre_pairs = [int(s) for s in f.readline().strip()[len('seeds: '):].split(' ')]

    seed_groups = []
    for i in range(0, len(seed_pre_pairs), 2):
        seed_groups.append((seed_pre_pairs[i], seed_pre_pairs[i] + seed_pre_pairs[i + 1] - 1))

    f.readline()
    f.readline()

    almanac = parse_almanac(f)
    seed_groups = reduce_seed_groups(seed_groups, almanac)
    
    smallest = float('inf')
    for seed in seed_groups:
        loc = almanac.seed_to_loc(seed)
        if loc < smallest:
            smallest = loc
    print(smallest)