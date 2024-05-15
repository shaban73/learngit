def are_anagrams(str_1, str_2):
    if len(str_1) != len(str_2):
        return False
    else:
        return sorted(str_1) == sorted(str_2)

# Example usage:
str1 = input("Enter the 1st string: ")
str2 = input("Enter the 2nd string: ")

result = are_anagrams(str1, str2)

if result:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
