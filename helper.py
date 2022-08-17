import staaten

def without(a: list[int], b: list[int]) -> list[int]:
    # a without b
    c = []
    for elem in a:
        if elem not in b:
            c.append(elem)
            
    return(c)            
    
def is_winning(input_coal: list[int]) -> bool:
    if len(input_coal) >= 25:
        # print("over 25")
        return True

    if len(input_coal) >= len(staaten.state_names) * 0.55:
        pop_c = 0
        for elem in input_coal:
            pop_c += staaten.state_share[elem]
        # print(pop_c)
        if pop_c >= 0.65:
            return True
    return False


