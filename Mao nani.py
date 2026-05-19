
import customtkinter as ctk
from tkinter import messagebox

menu = {
    "Classic Burger": 50,
    "Cheese Burger": 65,
    "Fried Chicken": 75,
    "Coke Mismo": 25,
    "French Fries": 30
}

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class SimpleDinerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Helios Diner")
        self.geometry("600x500")

        self.order_total = 0
        self.selected_items = {}
        
        self.build_screen()

    def build_screen(self):
        ctk.CTkLabel(
            self, text="☀️ Helios Diner", font=("Arial", 24, "bold"), text_color="#FFC300"
        ).pack(pady=10)

        ctk.CTkLabel(self, text="Click to Add Items:", font=("Arial", 14)).pack()
        
        for item_name, price in menu.items():
            ctk.CTkButton(
                self, 
                text=f"{item_name} - ₱{price}", 
                fg_color="#FF7A00", 
                command=lambda name=item_name, p=price: self.add_to_cart(name, p)
            ).pack(pady=5)

        ctk.CTkLabel(self, text="--- Your Cart ---", font=("Arial", 16)).pack(pady=10)
        
        self.cart_label = ctk.CTkLabel(self, text="Cart is empty", font=("Arial", 14))
        self.cart_label.pack()

        self.total_label = ctk.CTkLabel(self, text="Total: ₱0", font=("Arial", 18, "bold"), text_color="#FFC300")
        self.total_label.pack(pady=10)

        ctk.CTkButton(
            self, text="Place Order (Print Receipt)", fg_color="#FFC300", text_color="black",
            command=self.print_receipt
        ).pack(pady=10)

    def add_to_cart(self, item_name, price):
        self.order_total += price
        
        if item_name in self.selected_items:
            self.selected_items[item_name] += 1
        else:
            self.selected_items[item_name] = 1
            
        self.total_label.configure(text=f"Total: ₱{self.order_total}")
        
        cart_text = ""
        for name, quantity in self.selected_items.items():
            cart_text += f"{quantity}x {name}\n"
            
        self.cart_label.configure(text=cart_text)

    def print_receipt(self):
        if self.order_total == 0:
            messagebox.showinfo("Error", "Cart is empty!")
            return
            
        try:
            with open("Simple_Receipt.txt", "w") as file:
                file.write("=== HELIOS DINER ===\n")
                
                for item, qty in self.selected_items.items():
                    price = menu[item]
                    file.write(f"{qty}x {item} (P{price*qty})\n")
                    
                file.write(f"\nTOTAL: P{self.order_total}\n")
                file.write("====================\n")
                
            messagebox.showinfo("Success", f"Order placed for P{self.order_total}!\nReceipt saved to computer.")
            
            self.order_total = 0
            self.selected_items.clear()
            self.cart_label.configure(text="Cart is empty")
            self.total_label.configure(text="Total: ₱0")
            
        except Exception as error:
            messagebox.showerror("Error", f"Failed to save receipt: {error}")

if __name__ == "__main__":
    app = SimpleDinerApp()
    app.mainloop()