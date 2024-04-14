import random
import string


def generate_random_content():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
