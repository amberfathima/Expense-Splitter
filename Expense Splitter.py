import tkinter as tk
from tkinter import messagebox

# --- Expense Logic ---
class ExpenseSplitter:
    def __init__(self):
        self.balances = {}  # stores each person's balance (owed or owes)

    def add_expense(self, payer, amount, participants):
        # Add everyone to the balance sheet if not already present
        for person in [payer] + participants:
            self.balances.setdefault(person, 0)

        split_amount = amount / len(participants)  # amount each participant owes
        self.balances[payer] += amount              # payer gets credit
        for p in participants:
            self.balances[p] -= split_amount         # each participant owes their share

    def get_balances(self):
        # Returns dictionary with rounded balances
        return {p: round(b, 2) for p, b in self.balances.items()}

# --- GUI (Tkinter) ---
def add_expense():
    payer = payer_entry.get().strip()
    amount = amount_entry.get().strip()
    participants = [p.strip() for p in participants_entry.get().split(",") if p.strip()]

    if not payer or not amount or not participants:
        messagebox.showwarning("Error", "Fill all fields!")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning("Error", "Enter a valid number!")
        return

    splitter.add_expense(payer, amount, participants)
    messagebox.showinfo("Success", f"Added: {payer} paid ₹{amount}")
    payer_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    participants_entry.delete(0, tk.END)

def show_balances():
    output.delete(1.0, tk.END)
    balances = splitter.get_balances()

    if not balances:
        output.insert(tk.END, "No expenses yet!\n")
        return

    for person, bal in balances.items():
        if bal > 0:
            output.insert(tk.END, f"{person} is owed ₹{bal}\n")
        elif bal < 0:
            output.insert(tk.END, f"{person} owes ₹{-bal}\n")
        else:
            output.insert(tk.END, f"{person} is settled.\n")

# --- Window setup ---
root = tk.Tk()
root.title("Expense Splitter 💸")
root.geometry("400x400")
root.config(bg="#fdf6f0")

splitter = ExpenseSplitter()  # Create logic object

# --- UI Elements ---
tk.Label(root, text="Expense Splitter", font=("Arial", 16, "bold"), bg="#fdf6f0").pack(pady=10)

tk.Label(root, text="Payer:", bg="#fdf6f0").pack()
payer_entry = tk.Entry(root)
payer_entry.pack()

tk.Label(root, text="Amount:", bg="#fdf6f0").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Participants (comma separated):", bg="#fdf6f0").pack()
participants_entry = tk.Entry(root)
participants_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense, bg="#c1cefe").pack(pady=5)
tk.Button(root, text="Show Balances", command=show_balances, bg="#ffd6a5").pack(pady=5)

output = tk.Text(root, height=10, width=40, bg="#fffaf7")
output.pack(pady=10)

root.mainloop()
