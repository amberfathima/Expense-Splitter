# Expense Splitter (Python Tkinter GUI)

A simple and aesthetic **Expense Splitter App** built using Python’s `tkinter`.  
It helps you easily divide shared expenses among friends, track who owes whom, and view balances — all in a clean pastel interface 

---

## Features
-  Add shared expenses with payer and participants  
-  Automatically splits the cost evenly  
-  View balances instantly  
-  Alerts for missing or invalid inputs  
-  Cute pastel GUI (student aesthetic)

---

## How It Works
When someone pays for a group:
- The **payer** gets credit for the full amount.
- The **participants** each owe their equal share.
- Balances update automatically — so you can see who owes or is owed.

Example:
```
Amber pays ₹120 for Amber, Insiya, and Anshika
→ Amber is owed ₹80
→ Insiya owes ₹40
→ Anshika owes ₹40
```

---

## Preview
*(You can add your own screenshot later)*

```
┌───────────────────────────────┐
│      Expense Splitter 💸       │
│ Payer: [Amber      ]           │
│ Amount: [120        ]          │
│ Participants: [Amber, Insiya]  │
│ [Add Expense] [Show Balances]  │
│                                │
│ Amber is owed ₹80              │
│ Insiya owes ₹40                │
└───────────────────────────────┘
```

---

## Getting Started

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<your-username>/Expense-Splitter.git
cd Expense-Splitter
```

### 2️⃣ Run the app
Make sure Python is installed (v3.7+ recommended).

```bash
python expense_splitter.py
```

---

## Requirements
- Python 3.x  
- Tkinter (comes pre-installed with Python)

No extra libraries required 

---

## File Structure
```
Expense-Splitter/
│
├── expense_splitter.py     # Main program file
├── README.md               # Project documentation
└── (optional) screenshot.png
```

---

## Customization
Want to make it aesthetic?  
- Change colors inside `.config(bg="#fdf6f0")` and button `bg` options.  
- Add emojis to labels and buttons for extra charm 

---

## Author
**Amber Fathima**  
*BBA AI Student @ Symbiosis*  

---

> *"Split bills easily, stay chill financially."* 

---

## How to Run

1. Make sure you have Python installed on your computer.
2. Open your terminal or command prompt.
3. Navigate to the folder containing this project.
4. Run the following command:
   ```bash
   python "Expense Splitter.py"