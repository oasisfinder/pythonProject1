# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name}바보')  # Press Ctrl+F8 to toggle the breakpoint.

def random_string(n):
    name_samples =["누리", "우기", "영훈", "지회", "바보", "꼬부기", "서진", "냄새꼬"]
    result = ""
    for i in range(n):
        result += random.choice(name_samples)
    return result

# Press the green button in the gutter to run the script.
a= random_string(1)
print_hi(a)
