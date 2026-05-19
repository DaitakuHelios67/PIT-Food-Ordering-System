import customtkinter as ctk
from tkinter import messagebox

menu = {
    "Main Food": {
        "Classic Burger": 50,
        "Cheese Burger": 65,
        "Pepperoni Pizza": 120,
        "Spaghetti": 85,
        "Fried Chicken (1pc)": 75
    },
    "Beverages": {
        "Coke Mismo": 25,
        "Sprite Mismo": 25,
        "Iced Tea": 30,
        "Iced Coffee": 45,
        "Bottled Water": 20
    },
    "Add Ons": {
        "French Fries": 30,
        "Sundae Ice Cream": 30,
        "Extra Cheese": 15,
        "Extra Rice": 20
    }
}

HELIOS_ORANGE = "#FF7A00"  
HELIOS_GOLD = "#FFC300"    
RAYFIELD_BG = "#1E1E1E"    
RAYFIELD_CARD = "#2A2A2A"  
WHITE_TEXT = "#FFFFFF"

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class FoodOrderingApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Helios Diner Kiosk - Dashboard")
        self.geometry("1150x650")
        self.configure(fg_color=RAYFIELD_BG)

        self.order_total = 0
        self.selected_items = {} 
        self.total_item_count = 0
        
        self.create_widgets()

    def create_widgets(self):
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color=HELIOS_ORANGE)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        ctk.CTkLabel(
            self.sidebar, text="HELIOS\nDINER", font=ctk.CTkFont(family="Helvetica", size=26, weight="bold"), 
            text_color=WHITE_TEXT
        ).pack(pady=(35, 0))
        
        ctk.CTkLabel(
            self.sidebar, text="Kiosk System v1.0", font=ctk.CTkFont(size=12), 
            text_color=WHITE_TEXT
        ).pack(pady=(0, 40))

        ctk.CTkLabel(
            self.sidebar, text="Status: Online\nTerminal: #01", font=ctk.CTkFont(size=14, weight="bold"), 
            text_color=WHITE_TEXT, justify="left"
        ).pack(side="bottom", pady=30)

        self.menu_view = ctk.CTkFrame(self, fg_color="transparent")
        self.menu_view.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(
            self.menu_view, text="☀️ Our Menu", font=ctk.CTkFont(size=26, weight="bold"), 
            text_color=WHITE_TEXT, anchor="w"
        ).pack(fill="x", pady=(0, 15))

        self.category_var = ctk.StringVar(value="Main Food")
        self.category_tabs = ctk.CTkSegmentedButton(
            self.menu_view, 
            values=["Main Food", "Beverages", "Add Ons"],
            variable=self.category_var,
            command=self.load_menu_category,
            font=ctk.CTkFont(size=14, weight="bold"),
            selected_color=HELIOS_GOLD,
            selected_hover_color="#E5A900",
            unselected_color=RAYFIELD_CARD,
            unselected_hover_color="#333333",
            text_color=RAYFIELD_BG
        )
        self.category_tabs.pack(fill="x", pady=(0, 15))

        self.menu_scroll_frame = ctk.CTkScrollableFrame(self.menu_view, fg_color="transparent")
        self.menu_scroll_frame.pack(fill="both", expand=True)

        self.load_menu_category("Main Food")

        self.cart_view = ctk.CTkFrame(self, fg_color="transparent", width=400)
        self.cart_view.pack(side="right", fill="y", padx=(0, 20), pady=20)
        self.cart_view.pack_propagate(False) 
        
        self.cart_title = ctk.CTkLabel(
            self.cart_view, text="🛒 Your Order (0)", font=ctk.CTkFont(size=26, weight="bold"), 
            text_color=WHITE_TEXT, anchor="w"
        )
        self.cart_title.pack(fill="x", pady=(0, 20))

        self.cart_scroll_frame = ctk.CTkScrollableFrame(self.cart_view, fg_color="transparent")
        self.cart_scroll_frame.pack(fill="both", expand=True)

        self.checkout_panel = ctk.CTkFrame(self.cart_view, fg_color=RAYFIELD_CARD, corner_radius=10)
        self.checkout_panel.pack(fill="x", pady=(15, 0))

        self.total_label = ctk.CTkLabel(
            self.checkout_panel, text="Total: ₱0", font=ctk.CTkFont(size=22, weight="bold"), 
            text_color=HELIOS_GOLD
        )
        self.total_label.pack(side="left", padx=20, pady=20)

        ctk.CTkButton(
            self.checkout_panel, text="PLACE ORDER", font=ctk.CTkFont(size=14, weight="bold"), 
            fg_color=HELIOS_GOLD, hover_color="#E5A900", text_color="black",
            corner_radius=8, height=40, width=120, command=self.place_order
        ).pack(side="right", padx=15, pady=15)
        
        ctk.CTkButton(
            self.checkout_panel, text="Clear", font=ctk.CTkFont(size=14, weight="bold"), 
            fg_color="transparent", hover_color="#333333", text_color=HELIOS_ORANGE,
            corner_radius=8, height=40, width=60, border_width=1, border_color=HELIOS_ORANGE,
            command=self.clear_order
        ).pack(side="right", padx=5, pady=15)

        self.update_cart_ui()

    def load_menu_category(self, category_name):
        for widget in self.menu_scroll_frame.winfo_children():
            widget.destroy()
            
