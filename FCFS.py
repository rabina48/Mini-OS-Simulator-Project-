# # # import tkinter as tk
# # # from tkinter import ttk, messagebox

# # # class SchedulerOS(tk.Tk):
# # #     def __init__(self):
# # #         super().__init__()
# # #         self.title("Mini OS Simulator – CPU Scheduling")
# # #         self.geometry("1000x650")

# # #         self.processes = []

# # #         self.create_widgets()

# # #     def create_widgets(self):
# # #         # -------- Input Frame --------
# # #         input_frame = tk.LabelFrame(self, text="Add Process", font=("Arial", 12))
# # #         input_frame.pack(fill="x", padx=10, pady=10)

# # #         tk.Label(input_frame, text="Process ID").grid(row=0, column=0, padx=5)
# # #         tk.Label(input_frame, text="Arrival Time").grid(row=0, column=2, padx=5)
# # #         tk.Label(input_frame, text="Burst Time").grid(row=0, column=4, padx=5)

# # #         self.pid_entry = tk.Entry(input_frame, width=10)
# # #         self.at_entry = tk.Entry(input_frame, width=10)
# # #         self.bt_entry = tk.Entry(input_frame, width=10)

# # #         self.pid_entry.grid(row=0, column=1)
# # #         self.at_entry.grid(row=0, column=3)
# # #         self.bt_entry.grid(row=0, column=5)

# # #         tk.Button(input_frame, text="Add Process", command=self.add_process)\
# # #             .grid(row=0, column=6, padx=10)

# # #         # -------- Options --------
# # #         option_frame = tk.LabelFrame(self, text="Scheduling Options", font=("Arial", 12))
# # #         option_frame.pack(fill="x", padx=10, pady=10)

# # #         self.algorithm = tk.StringVar(value="FCFS")
# # #         self.mode = tk.StringVar(value="Non-Preemptive")

# # #         ttk.Radiobutton(option_frame, text="FCFS",
# # #                         variable=self.algorithm, value="FCFS").pack(side="left", padx=10)
# # #         ttk.Radiobutton(option_frame, text="SJF",
# # #                         variable=self.algorithm, value="SJF").pack(side="left", padx=10)

# # #         ttk.Radiobutton(option_frame, text="Non-Preemptive",
# # #                         variable=self.mode, value="Non-Preemptive").pack(side="left", padx=20)
# # #         ttk.Radiobutton(option_frame, text="Preemptive",
# # #                         variable=self.mode, value="Preemptive").pack(side="left")

# # #         tk.Button(option_frame, text="Run Scheduling",
# # #                   command=self.run_scheduling).pack(side="right", padx=20)

# # #         # -------- Process Table --------
# # #         self.table = ttk.Treeview(self, columns=("PID", "AT", "BT", "WT", "TAT"),
# # #                                   show="headings", height=8)
# # #         for col in ("PID", "AT", "BT", "WT", "TAT"):
# # #             self.table.heading(col, text=col)
# # #         self.table.pack(fill="x", padx=10, pady=10)

# # #         # -------- Gantt Chart --------
# # #         tk.Label(self, text="Gantt Chart", font=("Arial", 14)).pack()
# # #         self.canvas = tk.Canvas(self, height=120, bg="white")
# # #         self.canvas.pack(fill="x", padx=10, pady=10)

# # #     # ---------------- Logic ----------------
# # #     def add_process(self):
# # #         try:
# # #             pid = self.pid_entry.get()
# # #             at = int(self.at_entry.get())
# # #             bt = int(self.bt_entry.get())

# # #             if not pid:
# # #                 raise ValueError

# # #             self.processes.append({
# # #                 "pid": pid,
# # #                 "at": at,
# # #                 "bt": bt
# # #             })

# # #             self.table.insert("", "end", values=(pid, at, bt, "-", "-"))

# # #             self.pid_entry.delete(0, tk.END)
# # #             self.at_entry.delete(0, tk.END)
# # #             self.bt_entry.delete(0, tk.END)

# # #         except:
# # #             messagebox.showerror("Error", "Invalid input")

