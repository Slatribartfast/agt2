import time
import os
import matplotlib.pyplot as plt
from multiprocessing import Process

import staaten
import calculateLoosingKoalition
import statistics
from cover import get_cover

def a_process_for_parallel_execution(name ="file.txt", runtime = 3600, id = -1, max_out = 5, max_overall: int = 15, min_gain: int = 6, kick_strategy:str = "random", kick_rate: int = 100, give_up_rate: int = 1000, min_avg_pop_size = 0.645,min_pop_size=0.62):
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
            best = res
            if best > 6:
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


def test(param_id:str,
        max_overall_params: list[int],
        min_avg_pop_params: list[float],
        min_pop_params: list[float],
        runtime = 1800,
        date = ""
        ):
    n = len(max_overall_params)
    if not (n == len(min_avg_pop_params) == len(min_pop_params)):
        print("Error: Parameter lists differ in length!")
        return


    for i in range(n):
        proc = []

        # default settings
        num_processes = 8
        max_out_l = [5] * num_processes
        min_gain_l = [7] * num_processes
        kick_strategy_l = ["random"] * num_processes
        kick_rate_l = [100] * num_processes
        give_up_rate_l = [1000] * num_processes

        # assign parameters to study
        max_overall_l = [max_overall_params[i]] * num_processes
        min_avg_pop_size_l = [min_avg_pop_params[i]] * num_processes
        min_pop_size_l = [min_pop_params[i]] * num_processes

        name = param_id + "/" + date + "/p_" + str(i) + ".txt"
        os.makedirs(os.path.dirname(name), exist_ok=True)
        with open(name, 'w') as f:
            f.write("Results")
            f.write("\nMax overall: " + str(max_overall_l[0]))
            f.write("\nMin avg pop: " + str(min_avg_pop_size_l[0]))
            f.write("\nMin pop: " + str(min_pop_size_l[0]) + "\n\n")
            f.flush()

        for i in range(num_processes):
            proc.append(Process(target=a_process_for_parallel_execution, args=(
                name, runtime, i, max_out_l[i], max_overall_l[i], min_gain_l[i], kick_strategy_l[i], kick_rate_l[i],
                give_up_rate_l[i], min_avg_pop_size_l[i], min_pop_size_l[i])))
            proc[-1].start()
            time.sleep(0.1)
        for i in range(len(proc)):
            proc[i].join()

def plot_results(param_id:str, directory:str, file_count:int, show_plt = False):
    max_overall, min_avg_pop, min_pop = [], [], []
    stats = []
    for i in range(file_count):
        #get cover counts and parameters from output files
        name = param_id + "/" + directory + "/p_" + str(i) + ".txt"
        stats.append(statistics.get_cover_count(name))
        line_c = 0
        with open(name, 'r') as f:
            for line in f:
                if line_c == 1:
                    max_overall.append(int("".join(i for i in line if i.isdigit()))) #get max_overall parameter
                elif line_c == 2:
                    min_avg_pop.append(float("".join(i for i in line if i.isdigit() or i == "."))) #get min_avg_pop
                elif line_c == 3:
                    min_pop.append(float("".join(i for i in line if i.isdigit() or i == "."))) #get min_pop
                elif line_c == 4:
                    break

                line_c +=1

    covers_5 = [elem[0] if len(elem) > 0 else 0 for elem in stats]
    covers_6 = [elem[1] if len(elem) > 1 else 0 for elem in stats]
    covers_7 = [elem[2] if len(elem) > 2 else 0 for elem in stats]

    if any(covers_7):
        plt_7 = True
    else:
        plt_7 = False

    if param_id == "min_pop":
        plt.plot(min_pop, covers_5)
        plt.plot(min_pop, covers_6)
        if plt_7:
            plt.plot(min_pop, covers_7)
    elif param_id == "min_avg_pop":
        plt.plot(min_avg_pop, covers_5)
        plt.plot(min_avg_pop, covers_6)
        if plt_7:
            plt.plot(min_avg_pop, covers_7)
    elif param_id == "max_overall":
        plt.plot(max_overall, covers_5)
        plt.plot(max_overall, covers_6)
        if plt_7:
            plt.plot(max_overall, covers_7)
    else:
        print("Param_id not recognized")

    if plt_7:
        plt.legend(("not 5 covers", "not 6 covers", "not 7 covers"))
    else:
        plt.legend(("not 5 covers", "not 6 covers"))
    plt.xlabel(param_id)
    plt.ylabel("Covers")
    plt.title("Parameter study: Varying " + param_id)
    savepath = param_id + "/" + directory + "/" + "pyplot.pdf"
    plt.savefig(savepath)
    if show_plt:
        plt.show()
    plt.close()

    #create seperate plot showing only 7 covers excluded
    if plt_7:
        if param_id == "min_pop":
            plt.plot(min_pop, covers_7)
        elif param_id == "min_avg_pop":
            plt.plot(min_avg_pop, covers_7)
        elif param_id == "max_overall":
            plt.plot(max_overall, covers_7)
        else:
            print("Param_id not recognized")

        plt.xlabel(param_id)
        plt.ylabel("Covers")
        plt.title("Parameter study: Varying " + param_id)
        plt.legend(("not 7 covers",))
        savepath = param_id + "/" + directory + "/" + "pyplot_7c.pdf"
        plt.savefig(savepath)
        plt.close()

if __name__ == "__main__":
    plot_results("max_overall","20220821-171807", 4, show_plt = True)