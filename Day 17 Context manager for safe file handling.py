class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f"The File {self.filename} is opened in '{self.mode}' mode.")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"The File {self.filename} is closed safely.")
        if exc_type:
            print(f"Error occurred: {exc_type}, {exc_val}")
        return True  # Prevent crashing on exceptions

with FileManager("sample.txt", "w") as f:
    f.write("This file is safely handled using a custom context manager.\n")

with FileManager("sample.txt", "r") as f:
    print("File Content:", f.read())