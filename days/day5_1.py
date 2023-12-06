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

    def convert_seed_to_location(self, seed: int):
        val = seed
        for m in self.maps:
            val = m.convert(val)
        return val
    
    def trace(self, seed):
        t = []
        val = seed
        for m in self.maps:
            t.append(m.trace(val))
            val = m.convert(val)
        return t
    
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


with open("inputs/day5_1.txt", 'r') as f:
    seeds = [int(s) for s in f.readline().strip()[len('seeds: '):].split(' ')]

    f.readline()
    f.readline()

    almanac = parse_almanac(f)

    smallest = float('inf')
    for seed in seeds:
        loc = almanac.convert_seed_to_location(seed)
        if loc < smallest:
            smallest = loc
            
    print(smallest)