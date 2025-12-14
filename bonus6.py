contents = ["All caarrots are to be slided down the hill", "Do not eat the yellow snow.", "Remember to water the plants."]
files = ["files/dox.txt", "files/pre.txt", "files/todos.txt" ]

for content, file in zip(contents, files):
    file = open(file, "w")
    file.write(content)