# # #     def run_scheduling(self):
# # #         if not self.processes:
# # #             return

# # #         if self.algorithm.get() == "FCFS":
# # #             schedule = self.fcfs()
# # #         else:
# # #             schedule = self.sjf()

# # #         self.display_results(schedule)
# # #         self.draw_gantt(schedule)

# # #     # ---------------- FCFS ----------------
# # #     def fcfs(self):
# # #         time = 0
# # #         result = []
# # #         for p in sorted(self.processes, key=lambda x: x["at"]):
# # #             if time < p["at"]:
# # #                 time = p["at"]
# # #             start = time
# # #             time += p["bt"]
# # #             result.append((p["pid"], start, time))
# # #         return result

# # #     # ---------------- SJF ----------------
# # #     def sjf(self):
# # #         time = 0
# # #         completed = []
# # #         ready = []
# # #         processes = self.processes.copy()

# # #         while processes or ready:
# # #             for p in processes[:]:
# # #                 if p["at"] <= time:
# # #                     ready.append(p)
# # #                     processes.remove(p)

# # #             if not ready:
# # #                 time += 1
# # #                 continue

# # #             if self.mode.get() == "Non-Preemptive":
# # #                 p = min(ready, key=lambda x: x["bt"])
# # #                 ready.remove(p)
# # #                 start = time
# # #                 time += p["bt"]
# # #                 completed.append((p["pid"], start, time))
# # #             else:
# # #                 p = min(ready, key=lambda x: x["bt"])
# # #                 start = time
# # #                 time += 1
# # #                 p["bt"] -= 1
# # #                 completed.append((p["pid"], start, time))
# # #                 if p["bt"] == 0:
# # #                     ready.remove(p)

# # #         return completed

# # #     # ---------------- Results ----------------
# # #     def display_results(self, schedule):
# # #         self.table.delete(*self.table.get_children())
# # #         for p in self.processes:
# # #             completion = max(t for pid, _, t in schedule if pid == p["pid"])
# # #             tat = completion - p["at"]
# # #             wt = tat - p["bt"]
# # #             self.table.insert("", "end",
# # #                               values=(p["pid"], p["at"], p["bt"], wt, tat))

# # #     # ---------------- Gantt Chart ----------------
# # #     def draw_gantt(self, schedule):
# # #         self.canvas.delete("all")
# # #         x = 20
# # #         for pid, start, end in schedule:
# # #             width = (end - start) * 30
# # #             self.canvas.create_rectangle(x, 40, x + width, 80, fill="skyblue")
# # #             self.canvas.create_text(x + width/2, 60, text=pid)
# # #             self.canvas.create_text(x, 90, text=start)
# # #             x += width
# # #         self.canvas.create_text(x, 90, text=schedule[-1][2])

# # # # ---------------- Run ----------------
# # # if __name__ == "__main__":
# # #     app = SchedulerOS()
# # #     app.mainloop()
# # import tkinter as tk
# # from tkinter import ttk, messagebox

# # class SchedulerOS(tk.Tk):
# #     def __init__(self):
# #         super().__init__()
# #         self.title("Mini OS Simulator – CPU Scheduling")
# #         self.geometry("1050x700")

# #         self.processes = []     # stores user entered processes
# #         self.schedule = []      # stores final schedule

# #         self.create_widgets()

# #     # ---------------- GUI ----------------
# #     def create_widgets(self):

# #         # -------- Input Frame --------
# #         input_frame = tk.LabelFrame(self, text="Add Process", font=("Arial", 12))
# #         input_frame.pack(fill="x", padx=10, pady=10)

# #         tk.Label(input_frame, text="PID").grid(row=0, column=0, padx=5)
# #         tk.Label(input_frame, text="Arrival Time").grid(row=0, column=2, padx=5)
# #         tk.Label(input_frame, text="Burst Time").grid(row=0, column=4, padx=5)

# #         self.pid_entry = tk.Entry(input_frame, width=10)
# #         self.at_entry = tk.Entry(input_frame, width=10)
# #         self.bt_entry = tk.Entry(input_frame, width=10)

