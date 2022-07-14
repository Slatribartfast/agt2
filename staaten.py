import numpy as np

print("loaded states")
# names are used for counting
state_names = np.array(["Germany",
                        "France",
                        "UK",
                        "Italy",
                        "Spain",
                        "Poland",
                        "Romania",
                        "Netherlands",
                        "Belgium",
                        "Greece",
                        "Czech Republic",
                        "Portugal",
                        "Hungary",
                        "Sweden",
                        "Austria",
                        "Bulgaria",
                        "Denmark",
                        "Finland",
                        "Slovakia",
                        "Ireland",
                        "Croatia",
                        "Lithuania",
                        "Slovenia",
                        "Latvia",
                        "Estonia",
                        "Cyprus",
                        "Luxembourg",
                        "Malta"])

state_pop = np.array([80780000, 8507786, 65856609, 7245677, 64308261, 5627235, 60782668,
                      5451270, 46507760, 5415949, 38495659, 4604029, 19942642, 4246700,
                      16829289, 2943472, 11203992, 2061085, 10992589, 2001468, 10512419,
                      1315819, 10427301, 858000, 9879000, 549680, 9644864, 425384])

state_pop = np.sort(state_pop)[::-1]

pop_all = 0
for elem in state_pop:
    pop_all = pop_all + elem

state_share = np.empty(len(state_names))

for i in range(len(state_share)):
    state_share[i] = state_pop[i] / pop_all

def make_readable_alla_paper(l: list[int]) -> list[int]:
    res = []
    for i in range(len(state_names)):
        if i not in l:
            res.append(i + 1)
    return res    
    
def from_paper_name_to_real(l:list[int]) -> list[int]:
    res = []
    for i in range(len(state_names)):
        if i+1 not in l:
            res.append(i)
    return res