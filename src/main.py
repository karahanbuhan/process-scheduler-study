from algorithms import fcfs
from fractions import Fraction

processes = [
    {"pid": "p1", "arrival_time": 0, "burst_time": 2},
    {"pid": "p2", "arrival_time": 0, "burst_time": 2},
    {"pid": "p3", "arrival_time": 0, "burst_time": 4},
    {"pid": "p4", "arrival_time": 0, "burst_time": 5},
    {"pid": "p5", "arrival_time": 0, "burst_time": 6},
]

schedules, wt, awt = fcfs(processes)

print("Schedules are ", schedules)
print("Waiting Times are ", wt)
n, d = Fraction.from_float(awt).limit_denominator().as_integer_ratio()
print("Average WT is %s=%s/%s" % (awt, n, d))
