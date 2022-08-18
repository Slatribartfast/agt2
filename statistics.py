def get_cover_count(name:str):
    bool_c = False
    res = []
    ret = []
    with open(name) as file:
        for line in file:
            if line == "\n":
                bool_c = True
            if bool_c and line != "\n":
                bool_c = False
                try:
                    res.append(int(line.rstrip()))
                except:
                    print("Error reading from file")

    print(f"logged {len(res)} nicht covers")
    c = 0
    i = 0
    while c < len(res):
        i = i + 1
        if i > 100:
            print("verzaehlt")
            break
        if res.count(i) > 0:
            print(f"Es wurden {res.count(i)} nicht {i} covers gefunden")
            ret.append(res.count(i))
            c = c + res.count(i)

            if (i >= 7):
                print("7 cover excluded in " + name)
                get_7_covers(name)
                with open("___7cover_found.txt", "a") as f:
                    f.write(name + "\n")


    return ret

def get_7_covers(name:str):
    cover_l = []
    bool_c, lines_to_copy = False, 0
    with open(name, "r") as f:
        for line in f:
            if line == "\n":
                bool_c = True
            elif bool_c:
                bool_c = False
                cover = int(line.rstrip())
                if cover >= 7:
                    #Hardcoded to match length of individual results; must be adapted for different max_overall lengths
                    lines_to_copy = 21
                    cover_l.append([])

            if (lines_to_copy > 0):
                lines_to_copy -= 1
                cover_l[-1].append(line.rstrip())

    with open("7_covers/7_covers.txt", "a") as f:
        f.write("\n\n Name: " + name + "\n")
        for i in range(len(cover_l)):
            f.write(str(cover_l[i]))
            f.write("\n")

