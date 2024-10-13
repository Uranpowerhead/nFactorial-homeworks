def exercise_1():
    print('Exercise 1: Begin')
    number_1, number_2 = 4, 6
    summa = number_1 + number_2
    print(f'Summ of {number_1} and {number_2} equals {summa}')
    print('Exercise 1: End\n')


def exercise_2():
    print('Exercise 2: Begin')
    string_origin = 'Exercise 2 homework Duganov Alisher'
    string_origin_reversed = string_origin[::-1]
    print(f'Origin string: {string_origin}\nReversed string: {string_origin_reversed}')
    print('Exercise 2: End\n')


def exercise_3():
    print('Exercise 3: Begin')
    string = 'Exercise 3 homework Duganov Alisher'
    string_length = len(string)
    print(f'Length of string {string} equals: {string_length}')
    print('Exercise 3: End\n')


def exercise_4():
    print('Exercise 4: Begin')
    string_one, string_two = 'Duganov ', 'Alisher'
    concatenated_string = string_one + string_two
    print(f'Origin strings: {string_one} and {string_two}')
    print('Concatenated string:', concatenated_string)
    print('Exercise 4: End\n')


def exercise_5():
    print('Exercise 5: Begin')
    character = 'e'
    character_vowel = character.lower() in 'euioa'
    print(f'character: {character}\n{character} is vowel? {character_vowel}')
    print('Exercise 5: End\n')


def exercise_6():
    print('Exercise 6: Begin')
    string_original = "Duganov Alisher NFactorial's best student"
    modified_string = string_original[-1] + string_original[1:-1] + string_original[0]
    print('Origin string:', string_original)
    print('Modified string:', modified_string)
    print('Exercise 6: End\n')


def exercise_7():
    print('Exercsie 7: Begin')
    string_original = "mellstroy casino money"
    string_upper = string_original.upper()
    print(f'Original string {string_original}\nUppercase string {string_upper}\nExercise 7: End\n')


def exercise_8():
    length = 66
    width = 88
    area = length * width
    print(f'Exercise 8: Begin\nlength = {length}\nwidth = {width}\narea = {area}\nExercise 8: End\n')


def exercise_9():
    number = 486
    even_number = number % 2 == 0
    print(f'Exercise 9: Begin\nnumber = {number}\nis {number} even? {even_number}\nExercise 9: End\n')


def exercise_10():
    string = 'BOBR KURWA'
    first_three = string[0:3]
    print(f'Exercise 10: Begin\nstring: {string}\nextracted characters: {first_three}\nExercise 10: End\n')


def exercise_11():
    name = 'Alisher'
    age = '26'
    interpolation = f'My name is {name}, and i {age} years old'
    print('Exercise 11: Begin\n'
          f'name: {name}\n'
          f'age: {age}\n'
          f'Interpolation: {interpolation}\n'
          'Exercise 11: End\n')
    

def exercise_12():
    string = 'VOLKSWAGEN AUDI PERDOLE'
    string_slice = string[2:6]
    print('Exercise 12: Begin\n'
          f'original string: {string}\n'
          f'extracted characters from 2 to 5 (inclusive) {string_slice}\n'
          'Exercise 12: End\n')
    

def exercise_13():
    string_number = '123456789'
    int_number = int(string_number)
    print('Exercise 13: Begin\n'
          f'string number {string_number}\n'
          f'integer number {int_number}\n'
          'Exercise 13: End\n')


def exercise_14():
    string = 'SecuRity'
    print('Exercise 14: Begin\n'
          f'Original string: {string}\n'
          'Repeated string:', string * 3, '\n'
          'Exercise 14: End\n')
    

def exercise_15():
    number_1, number_2 = 789, 456
    print('Exercise 15: Begin\n'
          f'two numbers: {number_1}, {number_2}\n'
          f'quotient of {number_1} / {number_2} equals', number_1 // number_2, '\n'
          f'remainder of {number_1} / {number_2} equals', number_1 % number_2, '\n'
          'Exercise 15: End\n')


def exercise_16():
    number_1, number_2 = 456.78, 905.33
    print('Exercise 16: Begin\n'
          f'Float division of {number_1} and {number_2} =', number_1 / number_2, '\n'
          'Exercise 16: End\n')


def exercise_17():
    string = 'boBR Bobr boBr Bobr Kurwa'
    counts = string.count('bo')
    print('Exercise 17: Begin\n'
          f"Occurences of 'bo' in {string}:", counts, '\n'
          'Exercise 17: End\n')


def exercise_18():
    string = "This is text with \"double quotes\" inside"
    print('Exercise 18: Begin\n'
          f'String with double quotes inside: {string}\n'
          'Exercise 18: End\n')
    

def exercise_19():
    multi_line_string = """Eto stroka
multiline string
Hello World1234"""
    print('Exercise 19: Begin\n'
          f'Multi-line string:\n{multi_line_string}\n'
          'Exercise 19: End\n')
    

def exercise_20():
    base = -17
    exponent = 2
    print('Exercise 20: Begin\n'
          f'Base = {base}, exponent = {exponent}\n'
          'Result of base to the power of exponent =', base ** exponent, '\n'
          'Exercise 20: End\n')


def exercise_21():
    text = 'ZoobelttobeRussiaissurebottlebooz'
    print('Exercise 21: Begin\n'
          'Is', text, 'is palindrome?\n',text[::].lower() == text[::-1].lower())
    print('Exercise 21: End\n')


def exercise_22():
    first_string = 'логика'
    second_string = 'иголка'
    first = sorted(first_string)
    second = sorted(second_string)
    print('Exercise 22: Begin\n'
          f'Is {first_string} and {second_string} anagram?\n', first == second, '\n'
          'Exercise 22: End')    
if __name__ == '__main__':
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
    exercise_9()
    exercise_10()
    exercise_11()
    exercise_12()
    exercise_13()
    exercise_14()
    exercise_15()
    exercise_16()
    exercise_17()
    exercise_18()
    exercise_19()
    exercise_20()
    exercise_21()
    exercise_22()