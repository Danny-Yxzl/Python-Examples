import random


length = 8


def encrypt_string(text):
    random.seed(text)
    secret_key = int(random.random() * pow(10, length))
    return str(secret_key)


if __name__ == "__main__":
    print(encrypt_string("nh"))