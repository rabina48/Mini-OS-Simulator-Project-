# # # import tkinter as tk
# # # from tkinter import messagebox, simpledialog, ttk
# # # import os

# # # # ------------------ Main Application ------------------
# # # class FileManagementOS(tk.Tk):
# # #     def __init__(self):
# # #         super().__init__()
# # #         self.title("Mini OS File Management Simulator")
# # #         self.geometry("700x500")
# # #         self.files = []  # Directory in memory

# # #         # --- Tabs ---
# # #         self.tab_control = ttk.Notebook(self)
# # #         self.file_tab = ttk.Frame(self.tab_control)
# # #         self.tab_control.add(self.file_tab, text="File Management")
# # #         self.tab_control.pack(expand=1, fill="both")

# # #         # --- Widgets ---
# # #         self.create_widgets()

# # #     # ------------------ Widgets ------------------
# # #     def create_widgets(self):
# # #         # Buttons
# # #         button_frame = tk.Frame(self.file_tab)
# # #         button_frame.pack(pady=10)

# # #         tk.Button(button_frame, text="Create File", width=15, command=self.create_file).pack(side="left", padx=5)
# # #         tk.Button(button_frame, text="Delete File", width=15, command=self.delete_file).pack(side="left", padx=5)
# # #         tk.Button(button_frame, text="Read File", width=15, command=self.read_file).pack(side="left", padx=5)
# # #         tk.Button(button_frame, text="List Files", width=15, command=self.list_files).pack(side="left", padx=5)

# # #         # File Table
# # #         self.file_table = ttk.Treeview(self.file_tab, columns=("Name", "Size"), show="headings")
# # #         self.file_table.heading("Name", text="File Name")
# # #         self.file_table.heading("Size", text="Size (bytes)")
# # #         self.file_table.pack(expand=1, fill="both", padx=10, pady=10)

# # #     # ------------------ Functions ------------------
# # #     def create_file(self):
# # #         name = simpledialog.askstring("Input", "Enter file name:")
# # #         if not name:
# # #             return
# # #         content = simpledialog.askstring("Input", "Enter file content:")
# # #         if content is None:
# # #             content = ""

# # #         # Check if file already exists
# # #         for f in self.files:
# # #             if f['name'] == name:
# # #                 messagebox.showwarning("Warning", "File already exists!")
# # #                 return

# # #         # Save file on disk
# # #         with open(name, "w") as f_disk:
# # #             f_disk.write(content)

# # #         # Add to memory directory
# # #         self.files.append({'name': name, 'size': len(content), 'content': content})
# # #         messagebox.showinfo("Success", f"File '{name}' created successfully.")
# # #         self.update_file_table()

# # #     def delete_file(self):
# # #         selected = self.file_table.focus()
# # #         if not selected:
# # #             messagebox.showwarning("Warning", "Select a file to delete!")
# # #             return
# # #         file_name = self.file_table.item(selected)['values'][0]

# # #         # Remove from memory
# # #         for f in self.files:
# # #             if f['name'] == file_name:
# # #                 self.files.remove(f)
# # #                 break

# # #         # Remove from disk
# # #         if os.path.exists(file_name):
# # #             os.remove(file_name)

# # #         messagebox.showinfo("Deleted", f"File '{file_name}' deleted successfully.")
# # #         self.update_file_table()

# # #     def read_file(self):
# # #         selected = self.file_table.focus()
# # #         if not selected:
# # #             messagebox.showwarning("Warning", "Select a file to read!")
# # #             return
# # #         file_name = self.file_table.item(selected)['values'][0]

# # #         # Read content
# # #         for f in self.files:
# # #             if f['name'] == file_name:
# # #                 messagebox.showinfo(f"File: {file_name}", f"Content:\n{f['content']}")
# # #                 return

# # #     def list_files(self):
# # #         self.update_file_table()
# # #         messagebox.showinfo("Files Listed", "All files displayed in table.")

# # #     def update_file_table(self):
# # #         # Clear table
# # #         for item in self.file_table.get_children():
# # #             self.file_table.delete(item)
# # #         # Insert all files
# # #         for f in self.files:
# # #             self.file_table.insert("", "end", values=(f['name'], f['size']))

# # # # ------------------ Run Application ------------------
# # # if __name__ == "__main__":
# # #     app = FileManagementOS()
# # #     app.mainloop()


# # import tkinter as tk
# # from tkinter import messagebox, simpledialog, ttk
# # import os

