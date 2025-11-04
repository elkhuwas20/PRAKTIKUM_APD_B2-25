import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")
