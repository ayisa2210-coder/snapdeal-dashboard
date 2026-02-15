import tkinter as tk
from tkinter import ttk

# ================= SAMPLE DATA =================
products = [
    {"Product Name": "Laptop A", "Price": 800, "Discount": 55, "Rating": 4.2},
    {"Product Name": "Laptop B", "Price": 950, "Discount": 8, "Rating": 2.9},
    {"Product Name": "Laptop C", "Price": 1200, "Discount": 25, "Rating": 3.8},
    {"Product Name": "Laptop D", "Price": 700, "Discount": 60, "Rating": 4.5},
]

# ================= CREATE WINDOW =================
root = tk.Tk()
root.title("Products Table with Conditional Formatting")
root.geometry("700x300")

# ================= CREATE TREEVIEW =================
columns = ("Product Name", "Price", "Discount", "Rating")
table = ttk.Treeview(root, columns=columns, show="headings")

# Headings
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=150, anchor="center")

# ================= INSERT DATA WITH CONDITIONAL FORMATTING =================
for p in products:
    discount = p["Discount"]
    rating = p["Rating"]

    # Default background
    bg_color = "white"

    # Conditional formatting
    if discount > 50:
        bg_color = "lightgreen"
    elif discount < 10:
        bg_color = "red"
    elif rating < 3:
        bg_color = "orange"

    table.insert("", "end", values=(p["Product Name"], p["Price"], discount, rating),
                 tags=(bg_color,))

# Define tag colors
table.tag_configure("lightgreen", background="lightgreen")
table.tag_configure("red", background="red")
table.tag_configure("orange", background="orange")
table.tag_configure("white", background="white")

# Pack table
table.pack(expand=True, fill="both", padx=10, pady=10)

# Run Window
root.mainloop()