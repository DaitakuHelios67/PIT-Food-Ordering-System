
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class FoodApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QuickBite POS System")
        self.root.geometry("400x500")

        # Data: Menu items and prices
        self.menu = {
            "Burger": 8.99,
            "Pizza": 12.50,
            "Fries": 3.25,
            "Soda": 1.99,
            "Salad": 7.50
        }

        self.cart = []

        # Title
        tk.Label(
            root,
            text="Welcome to QuickBite",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        # Menu Buttons
        menu_frame = tk.Frame(root)
        menu_frame.pack(pady=10)

        for item, price in self.menu.items():
            btn = tk.Button(
                menu_frame,
                text=f"Add {item} (${price})",
                width=25,
                command=lambda i=item, p=price: self.add_to_cart(i, p)
            )
            btn.pack(pady=2)

        # Receipt Area
        tk.Label(
            root,
            text="Your Current Order:",
            font=("Arial", 10, "italic")
        ).pack(pady=(10, 0))

        self.receipt_box = tk.Listbox(root, width=40, height=8)
        self.receipt_box.pack(pady=5)

        # Total Label
        self.total_label = tk.Label(
            root,
            text="Total: $0.00",
            font=("Arial", 12, "bold")
        )
        self.total_label.pack(pady=5)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="Clear Cart",
            command=self.clear_cart,
            bg="#FFCDD2"
        ).pack(side="left", padx=5)

        tk.Button(
            btn_frame,
            text="Checkout",
            command=self.checkout,
            bg="#C8E6C9"
        ).pack(side="left", padx=5)

    def add_to_cart(self, item, price):
        self.cart.append((item, price))
        self.receipt_box.insert(tk.END, f"{item} - ${price:.2f}")
        self.update_total()

    def update_total(self):
        total = sum(price for item, price in self.cart)
        self.total_label.config(text=f"Total: ${total:.2f}")

    def clear_cart(self):
        self.cart = []
        self.receipt_box.delete(0, tk.END)
        self.update_total()

    def checkout(self):
        if not self.cart:
            messagebox.showwarning(
                "Empty Cart",
                "Please add items before checking out!"
            )
            return

        # Create receipt window
        receipt_window = tk.Toplevel(self.root)
        receipt_window.title("Receipt")
        receipt_window.geometry("350x400")

        receipt_text = tk.Text(receipt_window, width=40, height=20)
        receipt_text.pack(pady=10)

        # Receipt Header
        receipt_text.insert(tk.END, "====== QUICKBITE RECEIPT ======\n")
        receipt_text.insert(
            tk.END,
            f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        receipt_text.insert(tk.END, "-" * 35 + "\n")

        total = 0

        # Display ordered items
        for item, price in self.cart:
            receipt_text.insert(
                tk.END,
                f"{item:<15} ${price:.2f}\n"
            )
            total += price

        receipt_text.insert(tk.END, "-" * 35 + "\n")
        receipt_text.insert(
            tk.END,
            f"TOTAL: ${total:.2f}\n"
        )
        receipt_text.insert(tk.END, "\nThank you for your order!\n")

        receipt_text.config(state="disabled")

        # Clear cart after checkout
        self.clear_cart()


if __name__ == "__main__":
    root = tk.Tk()
    app = FoodApp(root)
    root.mainloop()