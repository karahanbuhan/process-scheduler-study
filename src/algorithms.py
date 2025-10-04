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
    # Süreçleri arrival_time'a göre sırala, aynı arrival_time için orijinal sırayı koru
    # Orijinal index'i takip etmek için enumerate kullanıyoruz
    indexed_processes = [(i, p) for i, p in enumerate(processes)]
    sorted_processes = sorted(indexed_processes, key=lambda x: (x[1]['arrival_time'], x[0]))
    
    schedule = []
    waiting_times = {}
    current_time = 0
    
    for _, process in sorted_processes:
        pid = process['pid']
        arrival = process['arrival_time']
        burst = process['burst_time']
        
        # Sürecin başlayacağı zaman: ya arrival_time ya da mevcut zaman (hangisi büyükse)
        start_time = max(current_time, arrival)
        end_time = start_time + burst
        
        # Schedule için ekle
        schedule.append({"process": pid, "start": start_time, "end": end_time})
        
        # Waiting time: Başlama zamanı - varış zamanı
        waiting_times[pid] = start_time - arrival
        
        # Mevcut zamanı güncelle
        current_time = end_time
    
    # Ortalama bekleme süresini hesapla
    avg_waiting_time = sum(waiting_times.values()) / len(waiting_times) if waiting_times else 0
    
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
            - avg_waiting_time: Fraction, average waiting time as a fraction
    """
    # Süreçleri index ile takip et
    indexed_processes = [(i, p) for i, p in enumerate(processes)]
    schedule = []
    waiting_times = {}
    current_time = 0
    completed = set()  # Tamamlanan süreçlerin PID'leri
    
    while len(completed) < len(processes):
        # Hazır süreçler: arrival_time <= current_time ve henüz tamamlanmamış
        ready_processes = [
            (i, p) for i, p in indexed_processes
            if p['pid'] not in completed and p['arrival_time'] <= current_time
        ]
        
        if not ready_processes:
            # Hazır süreç yoksa, en erken gelen sürece ilerle
            future_processes = [(i, p) for i, p in indexed_processes if p['pid'] not in completed]
            if future_processes:
                next_arrival = min(p['arrival_time'] for i, p in future_processes)
                current_time = next_arrival
                continue
        
        # En kısa burst_time'a sahip süreci seç (aynı burst_time'da index'e göre)
        selected = min(ready_processes, key=lambda x: (x[1]['burst_time'], x[0]))
        index, process = selected
        pid = process['pid']
        arrival = process['arrival_time']
        burst = process['burst_time']
        
        # Süreci çalıştır
        start_time = max(current_time, arrival)
        end_time = start_time + burst
        schedule.append({"process": pid, "start": start_time, "end": end_time})
        waiting_times[pid] = start_time - arrival
        completed.add(pid)
        current_time = end_time
    
    # Ortalama bekleme süresi
    total_waiting = sum(waiting_times.values())
    num_processes = len(waiting_times)
    avg_waiting_time = sum(waiting_times.values()) / len(waiting_times) if waiting_times else 0
    
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
    # Süreçleri kopyala ve kalan burst_time'ları takip et
    processes_copy = [
        {"pid": p["pid"], "arrival_time": p["arrival_time"], "burst_time": p["burst_time"], "remaining_time": p["burst_time"]}
        for p in processes
    ]
    indexed_processes = [(i, p) for i, p in enumerate(processes_copy)]
    
    schedule = []
    waiting_times = {p["pid"]: 0 for p in processes}
    completion_times = {p["pid"]: 0 for p in processes}
    current_time = 0
    queue = []
    completed = set()
    
    # İlk hazır süreci bulmak için minimum arrival_time
    if processes_copy:
        current_time = min(p["arrival_time"] for p in processes_copy)
    
    while len(completed) < len(processes):
        # Hazır süreçleri kuyruğa ekle
        ready = [
            (i, p) for i, p in indexed_processes
            if p["pid"] not in completed and p["arrival_time"] <= current_time and p not in [q[1] for q in queue]
        ]
        ready.sort(key=lambda x: (x[1]["arrival_time"], x[0]))
        queue.extend(ready)
        
        if not queue:
            # Kuyruk boşsa, bir sonraki arrival_time'a ilerle
            future_processes = [(i, p) for i, p in indexed_processes if p["pid"] not in completed]
            if future_processes:
                current_time = min(p["arrival_time"] for i, p in future_processes)
                continue
        
        # Kuyruğun başındaki süreci al
        index, process = queue.pop(0)
        pid = process["pid"]
        remaining = process["remaining_time"]
        
        # Quantum veya kalan süre kadar çalıştır
        run_time = min(quantum, remaining)
        schedule.append({"process": pid, "start": current_time, "end": current_time + run_time})
        
        # Süreci güncelle
        process["remaining_time"] -= run_time
        current_time += run_time
        
        # Tamamlandıysa
        if process["remaining_time"] == 0:
            completion_times[pid] = current_time
            completed.add(pid)
        else:
            # Kuyruğa geri ekle
            queue.append((index, process))
    
    # Waiting time = completion_time - arrival_time - burst_time
    for p in processes:
        pid = p["pid"]
        waiting_times[pid] = completion_times[pid] - p["arrival_time"] - p["burst_time"]
    
    # Ortalama bekleme süresi
    total_waiting = sum(waiting_times.values())
    num_processes = len(waiting_times)
    avg_waiting_time = total_waiting / num_processes if num_processes > 0 else 0.0
    
    return schedule, waiting_times, avg_waiting_time