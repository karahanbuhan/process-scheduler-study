from algorithms import fcfs, sjf_non_preemptive, rr
from fractions import Fraction

def _rr_test():
    processes = [
        {"pid": "p1", "arrival_time": 0, "burst_time": 2},
        {"pid": "p2", "arrival_time": 0, "burst_time": 3},
        {"pid": "p3", "arrival_time": 0, "burst_time": 2},
    ]

    schedules, wt, awt = rr(processes, 1)

    print("Schedules are ", schedules)
    print("Waiting Times are ", wt)
    n, d = Fraction.from_float(awt).limit_denominator().as_integer_ratio()
    print("Average WT is %s=%s/%s" % (awt, n, d))

def _sfj_test():
    processes = [
        {"pid": "p1", "arrival_time": 0, "burst_time": 2},
        {"pid": "p2", "arrival_time": 0, "burst_time": 1},
        {"pid": "p3", "arrival_time": 0, "burst_time": 3},
        {"pid": "p4", "arrival_time": 0, "burst_time": 2},
    ]

    schedules, wt, awt = sjf_non_preemptive(processes)

    print("Schedules are ", schedules)
    print("Waiting Times are ", wt)
    n, d = Fraction.from_float(awt).limit_denominator().as_integer_ratio()
    print("Average WT is %s=%s/%s" % (awt, n, d))

def _fcfs_test():
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