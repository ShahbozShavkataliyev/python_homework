task1


import threading

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def check_primes(start, end, result_list):
    for num in range(start, end + 1):
        if is_prime(num):
            result_list.append(num)


if __name__ == "__main__":
    start_range = 1
    end_range = 200
    num_threads = 4

    primes = []

    threads = []

    step = (end_range - start_range + 1) // num_threads

    for i in range(num_threads):
        s = start_range + i * step
        e = start_range + (i + 1) * step - 1
        if i == num_threads - 1:
            e = end_range  # last thread takes remainder

        t = threading.Thread(target=check_primes, args=(s, e, primes))
        threads.append(t)
        t.start()

 
    for t in threads:
        t.join()

    primes.sort()
    print("Prime numbers:", primes)


task2

import threading
from collections import defaultdict

def count_words(lines, result_dict):
    local_dict = defaultdict(int)
    for line in lines:
        words = line.strip().split()
        for w in words:
            local_dict[w.lower()] += 1

    for word, count in local_dict.items():
        result_dict[word] += count


if __name__ == "__main__":
    filename = "example.txt"
    num_threads = 4

    with open(filename, "r") as f:
        lines = f.readlines()

    word_count = defaultdict(int)

   
    step = len(lines) // num_threads
    threads = []

    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step
        if i == num_threads - 1:
            end = len(lines)  # last thread gets all remaining lines

        t = threading.Thread(target=count_words, args=(lines[start:end], word_count))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Word occurrences:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

