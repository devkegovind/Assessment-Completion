"""
Question 2: Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if 
he can remove just one character at the index in the string, and the remaining characters will occur the same 
number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .
Note - You have to write at least 2 additional test cases in which your program will run successfully and provide 
an explanation for the same.
Example input 1 - s = “abc”. This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 }
Example output 1- YES
Example input 2 - s “abcc”. This string is not valid as we can remove only 1 occurrence of “c”. That leaves 
character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }
Example output 2 - YES
Example input 3 - s “abccc”. This string is not valid as we can remove only 1 occurrence of “c”. That leaves 
character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }
Example output 2 - NO
"""

def is_valid_string(string):
    # Count the frequency of each character
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    print(char_count)
    # Find the frequencies of the characters
    frequencies = list(char_count.values())

    # Check if all frequencies are the same
    if len(set(frequencies)) == 1:
        return "YES"

    # Check if removing one character makes all frequencies the same
    for index in range(len(string)):
        # Remove one character at index and count frequencies
        remaining_string = string[:index] + string[index+1:]
        remaining_char_count = {}
        for char in remaining_string:
            remaining_char_count[char] = remaining_char_count.get(char, 0) + 1
        remaining_frequencies = list(remaining_char_count.values())

        # Check if all remaining frequencies are the same
        if len(set(remaining_frequencies)) == 1:
            return "YES"

    return "NO"


# Example usage
input_string = input("Enter a string: ")
result = is_valid_string(input_string)
print(result)

"""
input1: “abc”
output:YES 
Explanation: {'a': 1, 'b': 1, 'c': 1}
All characters occur once times. We can delete one instance of  to have a valid string.


input2 :  “abcc”
Output: Yes
Explanation: Frequency counts for the letters are as follows:
{'a': 1, 'b': 1, 'c': 2}

input3 :  “abccc”
Output: NO
Explanation: Frequency counts for the letters are as follows:
{'a': 1, 'b': 1, 'c': 3}
"""