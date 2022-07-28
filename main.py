
import time

import staaten
import loosingKoalition
import calculateLoosingKoalition

from cover import get_cover

from multiprocessing import Process

def a_process_for_parallel_execution(name ="file.txt", runtime = 3600, id = -1, max_out = 5, max_overall: int = 15, min_gain: int = 6, kick_strategy:str = "random", kick_rate: int = 100, give_up_rate: int = 1000, min_avg_pop_size = 0.645,min_pop_size=0.62):  
    print("go")
    search_space = calculateLoosingKoalition.get_search_space(max_out, min_pop_size)
    best = 0
    tries = 0 
    start_time = time.time()
    points = 0
    # endlosschleife immer get loosing and get over nacheinander und ab 5 in datei
    # ToDo aufteilen mit variablen      
    while(time.time() < start_time + runtime):  
        tries += 1
        if True:
            if tries % 10 == 0:
                pass
                # print(f"id: {id}, tries: {tries}")
        lk = calculateLoosingKoalition.get_loosing_coalition(loosing_coals_all = search_space, max_out = max_out, max_overall = max_overall, min_gain = min_gain, kick_strategy = kick_strategy, kick_rate = kick_rate, give_up_rate = give_up_rate, min_avg_pop_size = min_avg_pop_size)
        res = get_cover(lk = lk, debug = False)
        if res > 4:
            if res == 5:
                points += 1
            elif res == 6:
                points += 100
            best = res
            print(best)
            with open(name, 'a') as f: 
                f.write(str(best)+ "\n")
                f.write(f"process id {id}\n")
                f.write("stats\n")
                f.write(f"{max_out}, {max_overall}, {min_gain}, {kick_rate}, {give_up_rate}\n")
                f.write(str(time.strftime("%Y%m%d-%H%M%S")))
                f.write("\nloosing coalitions taken\n")
                for elem in lk:
                    f.write(str(staaten.make_readable_alla_paper(elem)) + "\n")
                f.write("\n")
                f.write("\n")
                f.flush()
    
