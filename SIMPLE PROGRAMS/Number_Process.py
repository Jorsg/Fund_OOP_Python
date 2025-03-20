#NUMBER PROCESSING

def number_process(number):
    strings = number.split()
    total = 0
    try:
        for substr in strings:
            total += float(substr)
        print("Total is: ", total)
    except TypeError:
        print(substr, "doesn't a number")


number_process("12 56 89 909 3.3 34.6033 231154332.2 ")