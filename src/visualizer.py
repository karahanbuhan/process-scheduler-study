import matplotlib.pyplot as plt
from fractions import Fraction

def visualize_results(schedule, waiting_times, avg_waiting_time, mode='gui'):
    """
    Visualize the scheduling results with a Gantt Chart and display waiting times.
    
    Args:
        schedule (list): List of dicts [{'process': str, 'start': int, 'end': int}, ...]
        waiting_times (dict): Waiting times {'pid': int, ...}
        avg_waiting_time (float): Average waiting time
        mode (str): 'gui' for Matplotlib
    """
    if mode == 'gui':
        # Kesir formatını hesapla
        n, d = Fraction.from_float(avg_waiting_time).limit_denominator().as_integer_ratio()
        
        # Konsol çıktısı
        print("Waiting Times:")
        for pid, wt in waiting_times.items():
            print(f"{pid}: {wt}")
        print("Average WT is %s=%s/%s" % (avg_waiting_time, n, d))
        
        # Gantt Chart
        fig, ax = plt.subplots(figsize=(10, 4))
        for s in schedule:
            ax.barh(s['process'], s['end'] - s['start'], left=s['start'], height=0.4)
        
        # AWT'yi grafik başlığına ekle
        ax.set_title(f'Gantt Chart (Avg Waiting Time: {avg_waiting_time:.2f} = {n}/{d})')
        ax.set_xlabel('Time')
        ax.set_ylabel('Processes')
        plt.tight_layout()
        plt.show()