from collections import deque

order = [int(s.strip()) for s in open("./input.txt").readlines()]

def get_queue(key = 1):
    return deque([(index, value * key) for index, value in enumerate(order)])

def decrypt(queue):
    for index in range(len(order)):
        while queue[0][0] != index:
            queue.rotate(-1)

        item = queue.popleft()
        steps = item[1] % (len(order) - 1)
        queue.rotate(-steps)
        queue.append(item)

def until_zero(queue):
    while queue[0][1] != 0:
        queue.rotate(-1)

def sum_of_thousands(queue):
    _sum = 0
    for _ in range(3):
        queue.rotate(-1000)
        _sum += queue[0][1]
    return _sum

def solve_part_one():
    queue = get_queue()
    decrypt(queue)
    until_zero(queue)
    print(sum_of_thousands(queue))

def solve_part_two():
    decryption_key = 811589153
    queue = get_queue(decryption_key)

    for _ in range(10):
        decrypt(queue)

    until_zero(queue)
    print(sum_of_thousands(queue))

solve_part_two()
