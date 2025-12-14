filename = ["1.Raw Data.txt", "2.Processed Data.txt", "3.Summary.txt"]
for file in filename:
    file = file.replace(".", "_", 1)
    print(file)
print(filename)