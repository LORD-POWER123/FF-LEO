import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import random

APP_TITLE = "Leo's Free Fire Top-Up Simulator"
PACKAGES = [
    ("100 Diamonds", "₹80"),
    ("310 Diamonds", "₹250"),
    ("520 Diamonds", "₹400"),
    ("1060 Diamonds", "₹800"),
    ("2180 Diamonds", "₹1,600"),
]

class TopUpSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("760x610")
        self.root.minsize(700, 570)
        self.root.configure(bg="#10131c")
        self.history = []

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox", fieldbackground="#202638", background="#202638",
                        foreground="#ffffff", arrowcolor="#ffffff")
        style.map("TCombobox", fieldbackground=[("readonly", "#202638")],
                  foreground=[("readonly", "#ffffff")])

        self.build_ui()

    def label(self, parent, text, size=10, color="#dce3f2", bold=False):
        return tk.Label(parent, text=text, bg=parent.cget("bg"), fg=color,
                        font=("Segoe UI", size, "bold" if bold else "normal"))

    def build_ui(self):
        header = tk.Frame(self.root, bg="#171d2b", padx=22, pady=18)
        header.pack(fill="x")
        tk.Label(header, text="LEO'S TOP-UP LAB", bg="#171d2b", fg="#7c9cff",
                 font=("Segoe UI", 20, "bold")).pack(anchor="w")
        tk.Label(header, text="FREE FIRE • PAYMENT FLOW DEMO • SIMULATION ONLY",
                 bg="#171d2b", fg="#aab4c8", font=("Segoe UI", 9)).pack(anchor="w", pady=(3, 0))

        warning = tk.Frame(self.root, bg="#392b18", padx=12, pady=9)
        warning.pack(fill="x", padx=20, pady=(16, 10))
        tk.Label(warning, text="DEMO ONLY — No real payments. Never enter real card details.",
                 bg="#392b18", fg="#ffd48a", font=("Segoe UI", 10, "bold")).pack(anchor="w")

        body = tk.Frame(self.root, bg="#10131c", padx=22, pady=8)
        body.pack(fill="both", expand=True)

        left = tk.Frame(body, bg="#171d2b", padx=18, pady=16)
        left.pack(side="left", fill="both", expand=True, padx=(0, 10))
        right = tk.Frame(body, bg="#171d2b", padx=18, pady=16, width=245)
        right.pack(side="right", fill="y")
        right.pack_propagate(False)

        self.label(left, "Create a test top-up", 15, "#ffffff", True).pack(anchor="w", pady=(0, 14))
        self.label(left, "Player ID (demo)", 9, "#aab4c8", True).pack(anchor="w")
        self.player = tk.Entry(left, bg="#202638", fg="white", insertbackground="white",
                               relief="flat", font=("Segoe UI", 11))
        self.player.pack(fill="x", ipady=9, pady=(5, 12))
        self.player.insert(0, "123456789")

        self.label(left, "Diamond package", 9, "#aab4c8", True).pack(anchor="w")
        self.package = ttk.Combobox(left, values=[f"{name} — {price}" for name, price in PACKAGES],
                                    state="readonly", font=("Segoe UI", 10))
        self.package.current(1)
        self.package.pack(fill="x", ipady=6, pady=(5, 12))

        self.label(left, "Payment method (simulated)", 9, "#aab4c8", True).pack(anchor="w")
        self.method = ttk.Combobox(left, values=["Demo card", "Demo UPI", "Test wallet"],
                                   state="readonly", font=("Segoe UI", 10))
        self.method.current(0)
        self.method.pack(fill="x", ipady=6, pady=(5, 12))

        self.label(left, "Test result", 9, "#aab4c8", True).pack(anchor="w")
        self.result = ttk.Combobox(left, values=["Random success/failure", "Always succeed", "Always fail"],
                                   state="readonly", font=("Segoe UI", 10))
        self.result.current(0)
        self.result.pack(fill="x", ipady=6, pady=(5, 16))

        tk.Button(left, text="RUN TEST TRANSACTION", command=self.run_transaction,
                  bg="#5578ff", fg="white", activebackground="#3f61e8",
                  activeforeground="white", relief="flat", cursor="hand2",
                  font=("Segoe UI", 10, "bold"), pady=12).pack(fill="x")
        self.status = tk.Label(left, text="Ready for a safe demo.", bg="#171d2b",
                               fg="#aab4c8", font=("Segoe UI", 9), wraplength=390,
                               justify="left")
        self.status.pack(anchor="w", pady=(14, 0))

        self.label(right, "SESSION SUMMARY", 11, "#ffffff", True).pack(anchor="w", pady=(0, 12))
        self.total_label = self.label(right, "0", 24, "#7c9cff", True)
        self.total_label.pack(anchor="w")
        self.label(right, "Test transactions", 9, "#aab4c8").pack(anchor="w")
        ttk.Separator(right).pack(fill="x", pady=14)
        self.label(right, "Recent activity", 10, "#ffffff", True).pack(anchor="w", pady=(0, 8))
        self.log = tk.Listbox(right, height=14, bg="#202638", fg="#dce3f2",
                              selectbackground="#3b4f80", relief="flat",
                              font=("Consolas", 8), activestyle="none")
        self.log.pack(fill="both", expand=True)
        tk.Button(right, text="Clear history", command=self.clear_history,
                  bg="#30394d", fg="white", activebackground="#414d66",
                  relief="flat", cursor="hand2", pady=7).pack(fill="x", pady=(10, 0))

        footer = tk.Label(self.root, text="This is an independent educational simulator, not affiliated with Garena or Free Fire.",
                          bg="#10131c", fg="#7e899f", font=("Segoe UI", 8))
        footer.pack(pady=(0, 12))

    def run_transaction(self):
        player_id = self.player.get().strip()
        if not player_id.isdigit() or not (6 <= len(player_id) <= 20):
            messagebox.showwarning("Check Player ID", "Enter a demo Player ID containing 6–20 digits.")
            return

        selected = self.package.get()
        package_name, price = selected.split(" — ")
        mode = self.result.get()
        if mode == "Always succeed":
            success = True
        elif mode == "Always fail":
            success = False
        else:
            success = random.choice([True, False])

        txn = f"DEMO-{random.randint(100000, 999999)}"
        timestamp = datetime.now().strftime("%H:%M:%S")
        state = "SUCCESS" if success else "FAILED"
        self.history.insert(0, (timestamp, state, package_name, price, txn))
        self.total_label.config(text=str(len(self.history)))
        self.log.insert(0, f"{timestamp}  {state}")
        color = "#79dfa8" if success else "#ff8c8c"
        self.status.config(
            text=f"{state}: {package_name} ({price}) for demo ID {player_id}. "
                 f"Reference: {txn}. No money was charged and no diamonds were delivered.",
            fg=color
        )

    def clear_history(self):
        self.history.clear()
        self.log.delete(0, tk.END)
        self.total_label.config(text="0")
        self.status.config(text="History cleared. Ready for another demo.", fg="#aab4c8")

if __name__ == "__main__":
    root = tk.Tk()
    TopUpSimulator(root)
    root.mainloop()
