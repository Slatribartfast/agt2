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
                res.append(int(line.rstrip()))

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

    return ret
