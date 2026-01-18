import matplotlib.pyplot as plt
from fractions import Fraction

from algorithms import ata_and_art


def visualize_results(
    schedule,
    waiting_times,
    avg_waiting_time,
    mode="gui",
    algorithm="Unknown",
    processes=None,
):
    """
    Visualize the scheduling results with a Gantt Chart and display waiting times.

    Args:
        schedule (list): List of dicts [{'process': str, 'start': int, 'end': int}, ...]
        waiting_times (dict): Waiting times {'pid': int, ...}
        avg_waiting_time (float): Average waiting time
        mode (str): 'gui' for Matplotlib
        algorithm (str): Name of the scheduling algorithm (e.g., 'FCFS', 'SJF', 'RR', 'SRTF', 'LJF')
        processes (list): List of process dicts [{'pid': str, 'burst_time': int, ...}, ...]
    """
    if mode == "gui":
        awt_n, awt_d = (
            Fraction.from_float(avg_waiting_time).limit_denominator().as_integer_ratio()
        )

        print("Waiting Times:")
        for pid, wt in waiting_times.items():
            print(f"{pid}: {wt}")
        print("Average WT is %s=%s/%s" % (avg_waiting_time, awt_n, awt_d))

        ata, art = ata_and_art(schedule)
        ata_n, ata_d = (
            Fraction.from_float(ata).limit_denominator().as_integer_ratio()
        )
        print("Average TAT is %s=%s/%s" % (ata, ata_n, ata_d))

        art_n, art_d = (
            Fraction.from_float(art).limit_denominator().as_integer_ratio()
        )
        print("Average RT is %s=%s/%s" % (art, art_n, art_d))

        burst_times_str = "No Processes"
        if processes:
            try:
                burst_times_str = ", ".join(
                    [f"{p['pid']}={p['burst_time']}" for p in processes]
                )
            except (KeyError, TypeError):
                burst_times_str = "Invalid Processes"

        # Gantt Chart
        fig, ax = plt.subplots(figsize=(10, 4))
        for s in schedule:
            try:
                ax.barh(
                    s["process"], s["end"] - s["start"], left=s["start"], height=0.4
                )
            except (KeyError, TypeError):
                print(f"Error: Invalid schedule entry {s}")
                continue

        ax.set_title(
            f"Gantt Chart ({algorithm}, Processes: {burst_times_str}, AWT: {avg_waiting_time:.2f} = {awt_n}/{awt_d}, ATA: {ata:.2f} = {ata_n}/{ata_d}, ART: {art:.2f} = {art_n}/{art_d})"
        )
        ax.set_xlabel("Time")
        ax.set_ylabel("Processes")
        plt.tight_layout()
        plt.show()
