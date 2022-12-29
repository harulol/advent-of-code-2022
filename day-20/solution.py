from typing import Union

numbers = [int(s.strip()) for s in open("./input.txt").readlines()]
length = len(numbers)

class Node:
    val: int
    prev: 'Node'
    next: 'Node'

    def __init__(self, val: int) -> None:
        self.val = val

    def traverse(self):
        start = self.val
        current = self

        while True:
            print(f"{current.val}",end=" ")
            current = current.next

            if current.val == start:
                break
        print()

    def find(self, val: int):
        current = self
        while current.val != val:
            current = current.next
        return current

    def get(self, steps: int):
        current = self
        for _ in range(steps):
            current = current.next
        return current

    def link_next(self, other: 'Node'):
        self.next = other
        other.prev = self

    def move(self):
        if self.val == 0:
            return

        current = self.get(self.val % (length - 1))

        # Sever connection before.
        self.prev.link_next(self.next)

        # Create new links between.
        self.link_next(current.next)
        current.link_next(self)

def parse_input() -> Node:
    dummy_head = Node(0)
    current = dummy_head

    for num in numbers:
        current.link_next(Node(num))
        current = current.next

    current.link_next(dummy_head.next)
    return dummy_head.next

def solve_part_one():
    head = parse_input()
    for num in numbers:
        node = head.find(num)
        node.move()

    zero = head.find(0)
    one_thousand = zero.get(1000)
    two_thousand = zero.get(2000)
    three_thousand = zero.get(3000)
    print(f"{one_thousand.val} {two_thousand.val} {three_thousand.val}")
    print(sum([one_thousand.val, two_thousand.val, three_thousand.val]))

solve_part_one()
