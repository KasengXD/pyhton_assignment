import tkinter as tk
from tkinter import messagebox

# 1. THE BRAIN (Logic)
def recommend_course():
    user_interest = entry.get().lower()
    
    # Simple logic: If user mentions 'car', suggest Automotive
    if "car" in user_interest or "engine" in user_interest:
        result = "Recommended: Automotive Engineering"
    elif "computer" in user_interest or "code" in user_interest:
        result = "Recommended: Information Technology"
    else:
        result = "Try keywords like 'car' or 'computer'."
        
    messagebox.showinfo("Result", result)

# 2. THE FACE (GUI)
root = tk.Tk()
root.title("T-VET Recommender")
root.geometry("400x300")

label = tk.Label(root, text="Enter your interest:")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

btn = tk.Button(root, text="Find Course", command=recommend_course)
btn.pack(pady=20)

root.mainloop()
