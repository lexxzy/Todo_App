import zipfile
import pathlib

def make_arcive(filepaths, dest_dir):
    dest_dir = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_dir, 'w') as zipf:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            zipf.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_arcive(["todos.txt", "16function.py"], ".")