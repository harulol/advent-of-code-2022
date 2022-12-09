lines = [line.strip() for line in open("./input.txt", "r").readlines()]

class Node:
    x: int
    y: int

    def __init__(self):
        self.x = 0
        self.y = 0

    def tuple(self):
        return (self.x, self.y)

    def move(self, direction: str):
        if direction.find("L") >= 0:
            self.x -= 1
        if direction.find("R") >= 0:
            self.x += 1
        if direction.find("U") >= 0:
            self.y += 1
        if direction.find("D") >= 0:
            self.y -= 1

    def move_to(self, node: 'Node'):
        targetX, targetY = node.tuple()
        currentX, currentY = self.tuple()

        # No need to move here.
        if abs(targetX - currentX) <= 1 and abs(targetY - currentY) <= 1:
            return

        # Moving vertically.
        if targetX == currentX:
            # It is currently below.
            if targetY < currentY: 
                self.move("D")
            else: self.move("U")
            return
        
        # Moving horizontally
        if targetY == currentY:
            # It is to the left.
            if targetX < currentX:
                self.move("L")
            else: self.move("R")
            return

        # Moving diagonally.
        if targetX < currentX:
            self.move("L")
        else: self.move("R")

        if targetY < currentY:
            self.move("D")
        else: self.move("U")

def move_chain(nodes_count: int):
    nodes = [Node() for _ in range(nodes_count)]
    slots = set()

    for line in lines:
        direction, count_str = line.split(" ")
        count = int(count_str)

        for _ in range(count):
            nodes[0].move(direction)
            for i in range(1, nodes_count):
                nodes[i].move_to(nodes[i - 1])
            slots.add(nodes[-1].tuple())

    print(len(slots))

# Part 1 is head & tail. 2 nodes.
move_chain(2)

# Part 2 is a bridge of 10 nodes.
move_chain(10)