# #         self.pid_entry.grid(row=0, column=1)
# #         self.at_entry.grid(row=0, column=3)
# #         self.bt_entry.grid(row=0, column=5)

# #         tk.Button(input_frame, text="Add Process", command=self.add_process)\
# #             .grid(row=0, column=6, padx=10)

# #         # -------- Options --------
# #         option_frame = tk.LabelFrame(self, text="Scheduling Options", font=("Arial", 12))
# #         option_frame.pack(fill="x", padx=10, pady=10)

# #         self.algorithm = tk.StringVar(value="FCFS")
# #         self.mode = tk.StringVar(value="Non-Preemptive")

# #         ttk.Radiobutton(option_frame, text="FCFS",
# #                         variable=self.algorithm, value="FCFS").pack(side="left", padx=10)
# #         ttk.Radiobutton(option_frame, text="SJF",
# #                         variable=self.algorithm, value="SJF").pack(side="left", padx=10)

# #         ttk.Radiobutton(option_frame, text="Non-Preemptive",
# #                         variable=self.mode, value="Non-Preemptive").pack(side="left", padx=20)
# #         ttk.Radiobutton(option_frame, text="Preemptive",
# #                         variable=self.mode, value="Preemptive").pack(side="left")

# #         tk.Button(option_frame, text="Run Scheduling",
# #                   command=self.run_scheduling).pack(side="right", padx=20)

# #         # -------- Process Table --------
# #         self.table = ttk.Treeview(self, columns=("PID", "AT", "BT", "WT", "TAT"),
# #                                   show="headings", height=8)
# #         for col in ("PID", "AT", "BT", "WT", "TAT"):
# #             self.table.heading(col, text=col)
# #         self.table.pack(fill="x", padx=10, pady=10)

# #         # -------- Gantt Chart --------
# #         tk.Label(self, text="Gantt Chart", font=("Arial", 14)).pack()
# #         self.canvas = tk.Canvas(self, height=150, bg="white")
# #         self.canvas.pack(fill="x", padx=10, pady=10)

# #     # ---------------- Add Process ----------------
# #     def add_process(self):
# #         try:
# #             pid = self.pid_entry.get()
# #             at = int(self.at_entry.get())
# #             bt = int(self.bt_entry.get())

# #             if not pid:
# #                 raise ValueError

# #             self.processes.append({
# #                 "pid": pid,
# #                 "at": at,
# #                 "bt": bt,
# #                 "remaining": bt
# #             })

# #             self.table.insert("", "end", values=(pid, at, bt, "-", "-"))

# #             self.pid_entry.delete(0, tk.END)
# #             self.at_entry.delete(0, tk.END)
# #             self.bt_entry.delete(0, tk.END)

# #         except:
# #             messagebox.showerror("Error", "Invalid process details")

# #     # ---------------- Run Scheduling ----------------
# #     def run_scheduling(self):
# #         if not self.processes:
# #             messagebox.showwarning("Warning", "Add processes first!")
# #             return

# #         self.schedule.clear()

# #         if self.algorithm.get() == "FCFS":
# #             self.fcfs()
# #         else:
# #             self.sjf()

# #         self.calculate_times()
# #         self.draw_gantt()

# #     # ---------------- FCFS ----------------
# #     def fcfs(self):
# #         time = 0
# #         for p in sorted(self.processes, key=lambda x: x["at"]):
# #             if time < p["at"]:
# #                 time = p["at"]
# #             start = time
# #             end = start + p["bt"]
# #             time = end
# #             self.schedule.append((p["pid"], start, end))

# #     # ---------------- SJF ----------------
# #     def sjf(self):
# #         time = 0
# #         completed = 0
# #         n = len(self.processes)

# #         while completed < n:
# #             ready = [p for p in self.processes if p["at"] <= time and p["remaining"] > 0]

# #             if not ready:
# #                 time += 1
# #                 continue

