import time
import argparse
import random
import string
import requests


def generate_data(size):
    numbers_count = size - random.randint(0, size)
    data = [
        random.uniform(0, 100)
        for _ in range(numbers_count)
    ]
    chars_count = size - numbers_count
    data += random.choices(string.ascii_letters, k=chars_count)
    random.shuffle(data)
    return data


def main(args):
    while True:
        data = generate_data(args.array_size)
        response = requests.post(args.url, json=data)
        print(f'Sent: {data}\nGot: {response.text}\n-----')
        time.sleep(args.timeout)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str)
    parser.add_argument('--array_size', type=int)
    parser.add_argument('--timeout', type=float)

    try:
        main(parser.parse_args())
    except KeyboardInterrupt:
        print('Bye')
