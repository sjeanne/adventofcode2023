input_file = open('1.txt', 'r')

def parse_convert_map():
    output_map = []
    line = input_file.readline().strip()
    while len(line) > 0:
        output_map.append(list(map(int, line.split()))) #(dest, source, length)
        line = input_file.readline().strip()
    return output_map

def get_destination_from_map(convert_maps, source:int):
    for convert_map in convert_maps:
        print(convert_map)
        if convert_map[1] <= source and source < convert_map[1]+convert_map[2]:
            return convert_map[0]+ (source - convert_map[1])
    return source

input_line = input_file.readline().strip()
seeds = map(int, input_line.split(':')[1].split())
print(f"Seeds: {seeds}")

input_file.readline() #empty

input_file.readline() # seed-to-soil map:
seeds_to_soil = parse_convert_map()
print(f"Seed to soil: {seeds_to_soil}")

input_file.readline() # soil to fertilizer map:
soil_to_fertilizer = parse_convert_map()
print(f"soil to fertilizer: {soil_to_fertilizer}")

input_file.readline() # fertilizer-to-water map:
fertilizer_to_water = parse_convert_map()
print(f"fertilizer_to_water: {fertilizer_to_water}")

input_file.readline() # water-to-light  map:
water_to_light  = parse_convert_map()
print(f"water_to_light: {water_to_light}")

input_file.readline() # light-to-temperature  map:
light_to_temperature  = parse_convert_map()
print(f"light_to_temperature: {light_to_temperature}")

input_file.readline() # temperature-to-humidity   map:
temperature_to_humidity  = parse_convert_map()
print(f"temperature_to_humidity: {temperature_to_humidity}")


input_file.readline() # humidity-to-location map:
humidity_to_location  = parse_convert_map()
print(f"humidity_to_location: {humidity_to_location}")

seed_location = []

for seed in seeds:
    soil = get_destination_from_map(seeds_to_soil, seed)
    fertilizer = get_destination_from_map(soil_to_fertilizer, soil) 
    water = get_destination_from_map(fertilizer_to_water, fertilizer)
    light = get_destination_from_map(water_to_light, water) 
    temperature = get_destination_from_map(light_to_temperature, light) 
    humidity = get_destination_from_map(temperature_to_humidity, temperature)
    location = get_destination_from_map(humidity_to_location, humidity)
    seed_location.append((seed,location))
seed_location.sort(key=lambda sl: sl[1])
print(seed_location)
