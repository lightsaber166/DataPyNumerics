import dill
import random

class DatPack:
    def __init__(self):
        self.values = []
        self.id = ''
        for i in range(10):
            i = random.randint(1, 9)
            self.id = self.id + str(i)
        self.id = 'dpk-' + self.id

    def add_value(self, value):
        self.values.append(value)

    def get_value(self, valueidx):
        if 0 <= valueidx < len(self.values):
            return self.values[valueidx]
        else:
            return None

    def get_id(self):
        return self.id

    def save(self, file):
        with open(file, 'wb') as f:
            dill.dump(self, f)

    @classmethod
    def load(cls, file):
        with open(file, 'rb') as f:
            return dill.load(f)

class Array:
    def __init__(self, array):
        self.array = array
        self.id = random.randint(100, 900)

    def alter(self, newarray):
        self.array = newarray

    def get_id(self):
        return self.id

    def reset(self):
        self.array = []

class Value:
    def __init__(self, value):
        self.value = value
        self.id = random.randint(100, 900)

    def alter(self, newvalue):
        self.value = newvalue

    def get_id(self):
        return self.id

    def reset(self):
        self.value = None

# New class to calculate statistics on an array of values
class ArrayStatistics:
    def __init__(self, array):
        self.array = array

    def mean(self):
        if not self.array:
            return None
        return sum(self.array) / len(self.array)

    def median(self):
        if not self.array:
            return None
        sorted_array = sorted(self.array)
        n = len(sorted_array)
        if n % 2 == 1:
            return sorted_array[n // 2]
        else:
            mid1 = sorted_array[n // 2 - 1]
            mid2 = sorted_array[n // 2]
            return (mid1 + mid2) / 2

# New function to generate a random password
def generate_random_password(length=12):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
