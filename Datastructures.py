oloture = open("oloture.2019.srt", "r")
counter = 0

for line in oloture.readlines():
    if "forze speciali" in line.lower():
        print(f"found in line {counter +1} " ,line)
    counter += 1

print(oloture.read())

oloture.close()