# #             if self.mode.get() == "Non-Preemptive":
# #                 p = min(ready, key=lambda x: x["remaining"])
# #                 start = time
# #                 time += p["remaining"]
# #                 p["remaining"] = 0
# #                 completed += 1
# #                 self.schedule.append((p["pid"], start, time))
# #             else:
# #                 p = min(ready, key=lambda x: x["remaining"])
# #                 start = time
# #                 time += 1
# #                 p["remaining"] -= 1
# #                 self.schedule.append((p["pid"], start, time))
# #                 if p["remaining"] == 0:
# #                     completed += 1

# #     # ---------------- Calculate WT & TAT ----------------
# #     def calculate_times(self):
# #         self.table.delete(*self.table.get_children())

# #         for p in self.processes:
# #             completion = max(end for pid, _, end in self.schedule if pid == p["pid"])
# #             tat = completion - p["at"]
# #             wt = tat - p["bt"]

# #             self.table.insert("", "end",
# #                               values=(p["pid"], p["at"], p["bt"], wt, tat))

# #     # ---------------- Draw Gantt Chart ----------------
# #     def draw_gantt(self):
# #         self.canvas.delete("all")
# #         x = 20

# #         for pid, start, end in self.schedule:
# #             width = (end - start) * 30
# #             self.canvas.create_rectangle(x, 50, x + width, 100, fill="lightblue")
# #             self.canvas.create_text(x + width/2, 75, text=pid)
# #             self.canvas.create_text(x, 110, text=start)
# #             x += width

# #         self.canvas.create_text(x, 110, text=self.schedule[-1][2])

# # # ---------------- Run ----------------
# # if __name__ == "__main__":
# #     app = SchedulerOS()
# #     app.mainloop()
# import tkinter as tk
# from tkinter import ttk, messagebox

# class SchedulerOS(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Mini OS Simulator – CPU Scheduling")
#         self.geometry("1100x750")

#         self.processes = []
#         self.schedule = []

#         self.create_widgets()

#     # ---------------- GUI ----------------
#     def create_widgets(self):

#         # -------- Input Frame --------
#         input_frame = tk.LabelFrame(self, text="Add Process", font=("Arial", 12))
#         input_frame.pack(fill="x", padx=10, pady=10)

#         tk.Label(input_frame, text="PID").grid(row=0, column=0, padx=5)
#         tk.Label(input_frame, text="Arrival Time").grid(row=0, column=2, padx=5)
#         tk.Label(input_frame, text="Burst Time").grid(row=0, column=4, padx=5)

#         self.pid_entry = tk.Entry(input_frame, width=10)
#         self.at_entry = tk.Entry(input_frame, width=10)
#         self.bt_entry = tk.Entry(input_frame, width=10)

#         self.pid_entry.grid(row=0, column=1)
#         self.at_entry.grid(row=0, column=3)
#         self.bt_entry.grid(row=0, column=5)

#         tk.Button(input_frame, text="Add Process",
#                   command=self.add_process).grid(row=0, column=6, padx=10)

#         tk.Button(input_frame, text="Delete Selected",
#                   command=self.delete_process).grid(row=0, column=7, padx=10)

#         # -------- Options --------
#         option_frame = tk.LabelFrame(self, text="Scheduling Options", font=("Arial", 12))
#         option_frame.pack(fill="x", padx=10, pady=10)

#         self.algorithm = tk.StringVar(value="FCFS")
#         self.mode = tk.StringVar(value="Non-Preemptive")

#         ttk.Radiobutton(option_frame, text="FCFS",
#                         variable=self.algorithm, value="FCFS").pack(side="left", padx=10)
#         ttk.Radiobutton(option_frame, text="SJF",
#                         variable=self.algorithm, value="SJF").pack(side="left", padx=10)

#         ttk.Radiobutton(option_frame, text="Non-Preemptive",
#                         variable=self.mode, value="Non-Preemptive").pack(side="left", padx=20)
#         ttk.Radiobutton(option_frame, text="Preemptive",
#                         variable=self.mode, value="Preemptive").pack(side="left")

#         tk.Button(option_frame, text="Run Scheduling",
#                   command=self.run_scheduling).pack(side="right", padx=20)

#         # -------- Process Table --------
#         self.table = ttk.Treeview(
#             self,
#             columns=("PID", "AT", "BT", "WT", "TAT"),
#             show="headings",
#             height=8
#         )

