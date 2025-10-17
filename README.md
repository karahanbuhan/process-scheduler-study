# Process Scheduler Study

**process_scheduler_study** is a Python-based educational tool designed to simulate CPU scheduling algorithms (FCFS, SJF Non-Preemptive, RR (Round Robin) and SRTF) for operating systems courses.
It allows users to input process details (PID, arrival time, burst time), select an algorithm, and specify a quantum for Round Robin.
The tool generates a Gantt Chart using Matplotlib and calculates waiting times and average waiting time to aid in studying scheduling concepts.

---

## Screenshots

<img width="2370" height="1500" alt="screenshot1" src="https://github.com/user-attachments/assets/1a4f1a0f-21a1-4260-b05d-247b3bcb88e2" />

<img width="2370" height="1500" alt="screenshot2" src="https://github.com/user-attachments/assets/0f1c61de-5c32-4ac5-aca6-b6b59e0ddbf6" />

---

## Features

* Supports FCFS, SJF (Non-Preemptive), Round Robin and SRTF scheduling algorithms.
* Interactive Tkinter GUI for entering process details and algorithm selection.
* Random process generation for quick testing.
* Visualizes results with Gantt Charts and displays waiting times.
* Calculates average waiting time as a float (e.g., 5.4) and also in fraction format (e.g. 3/10).

---

## Requirements

* Python 3.6 or higher
* Matplotlib (`pip install matplotlib`)

---

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/your-username/process_scheduler_study.git
cd process_scheduler_study
```

## Install Dependencies and Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python3 src/main.py
```

This launches a Tkinter GUI where you can input processes, select an algorithm, and view the Gantt Chart and results.

---

## Usage

1. Enter the number of processes (1–10) in the GUI.
2. Provide PID, arrival time, and burst time for each process, or click **"Generate Random"** for automatic input.
3. Select an algorithm (**FCFS**, **SJF**, **RR** or **SRTF**) from the dropdown menu.
4. For **RR**, specify a quantum value.
5. Click **"Run"** to simulate and view the Gantt Chart, waiting times, and average waiting time.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
