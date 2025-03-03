def word_to_num(number:str)->str:

    '''
    Converts a string of words representing a number into its digit equivalent.
    word_to_num("onefive") -> "15"

    Args:
    number: A string representing the number in words (e.g., "one", "two", "three").
    
    Return:
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

    for key in num_dict:
        number = number.replace(key,num_dict[key])

    return number


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

    num_in_words = ""
    for digit in number:
        num_in_words += word_dict[digit]
    return num_in_words

def gcd(num1:int,num2:int)->int:
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



