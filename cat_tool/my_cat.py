import sys

def my_cat(file_handle, number_lines=False, number_non_blank=False, start_line_number=1):

    current_line_number = start_line_number

    for line in file_handle:
        if number_lines:
            print(f"{current_line_number} {line}", end='')
            current_line_number += 1
        elif number_non_blank:
            if line.strip():
                print(f"{current_line_number} {line}", end='')
                current_line_number += 1
            else:
                print(line, end='')
        else:
            print(line, end='')
    return current_line_number  # Return the last line number processed


def main():
    # Check if standard input is not a TTY, indicating it is being piped
    if not sys.stdin.isatty():
        if len(sys.argv) > 1 and sys.argv[1] == "-n":
            number_lines = True
            number_non_blank = False
        elif len(sys.argv) > 1 and sys.argv[1] == "-b":
            number_lines = False
            number_non_blank = True
        else:
            number_lines = False
            number_non_blank = False
        
        my_cat(file_handle=sys.stdin, number_lines=number_lines, number_non_blank=number_non_blank)
        return

    if len(sys.argv) < 2:
        print("Usage: python my_cat.py [-n] <filename1> <filename2> ...")
        sys.exit(1)

    # Check if -n or -b option is provided
    number_lines = False
    number_non_blank = False
    if sys.argv[1] == '-n':
        number_lines = True
        filenames = sys.argv[2:]
    elif sys.argv[1] == '-b':
        number_non_blank = True
        filenames = sys.argv[2:]
    else:
        filenames = sys.argv[1:]

    current_line_number = 1

    if not filenames:
        print("Usage: python my_cat.py [-n] <filename1> <filename2> ...")
        sys.exit(1)

    for i, filename in enumerate(filenames):
        if i > 0:
            print()   # Print new line in the beginning of next file
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                current_line_number = my_cat(file_handle=file, 
                                            number_lines=number_lines,
                                            number_non_blank=number_non_blank,
                                            start_line_number=current_line_number
                                            )
        except FileNotFoundError:
            print(f"File '{filename}' not found")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()