import PySimpleGUI as ss

Layout = [[ss.Text("This is my todoaap",key="text")],
          [ss.InputText(tooltip="Enter your todo id her"),ss.Button("Enter")],

          ]
window = ss.Window(title="Todosaap" , layout=Layout,font=("Bold",20))


window.read()
window.close()