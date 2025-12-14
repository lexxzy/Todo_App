filenames = ["1.dox", "2.pre", "3.todos.txt"]
filenames = [filename.replace(".", "-") + ".txt" for filename in filenames ]
print(filenames)