#         for col in ("PID", "AT", "BT", "WT", "TAT"):
#             self.table.heading(col, text=col)

#         self.table.pack(fill="x", padx=10, pady=10)

#         # -------- Average Results --------
#         self.avg_label = tk.Label(
#             self,
#             text="Average WT: -    Average TAT: -",
#             font=("Arial", 12, "bold")
#         )
#         self.avg_label.pack(pady=10)

#         # -------- Gantt Chart --------
#         tk.Label(self, text="Gantt Chart", font=("Arial", 14)).pack()
#         self.canvas = tk.Canvas(self, height=150, bg="white")
#         self.canvas.pack(fill="x", padx=10, pady=10)

#     # ---------------- Add Process ----------------
#     def add_process(self):
#         try:
#             pid = self.pid_entry.get()
#             at = int(self.at_entry.get())
#             bt = int(self.bt_entry.get())

#             if not pid or at < 0 or bt <= 0:
#                 raise ValueError

#             self.processes.append({
#                 "pid": pid,
#                 "at": at,
#                 "bt": bt,
#                 "remaining": bt
#             })

#             self.table.insert("", "end", values=(pid, at, bt, "-", "-"))

#             self.pid_entry.delete(0, tk.END)
#             self.at_entry.delete(0, tk.END)
#             self.bt_entry.delete(0, tk.END)

#         except:
#             messagebox.showerror("Error", "Invalid input")

#     # ---------------- Delete Process ----------------
#     def delete_process(self):
#         selected = self.table.selection()
#         if not selected:
#             messagebox.showwarning("Warning", "Select a process to delete")
#             return

#         pid = self.table.item(selected[0])["values"][0]

#         self.processes = [p for p in self.processes if p["pid"] != pid]
#         self.table.delete(selected[0])

#     # ---------------- Run Scheduling ----------------
#     def run_scheduling(self):
#         if not self.processes:
#             messagebox.showwarning("Warning", "Add processes first")
#             return

#         # Reset remaining time
#         for p in self.processes:
#             p["remaining"] = p["bt"]

#         self.schedule.clear()
#         self.canvas.delete("all")
#         self.avg_label.config(text="Average WT: -    Average TAT: -")

#         if self.algorithm.get() == "FCFS":
#             self.fcfs()
#         else:
#             self.sjf()

#         self.calculate_times()
#         self.draw_gantt()

#     # ---------------- FCFS ----------------
#     def fcfs(self):
#         time = 0
#         for p in sorted(self.processes, key=lambda x: x["at"]):
#             if time < p["at"]:
#                 time = p["at"]
#             start = time
#             end = start + p["bt"]
#             time = end
#             self.schedule.append((p["pid"], start, end))

#     # ---------------- SJF ----------------
#     def sjf(self):
#         time = 0
#         completed = 0
#         n = len(self.processes)

#         while completed < n:
#             ready = [p for p in self.processes
#                      if p["at"] <= time and p["remaining"] > 0]

#             if not ready:
#                 time += 1
#                 continue

#             if self.mode.get() == "Non-Preemptive":
#                 p = min(ready, key=lambda x: x["remaining"])
#                 start = time
#                 time += p["remaining"]
#                 p["remaining"] = 0
#                 completed += 1
#                 self.schedule.append((p["pid"], start, time))
#             else:
#                 p = min(ready, key=lambda x: x["remaining"])
#                 start = time
#                 time += 1
#                 p["remaining"] -= 1
#                 self.schedule.append((p["pid"], start, time))
#                 if p["remaining"] == 0:
#                     completed += 1

#     # ---------------- Calculate WT & TAT ----------------
#     def calculate_times(self):
#         self.table.delete(*self.table.get_children())

#         total_wt = 0
#         total_tat = 0
#         n = len(self.processes)

#         for p in self.processes:
#             completion = max(end for pid, _, end in self.schedule if pid == p["pid"])
#             tat = completion - p["at"]
#             wt = tat - p["bt"]

#             total_wt += wt
#             total_tat += tat

