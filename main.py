import PySimpleGUI as ss
from jinja2.nodes import Add

import function
list_box = ss.Listbox(values = function.file(), key="main",size=[45,15])
Layout = [[ss.Text("This is my todoaap",key="text")],
          [ss.InputText(tooltip="Enter your todo id her",key="todo"),
           ss.Button("Add")],[list_box,ss.Button("edit",key="edit"),
           ss.Button("complete",key="complete")],[ss.Button("Exit")]
          ]
window = ss.Window(title="Todosaap" , layout=Layout,font=("Bold",10))

while True:
    event , values = window.read()
    match event:
        case "Add":
            new_todo = values["todo"] + "\n"
            todos=function.file()
            todos.append(new_todo)
            function.write(todos)
            window["main"].update(values=todos)
            window["todo"].update(value="")
        case "edit":
            try:
               edit_todo=values["main"][0]
               new_todo=values["todo"] + "\n"
               todos = function.file()
               index=todos.index(edit_todo)
               todos[index]=new_todo
               function.write(todos)
               window["main"].update(values=todos)
               window["todo"].update(value="")
            except IndexError:
                ss.popup("plz select the value for edit")
        case "complete":
           try:
              complete_todo=values["main".strip("\n")][0]
              todos = function.file()
              todos.remove(complete_todo)
              function.write(todos)
              window["main"].update(values=todos)
              window["todo"].update(value="")
           except IndexError:
               ss.popup("plz select the value complete")
        case "Exit":
            break

window.close()