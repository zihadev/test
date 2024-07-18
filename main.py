import FreeSimpleGUI as fsg
import functions

label1 = fsg.Text("Select file(s) to compress: ")
input_box1 = fsg.InputText()
add_button1 = fsg.FilesBrowse("Choose")

label2 = fsg.Text("Select destination: ")
input_box2 = fsg.InputText()
add_button2 = fsg.FolderBrowse("Choose")
compress_button = fsg.Button("Compress")

layout = [
    [label1],
    [input_box1,add_button1],
    [label2],
    [input_box2, add_button2],
    [compress_button]
]

# Tworzenie okna z tytułem "My App"
window = fsg.Window('My App', layout)

# Pętla wydarzeń
window.read()
window.close()
