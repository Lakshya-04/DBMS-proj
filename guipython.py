import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

def on_submit():
    selected_options = []

    # Degree
    if var_btech.get():
        selected_options.append("Btech")
    if var_mtech.get():
        selected_options.append("Mtech")

    # Course
    selected_courses = [course_options[i] for i in range(len(course_vars)) if course_vars[i].get()]
    selected_options.extend(selected_courses)

    # Year of study
    selected_years = [year_options[i] for i in range(len(year_vars)) if year_vars[i].get()]
    selected_options.extend(selected_years)

    # Accommodation type
    if var_hosteller.get():
        selected_options.append("Hosteller")
    if var_day_scholar.get():
        selected_options.append("Day-Scholar")

    # Hostel
    selected_hostels = [hostel_options[i] for i in range(len(hostel_vars)) if hostel_vars[i].get()]
    selected_options.extend(selected_hostels)

    # CGPA
    if var_cgpa_above_9.get():
        selected_options.append("CGPA Above 9.0")
    if var_cgpa_below_9.get():
        selected_options.append("CGPA Below 9.0")

    result_label.config(text=", ".join(selected_options))

# Create the main window
root = tk.Tk()
root.title("Student Information")

# Apply Material theme with bright colors
style = ThemedStyle(root)
style.set_theme("arc")

# Create a frame for degree options
degree_frame = ttk.LabelFrame(root, text="Degree")
degree_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

# Create checkboxes for Degree
var_btech = tk.BooleanVar(value=True)
var_mtech = tk.BooleanVar(value=True)
checkbox_btech = ttk.Checkbutton(degree_frame, text="Btech", variable=var_btech)
checkbox_btech.grid(row=0, column=0, padx=5, pady=2, sticky="w")
checkbox_mtech = ttk.Checkbutton(degree_frame, text="Mtech", variable=var_mtech)
checkbox_mtech.grid(row=1, column=0, padx=5, pady=2, sticky="w")

# Course options
course_frame = ttk.LabelFrame(root, text="Course")
course_frame.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

course_options = ["CSE", "CSE AIML", "CSE AIR", "CSE CPS", "EEE", "ECM", "Mech", "Mechatronics"]
course_vars = [tk.BooleanVar(value=True) for _ in range(len(course_options))]
for i, course in enumerate(course_options):
    checkbox_course = ttk.Checkbutton(course_frame, text=course, variable=course_vars[i])
    checkbox_course.grid(row=i, column=0, padx=5, pady=2, sticky="w")

# Year of study options
year_frame = ttk.LabelFrame(root, text="Year of Study")
year_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

year_options = ["1st Year", "2nd Year", "3rd Year", "4th Year"]
year_vars = [tk.BooleanVar(value=True) for _ in range(len(year_options))]
for i, year in enumerate(year_options):
    checkbox_year = ttk.Checkbutton(year_frame, text=year, variable=year_vars[i])
    checkbox_year.grid(row=i, column=0, padx=5, pady=2, sticky="w")

# Accommodation type
accommodation_frame = ttk.LabelFrame(root, text="Accommodation Type")
accommodation_frame.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

var_hosteller = tk.BooleanVar(value=True)
var_day_scholar = tk.BooleanVar(value=True)
checkbox_hosteller = ttk.Checkbutton(accommodation_frame, text="Hosteller", variable=var_hosteller)
checkbox_hosteller.grid(row=0, column=0, padx=5, pady=2, sticky="w")
checkbox_day_scholar = ttk.Checkbutton(accommodation_frame, text="Day Scholar", variable=var_day_scholar)
checkbox_day_scholar.grid(row=1, column=0, padx=5, pady=2, sticky="w")

# Hostel options
hostel_frame = ttk.LabelFrame(root, text="Which Hostel")
hostel_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

hostel_options = ["A", "D1", "D2", "B", "C"]
hostel_vars = [tk.BooleanVar(value=True) for _ in range(len(hostel_options))]
for i, hostel in enumerate(hostel_options):
    checkbox_hostel = ttk.Checkbutton(hostel_frame, text=hostel, variable=hostel_vars[i])
    checkbox_hostel.grid(row=0, column=i, padx=5, pady=2, sticky="w")

# CGPA options
cgpa_frame = ttk.LabelFrame(root, text="CGPA")
cgpa_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

var_cgpa_above_9 = tk.BooleanVar(value=True)
var_cgpa_below_9 = tk.BooleanVar(value=True)
checkbox_cgpa_above_9 = ttk.Checkbutton(cgpa_frame, text="Above 9.0", variable=var_cgpa_above_9)
checkbox_cgpa_above_9.grid(row=0, column=0, padx=5, pady=2, sticky="w")
checkbox_cgpa_below_9 = ttk.Checkbutton(cgpa_frame, text="Below 9.0", variable=var_cgpa_below_9)
checkbox_cgpa_below_9.grid(row=0, column=1, padx=5, pady=2, sticky="w")

# Create submit button
submit_button = ttk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Create label to display result
result_label = ttk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

# Run the main event loop
root.mainloop()