# # # ------------------ Main Application ------------------
# # class FileManagementOS(tk.Tk):
# #     def __init__(self):
# #         super().__init__()
# #         self.title("Mini OS File Management Simulator")
# #         self.geometry("700x500")
# #         self.files = []  # Directory in memory

# #         # --- Tabs ---
# #         self.tab_control = ttk.Notebook(self)
# #         self.file_tab = ttk.Frame(self.tab_control)
# #         self.tab_control.add(self.file_tab, text="File Management")
# #         self.tab_control.pack(expand=1, fill="both")

# #         # --- Widgets ---
# #         self.create_widgets()

# #     # ------------------ Widgets ------------------
# #     def create_widgets(self):
# #         # Buttons
# #         button_frame = tk.Frame(self.file_tab)
# #         button_frame.pack(pady=10)

# #         tk.Button(button_frame, text="Create File", width=15, command=self.create_file).pack(side="left", padx=5)
# #         tk.Button(button_frame, text="Delete File", width=15, command=self.delete_file).pack(side="left", padx=5)
# #         tk.Button(button_frame, text="Read File", width=15, command=self.read_file).pack(side="left", padx=5)
# #         tk.Button(button_frame, text="List Files", width=15, command=self.list_files).pack(side="left", padx=5)

# #         # File Table
# #         self.file_table = ttk.Treeview(self.file_tab, columns=("Name", "Size"), show="headings", selectmode="browse")
# #         self.file_table.heading("Name", text="File Name")
# #         self.file_table.heading("Size", text="Size (bytes)")
# #         self.file_table.pack(expand=1, fill="both", padx=10, pady=10)

# #     # ------------------ Functions ------------------
# #     def create_file(self):
# #         name = simpledialog.askstring("Input", "Enter file name:")
# #         if not name:
# #             return
# #         content = simpledialog.askstring("Input", "Enter file content:")
# #         if content is None:
# #             content = ""

# #         # Check if file already exists
# #         for f in self.files:
# #             if f['name'] == name:
# #                 messagebox.showwarning("Warning", "File already exists!")
# #                 return

# #         # Save file on disk
# #         with open(name, "w") as f_disk:
# #             f_disk.write(content)

# #         # Add to memory directory
# #         self.files.append({'name': name, 'size': len(content), 'content': content})
# #         messagebox.showinfo("Success", f"File '{name}' created successfully.")
# #         self.update_file_table()

# #     def delete_file(self):
# #         selected_items = self.file_table.selection()
# #         if not selected_items:
# #             messagebox.showwarning("Warning", "Select a file to delete!")
# #             return

# #         for item in selected_items:
# #             file_name = self.file_table.item(item)['values'][0]

# #             # Remove from memory
# #             for f in self.files:
# #                 if f['name'] == file_name:
# #                     self.files.remove(f)
# #                     break

# #             # Remove from disk
# #             if os.path.exists(file_name):
# #                 os.remove(file_name)

# #         messagebox.showinfo("Deleted", "Selected file(s) deleted successfully.")
# #         self.update_file_table()

# #     def read_file(self):
# #         selected_items = self.file_table.selection()
# #         if not selected_items:
# #             messagebox.showwarning("Warning", "Select a file to read!")
# #             return

# #         file_name = self.file_table.item(selected_items[0])['values'][0]

# #         # Read content
# #         for f in self.files:
# #             if f['name'] == file_name:
# #                 messagebox.showinfo(f"File: {file_name}", f"Content:\n{f['content']}")
# #                 return

# #         messagebox.showerror("Error", "File not found in memory.")

# #     def list_files(self):
# #         if not self.files:
# #             messagebox.showinfo("Files Listed", "No files in directory.")
# #             self.update_file_table()
# #             return

# #         self.update_file_table()
# #         messagebox.showinfo("Files Listed", f"{len(self.files)} file(s) displayed in table.")

# #     def update_file_table(self):
# #         # Clear table
# #         for item in self.file_table.get_children():
# #             self.file_table.delete(item)
# #         # Insert all files
# #         for f in self.files:
# #             self.file_table.insert("", "end", values=(f['name'], f['size']))

# # # ------------------ Run Application ------------------
# # if __name__ == "__main__":
# #     app = FileManagementOS()
# #     app.mainloop()


# import tkinter as tk
# from tkinter import messagebox, simpledialog, ttk
# import os

# class FileManagementOS(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Mini OS File Management Simulator")
#         self.geometry("700x500")
#         self.files = []  # In-memory directory

#         # Tabs
#         self.tab_control = ttk.Notebook(self)
#         self.file_tab = ttk.Frame(self.tab_control)
#         self.tab_control.add(self.file_tab, text="File Management")
#         self.tab_control.pack(expand=1, fill="both")

