import random


class RandomComponentGenerator:
    @staticmethod
    def random_identifier():
        first_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        other_char = first_char + "0123456789_"
        return random.choice(first_char) + ''.join(random.choice(other_char) for _ in range(random.randint(1, 9)))

    @staticmethod
    def random_floating_point():
        return str((random.random() - 0.5) * 100000000)

    @staticmethod
    def random_double():
        return random.choice([RandomComponentGenerator.random_floating_point,
                              RandomComponentGenerator.random_scientific_notation])()

    @staticmethod
    def random_scientific_notation():
        return f"{RandomComponentGenerator.random_floating_point()}e{random.randint(-100, 100)}"
