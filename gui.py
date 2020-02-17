import PySimpleGUI as sg

# Very basic form.  Return values as a list
form = sg.FlexForm('GUI for the Project')  # begin with a blank form

layout = [
          [sg.Text('Number of entries, Number of characters, Character ')],
          [sg.Text('Number of entries', size=(15, 1)), sg.InputText('')],
          [sg.Text('Character', size=(15, 1)), sg.InputText('')],
          [sg.Submit(), sg.Cancel()]
         ]

button, values = form.Layout(layout).Read()
import os
os.system('cmd /C "python app.py 10 10 C"')
if values[0]==10:
    os.system('cmd /C "python app.py 15 10 C"')
if values[0]==50:
    os.system('cmd /C "python app.py 15 100 C"')
if values[0]==100:
    os.system('cmd /C "python app.py 15 100 C"')
if values[1] =='N':
    os.system('cmd /C "python app.py 15 10 N"')
if values[1]=='D':
    os.system('cmd /C "python app.py 15 10 D"')



#print(button, values[0], values[1], values[2])