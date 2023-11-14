# lab7
#2
import random

def read_random_line(name):
    try:
        with open(name, 'r') as file:
            lines = file.readlines()
            print(random.choice(lines).strip() if lines else f"File '{name}' is yes.")
    except FileNotFoundError:
        print(f"no '{name}'  found.")

read_random_line('text1.txt')

#3
def count_uppercase_zaglav_characters(fname):
    try:
        with open(fname, 'r') as file:
            text = file.read()
            uppercase_count = sum(1 for char in text if char.isupper())
            print(f"Result of numbers in '{fname}': {uppercase_count}")
    except FileNotFoundError:
        print(f"File '{fname}' not found.")

count_uppercase_zaglav_characters('text1.txt')
#4
def count_lines_not_starting_with_d(fname):
    try:
        with open(fname, 'r') as file:
            lines = file.readlines()
            count = sum(1 for line in lines if not line.startswith('D'))
            print(f"количества строк которые не начинаются с ‘D’в '{fname}': {count}")
    except FileNotFoundError:
        print(f"File '{fname}' not found.")

count_lines_not_starting_with_d('text1.txt')
#5
def count_words_ending_with_f(fname):
    try:
        with open(fname, 'r') as file:
            text = file.read()
            words = text.split()
            f_words_count = sum(1 for word in words if word.lower().endswith('f'))
            print(f"Number of words ending with 'F' in '{fname}': {f_words_count}")
    except FileNotFoundError:
        print(f"File '{fname}' not found.")

count_words_ending_with_f('text1.txt')
#6
def count_all_none_words(fname):
    try:
        with open(fname, 'r') as file:
            text = file.read().lower()
            print(f" 'all': {text.count('all')}")
            print(f" 'none': {text.count('none')}")
    except FileNotFoundError:
        print(f"File '{fname}' not found.")

count_all_none_words('text1.txt')

#7
import string

def count_word_frequency(fname):
    try:
        with open(fname, 'r') as file:
            words = file.read().lower().translate(str.maketrans('', '', string.punctuation)).split()
            
            word_frequency = {}
            
            for word in words:
                word_frequency[word] = word_frequency.get(word, 0) + 1
            
            print(f"Word frequency in '{fname}':")
            for word, frequency in word_frequency.items():
                print(f"{word}: {frequency}")
                
    except FileNotFoundError:
        print(f"File '{fname}' not found.")

count_word_frequency('text1.txt')
#8
def find_longest_word(fname):
    try:
        with open(fname, 'r') as file:
            longest_word = max(file.read().split(), key=len, default="")
            print(f"The longest word in '{fname}' is: {longest_word}")
    except FileNotFoundError:
        print(f"File '{fname}' not found.")

find_longest_word('text1.txt')
#9
def correct_file_content(fname):
    try:
        with open(fname, 'r') as file:
            print(file.read().replace('B', 'J'))
    except FileNotFoundError:
        print(f"File '{fname}' not found.")

correct_file_content('text1.txt')
#10
def count_A_and_B(fname):
    try:
        with open(fname, 'r') as file:
            text = file.read().lower()
            count_A = text.count('a')
            count_B = text.count('b')
            print(f" A: {count_A}, B: {count_B}")
    except FileNotFoundError:
        print(f"File '{fname}' not found.")

count_A_and_B('text1.txt')
