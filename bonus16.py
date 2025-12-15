import FreeSimpleGUI as sg

label1 = sg.Text("Select your Files: ")
inpu1 = sg.Input()
choose1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select your Folder: ")
inpu2 = sg.Input()
choose2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress", button_color="green", size=10)

window = sg.Window("File and Folder Selector", layout=[
    [label1],
    [inpu1, choose1],
    [label2],
    [inpu2, choose2],
    [compress_button]
])
window.read()
window.close()