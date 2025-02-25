from math import inf

def get_next_index(index,n):
    return (index + 1) % n

def canCompleteCircuit( gas, cost) -> int:
    n = len(gas)
    cum_tank_diff = 0
    start_index = None
    for i in range(len(gas)):
        cum_tank_diff += gas[i] - cost[i]
        if cum_tank_diff < 0 :
            start_index = i+1
            cum_tank_diff = 0
    start_index = start_index % n
    if start_index is None:
        return -1
    curr_index = get_next_index(start_index, n)
    fuel_diff = gas[start_index] - cost[start_index]
    fuel_left = fuel_diff + gas[curr_index]
    while curr_index != start_index:
        if fuel_left < cost[curr_index]:
            return -1
        fuel_diff = fuel_left - cost[curr_index]
        curr_index = get_next_index(curr_index, n)
        fuel_left = fuel_diff + gas[curr_index]
    return start_index

def canCompleteCircuit1( gas, cost) -> int:
    diff = list(map(lambda x, y: x - y, gas, cost))
    if sum(cost) > sum(gas):
        return -1
    n = len(gas)
    cum_tank_diff = 0
    start_index = 0
    for i in range(n):
        cum_tank_diff += gas[i] - cost[i]
        if cum_tank_diff <= 0:
            start_index = i + 1
            cum_tank_diff = 0
    start_index = start_index % n
    return start_index


# print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
# print(canCompleteCircuit([2,3,4], [3,4,3]))
# print(canCompleteCircuit([5,8,2,8], [6,5,6,6]))


# print(canCompleteCircuit1([1,2,3,4,5], [3,4,5,1,2]))
# print(canCompleteCircuit1([2,3,4], [3,4,3]))
# print(canCompleteCircuit1([3,1,1], [1,2,2]))
print(canCompleteCircuit1([5], [4]))
# print(canCompleteCircuit1([5,8,2,8], [6,5,6,6]))
# print(canCompleteCircuit1([5,1,2,3,4], [4,4,1,5,1]))