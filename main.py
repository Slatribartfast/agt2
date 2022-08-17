import time

import staaten
import loosingKoalition
import test_params

if __name__ == '__main__':
    
    for elem in loosingKoalition.loosing_coalitions:
        #print(elem)
        c = 0 
        for s in elem:
            c += staaten.state_share[s]
        print(str(c))

        # param_ids: "max_overall", "min_avg_pop", "min_pop"
    mode = "min_pop"
    runtime = 10
    param_count = 4
    max_overall_params = [15] * param_count

    min_avg_pop_params = [0.64] * param_count
    min_pop_params = [(i * 0.005 + 0.630) for i in range(param_count)]

    date = time.strftime("%Y%m%d-%H%M%S")
    test_params.test(mode, max_overall_params, min_avg_pop_params, min_pop_params, runtime, date)
    test_params.plot_results(mode, date, param_count)
