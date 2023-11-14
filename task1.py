def read_and_display(fname):
    try:
        with open(fname, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"File '{fname}' not found.")

read_and_display('text1.txt')