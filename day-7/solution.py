lines = [s.strip() for s in open("./input.txt", "r").readlines()]
i = 0
wd = []

directories = {}
files = {}

def checkwd():
    return '/' + '/'.join(wd)

def path(name: str):
    return f"{checkwd()}/{name}" if len(wd) > 0 else f"/{name}"

def cd(val: str):
    if val == "/":
        wd.clear()
    elif val == "..":
        wd.pop()
    else:
        wd.append(val)

def ls():
    global i
    i += 1

    if i >= len(lines):
        return

    if lines[i].startswith("$"):
        return

    arr = lines[i].split(" ")
    if arr[0] == "dir":
        directories[path(arr[1])] = -1
    else:
        files[path(arr[1])] = int(arr[0])

    ls()

def findlen(dir: str) -> int:
    if directories.get(dir, -1) >= 0:
        return directories[dir]

    s = 0
    for k, v in files.items():
        if k.startswith(dir):
            s += v
    directories[dir] = s
    return s
    
while i < len(lines):
    line = lines[i]
    if line.startswith("$ cd"):
        cd(line[5:])
        i += 1
    elif line.startswith("$ ls"):
        ls()

# Problem 1, find all directories with length <= 100k.
under100k = 0

# Problem 2. Given 70000000 space. We need to free 30000000.
# Find the smallest directory that, if deleted, would free up enough space.
free = 30000000 - (70000000 - findlen("/"))
delete_dirs = []

for k in directories.keys():
    v = findlen(k)
    if v <= 100000:
        under100k += v
    if v >= free:
        delete_dirs.append(v)

print(under100k)
print(min(delete_dirs))
