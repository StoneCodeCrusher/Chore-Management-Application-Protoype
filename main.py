import tkinter as tk
from chore_list import ChoreList


## --root window--

## root window, title, dimensions
root = tk.Tk()
root.title("Chore Management")
root_width = 1000
root_height = 500

screen_width = root.winfo_screenwidth()
x = (screen_width // 2) - (root_width // 2)
y = 0

root.geometry(f"{root_width}x{root_height}+{x}+{y}")
root.resizable(False, False)


## --Frames--

## Header frame
header_frame = tk.Frame(root, width=root_width, height=50, bg="lightgray")
header_frame.pack(side="top", fill = "x")
header_frame.pack_propagate(False)
header = tk.Label(header_frame, text="Manage Your Chores!", bg="lightgray", font=("Arial",14))
header.pack(expand=True)

# Main frame 
main_frame = tk.Frame(root, width=root_width, height=root_height-50)
main_frame.pack(side="top", fill="both")
main_frame.pack_propagate(False)

# Left frame inside main 
left_frame = tk.Frame(main_frame, width=500, height=root_height-50)
left_frame.pack(side="left", fill="y")
left_frame.pack_propagate(False)

# Right frame inside main 
right_frame = tk.Frame(main_frame, width=500, height=root_height-50)
right_frame.pack(side="left", fill="y")
right_frame.pack_propagate(False)


## --Left frame widgets--

## Chore Entry Field
choretxt = tk.Entry(left_frame, width=20)
choretxt.pack(pady = 10)
choretxt.focus()

notice = tk.Label(left_frame, text = "Add Chore", font = ("Arial", 14))
notice.pack(pady=20)



## Create chore list
chore_list = ChoreList()


## --Methods -- 
## Event Notice Add Button *declare before button*
def add_chore_click():
    global pending_chore
    pending_chore = choretxt.get().strip()
    
    
    if not pending_chore:
        notice.config(text="Please enter a chore")
        return
    
    if pending_chore:
        notice.config(text="Select chore frequency")

        
    cleaned = pending_chore.replace(" ", "")
    if not cleaned.isalnum():
        notice.config(text="Chore name must contain only letters and numbers")

        return    
        
    add_button.config(state="disabled")
    add_button.config(state="disabled")
    enable_freq_buttons()
    freq_frame.pack(pady=10)

    notice.config(text= "Select a schedule for this chore")

    
def handle_chore_freq(frequency):
    chore_list.add_chore(pending_chore, frequency)
    
    notice.config(
        text = f"{pending_chore} was added to the {frequency} list")
    
    ## wipe input from field
    choretxt.delete(0, tk.END)
      
    disable_freq_buttons()
    add_button.config(state="normal")
    choretxt.focus()

    
    refresh_chore_list()

def disable_freq_buttons():
    for btn in freq_buttons:
        btn.config(state="disabled")

def enable_freq_buttons():
    for btn in freq_buttons:
        btn.config(state="normal")        

 

add_button = tk.Button(left_frame, text="Add Chore", width=10, command = add_chore_click)
add_button.pack() 

freq_frame = tk.Frame(left_frame)
freq_frame.pack(pady=10) 

## --Add Frequency buttons--
daily_btn = tk.Button(freq_frame, text="Daily",
            width=10,
            command=lambda: handle_chore_freq("Daily"))

weekly_btn = tk.Button(freq_frame, text="Weekly",
             width=10,
             command=lambda: handle_chore_freq("Weekly"))

monthly_btn = tk.Button(freq_frame, text="Monthly",
               width=10,
               command=lambda: handle_chore_freq("Monthly"))

yearly_btn = tk.Button(freq_frame, text="Yearly",
             width=10,
             command=lambda: handle_chore_freq("Yearly"))

## store as list for enable/disable
freq_buttons = [daily_btn, weekly_btn, monthly_btn, yearly_btn]

## pack freq buttons
for btn in freq_buttons:
    btn.pack(side = "left", padx = 5)
    disable_freq_buttons()

          
## --list button control frame--
control_frame = tk.Frame(left_frame)
control_frame.pack(pady = 10)

def refresh_chore_list(filter_freq = None):
    # clear existing rows
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    for chore in chore_list.get_all():
        if filter_freq is None or chore.frequency == filter_freq:
            row = tk.Frame(scrollable_frame)
            row.pack(fill="x", pady=2, padx=5)

            tk.Label(row, text=chore.name, width=20, anchor="w").pack(side="left")
            tk.Label(row, text=chore.frequency, width=10).pack(side="left")
            
def filter_chore_list(frequency=None):
    refresh_chore_list(filter_freq=frequency)

def view_list_click():
    filter_frame.pack(fill="x", pady = 5)
    list_container.pack(fill="both", expand=True, pady=10)
    refresh_chore_list()
    
    view_button.config(state="disabled")
    hide_button.config(state="normal")

def hide_list_click():
    filter_frame.pack_forget()
    list_container.pack_forget()
    
    hide_button.config(state="disabled")
    view_button.config(state="normal")

## Add Chore list button
view_button = tk.Button(control_frame, text="View Chores", width=12, command = view_list_click)
view_button.pack(side = "left", padx = 5)

## Add Hide list button
hide_button = tk.Button(control_frame, text="Hide Chores", width=12, command = hide_list_click)
hide_button.pack(side = "left", padx = 5)                     
hide_button.config(state="disabled")                  

## --Add Chore button--


## Schedule Filter frame
filter_frame = tk.Frame(right_frame)

## Filter Buttons
tk.Button(filter_frame, text="All", width=8, command=lambda: filter_chore_list()).pack(side="left", padx=3)
tk.Button(filter_frame, text="Daily", width=8, command=lambda: filter_chore_list("Daily")).pack(side="left", padx=3)
tk.Button(filter_frame, text="Weekly", width=8, command=lambda: filter_chore_list("Weekly")).pack(side="left", padx=3)
tk.Button(filter_frame, text="Monthly", width=8, command=lambda: filter_chore_list("Monthly")).pack(side="left", padx=3)
tk.Button(filter_frame, text="Yearly", width=8, command=lambda: filter_chore_list("Yearly")).pack(side="left", padx=3)


## Chore List
list_container = tk.Frame(right_frame)
canvas = tk.Canvas(list_container, highlightthickness=0)
scrollbar = tk.Scrollbar(list_container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

## --Button Bindings--

root.bind("<Return>", lambda event: add_chore_click())

root.mainloop()