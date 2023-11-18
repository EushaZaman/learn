from pathlib import Path
DIR = r"C:\Users\eusha\PycharmProjects\learn"
path = Path(DIR)
def printdirectory():
    for p in path.iterdir():
        print(p)
if __name__ == "__main__":
    print(printdirectory())