#         self.create_widgets()

#     def create_widgets(self):
#         # Buttons
#         button_frame = tk.Frame(self.file_tab)
#         button_frame.pack(pady=10)

#         tk.Button(button_frame, text="Create File", width=15, command=self.create_file).pack(side="left", padx=5)
#         tk.Button(button_frame, text="Delete File", width=15, command=self.delete_file).pack(side="left", padx=5)
#         tk.Button(button_frame, text="Read File", width=15, command=self.read_file).pack(side="left", padx=5)
#         tk.Button(button_frame, text="List Files", width=15, command=self.list_files).pack(side="left", padx=5)

#         # File table
#         self.file_table = ttk.Treeview(self.file_tab, columns=("Name", "Size"), show="headings", selectmode="browse")
#         self.file_table.heading("Name", text="File Name")
#         self.file_table.heading("Size", text="Size (bytes)")
#         self.file_table.pack(expand=1, fill="both", padx=10, pady=10)

#     # ------------------ Functions ------------------
#     def create_file(self):
#         name = simpledialog.askstring("Input", "Enter file name:")
#         if not name:
#             return
#         content = simpledialog.askstring("Input", "Enter file content:")
#         if content is None:
#             content = ""

#         # Check if file already exists
#         for f in self.files:
#             if f['name'] == name:
#                 messagebox.showwarning("Warning", "File already exists!")
#                 return

#         # Save to disk
#         with open(name, "w") as f_disk:
#             f_disk.write(content)

#         # Add to memory directory
#         self.files.append({'name': name, 'size': len(content), 'content': content})
#         messagebox.showinfo("Success", f"File '{name}' created successfully.")
#         self.update_file_table()

#     def delete_file(self):
#         selected_items = self.file_table.selection()  # FIXED
#         if not selected_items:
#             messagebox.showwarning("Warning", "Select a file to delete!")
#             return

#         for item in selected_items:
#             file_name = self.file_table.item(item)['values'][0]

#             # Remove from memory
#             for f in self.files:
#                 if f['name'] == file_name:
#                     self.files.remove(f)
#                     break

#             # Remove from disk
#             if os.path.exists(file_name):
#                 os.remove(file_name)

#         messagebox.showinfo("Deleted", "Selected file(s) deleted successfully.")
#         self.update_file_table()

#     def read_file(self):
#         selected_items = self.file_table.selection()  # FIXED
#         if not selected_items:
#             messagebox.showwarning("Warning", "Select a file to read!")
#             return

#         file_name = self.file_table.item(selected_items[0])['values'][0]

#         # Find content
#         for f in self.files:
#             if f['name'] == file_name:
#                 messagebox.showinfo(f"File: {file_name}", f"Content:\n{f['content']}")
#                 return

#         messagebox.showerror("Error", "File not found.")

#     def list_files(self):
#         if not self.files:
#             messagebox.showinfo("Files Listed", "No files in directory.")
#         self.update_file_table()
#         messagebox.showinfo("Files Listed", f"{len(self.files)} file(s) displayed in table.")

#     def update_file_table(self):
#         # Clear table
#         for item in self.file_table.get_children():
#             self.file_table.delete(item)
#         # Add all files
#         for f in self.files:
#             self.file_table.insert("", "end", values=(f['name'], f['size']))

# # ------------------ Run ------------------
# if __name__ == "__main__":
#     app = FileManagementOS()
#     app.mainloop()


import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import os

