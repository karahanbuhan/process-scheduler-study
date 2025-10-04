import matplotlib.pyplot as plt

def visualize_results(schedule, waiting_times, avg_waiting_time, mode='gui'):
    """
    Visualize the scheduling results with a Gantt Chart and print waiting times.
    
    Args:
        schedule (list): List of dicts [{'process': str, 'start': int, 'end': int}, ...]
        waiting_times (dict): Waiting times {'pid': int, ...}
        avg_waiting_time (float): Average waiting time
        mode (str): 'gui' for Matplotlib
    """
    if mode == 'gui':
        fig, ax = plt.subplots(figsize=(10, 4))
        for s in schedule:
            ax.barh(s['process'], s['end'] - s['start'], left=s['start'], height=0.4)
        ax.set_xlabel('Time')
        ax.set_ylabel('Processes')
        ax.set_title('Gantt Chart')
        plt.tight_layout()
        plt.show()
        
        # Waiting times ve ortalama yazdır
        print("Waiting Times:")
        for pid, wt in waiting_times.items():
            print(f"{pid}: {wt}")
        print(f"Average Waiting Time: {avg_waiting_time:.2f}")