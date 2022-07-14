
import staaten

from itertools import combinations
import random
from helper import without
from helper import is_winning


def calc_gain(l_1:list[int], l_2:list[int]):
    # distance l_1 to l_2
    # no real distance because order matters
    # count states only in one list not both
    res = 0
    for i in range(len(staaten.state_names)):
        if i in l_1 and i not in l_2:
            res += 1
        elif i not in l_1 and i in l_2:
            res += 1          
    return res

def get_search_space(max_out = 5, min_pop_size = 0.625):
    loosing_coals_all = []
    for i in range(max_out + 1):
        loosing_coals_pre = []
        bool_array = []
        for positions in combinations(range(len(staaten.state_names)), len(staaten.state_names) - i):
                p = [0] * len(staaten.state_names)

                for i in positions:
                    p[i] = 1
                bool_array.append(p)   
                   
        for elem in bool_array: 
            test_coal = []
            for j in range(len(elem)):               
                if elem[j]:
                    test_coal.append(j)
            if not is_winning(test_coal):
                # and pop enough
                c = 0
                for elem in test_coal:
                    c = c + staaten.state_share[elem]
                if c > min_pop_size:
                    loosing_coals_pre.append(test_coal)
        if len(loosing_coals_pre)  > 0:
           loosing_coals_all.append(loosing_coals_pre) 
                     
    c = 0
    for s in loosing_coals_all:
        c = c + len(s)
    print(f"There are {c} coalitions left this is the search space ({c} hoch 15)")
    return loosing_coals_all

def kick_random(input):
    input.pop(random.randrange(len(input)))
    return input


def get_loosing_coalition(loosing_coals_all = [], max_out = 5, max_overall: int = 15, min_gain: int = 6, kick_strategy:str = "random", kick_rate: int = 100, give_up_rate: int = 1000, min_avg_pop_size = 0.645)-> list[list]:
    
    loosing_coals = [] # result
    c_bad_luck = 0  # wie lange wurde kein weiteres element gefunden ?
    current_max_length = 0 # bisherige gesamtlange von loosing_coals (result)
 
    # bis die gewünschte länge erreicht ist, mache:
    while len(loosing_coals) <  max_overall- 1:     
        c_bad_luck = c_bad_luck + 1
        if c_bad_luck % kick_rate == 0:
            if len(loosing_coals) < 2:
                continue
            
            # ToDo different kick strategies implementation
            # kick one randomly
            if kick_strategy == "random":
                loosing_coals = kick_random(loosing_coals)
            
            
            # and the least populated one
            #c_pop_l = []
            #for elem in loosing_coals:  
            #   count_pop = 0        
            #    for s in elem:
            #        count_pop += staaten.state_share[s]
            #    c_pop_l.append(count_pop)
            #min_value = min(c_pop_l)
            #return the index of minimum value 
            #min_index=c_pop_l.index(min_value)   
            #loosing_coals.pop(min_index)
            
        if c_bad_luck == give_up_rate:
            # if give up decrease min gain
            min_gain = min_gain - 1
            c_bad_luck = 0
        
        # random length of loosing coaltion to choose from    
        wanted_length_ix = random.randint(0, len(loosing_coals_all)-1)
        cand = random.choice(loosing_coals_all[wanted_length_ix])
        
        # wenn schon drin -> cnotinue
        if cand in loosing_coals:
            continue
        
        # wenn noch nicht drin -> schauen, ob voraussetzungen erfüllt
        # vorraussetzung 1 min gain
        min_dist = min_gain
        for elem in loosing_coals:
            d = calc_gain(elem, cand)
            if d < min_dist:
                min_dist = d
        
        # vorraussetzung 2 min avg pop
        c_pop_1 = 0
        avg_pop = 1
        if len(loosing_coals)  > 0:
            for elem in loosing_coals:          
                for s in elem:
                    c_pop_1 = c_pop_1 + staaten.state_share[s]                   
        
        for elem in cand:
           c_pop_1 = c_pop_1 + staaten.state_share[elem] 
        
        avg_pop = (c_pop_1) / (len(loosing_coals) + 1)
          
        # penelty for colaitions with less parties
        min_dist = min_dist + (max_out - (len(staaten.state_names) - len(cand)))
        
        # wenn vorraussetzung 1 und 2 erfüllt, dann append
        if min_dist >= min_gain and avg_pop > min_avg_pop_size:
            loosing_coals.append(cand)
            if current_max_length < len(loosing_coals):
                current_max_length = len(loosing_coals)
                c_bad_luck = 0
 
        
                
    # the last sepcial one
    # contruct die lange, die von hinten auffüllen
    is_loosing = True
    c = 0
    while(is_loosing):
        c = c + 1
        test_coal = []
        for j in range(len(staaten.state_names)):
            if j <= c:
                test_coal.append(j)
        if is_winning(test_coal):
                loosing_coals.append(test_coal[:-1])
                is_loosing = False
        
    return loosing_coals

                
if __name__ == '__main__':
    for _ in range(100):
        search_space = get_search_space()
        for elem in get_loosing_coalition(loosing_coals_all = search_space):
            invert_to_readable = []
            for i in range(len(staaten.state_names)):
                if i in elem:
                    pass
                else:
                    invert_to_readable.append(i+1)
            print(invert_to_readable)
                    
        