"""
GUI Application for Sum of Numbers using Tkinter
This program provides a graphical user interface to calculate the sum of user input numbers.
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import font


class SumCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sum Calculator")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        self.root.config(bg="#f0f0f0")
        
        # Data storage
        self.numbers = []
        
        # Set up custom fonts
        title_font = font.Font(family="Helvetica", size=18, weight="bold")
        label_font = font.Font(family="Helvetica", size=11)
        result_font = font.Font(family="Helvetica", size=12, weight="bold")
        
        # Title
        title_label = tk.Label(
            self.root,
            text="Sum Calculator",
            font=title_font,
            bg="#f0f0f0",
            fg="#333"
        )
        title_label.pack(pady=20)
        
        # Input Frame
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=15, padx=20, fill="x")
        
        input_label = tk.Label(
            input_frame,
            text="Enter a number:",
            font=label_font,
            bg="#f0f0f0"
        )
        input_label.pack(side="left", padx=5)
        
        self.input_entry = tk.Entry(
            input_frame,
            font=label_font,
            width=15,
            bd=2,
            relief="solid"
        )
        self.input_entry.pack(side="left", padx=5)
        self.input_entry.bind("<Return>", lambda event: self.add_number())
        
        # Button Frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10, padx=20, fill="x")
        
        add_btn = tk.Button(
            button_frame,
            text="Add Number",
            command=self.add_number,
            bg="#4CAF50",
            fg="white",
            font=label_font,
            padx=15,
            pady=8,
            relief="raised",
            cursor="hand2"
        )
        add_btn.pack(side="left", padx=5)
        
        clear_btn = tk.Button(
            button_frame,
            text="Clear All",
            command=self.clear_all,
            bg="#f44336",
            fg="white",
            font=label_font,
            padx=15,
            pady=8,
            relief="raised",
            cursor="hand2"
        )
        clear_btn.pack(side="left", padx=5)
        
        # Numbers Display Frame
        display_label = tk.Label(
            self.root,
            text="Numbers Entered:",
            font=label_font,
            bg="#f0f0f0"
        )
        display_label.pack(pady=(15, 5), padx=20, anchor="w")
        
        # Listbox with scrollbar
        listbox_frame = tk.Frame(self.root, bg="#f0f0f0")
        listbox_frame.pack(pady=5, padx=20, fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.pack(side="right", fill="y")
        
        self.numbers_listbox = tk.Listbox(
            listbox_frame,
            font=label_font,
            bd=2,
            relief="solid",
            yscrollcommand=scrollbar.set,
            height=10
        )
        self.numbers_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.numbers_listbox.yview)
        
        # Results Frame
        results_frame = tk.Frame(self.root, bg="#e8f5e9", relief="solid", bd=2)
        results_frame.pack(pady=15, padx=20, fill="x")
        
        results_title = tk.Label(
            results_frame,
            text="Results",
            font=result_font,
            bg="#e8f5e9",
            fg="#2e7d32"
        )
        results_title.pack(pady=10)
        
        # Count
        self.count_label = tk.Label(
            results_frame,
            text="Total Count: 0",
            font=label_font,
            bg="#e8f5e9"
        )
        self.count_label.pack(pady=5)
        
        # Sum
        self.sum_label = tk.Label(
            results_frame,
            text="Sum: 0",
            font=label_font,
            bg="#e8f5e9"
        )
        self.sum_label.pack(pady=5)
        
        # Average
        self.average_label = tk.Label(
            results_frame,
            text="Average: 0.00",
            font=label_font,
            bg="#e8f5e9"
        )
        self.average_label.pack(pady=10)
    
    def add_number(self):
        """Add a number to the list"""
        try:
            number_input = self.input_entry.get().strip()
            
            if not number_input:
                messagebox.showwarning("Input Error", "Please enter a number!")
                return
            
            number = float(number_input)
            self.numbers.append(number)
            
            # Update display
            self.update_display()
            
            # Clear input field
            self.input_entry.delete(0, tk.END)
            self.input_entry.focus()
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number!")
            self.input_entry.delete(0, tk.END)
            self.input_entry.focus()
    
    def clear_all(self):
        """Clear all numbers and reset the display"""
        self.numbers = []
        self.update_display()
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()
    
    def update_display(self):
        """Update the listbox and results"""
        # Clear listbox
        self.numbers_listbox.delete(0, tk.END)
        
        # Add numbers to listbox
        for i, number in enumerate(self.numbers, 1):
            self.numbers_listbox.insert(tk.END, f"{i}. {number}")
        
        # Update results
        if self.numbers:
            total_sum = sum(self.numbers)
            average = total_sum / len(self.numbers)
            
            self.count_label.config(text=f"Total Count: {len(self.numbers)}")
            self.sum_label.config(text=f"Sum: {total_sum}")
            self.average_label.config(text=f"Average: {average:.2f}")
        else:
            self.count_label.config(text="Total Count: 0")
            self.sum_label.config(text="Sum: 0")
            self.average_label.config(text="Average: 0.00")


if __name__ == "__main__":
    root = tk.Tk()
    app = SumCalculatorApp(root)
    root.mainloop()
