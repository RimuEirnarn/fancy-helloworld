from time import sleep
CLSLINE = "\r\033[2K\r"

MAPPED = "Hello, World!"
NEW = ""
position = 0

while True:
    if len(NEW) == len(MAPPED):
        break
    if len(NEW) < position+1:
        NEW += " "
    if NEW[position] == MAPPED[position]:
        position += 1
        continue
    NEW = NEW[:-1] + chr(ord(NEW[-1])+1)
    print(NEW, end="", flush=True)
    sleep(0.01)
    print(CLSLINE, end="", flush=True)

print(f"\033[32m{NEW}\033[0m", flush=True)