class MiniOS(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mini OS Simulator")
        self.geometry("900x600")

        # ------------------ Data ------------------
        self.files = []  # In-memory file directory
        # Simulated memory blocks (size in KB)
        self.memory_blocks = [500, 300, 400, 200, 600]  
        self.memory_allocation = {}  # file_name -> block index

        # ------------------ Tabs ------------------
        self.tab_control = ttk.Notebook(self)
        self.file_tab = ttk.Frame(self.tab_control)
        self.memory_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.file_tab, text="File Management")
        self.tab_control.add(self.memory_tab, text="Memory Management")
        self.tab_control.pack(expand=1, fill="both")

        # ------------------ Widgets ------------------
        self.create_file_tab()
        self.create_memory_tab()

    # ------------------ File Management Tab ------------------
    def create_file_tab(self):
        button_frame = tk.Frame(self.file_tab)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Create File", width=25, command=self.create_file).pack(side="left", padx=8)
        tk.Button(button_frame, text="Delete File", width=25, command=self.delete_file).pack(side="left", padx=8)
        tk.Button(button_frame, text="Read File", width=25, command=self.read_file).pack(side="left", padx=8)
        tk.Button(button_frame, text="List Files", width=25, command=self.list_files).pack(side="left", padx=8)

        # File table
        self.file_table = ttk.Treeview(self.file_tab, columns=("Name", "Size", "Block"), show="headings", selectmode="browse")
        self.file_table.heading("Name", text="File Name")
        self.file_table.heading("Size", text="Size (KB)")
        self.file_table.heading("Block", text="Memory Block")
        self.file_table.pack(expand=1, fill="both", padx=20, pady=20)

    # ------------------ Memory Management Tab ------------------
    def create_memory_tab(self):
        tk.Label(self.memory_tab, text="Memory Blocks Status", font=("Arial", 40)).pack(pady=20)
        self.memory_table = ttk.Treeview(self.memory_tab, columns=("Block", "Size", "Status"), show="headings")
        self.memory_table.heading("Block", text="Block ID")
        self.memory_table.heading("Size", text="Block Size (KB)")
        self.memory_table.heading("Status", text="Status")
        self.memory_table.pack(expand=1, fill="both", padx=20, pady=20)
        self.update_memory_table()

    # ------------------ File Management Functions ------------------
    def create_file(self):
        name = simpledialog.askstring("Input", "Enter file name:")
        if not name:
            return
        size = simpledialog.askinteger("Input", "Enter file size (KB):", minvalue=1)
        if not size:
            return
        content = simpledialog.askstring("Input", "Enter file content:")
        if content is None:
            content = ""

        # Check if file exists
        for f in self.files:
            if f['name'] == name:
                messagebox.showwarning("Warning", "File already exists!")
                return

        # Allocate memory (first-fit)
        allocated_block = None
        for i, block in enumerate(self.memory_blocks):
            if block >= size:
                self.memory_blocks[i] -= size
                self.memory_allocation[name] = i
                allocated_block = i
                break

        if allocated_block is None:
            messagebox.showerror("Memory Error", "Not enough memory to create file!")
            return

        # Save file on disk
        with open(name, "w") as f_disk:
            f_disk.write(content)

        # Add to memory
        self.files.append({'name': name, 'size': size, 'content': content})
        messagebox.showinfo("Success", f"File '{name}' created in Block {allocated_block+1}")
        self.update_file_table()
        self.update_memory_table()

    def delete_file(self):
        selected_items = self.file_table.selection()
        if not selected_items:
            messagebox.showwarning("Warning", "Select a file to delete!")
            return

        for item in selected_items:
            file_name = self.file_table.item(item)['values'][0]

            # Free memory
            block_index = self.memory_allocation.get(file_name)
            if block_index is not None:
                # Return size to memory block
                for f in self.files:
                    if f['name'] == file_name:
                        self.memory_blocks[block_index] += f['size']
                        break
                self.memory_allocation.pop(file_name)

            # Remove from memory
            for f in self.files:
                if f['name'] == file_name:
                    self.files.remove(f)
                    break

            # Remove from disk
            if os.path.exists(file_name):
                os.remove(file_name)

        messagebox.showinfo("Deleted", "Selected file(s) deleted successfully.")
        self.update_file_table()
        self.update_memory_table()

    def read_file(self):
        selected_items = self.file_table.selection()
        if not selected_items:
            messagebox.showwarning("Warning", "Select a file to read!")
            return

        file_name = self.file_table.item(selected_items[0])['values'][0]

        for f in self.files:
            if f['name'] == file_name:
                messagebox.showinfo(f"File: {file_name}", f"Content:\n{f['content']}")
                return
        messagebox.showerror("Error", "File not found.")

    def list_files(self):
        if not self.files:
            messagebox.showinfo("Files Listed", "No files in directory.")
        self.update_file_table()
        messagebox.showinfo("Files Listed", f"{len(self.files)} file(s) displayed in table.")

    def update_file_table(self):
        # Clear table
        for item in self.file_table.get_children():
            self.file_table.delete(item)
        # Add all files
        for f in self.files:
            block = self.memory_allocation.get(f['name'], '-')
            self.file_table.insert("", "end", values=(f['name'], f['size'], block+1 if block != '-' else '-'))

    def update_memory_table(self):
        # Clear table
        for item in self.memory_table.get_children():
            self.memory_table.delete(item)
        # Add blocks
        for i, block_size in enumerate(self.memory_blocks):
            status = "Free" if block_size > 0 else "Full"
            self.memory_table.insert("", "end", values=(i+1, block_size, status))


# ------------------ Run Application ------------------
if __name__ == "__main__":
    app = MiniOS()
    app.mainloop()
