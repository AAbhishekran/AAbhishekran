import PySimpleGUI as ss
from jinja2.nodes import Add

import function
list_box = ss.Listbox(values = function.file(), key="main",size=[45,15])
Layout = [[ss.Text("This is my todoaap",key="text")],
          [ss.InputText(tooltip="Enter your todo id her",key="todo"),
           ss.Button("Add")],[list_box]
          ]
window = ss.Window(title="Todosaap" , layout=Layout,font=("Bold",10))

while True:
    event , values = window.read()
    print(event)
    print(values)
    match event:
        case Add:
            new_todo = values["todo"] + "\n"
            todos=function.file()
            todos.append(new_todo)
            function.write(todos)
            window["main"].update(values=todos)
window.close()