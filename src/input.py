import tkinter as tk
from tkinter import messagebox
from random import randint
from algorithms import run_algorithm
from visualizer import visualize_results

class InputGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Process Scheduler Study")
        self.processes = []
        self.entries = []
        
        # Süreç sayısı
        tk.Label(root, text="Number of Processes (1-10):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.num_processes_var = tk.StringVar(value="3")
        tk.Entry(root, textvariable=self.num_processes_var, width=5).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(root, text="Set Processes", command=self.create_process_inputs).grid(row=0, column=2, padx=5, pady=5)
        
        # Algoritma seçimi
        tk.Label(root, text="Algorithm:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.algo_var = tk.StringVar(value="FCFS")
        tk.OptionMenu(root, self.algo_var, "FCFS", "SJF", "RR").grid(row=1, column=1, padx=5, pady=5)
        
        # Quantum (RR için)
        tk.Label(root, text="Quantum (for RR):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.quantum_var = tk.StringVar(value="2")
        self.quantum_entry = tk.Entry(root, textvariable=self.quantum_var, width=5)
        self.quantum_entry.grid(row=2, column=1, padx=5, pady=5)
        self.quantum_entry.config(state='disabled')
        
        # Algoritma değiştiğinde quantum kontrolü
        self.algo_var.trace("w", self.toggle_quantum)
        
        # Butonlar
        tk.Button(root, text="Generate Random", command=self.generate_random).grid(row=3, column=0, padx=5, pady=5)
        tk.Button(root, text="Run Simulation", command=self.run_simulation).grid(row=3, column=1, padx=5, pady=5)
        
        # Süreç giriş alanı
        self.process_frame = tk.Frame(root)
        self.process_frame.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
        
        # Varsayılan 3 süreç girişi
        self.create_process_inputs()
    
    def toggle_quantum(self, *args):
        """RR seçilirse quantum girişini etkinleştir."""
        self.quantum_entry.config(state='normal' if self.algo_var.get() == "RR" else 'disabled')
    
    def create_process_inputs(self):
        """Süreç sayısı kadar giriş alanı oluştur."""
        try:
            num = int(self.num_processes_var.get())
            if not 1 <= num <= 10:
                raise ValueError("Number of processes must be between 1 and 10")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number (1-10)")
            return
        
        # Eski girişleri temizle
        for widget in self.process_frame.winfo_children():
            widget.destroy()
        self.entries = []
        
        # Başlık satırı
        tk.Label(self.process_frame, text="PID").grid(row=0, column=0, padx=5, pady=2)
        tk.Label(self.process_frame, text="Arrival Time").grid(row=0, column=1, padx=5, pady=2)
        tk.Label(self.process_frame, text="Burst Time").grid(row=0, column=2, padx=5, pady=2)
        
        # Süreç girişleri
        for i in range(num):
            pid_var = tk.StringVar(value=f"p{i+1}")
            arrival_var = tk.StringVar(value="0")  # Arrival time set to 0
            burst_var = tk.StringVar(value=str(randint(1, 10)))
            
            tk.Entry(self.process_frame, textvariable=pid_var, width=10).grid(row=i+1, column=0, padx=5, pady=2)
            tk.Entry(self.process_frame, textvariable=arrival_var, width=10).grid(row=i+1, column=1, padx=5, pady=2)
            tk.Entry(self.process_frame, textvariable=burst_var, width=10).grid(row=i+1, column=2, padx=5, pady=2)
            
            self.entries.append((pid_var, arrival_var, burst_var))
    
    def generate_random(self):
        """Rastgele süreçler üret ve giriş alanlarını doldur."""
        try:
            num = int(self.num_processes_var.get())
            if not 1 <= num <= 10:
                raise ValueError("Number of processes must be between 1 and 10")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number (1-10)")
            return
        
        # Eski girişleri temizle
        for widget in self.process_frame.winfo_children():
            widget.destroy()
        self.entries = []
        
        # Başlık satırı
        tk.Label(self.process_frame, text="PID").grid(row=0, column=0, padx=5, pady=2)
        tk.Label(self.process_frame, text="Arrival Time").grid(row=0, column=1, padx=5, pady=2)
        tk.Label(self.process_frame, text="Burst Time").grid(row=0, column=2, padx=5, pady=2)
        
        # Rastgele süreç girişleri
        for i in range(num):
            pid_var = tk.StringVar(value=f"p{i+1}")
            arrival_var = tk.StringVar(value="0")  # Random arrival time set to 0
            burst_var = tk.StringVar(value=str(randint(1, 10)))
            
            tk.Entry(self.process_frame, textvariable=pid_var, width=10).grid(row=i+1, column=0, padx=5, pady=2)
            tk.Entry(self.process_frame, textvariable=arrival_var, width=10).grid(row=i+1, column=1, padx=5, pady=2)
            tk.Entry(self.process_frame, textvariable=burst_var, width=10).grid(row=i+1, column=2, padx=5, pady=2)
            
            self.entries.append((pid_var, arrival_var, burst_var))
    
    def run_simulation(self):
        """Süreçleri topla, algoritmayı çalıştır ve sonuçları göster."""
        try:
            processes = []
            seen_pids = set()
            for pid_var, arrival_var, burst_var in self.entries:
                pid = pid_var.get().strip()
                if not pid:
                    raise ValueError("PID cannot be empty")
                if pid in seen_pids:
                    raise ValueError(f"Duplicate PID: {pid}")
                seen_pids.add(pid)
                arrival = int(arrival_var.get())
                burst = int(burst_var.get())
                if arrival < 0 or burst <= 0:
                    raise ValueError("Arrival time must be non-negative, burst time must be positive")
                processes.append({
                    "pid": pid,
                    "arrival_time": arrival,
                    "burst_time": burst
                })
            
            algorithm = self.algo_var.get().lower()
            quantum = None
            if algorithm == "rr":
                quantum = int(self.quantum_var.get())
                if quantum <= 0:
                    raise ValueError("Quantum must be positive")
            
            # Algoritmayı çalıştır
            schedule, waiting_times, avg_waiting_time = run_algorithm(processes, algorithm, quantum)
            
            # Sonuçları göster
            visualize_results(schedule, waiting_times, avg_waiting_time, mode='gui')
        
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def get_process_input():
    """GUI'yi başlat."""
    root = tk.Tk()
    app = InputGUI(root)
    root.mainloop()