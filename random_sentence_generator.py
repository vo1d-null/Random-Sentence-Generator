import random

names = ["Nikolai", "Ivan", "Georgi", "Jane", "Peter", "Steve"]
places = ["Varna", "Plovdiv", "Los Angeles", "Sofia", "Cape Town"]
verbs = ["eats", "holds", "sucks", "sees", "plays with", "brings", "eats"]
nouns = ["stones", "cake", "apple", "laptop", "bikes", "dicks"]
details = ["near the river", "at home", "in the park", "at public event"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly", "furiously"]


def get_random_word(words):
    pass


def get_random_word(words):
    return random.choice(words)


print("Hello,This is your first random generated sentence:")

while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)
    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}")
    input("Click [Enter] to generate a new sentence.\n")
