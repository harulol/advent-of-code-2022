lines = [line.strip() for line in open("./input.txt", "r").readlines()]

# All for part one cuz I suck.
head = (0, 0)
tail = (0, 0)
slots = set()

def move_tail():
    global head, tail, slots
    headX, headY = head
    tailX, tailY = tail

    slots.add((tailX, tailY))

    if abs(headX - tailX) <= 1 and abs(headY - tailY) <= 1:
        print(f"Didn't need to move! {headX} {headY} - {tailX} {tailY} - {len(slots)}")
        return

    dirX, dirY = (headX - tailX, headY - tailY)

    if headX == tailX:
        if headY < tailY:
            tailY -= 1
        else:
            tailY += 1
        tail = (tailX, tailY)
        return

    if headY == tailY:
        if headX < tailX:
            tailX -= 1
        else:
            tailX += 1
        tail = (tailX, tailY)
        return

    if headX < tailX:
        tailX -= 1
    else:
        tailX += 1

    if headY < tailY:
        tailY -= 1
    else:
        tailY += 1
    tail = (tailX, tailY)

def loop(times, x, y):
    global head
    for _ in range(times):
        headX, headY = head
        head = (headX + x, headY + y)
        move_tail()

for line in lines:
    direction, count = line.split(" ")

    if direction == "R":
        loop(int(count), 1, 0)
    elif direction == "L":
        loop(int(count), -1, 0)
    elif direction == "U":
        loop(int(count), 0, 1)
    else:
        loop(int(count), 0, -1)

print(len(slots))

# Part 2, No. I'm too bad for that.