#             self.table.insert("", "end",
#                               values=(p["pid"], p["at"], p["bt"], wt, tat))

#         avg_wt = total_wt / n
#         avg_tat = total_tat / n

#         self.avg_label.config(
#             text=f"Average WT: {avg_wt:.2f}    Average TAT: {avg_tat:.2f}"
#         )

#     # ---------------- Gantt Chart ----------------
#     def draw_gantt(self):
#         x = 20
#         for pid, start, end in self.schedule:
#             width = (end - start) * 30
#             self.canvas.create_rectangle(x, 50, x + width, 100, fill="lightblue")
#             self.canvas.create_text(x + width/2, 75, text=pid)
#             self.canvas.create_text(x, 110, text=start)
#             x += width
#         self.canvas.create_text(x, 110, text=self.schedule[-1][2])

# # ---------------- Run ----------------
# if __name__ == "__main__":
#     app = SchedulerOS()
#     app.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox

class SchedulerOS(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mini OS Simulator – CPU Scheduling")
        self.geometry("1150x780")

        self.processes = []
        self.schedule = []

        self.create_widgets()

    # ---------------- GUI ----------------
    def create_widgets(self):

        # -------- Input Frame --------
        input_frame = tk.LabelFrame(self, text="Add Process", font=("Arial", 12))
        input_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(input_frame, text="PID").grid(row=0, column=0)
        tk.Label(input_frame, text="Arrival Time").grid(row=0, column=2)
        tk.Label(input_frame, text="Burst Time").grid(row=0, column=4)

        self.pid_entry = tk.Entry(input_frame, width=10)
        self.at_entry = tk.Entry(input_frame, width=10)
        self.bt_entry = tk.Entry(input_frame, width=10)

        self.pid_entry.grid(row=0, column=1, padx=5)
        self.at_entry.grid(row=0, column=3, padx=5)
        self.bt_entry.grid(row=0, column=5, padx=5)

        tk.Button(input_frame, text="Add Process",
                  command=self.add_process).grid(row=0, column=6, padx=8)

        tk.Button(input_frame, text="Delete Selected",
                  command=self.delete_process).grid(row=0, column=7, padx=8)

        # -------- Options --------
        option_frame = tk.LabelFrame(self, text="Scheduling Options", font=("Arial", 12))
        option_frame.pack(fill="x", padx=10, pady=10)

        self.algorithm = tk.StringVar(value="FCFS")
        self.mode = tk.StringVar(value="Non-Preemptive")

        ttk.Radiobutton(option_frame, text="FCFS",
                        variable=self.algorithm, value="FCFS").pack(side="left", padx=10)
        ttk.Radiobutton(option_frame, text="SJF",
                        variable=self.algorithm, value="SJF").pack(side="left", padx=10)

        ttk.Radiobutton(option_frame, text="Non-Preemptive",
                        variable=self.mode, value="Non-Preemptive").pack(side="left", padx=20)
        ttk.Radiobutton(option_frame, text="Preemptive",
                        variable=self.mode, value="Preemptive").pack(side="left")

        tk.Button(option_frame, text="Run Scheduling",
                  command=self.run_scheduling).pack(side="right", padx=10)

        tk.Button(option_frame, text="Clear Gantt Chart",
                  command=self.clear_gantt).pack(side="right", padx=10)

        # -------- Process Table --------
        self.table = ttk.Treeview(
            self, columns=("PID", "AT", "BT", "WT", "TAT"),
            show="headings", height=8
        )

        for col in ("PID", "AT", "BT", "WT", "TAT"):
            self.table.heading(col, text=col)

        self.table.pack(fill="x", padx=10, pady=10)

        # -------- Average Results --------
        self.avg_label = tk.Label(
            self, text="Average WT: -     Average TAT: -",
            font=("Arial", 12, "bold")
        )
        self.avg_label.pack(pady=10)

        # -------- Gantt Chart --------
        tk.Label(self, text="Gantt Chart", font=("Arial", 14)).pack()
        self.canvas = tk.Canvas(self, height=170, bg="white")
        self.canvas.pack(fill="x", padx=10, pady=10)

    # ---------------- Add / Delete Process ----------------
    def add_process(self):
        try:
            pid = self.pid_entry.get()
            at = int(self.at_entry.get())
            bt = int(self.bt_entry.get())

            if not pid or at < 0 or bt <= 0:
                raise ValueError

            self.processes.append({
                "pid": pid,
                "at": at,
                "bt": bt,
                "remaining": bt
            })

            self.table.insert("", "end", values=(pid, at, bt, "-", "-"))

            self.pid_entry.delete(0, tk.END)
            self.at_entry.delete(0, tk.END)
            self.bt_entry.delete(0, tk.END)

        except:
            messagebox.showerror("Error", "Invalid input")

    def delete_process(self):
        selected = self.table.selection()
        if not selected:
            return

        pid = self.table.item(selected[0])["values"][0]
        self.processes = [p for p in self.processes if p["pid"] != pid]
        self.table.delete(selected[0])

    # ---------------- Run Scheduling ----------------
    def run_scheduling(self):
        if not self.processes:
            return

        for p in self.processes:
            p["remaining"] = p["bt"]

        self.schedule.clear()
        self.canvas.delete("all")

        if self.algorithm.get() == "FCFS":
            self.fcfs()
        else:
            self.sjf()

        self.calculate_times()
        self.draw_gantt()

    # ---------------- FCFS (with IDLE) ----------------
    def fcfs(self):
        time = 0
        for p in sorted(self.processes, key=lambda x: x["at"]):
            if time < p["at"]:
                self.schedule.append(("IDLE", time, p["at"]))
                time = p["at"]
            start = time
            end = start + p["bt"]
            time = end
            self.schedule.append((p["pid"], start, end))

    # ---------------- SJF (with IDLE) ----------------
    def sjf(self):
        time = 0
        completed = 0
        n = len(self.processes)

        while completed < n:
            ready = [p for p in self.processes
                     if p["at"] <= time and p["remaining"] > 0]

            if not ready:
                self.schedule.append(("IDLE", time, time + 1))
                time += 1
                continue

            if self.mode.get() == "Non-Preemptive":
                p = min(ready, key=lambda x: x["remaining"])
                start = time
                time += p["remaining"]
                p["remaining"] = 0
                completed += 1
                self.schedule.append((p["pid"], start, time))
            else:
                p = min(ready, key=lambda x: x["remaining"])
                start = time
                time += 1
                p["remaining"] -= 1
                self.schedule.append((p["pid"], start, time))
                if p["remaining"] == 0:
                    completed += 1

    # ---------------- Calculate WT & TAT ----------------
    def calculate_times(self):
        self.table.delete(*self.table.get_children())

        total_wt = 0
        total_tat = 0
        n = len(self.processes)

        for p in self.processes:
            completion = max(end for pid, _, end in self.schedule if pid == p["pid"])
            tat = completion - p["at"]
            wt = tat - p["bt"]

            total_wt += wt
            total_tat += tat

            self.table.insert("", "end",
                              values=(p["pid"], p["at"], p["bt"], wt, tat))

        self.avg_label.config(
            text=f"Average WT: {total_wt/n:.2f}     Average TAT: {total_tat/n:.2f}"
        )

    # ---------------- Gantt Chart ----------------
    def draw_gantt(self):
        x = 20
        for pid, start, end in self.schedule:
            width = (end - start) * 30
            color = "lightgray" if pid == "IDLE" else "lightblue"

            self.canvas.create_rectangle(x, 60, x + width, 110, fill=color)
            self.canvas.create_text(x + width/2, 85, text=pid)
            self.canvas.create_text(x, 120, text=start)

            x += width

        self.canvas.create_text(x, 120, text=self.schedule[-1][2])

    # ---------------- Clear Gantt ----------------
    def clear_gantt(self):
        self.canvas.delete("all")
        self.schedule.clear()
        self.avg_label.config(text="Average WT: -     Average TAT: -")

# ---------------- Run ----------------
if __name__ == "__main__":
    app = SchedulerOS()
    app.mainloop()
