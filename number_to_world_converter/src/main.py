from constants import base_cases, tens_cases, above100


def num_to_word(num):
    """num_to_word converts a number to its word representation.
    this function is recursive and uses the base cases and above100 dictionaries to convert numbers to words.
    when the number is less than 20, it returns the corresponding word from the base_cases list.
    when the number is less than 100, it returns the corresponding word from the tens_cases
    list and the base_cases list for the remainder.
    when the number is greater than or equal to 100, it finds the largest key in the above100 dictionary that is less than or equal to the number,
    and returns the corresponding word from the above100 dictionary and the result of calling num_to_word on the quotient and remainder of the number divided by the pivot.

    :param num: the number to convert to words
    :type num: int
    :return: the word representation of the number
    :rtype: str
    """
    if num<20:
        return base_cases[num]
    elif num<100:
        remainder = num%10
        if remainder == 0:
            return tens_cases[num//10]
        return tens_cases[num//10] + ' ' + base_cases[remainder]
    
    pivot = max([key for key in above100 if key <= num])
    if num%pivot == 0:
        return f"{num_to_word(num//pivot)} {above100[pivot]}"
    return f"{num_to_word(num//pivot)} {above100[pivot]} {num_to_word(num%pivot)}"

if __name__ == "__main__":
    print(num_to_word(1200))
    print(num_to_word(234))
    print(num_to_word(1000000))
    print(num_to_word(1000000000))
    assert num_to_word(1200) == 'one thousand two hundred'
    assert num_to_word(234) == 'two hundred thirty four'
    assert num_to_word(1000000) == 'one million'
    assert num_to_word(1000000000) == 'one billion'
    