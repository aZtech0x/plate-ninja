# Barbell weight
bar = 20

# Attempts to convert the input to a float, asks you to try again if it fails
# Then, we calculate the plate load without the barbell
# Remaining plates are divided by two and bound to a variable, so we are only working with one half later
# We ensure that at least the smallest plates can be added each side (1.25)
# We check if the per-side weight value will become zero if divided into 1.25kg units, ensure correct weights are used
while True:
    total_load = input("What is the total weight in kg?: ")
    try:
        total_load = float(total_load)
    except ValueError:
        print("Please use numeric digits.")
        continue
    plate_load = total_load - bar
    remaining = plate_load / 2
    if plate_load < 2.5:
        print("Please enter a weight of at least 22.5kg.")
        continue
    if (plate_load / 2) % 1.25 != 0:
        print("Must be in 2.5kg increments.")
        continue
    break


# Creates a plate object, with multiple default arguments
# Symbol function within will draw the plate's symbol in it's assigned colour, then resets the colour each time
class Plate:
    def __init__(self, weight, colour_name, colour_code, symbol):
        self.weight = weight
        self.colour_name = colour_name
        self.symbol = f"{colour_code}{symbol}\033[0m"


# Creates a tuple (immutable, unable to be changed) which is the definitive list of plates.
plates_available = (
    Plate(25, "red", "\033[31m", "]"),
    Plate(20, "blue", "\033[34m", "]"),
    Plate(15, "yellow", "\033[33m", "]"),
    Plate(10, "green", "\033[32m", "]"),
    Plate(5, "white", "\033[37m", "]"),
    Plate(2.5, "black", "\033[37m", ":"),
    Plate(1.25, "small black", "\033[37m", "."),
)

# Dictionary is created for the tally of plates
# Here we iterate over the tuple we just created, starting from the top (red)
# Whilst the remaining load can fit another plate this loop will continue with the following instructions
# Initializes the count value of the colour to 0, so if none are used then a value still exists, no error
# If a plate fits and is used, the plate count for that colour increases by 1 in the dictionary
# Weight of the plate used is deducted from remaining weight value, then checks the first plate again
# This will check each plate in order, prioritising the highest value. Ends when remaining = 0.
plate_count = {}
for plate in plates_available:
    while remaining >= plate.weight:
        plate_count[plate.colour_name] = plate_count.get(plate.colour_name, 0) + 1
        remaining -= plate.weight

# We create a default barbell visual to add plates to
# Iterates over our tuple again
# If a plate colour exists in the dictionary then:
# Counts the colours of the plate and binds it to a new variable
# Appends the plate symbol * plate count to the existing plate visual string
plate_visual = "--"
for plate in plates_available:
    if plate.colour_name in plate_count:
        count = plate_count[plate.colour_name]
        plate_visual += plate.symbol * count

# Get colour and count of each plate in the dictionary
# Binds the count and plate colour string to the summary value
summary = []
for (
    colour,
    count,
) in plate_count.items():
    summary.append(f"{count} {colour}")

print()
print(f"{total_load}kg is your total weight.")
print(plate_visual)
print(", ".join(summary))
print()
