import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta, timezone

# Define time zone offsets relative to UTC
timezones = {
    "UTC (UTC+0)": 0,
    "ET (Eastern Time, UTC-4)": -4,
    "CET (Central European Time, UTC+1)": 1,
    "IST (Indian Standard Time, UTC+5:30)": 5.5,
    "CST (China Standard Time, UTC+8)": 8,
    "JST (Japan Standard Time, UTC+9)": 9,
    "AEST (Australian Eastern Standard Time, UTC+10)": 10,
    "PST (Pacific Standard Time, UTC-7)": -7,
    "MST (Mountain Standard Time, UTC-6)": -6,
    "CST (Central Standard Time, UTC-5)": -5,
    "GMT (Greenwich Mean Time, UTC+0)": 0,
    "BST (British Summer Time, UTC+1)": 1,
    "CEST (Central European Summer Time, UTC+2)": 2,
    "WET (Western European Time, UTC+0)": 0,
    "WEST (Western European Summer Time, UTC+1)": 1,
    "AKST (Alaska Standard Time, UTC-9)": -9,
    "HST (Hawaii-Aleutian Standard Time, UTC-10)": -10
}

def convert_time():
    input_time_str = time_entry.get()
    from_tz = from_tz_var.get()
    to_tz = to_tz_var.get()

    try:
        input_time = datetime.strptime(input_time_str, '%Y-%m-%d %H:%M')
    except ValueError:
        result_label.config(text="Invalid time format! Please use 'YYYY-MM-DD HH:MM'")
        return

    from_offset = timezones[from_tz]
    to_offset = timezones[to_tz]
    
    input_time = input_time.replace(tzinfo=timezone(timedelta(hours=from_offset)))
    converted_time = input_time + timedelta(hours=(to_offset - from_offset))

    result_label.config(text=f"Converted time: {converted_time.strftime('%Y-%m-%d %H:%M')}")

app = tk.Tk()
app.title("Time Zone Converter")

# Time Entry
tk.Label(app, text="Enter time (YYYY-MM-DD HH:MM):").grid(row=0, column=0, padx=10, pady=10)
time_entry = tk.Entry(app)
time_entry.grid(row=0, column=1, padx=10, pady=10)

# From Timezone Dropdown
tk.Label(app, text="From Timezone:").grid(row=1, column=0, padx=10, pady=10)
from_tz_var = tk.StringVar()
from_tz_dropdown = ttk.Combobox(app, textvariable=from_tz_var, values=list(timezones.keys()), width=30)
from_tz_dropdown.grid(row=1, column=1, padx=10, pady=10)
from_tz_dropdown.current(0)

# To Timezone Dropdown
tk.Label(app, text="To Timezone:").grid(row=2, column=0, padx=10, pady=10)
to_tz_var = tk.StringVar()
to_tz_dropdown = ttk.Combobox(app, textvariable=to_tz_var, values=list(timezones.keys()), width=30)
to_tz_dropdown.grid(row=2, column=1, padx=10, pady=10)
to_tz_dropdown.current(1)

# Convert Button
convert_button = tk.Button(app, text="Convert", command=convert_time)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Result Display
result_label = tk.Label(app, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()
