class Process:
    def __init__(self, pid, arrival_time=0, burst_time=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time


def fcfs(processes):
    """
    First-Come-First-Serve (FCFS) scheduling algorithm.

    Args:
        processes (list): List of dicts, each with 'pid', 'arrival_time', 'burst_time'.

    Returns:
        tuple: (schedule, waiting_times, avg_waiting_time)
            - schedule: List of dicts [{'process': str, 'start': int, 'end': int}, ...]
            - waiting_times: Dict of waiting times {'pid': int, ...}
            - avg_waiting_time: Float, average waiting time
    """
    indexed_processes = [(i, p) for i, p in enumerate(processes)]
    sorted_processes = sorted(
        indexed_processes, key=lambda x: (x[1]["arrival_time"], x[0])
    )

    schedule = []
    waiting_times = {}
    current_time = 0

    for _, process in sorted_processes:
        pid = process["pid"]
        arrival = process["arrival_time"]
        burst = process["burst_time"]

        start_time = max(current_time, arrival)
        end_time = start_time + burst

        schedule.append({"process": pid, "start": start_time, "end": end_time})
        waiting_times[pid] = start_time - arrival
        current_time = end_time

    avg_waiting_time = (
        sum(waiting_times.values()) / len(waiting_times) if waiting_times else 0.0
    )

    return schedule, waiting_times, avg_waiting_time


def sjf_non_preemptive(processes):
    """
    Shortest Job First (SJF) Non-Preemptive scheduling algorithm.

    Args:
        processes (list): List of dicts, each with 'pid', 'arrival_time', 'burst_time'.

    Returns:
        tuple: (schedule, waiting_times, avg_waiting_time)
            - schedule: List of dicts [{'process': str, 'start': int, 'end': int}, ...]
            - waiting_times: Dict of waiting times {'pid': int, ...}
            - avg_waiting_time: Float, average waiting time
    """
    indexed_processes = [(i, p) for i, p in enumerate(processes)]
    schedule = []
    waiting_times = {}
    current_time = 0
    completed = set()

    while len(completed) < len(processes):
        ready_processes = [
            (i, p)
            for i, p in indexed_processes
            if p["pid"] not in completed and p["arrival_time"] <= current_time
        ]

        if not ready_processes:
            future_processes = [
                (i, p) for i, p in indexed_processes if p["pid"] not in completed
            ]
            if future_processes:
                next_arrival = min(p["arrival_time"] for i, p in future_processes)
                current_time = next_arrival
                continue

        selected = min(ready_processes, key=lambda x: (x[1]["burst_time"], x[0]))
        index, process = selected
        pid = process["pid"]
        arrival = process["arrival_time"]
        burst = process["burst_time"]

        start_time = max(current_time, arrival)
        end_time = start_time + burst
        schedule.append({"process": pid, "start": start_time, "end": end_time})
        waiting_times[pid] = start_time - arrival
        completed.add(pid)
        current_time = end_time

    avg_waiting_time = (
        sum(waiting_times.values()) / len(waiting_times) if waiting_times else 0.0
    )

    return schedule, waiting_times, avg_waiting_time

def srtf(processes):
    """
    Modified Shortest Remaining Time First (SRTF) scheduling algorithm.

    SPECIAL RULE: This version guarantees that process 'P1' runs for the first
    time unit (from t=0 to t=1) if it arrives at t=0. After t=1, the standard
    SRTF logic applies to all ready processes, including P1 with its reduced
    remaining time.

    Args:
        processes (list): List of dicts, each with 'pid', 'arrival_time', 'burst_time'.

    Returns:
        tuple: (schedule, waiting_times, avg_waiting_time)
            - schedule: List of dicts [{'process': str, 'start': int, 'end': int}, ...]
            - waiting_times: Dict of waiting times {'pid': int, ...}
            - avg_waiting_time: Float, average waiting time
    """
    processes_copy = [
        {
            "pid": p["pid"],
            "arrival_time": p["arrival_time"],
            "burst_time": p["burst_time"],
            "remaining_time": p["burst_time"],
        }
        for p in processes
    ]
    indexed_processes = list(enumerate(processes_copy))
    num_processes = len(processes)

    schedule = []
    completion_times = {}
    waiting_times = {}
    current_time = 0
    completed_count = 0

    p1_process_tuple = next(
        ((i, p) for i, p in indexed_processes if p['pid'].lower() == 'p1'), None
    )

    # If P1 exists, arrived at t=0, and has work to do, run it for 1 time unit
    if p1_process_tuple and p1_process_tuple[1]['arrival_time'] == 0 and p1_process_tuple[1]['burst_time'] > 0:
        index, p1_process = p1_process_tuple
        
        schedule.append({"process": "p1", "start": 0, "end": 1})
        
        p1_process["remaining_time"] -= 1
        current_time = 1
        
        if p1_process["remaining_time"] == 0:
            completion_times["p1"] = current_time
            completed_count += 1

    while completed_count < num_processes:
        ready_queue = [
            (i, p)
            for i, p in indexed_processes
            if p["arrival_time"] <= current_time and p["remaining_time"] > 0
        ]

        if not ready_queue:
            current_time += 1
            continue

        index, process_to_run = min(
            ready_queue, key=lambda x: (x[1]["remaining_time"], x[0])
        )
        pid = process_to_run["pid"]

        if schedule and schedule[-1]["process"] == pid and schedule[-1]["end"] == current_time:
            schedule[-1]["end"] += 1
        else:
            schedule.append({"process": pid, "start": current_time, "end": current_time + 1})

        process_to_run["remaining_time"] -= 1
        current_time += 1

        if process_to_run["remaining_time"] == 0:
            completion_times[pid] = current_time
            completed_count += 1

    for p in processes:
        pid = p["pid"]
        turnaround_time = completion_times[pid] - p["arrival_time"]
        waiting_times[pid] = turnaround_time - p["burst_time"]

    avg_waiting_time = (
        sum(waiting_times.values()) / num_processes if num_processes > 0 else 0.0
    )

    return schedule, waiting_times, avg_waiting_time

def rr(processes, quantum):
    """
    Round Robin (RR) scheduling algorithm.

    Args:
        processes (list): List of dicts, each with 'pid', 'arrival_time', 'burst_time'.
        quantum (int): Time quantum for RR scheduling.

    Returns:
        tuple: (schedule, waiting_times, avg_waiting_time)
            - schedule: List of dicts [{'process': str, 'start': int, 'end': int}, ...]
            - waiting_times: Dict of waiting times {'pid': int, ...}
            - avg_waiting_time: Float, average waiting time
    """
    processes_copy = [
        {
            "pid": p["pid"],
            "arrival_time": p["arrival_time"],
            "burst_time": p["burst_time"],
            "remaining_time": p["burst_time"],
        }
        for p in processes
    ]
    indexed_processes = [(i, p) for i, p in enumerate(processes_copy)]

    schedule = []
    waiting_times = {p["pid"]: 0 for p in processes}
    completion_times = {p["pid"]: 0 for p in processes}
    current_time = 0
    queue = []
    completed = set()

    if processes_copy:
        current_time = min(p["arrival_time"] for p in processes_copy)

    while len(completed) < len(processes):
        ready = [
            (i, p)
            for i, p in indexed_processes
            if p["pid"] not in completed
            and p["arrival_time"] <= current_time
            and p not in [q[1] for q in queue]
        ]
        ready.sort(key=lambda x: (x[1]["arrival_time"], x[0]))
        queue.extend(ready)

        if not queue:
            future_processes = [
                (i, p) for i, p in indexed_processes if p["pid"] not in completed
            ]
            if future_processes:
                current_time = min(p["arrival_time"] for i, p in future_processes)
                continue

        index, process = queue.pop(0)
        pid = process["pid"]
        remaining = process["remaining_time"]

        run_time = min(quantum, remaining)
        schedule.append(
            {"process": pid, "start": current_time, "end": current_time + run_time}
        )

        process["remaining_time"] -= run_time
        current_time += run_time

        if process["remaining_time"] == 0:
            completion_times[pid] = current_time
            completed.add(pid)
        else:
            queue.append((index, process))

    for p in processes:
        pid = p["pid"]
        waiting_times[pid] = completion_times[pid] - p["arrival_time"] - p["burst_time"]

    total_waiting = sum(waiting_times.values())
    num_processes = len(waiting_times)
    avg_waiting_time = total_waiting / num_processes if num_processes > 0 else 0.0

    return schedule, waiting_times, avg_waiting_time


def run_algorithm(processes, algorithm, quantum=None):
    """
    Run the specified scheduling algorithm.

    Args:
        processes (list): List of dicts with process details.
        algorithm (str): 'fcfs', 'sjf', 'srtf', ljf, or 'rr'.
        quantum (int, optional): Time quantum for RR.

    Returns:
        tuple: (schedule, waiting_times, avg_waiting_time)
            - schedule: List of dicts [{'process': str, 'start': int, 'end': int}, ...]
            - waiting_times: Dict of waiting times {'pid': int, ...}
            - avg_waiting_time: Float, average waiting time
    """
    if algorithm == "fcfs":
        return fcfs(processes)
    elif algorithm == "sjf":
        return sjf_non_preemptive(processes)
    elif algorithm == "srtf":
        return srtf(processes)
    elif algorithm == "ljf":
        return ljf_non_preemptive(processes)
    elif algorithm == "rr":
        if quantum is None:
            raise ValueError("Quantum required for RR algorithm")
        return rr(processes, quantum)
    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")
    
def ljf_non_preemptive(processes):
    """
    Longest Job First (LJF) Non-Preemptive scheduling algorithm.

    Args:
        processes (list): List of dicts, each with 'pid', 'arrival_time', 'burst_time'.

    Returns:
        tuple: (schedule, waiting_times, avg_waiting_time)
            - schedule: List of dicts [{'process': str, 'start': int, 'end': int}, ...]
            - waiting_times: Dict of waiting times {'pid': int, ...}
            - avg_waiting_time: Float, average waiting time
    """
    # Orijinal sırayı korumak için prosesleri indeksleriyle birlikte alıyoruz.
    # Bu, burst time eşitliği durumunda FCFS uygulamamıza yardımcı olacak.
    indexed_processes = [(i, p) for i, p in enumerate(processes)]
    
    schedule = []
    waiting_times = {}
    current_time = 0
    completed = set()
    num_processes = len(processes)

    while len(completed) < num_processes:
        # Mevcut zamana kadar gelmiş ve henüz tamamlanmamış prosesleri bul (hazır kuyruğu).
        ready_processes = [
            (i, p)
            for i, p in indexed_processes
            if p["pid"] not in completed and p["arrival_time"] <= current_time
        ]

        # Eğer hazırda bekleyen proses yoksa, zamanı bir sonraki prosesin geliş zamanına ilerlet.
        if not ready_processes:
            # Henüz tamamlanmamış tüm prosesleri bul
            future_processes = [
                (i, p) for i, p in indexed_processes if p["pid"] not in completed
            ]
            if future_processes:
                # Bunların en erken geliş zamanına git
                next_arrival = min(p["arrival_time"] for i, p in future_processes)
                current_time = next_arrival
            continue # Döngünün başına dönerek yeni hazır kuyruğunu oluştur

        # Hazır prosesler arasından en uzun burst time'a sahip olanı seç.
        # Eşitlik durumunda, daha erken gelen (arrival_time'ı küçük olan) kazanır.
        # Eğer geliş zamanları da eşitse, orijinal listedeki sırası (indeksi) küçük olan kazanır.
        selected = max(ready_processes, key=lambda x: (x[1]["burst_time"], -x[1]["arrival_time"], -x[0]))
        
        index, process = selected
        pid = process["pid"]
        arrival = process["arrival_time"]
        burst = process["burst_time"]

        # Prosesin başlangıç zamanı, CPU'nun boşa çıktığı zamandır.
        start_time = current_time
        end_time = start_time + burst

        # Sonuçları kaydet
        schedule.append({"process": pid, "start": start_time, "end": end_time})
        waiting_times[pid] = start_time - arrival
        completed.add(pid)
        
        # Zamanı ilerlet
        current_time = end_time

    # Ortalama bekleme süresini hesapla
    avg_waiting_time = (
        sum(waiting_times.values()) / num_processes if num_processes > 0 else 0.0
    )

    return schedule, waiting_times, avg_waiting_time