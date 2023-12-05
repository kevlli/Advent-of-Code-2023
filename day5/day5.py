def parseLines(input):
    seeds = []
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    allMaps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]
    identifiers = ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"]
    n = 0
    while n < len(input):
        line = (input[n])[:-1]
        if line[:5] == "seeds":
            line = line[7:]
            seeds = list(map(int, line.split(' ')))
        if line in identifiers:
            index = identifiers.index(line)
            n += 1
            line = (input[n])[:-1]

            while (n < len(input)):
                line = (input[n])[:-1]
                if (line == ""):
                    break
                nums = list(map(int, line.split(' ')))
                allMaps[index].append([nums[1], nums[1] + nums[2], nums[0]])
                n += 1
        
        n += 1
    return seeds, allMaps
        
def convertToLocation(seeds, mappings):
    location = []
    for seed in seeds:
        for map in mappings:
            for i, num in enumerate(map):
                if seed in range(num[0], num[1]):
                    seed = seed - num[0] + num[2]
                    break
        location.append(seed)
    return location

def convertToLocation2(seeds, mappings):
    location = []

    for i in range(0, len(seeds), 2):
        seed_start = seeds[i]
        seed_end = seeds[i] + seeds[i + 1]
        tempLoc = []

        while seed_start < seed_end:
            nextMapping = 9999999999999999
            seed = seed_start
            for map in mappings:
                nextRange = 99999999999999
                for i, num in enumerate(map):
                    if seed in range(num[0], num[1]):
                        nextMapping = min(nextMapping, num[1] - seed)
                        # out of all the mappings, this finds the minimum distance from the source to the max source value.
                        # it can then skip ahead by this minimum value, since incrementing by this value will not change any mappings
                        # and any value that is skipped would only be greater than the previous value anyway
                        # effectively, this skips to a value where a mapping changes, since calculating any values within the same series
                        # of mappings is redundant
                        seed = seed - num[0] + num[2]
                        break
                    if seed < num[0]:
                        nextRange = min(nextRange, num[0] - seed)
                        # for this specific mapping, this stores the minimum distance from the source to any of the min source values,
                        # given that the min source value is greater than the source.
                        # this effectively finds the next closest interval / range if the source currently doesn't fall under one
                    if i == len(map) - 1:
                        nextMapping = min(nextRange, nextMapping)
                        # in the case where the source does not fall into any of the ranges, we can increment by the minimum of nextRange and nextMapping
                        # this effectively skips ahead until the next range that source falls into (nextRange) or the next value that will exit
                        # one of the mappings (nextMapping)
            tempLoc.append(seed)
            seed_start += nextMapping
        location.append(min(tempLoc))
    return location

def part1():
    file = open("input.txt", "r")
    lines = file.readlines()
    seeds, allMaps = parseLines(lines)
    locations = convertToLocation(seeds, allMaps)
    minLocation = min(locations)
    print(minLocation)

def part2():
    file = open("input.txt", "r")
    lines = file.readlines()
    seeds, allMaps = parseLines(lines)
    locations = convertToLocation2(seeds, allMaps)
    minLocation = min(locations)
    print(locations)
    print(minLocation)

part1()
part2()

