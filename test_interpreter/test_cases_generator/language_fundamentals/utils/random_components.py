import random


def random_floating_point():
    return str((random.random()-0.5) * 100000000)


def random_scientific_notation():
    return f"{random_floating_point()}e{random.randint(-100, 100)}"


def random_double():
    number = random.choice([random_floating_point, random_scientific_notation])
    return number()


def random_identifier():
    first_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    other_char = first_char + "0123456789_"
    return random.choice(first_char) + ''.join(random.choice(other_char) for _ in range(random.randint(1, 9)))
