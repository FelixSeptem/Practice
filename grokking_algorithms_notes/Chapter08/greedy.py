# -*- coding:utf-8 -*-  
# 集合覆盖问题

# states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]) ←------你传入一个数组，它被转换为集合

# stations = {}
# stations["kone"] = set(["id", "nv", "ut"])
# stations["ktwo"] = set(["wa", "id", "mt"])
# stations["kthree"] = set(["or", "nv", "ca"])
# stations["kfour"] = set(["nv", "ut"])
# stations["kfive"] = set(["ca", "az"])

def find_best_stations(states_needed, stations):
    best_stations = None
    states_cover = set()
    for stations, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    return best_station

def best_cover(states_needed, stations):
    solution = []
    need_cover = states_needed
    while len(need_cover)>0:
        best_station = find_best_stations(need_cover, stations)
        solution.append(best_station)
        need_cover -= stations[best_station]
    return solution

