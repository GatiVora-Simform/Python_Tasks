def word_to_num(number:str)->str:

    '''
    Converts a string of words representing a number into its digit equivalent.
    word_to_num("onefive") -> "15"

    Args:
    number: A string representing the number in words (e.g., "one", "two", "three").
    
    Returns:
    A string of digits corresponding to the word representation of the number (e.g., "1", "2", "3").
    '''

    num_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero':'0'
    }

    def replace_word(input_string: str, words: list) -> str:
        if not words:
            return input_string
        word = words[0]
        if word in input_string:
            input_string = input_string.replace(word, num_dict[word])
        return replace_word(input_string, words[1:])
    
    words = list(num_dict.keys())
    return replace_word(number, words)


def num_to_word(number:str)->str:

    """
    Converts a string of digits into its corresponding word representation.
    num_to_word("10") -> "onezero"
    
    Args:
    number: A string of digits (e.g., "1", "23", "45").
    
    Returns:
    A string representing the number in words
    """

    word_dict = {
        '1': 'one', 
        '2': 'two', 
        '3': 'three', 
        '4': 'four', 
        '5': 'five', 
        '6': 'six', 
        '7': 'seven', 
        '8': 'eight', 
        '9': 'nine', 
        '0': 'zero'
    }

    def build_word(input_string: str, index: int = 0) -> str:
        if index == len(input_string):
            return ""
        digit = input_string[index]
        return word_dict[digit] + build_word(input_string, index + 1)

    return build_word(number)

def gcd(num1:int,num2:int)->int:

    '''
    Finds the greatest common divisor of two numbers

    Args:
    num1: The first number
    num2: The second number
    
    Returns:
    The greatest common divisor of num1 and num2

    '''
    
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1

    if num1<num2:
        num1,num2 = num2,num1
    
    mod = num1 % num2
    if mod == 0:
        return num2
    else:
        return gcd(num2 ,mod)
   

number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

number1 = int(word_to_num(number1))
number2 = int(word_to_num(number2))

gcd_result = gcd(number1, number2)

gcd_in_words = num_to_word(str(gcd_result))
print(f"GCD of {number1} and {number2} is: {gcd_in_words}")



