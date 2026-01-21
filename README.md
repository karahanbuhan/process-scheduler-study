# Process Scheduler Study

**process_scheduler_study** is a Python-based educational tool designed to simulate CPU scheduling algorithms (FCFS, SJF Non-Preemptive, RR (Round Robin), LJF Non-Preemptive and SRTF) for operating systems courses.
It allows users to input process details (PID, arrival time, burst time), select an algorithm, and specify a quantum for Round Robin.
The tool generates a Gantt Chart using Matplotlib and calculates waiting times, average waiting time, average response time and average turn around time to aid in studying scheduling concepts.

---

## Screenshots
<img width="2370" height="1500" alt="fcfs" src="https://github.com/user-attachments/assets/7ac7fe68-6d88-47a5-80db-b86f4328accb" />
<img width="2370" height="1500" alt="rr" src="https://github.com/user-attachments/assets/f43a8577-9e91-4d7d-8e84-5c433bfb0786" />

> *AWT stands for Average Waiting Time, ATA for Average Turn-Around Time, ART for Average Response Time in graph titles*.

---

## Features

* Supports FCFS, SJF (Non-Preemptive), Round Robin, LJF (Non-Preemptive) and SRTF scheduling algorithms.
* Interactive Tkinter GUI for entering process details and algorithm selection.
* Random process generation for quick testing.
* Visualizes results with Gantt Charts and displays waiting times, response times and turn around times.
* Calculates average waiting time, response time and turn around times as a float (e.g., 5.4) and also in fraction format (e.g. 3/10).
* Shows each WT(pid), TAT(pid), RT(pid) instances in console.

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
5. Click **"Run"** to simulate and view the Gantt Chart, waiting times, average waiting time, average response time and average turn around time.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
