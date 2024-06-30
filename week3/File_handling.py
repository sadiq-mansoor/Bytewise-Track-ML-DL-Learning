def read_file(filename):
    "The method takes one agruement which is the filename and reads the file while also handling errors with try and except"

    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError as e:
        print(f"Error: File '{filename}'not found.")
        return None


def write_file(filename, content):
    """Writes content to a file and handles potential OSError.

     Args:
       filename, content
     """

    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Successfully wrote content to'{filename}'.")
    except OSError as e:
        print(f"Error writing to file '{filename}':{e}")


def count_words(content):
    if not content:
        return 0
    return len(content.split())


def main():
    contents = read_file("data.txt")
    if contents:
        print(contents)

        word_count=count_words(contents)
        print(f"Word count: {word_count}")

    user_input=input("Enter text to write to the file: ")
    write_file("output.txt", user_input)


if __name__ == "__main__":
    main()