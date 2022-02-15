# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import os


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    hi = f'{name} 먹자'  # Press Ctrl+F8 to toggle the breakpoint.
    return hi


def random_string():
    name_samples =["중식", "회", "일식", "한식", "치킨", "피자", "분식", "물","밥","오란다"]
    result = random.choice(name_samples)
    return result


# Press the green button in the gutter to run the script.

for i in range(10):
    a = random_string()
    filename = str(i) + a + ".txt"
    outfile = open(filename, 'w')
    outfile.write(print_hi(a))
    outfile.close()

