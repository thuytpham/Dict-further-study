"""Restaurant rating lister."""

def restaurant_ratings(filename):

    ratings = open(filename)

    ratings_dict = {}

    for line in ratings:
        line = line.rstrip("\n")
        line = line.split(":")

        key = line[0]
        value = line [1]

        ratings_dict[key] = value

    for item, number in ratings_dict.items():
        print(f"{item} is rated at {number}")


print(restaurant_ratings("scores.txt"))