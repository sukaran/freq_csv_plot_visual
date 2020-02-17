try:
    import tkinter as tk        # python v3
except:
    import Tkinter as tk        # python v2

# This function is called when the submit button is clicked
def submit_callback(input_entry):
    s = str(input_entry.get())

    import os
    os.system('cmd /c "python app.py"')
    if(s)
    return None


#######################  GUI ###########################
root = tk.Tk()
root.geometry('300x150')       #Set window size

# Heading
heading = tk.Label(root, text="A simple GUI")
heading.place(x = 100, y = 0)


input_label = tk.Label(root, text="Enter some text")
input_label.place(x = 0, y = 50)

input_entry = tk.Entry(root)
input_entry.place(x = 100, y = 50)


submit_button = tk.Button(root, text = "Submit", command = lambda: submit_callback(input_entry))
submit_button.place(x = 200, y = 90)
root.mainloop()
#############################################################
