def read_file(file_name):
    try:
        with open(file_name, "r") as fh:
            return fh.read()
    except FileNotFoundError:
        print("File not found")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def replace_text(text, old, new):
    try:
        return text.replace(old, new)
    except Exception as e:
        print(f"Error replacing text: {e}")
        return None

def write_file(file_name, text):
    try:
        with open(file_name, "w") as fh:
            fh.write(text)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

def main():
    file_name = input("Enter file name: ")
    text = read_file(file_name)
    if text is not None:
        old = input("Enter old string: ")
        new = input("Enter new string: ")

        if old == new:
            print("Error: The old and new strings are the same.")
        else:
            modified_text = replace_text(text, old, new)
            if modified_text is not None:
                if write_file(file_name, modified_text):
                    print("Done")

main()
