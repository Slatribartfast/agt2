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
    
    # res = get_cover(lk = calculateLoosingKoalition.get_loosing_coals())
    #a_process_for_parallel_execution()
    
    if True: 
        runtime = 120
        max_overall_params = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
        #min_avg_pop_params = [0.64, 0.64, 0.64, 0.64, 0.64, 0.64, 0.64, 0.64, 0.64, 0.64]
        #min_pop_params = [0.63, 0.631, 0.632, 0.633, 0.634, 0.635, 0.636, 0.637, 0.638, 0.639]
        min_avg_pop_params = [0.635, 0.636, 0.637, 0.638, 0.639, 0.64, 0.641, 0.642, 0.643, 0.644]
        min_pop_params = [0.633] * 10

        #param_ids: "max_overall", "min_avg_pop", "min_pop"
        test_params.test("min_avg_pop",max_overall_params, min_avg_pop_params, min_pop_params, runtime)