if __name__ == '__main__':
    
    for elem in loosingKoalition.loosing_coalitions:
        #print(elem)
        c = 0 
        for s in elem:
            c += staaten.state_share[s]
        print(str(c))
    
    # res = get_cover(lk = calculateLoosingKoalition.get_loosing_coals())
    #a_process_for_parallel_execution()
    
    if True: 
        """
        #1  
        proc = []
        
        num_processes = 16     
        max_out_l = [5] * num_processes
        max_overall_l = [15] * num_processes
        min_gain_l = [7] * num_processes
        kick_strategy_l = ["random"] * num_processes
        kick_rate_l = [100] * num_processes
        give_up_rate_l = [1000] * num_processes
        min_avg_pop_size_l = [0.64] * num_processes
        min_pop_size_l = [0.62] * num_processes
        runtime = 1800
        timestr = time.strftime("%Y%m%d-%H%M%S")
        name = "results"+timestr+".txt"
        name = "p_1.txt"
        with open(name, 'w') as f: 
                    f.write("Results\n\n")
                    f.flush()


        for i in range(num_processes):         
            proc.append(Process(target=a_process_for_parallel_execution, args=(name,runtime,i,max_out_l[i],max_overall_l[i],min_gain_l[i], kick_strategy_l[i],kick_rate_l[i],give_up_rate_l[i],min_avg_pop_size_l[i],min_pop_size_l[i])))
            proc[-1].start()
            time.sleep(0.1)
        for i in range(len(proc)):       
            proc[i].join() 
            
        #2    
        proc = []
        
        num_processes = 16     
        max_out_l = [5] * num_processes
        max_overall_l = [14] * num_processes
        min_gain_l = [7] * num_processes
        kick_strategy_l = ["random"] * num_processes
        kick_rate_l = [100] * num_processes
        give_up_rate_l = [1000] * num_processes
        min_avg_pop_size_l = [0.64] * num_processes
        min_pop_size_l = [0.62] * num_processes
        runtime = 1800
        timestr = time.strftime("%Y%m%d-%H%M%S")
        name = "results"+timestr+".txt"
        name = "p_2.txt"
        with open(name, 'w') as f: 
                    f.write("Results\n\n")
                    f.flush()


        for i in range(num_processes):         
            proc.append(Process(target=a_process_for_parallel_execution, args=(name,runtime,i,max_out_l[i],max_overall_l[i],min_gain_l[i], kick_strategy_l[i],kick_rate_l[i],give_up_rate_l[i],min_avg_pop_size_l[i],min_pop_size_l[i])))
            proc[-1].start()
            time.sleep(0.1)
        for i in range(len(proc)):       
            proc[i].join() 


        proc = []
        
        num_processes = 16     
        max_out_l = [5] * num_processes
        max_overall_l = [18] * num_processes
        min_gain_l = [7] * num_processes
        kick_strategy_l = ["random"] * num_processes
        kick_rate_l = [100] * num_processes
        give_up_rate_l = [1000] * num_processes
        min_avg_pop_size_l = [0.64] * num_processes
        min_pop_size_l = [0.62] * num_processes
        runtime = 1800
        timestr = time.strftime("%Y%m%d-%H%M%S")
        name = "results"+timestr+".txt"
        name = "p_3.txt"
        with open(name, 'w') as f: 
                    f.write("Results\n\n")
                    f.flush()


        for i in range(num_processes):         
            proc.append(Process(target=a_process_for_parallel_execution, args=(name,runtime,i,max_out_l[i],max_overall_l[i],min_gain_l[i], kick_strategy_l[i],kick_rate_l[i],give_up_rate_l[i],min_avg_pop_size_l[i],min_pop_size_l[i])))
            proc[-1].start()
            time.sleep(0.1)
        for i in range(len(proc)):       
            proc[i].join() 
            
        proc = []
        
        num_processes = 16     
        max_out_l = [5] * num_processes
        max_overall_l = [20] * num_processes
        min_gain_l = [7] * num_processes
        kick_strategy_l = ["random"] * num_processes
        kick_rate_l = [100] * num_processes
        give_up_rate_l = [1000] * num_processes
        min_avg_pop_size_l = [0.64] * num_processes
        min_pop_size_l = [0.62] * num_processes
        runtime = 1800
        timestr = time.strftime("%Y%m%d-%H%M%S")
        name = "results"+timestr+".txt"
        name = "p_4.txt"
        with open(name, 'w') as f: 
                    f.write("Results\n\n")
                    f.flush()


        for i in range(num_processes):         
            proc.append(Process(target=a_process_for_parallel_execution, args=(name,runtime,i,max_out_l[i],max_overall_l[i],min_gain_l[i], kick_strategy_l[i],kick_rate_l[i],give_up_rate_l[i],min_avg_pop_size_l[i],min_pop_size_l[i])))
            proc[-1].start()
            time.sleep(0.1)
        for i in range(len(proc)):       
            proc[i].join() 
            
        proc = []
        
        num_processes = 16     
        max_out_l = [5] * num_processes
        max_overall_l = [15] * num_processes
        min_gain_l = [7] * num_processes
        kick_strategy_l = ["random"] * num_processes
        kick_rate_l = [100] * num_processes
        give_up_rate_l = [1000] * num_processes
        min_avg_pop_size_l = [0.645] * num_processes
        min_pop_size_l = [0.62] * num_processes
        runtime = 1800
        timestr = time.strftime("%Y%m%d-%H%M%S")
        name = "results"+timestr+".txt"
        name = "p_5.txt"
        with open(name, 'w') as f: 
                    f.write("Results\n\n")
                    f.flush()


        for i in range(num_processes):         
            proc.append(Process(target=a_process_for_parallel_execution, args=(name,runtime,i,max_out_l[i],max_overall_l[i],min_gain_l[i], kick_strategy_l[i],kick_rate_l[i],give_up_rate_l[i],min_avg_pop_size_l[i],min_pop_size_l[i])))
            proc[-1].start()
            time.sleep(0.1)
        for i in range(len(proc)):       
            proc[i].join() 
            
        """    
        proc = []
        
        num_processes = 16     
        max_out_l = [5] * num_processes
        max_overall_l = [15] * num_processes
        min_gain_l = [7] * num_processes
        kick_strategy_l = ["random"] * num_processes
        kick_rate_l = [100] * num_processes
        give_up_rate_l = [1000] * num_processes
        min_avg_pop_size_l = [0.63] * num_processes
        min_pop_size_l = [0.62] * num_processes
        runtime = 1800
        timestr = time.strftime("%Y%m%d-%H%M%S")
        name = "results"+timestr+".txt"
        name = "p_6.txt"
        with open(name, 'w') as f: 
                    f.write("Results\n\n")
                    f.flush()
                    
        for i in range(num_processes):         
            proc.append(Process(target=a_process_for_parallel_execution, args=(name,runtime,i,max_out_l[i],max_overall_l[i],min_gain_l[i], kick_strategy_l[i],kick_rate_l[i],give_up_rate_l[i],min_avg_pop_size_l[i],min_pop_size_l[i])))
            proc[-1].start()
            time.sleep(0.1)
        for i in range(len(proc)):       
            proc[i].join() 

        proc = []
        
        num_processes = 16     
        max_out_l = [5] * num_processes
        max_overall_l = [15] * num_processes
        min_gain_l = [7] * num_processes
        kick_strategy_l = ["random"] * num_processes
        kick_rate_l = [100] * num_processes
        give_up_rate_l = [1000] * num_processes
        min_avg_pop_size_l = [0.64] * num_processes
        min_pop_size_l = [0.63] * num_processes
        runtime = 1800
        timestr = time.strftime("%Y%m%d-%H%M%S")
        name = "results"+timestr+".txt"
        name = "p_7.txt"
        with open(name, 'w') as f: 
                    f.write("Results\n\n")
                    f.flush()
                    
        for i in range(num_processes):         
            proc.append(Process(target=a_process_for_parallel_execution, args=(name,runtime,i,max_out_l[i],max_overall_l[i],min_gain_l[i], kick_strategy_l[i],kick_rate_l[i],give_up_rate_l[i],min_avg_pop_size_l[i],min_pop_size_l[i])))
            proc[-1].start()
            time.sleep(0.1)
        for i in range(len(proc)):       
            proc[i].join() 
                    
        proc = []
        
        num_processes = 16     
        max_out_l = [5] * num_processes
        max_overall_l = [15] * num_processes
        min_gain_l = [7] * num_processes
        kick_strategy_l = ["random"] * num_processes
        kick_rate_l = [100] * num_processes
        give_up_rate_l = [1000] * num_processes
        min_avg_pop_size_l = [0.64] * num_processes
        min_pop_size_l = [0.635] * num_processes
        runtime = 1800
        timestr = time.strftime("%Y%m%d-%H%M%S")
        name = "results"+timestr+".txt"
        name = "p_8.txt"
        with open(name, 'w') as f: 
                    f.write("Results\n\n")
                    f.flush()
                    
                    
        for i in range(num_processes):         
            proc.append(Process(target=a_process_for_parallel_execution, args=(name,runtime,i,max_out_l[i],max_overall_l[i],min_gain_l[i], kick_strategy_l[i],kick_rate_l[i],give_up_rate_l[i],min_avg_pop_size_l[i],min_pop_size_l[i])))
            proc[-1].start()
            time.sleep(0.1)
        for i in range(len(proc)):       
            proc[i].join() 

