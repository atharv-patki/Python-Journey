import tkinter as tk
from tkinter import messagebox
from matplotlib import pyplot as plt
from fpdf import FPDF
import os

# Function to generate the pie chart and save it as a PDF
def generate_pie_chart():
    try:
        name = name_entry.get()
        monthly_income = float(income_entry.get())  # Added monthly income
        travel_expense = float(travel_entry.get())
        food_expense = float(food_entry.get())
        shopping_expense = float(shopping_entry.get())
        entertainment_expense = float(entertainment_entry.get())
        others_expense = float(others_entry.get())

        total_expense = travel_expense + food_expense + shopping_expense + entertainment_expense + others_expense

        # Check if total expense exceeds income
        if total_expense > monthly_income:
            messagebox.showerror("Input Error", "Total expenses cannot exceed monthly income!")
            return

        # Data for pie chart
        expenses = [travel_expense, food_expense, shopping_expense, entertainment_expense, others_expense]
        categories = ['Travel', 'Food', 'Shopping', 'Entertainment', 'Others']

        # Generate pie chart
        plt.pie(expenses, labels=categories, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Save the chart as a PNG image
        chart_file = f"{name}_expense_chart.png"
        plt.savefig(chart_file)
        plt.show()

        # Create a PDF and embed the pie chart image
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, f"Expense Report for {name}", ln=True, align="C")
        pdf.cell(200, 10, f"Monthly Income: ${monthly_income:.2f}", ln=True, align="C")
        pdf.image(chart_file, x=50, y=50, w=100, h=100)
        pdf_file = f"{name}_expense_report.pdf"
        pdf.output(pdf_file)

        # Cleanup the temporary image file
        os.remove(chart_file)

        messagebox.showinfo("Success", f"Pie chart saved as {pdf_file}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")

# GUI Setup
root = tk.Tk()
root.title("Chart Generator")

# Set the window to full screen
root.state("zoomed")

# Define font styles
label_font = ("Goudy Old Style", 24)  # Larger font size for labels
entry_font = ("Goudy Old Style", 20)  # Larger font size for entries
button_font = ("Goudy Old Style", 24)  # Larger font size for button

# Create a frame to center the content
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Labels and input fields
tk.Label(frame, text="Enter your name:", font=label_font).grid(row=0, column=0, padx=20, pady=20)
name_entry = tk.Entry(frame, font=entry_font, width=15)
name_entry.grid(row=0, column=1, padx=20, pady=20)

tk.Label(frame, text="Monthly Income:", font=label_font).grid(row=1, column=0, padx=20, pady=20)  # Added income label
income_entry = tk.Entry(frame, font=entry_font, width=15)
income_entry.grid(row=1, column=1, padx=20, pady=20)

tk.Label(frame, text="Travel Expense:", font=label_font).grid(row=2, column=0, padx=20, pady=20)
travel_entry = tk.Entry(frame, font=entry_font, width=15)
travel_entry.grid(row=2, column=1, padx=20, pady=20)

tk.Label(frame, text="Food Expense:", font=label_font).grid(row=3, column=0, padx=20, pady=20)
food_entry = tk.Entry(frame, font=entry_font, width=15)
food_entry.grid(row=3, column=1, padx=20, pady=20)

tk.Label(frame, text="Shopping Expense:", font=label_font).grid(row=4, column=0, padx=20, pady=20)
shopping_entry = tk.Entry(frame, font=entry_font, width=15)
shopping_entry.grid(row=4, column=1, padx=20, pady=20)

tk.Label(frame, text="Entertainment Expense:", font=label_font).grid(row=5, column=0, padx=20, pady=20)
entertainment_entry = tk.Entry(frame, font=entry_font, width=15)
entertainment_entry.grid(row=5, column=1, padx=20, pady=20)

tk.Label(frame, text="Others Expense:", font=label_font).grid(row=6, column=0, padx=20, pady=20)
others_entry = tk.Entry(frame, font=entry_font, width=15)
others_entry.grid(row=6, column=1, padx=20, pady=20)

# Generate chart button
generate_button = tk.Button(frame, text="Generate Pie Chart", font=button_font, command=generate_pie_chart)
generate_button.grid(row=7, columnspan=2, pady=40)

root.mainloop()
