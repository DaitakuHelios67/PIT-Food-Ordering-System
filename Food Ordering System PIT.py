import tkinter as tk
from tkinter import messagebox


menu = {
    "Pizza": 120,
    "Coke Mismo": 25,
    "Burger": 50,
    "Fries": 30,
    "Ice Cream": 30
}


class FoodOrderingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Ordering System")
        self.root.geometry("400x400")

        self.order_total = 0
        self.selected_items = []