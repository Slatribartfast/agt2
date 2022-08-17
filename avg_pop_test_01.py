import time
import staaten
import loosingKoalition

import test_params

if __name__ == '__main__':
        # param_ids: "max_overall", "min_avg_pop", "min_pop"
        mode = "min_avg_pop"
        runtime = 600
        param_count = 18
        max_overall_params = [15] * param_count

        #First test
        """
        min_avg_pop_params = [(i * 0.001 + 0.630) for i in range(param_count)]
        min_pop_params = [0.620] * param_count

        date = time.strftime("%Y%m%d-%H%M%S")
        test_params.test(mode, max_overall_params, min_avg_pop_params, min_pop_params, runtime, date)
        test_params.plot_results(mode, date, param_count)"""

        #Second test with different min_pop
        min_avg_pop_params = [(i * 0.001 + 0.630) for i in range(param_count)]
        min_pop_params = [0.630] * param_count

        date = time.strftime("%Y%m%d-%H%M%S")
        test_params.test(mode, max_overall_params, min_avg_pop_params, min_pop_params, runtime, date)
        test_params.plot_results(mode, date, param_count)