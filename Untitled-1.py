from tkinter import Tk, StringVar, IntVar, Frame, Label, Radiobutton, Button, Spinbox

# Menu prices
prices = {
    "beef": 4000,
    "chicken": 3500,
    "soda": 1000,
    "chapati":500,
    "ugali and dagaa":1500,
    "miogomiitamu":200,
}


# Function to update the price label
def select_item() -> None:
    item = selected_item.get()
    if item in prices:
        price_label.config(text=f"price:${prices[item]:.2f}")
    else:
        price_label.config(text="price:$0.00")


# Function to update the quantity display
def update_quantity_display() -> None:
    quantity_label.config(text=f"Quantity: {quantity_var.get()}")


# Function to calculate the total
def calculate_total() -> None:
    item = selected_item.get()
    quantity = quantity_var.get()
    if item in prices:
        total = prices[item] * quantity
        total_label.config(text=f"total:${total:.2f}")
    else:
        total_label.config(text="total:$0.00")


# Main window
root = Tk()
root.title("baba ezekiel")
root.configure(bg="blue")

selected_item = StringVar(root)
quantity_var = IntVar(root, value=1)

# Menu frame
menu_frame = Frame(root, bg="lightgray")
menu_frame.pack(side="left", padx=10, pady=10)

# Menu items
for item in prices:
    Radiobutton(
        menu_frame,
        text=item,
        variable=selected_item,
        value=item,
        bg="lightblue",
        command=select_item,
    ).pack(anchor="w")

# Price label
price_label = Label(root, text="price:$0.00", bg="lightgrey")
price_label.pack(pady=10)

# Quantity controls
quantity_label = Label(root, text="Quantity: 1", bg="lightgrey")
quantity_label.pack(pady=5)

Spinbox(
    root,
    from_=1,
    to=1000,
    textvariable=quantity_var,
    width=10,
    command=update_quantity_display,
).pack(pady=5)

# Calculate total button
Button(root, text="calculate total", command=calculate_total, bg="lightgreen").pack(pady=10)

# Total label
total_label = Label(root, text="total:$0.00", bg="lavender")
total_label.pack(pady=10)

root.mainloop()