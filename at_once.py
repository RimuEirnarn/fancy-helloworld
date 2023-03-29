from time import sleep
from random import randint
CLSLINE = "\r\033[2K\r"

MAPPED = "Hello, World!"
length = len(MAPPED)
NEW = ' '*length
mapped = (36, 127)

def randomise(char, target):
    orded = ord(char)
    if orded == ord(target):
        return char
    if orded > ord(target):
        return chr(randint(orded-10, orded))
    if orded < ord(target):
        return chr(randint(orded, orded+10))

while True:
    for i in range(length):
        if NEW[i] == MAPPED[i]:
            continue
        if i == 0:
            new = randomise(NEW[0], MAPPED[0])
            NEW = new + NEW[1:]
            continue
        new = randomise(NEW[i], MAPPED[i])
        NEW = NEW[:i] + new + NEW[i+1:]
    print(NEW, end="", flush=True)
    sleep(0.1)
    print(CLSLINE, end="", flush=True)
    if NEW == MAPPED:
        break

print(f"\033[32m{NEW}\033[0m")
