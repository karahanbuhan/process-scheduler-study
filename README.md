process_scheduler_study
process_scheduler_study is a Python-based educational tool designed to simulate CPU scheduling algorithms (FCFS, SJF Non-Preemptive, and RR) for operating systems courses. It allows users to input process details (PID, arrival time, burst time), select an algorithm, and specify a quantum for Round Robin. The tool generates a Gantt Chart using Matplotlib and calculates waiting times and average waiting time to aid in studying scheduling concepts.
Features

Supports FCFS, SJF (Non-Preemptive), and Round Robin scheduling algorithms.
Interactive Tkinter GUI for entering process details and algorithm selection.
Random process generation for quick testing.
Visualizes results with Gantt Charts and displays waiting times.
Calculates average waiting time as a float (e.g., 5.4).

Requirements

Python 3.6 or higher
Matplotlib (pip install matplotlib)

Setup Instructions

Clone the Repository:
git clone https://github.com/your-username/process_scheduler_study.git
cd process_scheduler_study

Create and Activate a Virtual Environment:

Linux/MacOS:python -m venv venv
source venv/bin/activate

Windows:python -m venv venv
venv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt

Run the Application:
python main.py

This launches a Tkinter GUI where you can input processes, select an algorithm, and view the Gantt Chart and results.

Usage

Enter the number of processes (1–10) in the GUI.
Provide PID, arrival time, and burst time for each process, or click "Generate Random" for automatic input.
Select an algorithm (FCFS, SJF, or RR) from the dropdown menu.
For RR, specify a quantum value.
Click "Run" to simulate and view the Gantt Chart, waiting times, and average waiting time.

Project Structure
process_scheduler_study/
├── venv/                  # Virtual environment (not included in Git)
├── main.py                # Main script to run the GUI
├── input.py               # Tkinter GUI for input collection
├── algorithms.py          # FCFS, SJF, and RR implementations
├── visualizer.py          # Gantt Chart and result visualization
├── LICENSE                # MIT License
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies

License
This project is licensed under the MIT License - see the LICENSE file for details.