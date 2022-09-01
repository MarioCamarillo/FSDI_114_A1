def anagram(string_1, string_2):
    # https://www.w3schools.com/python/ref_func_input.asp
    # The next two lines are not necesary. The input function converts the arguments into strings.
    anagram_string_1 = str(string_1)
    anagram_string_2 = str(string_2)

    # https://www.geeksforgeeks.org/find-length-of-a-string-in-python-4-ways/

    # This is to use an index to check where are we within the string.
    # Also is used with the .format(a,b) that python suggests.
    # Converting to lower case both strings to compare each character equally
    input_string_1 = string_1.lower()
    input_string_2 = string_2.lower()

    # This is to use an index to check where are we within the string.
    anagram_string_1_length = (len(input_string_1))
    anagram_string_2_length = (len(input_string_2))

    # https://www.w3schools.com/python/python_conditions.asp
    if ((anagram_string_1_length or anagram_string_2_length) > 27):
        print("There is no anagram with more than 27 letters, you wrote a word with more")
    else:
        if (len(input_string_1)) != (len(input_string_2)):
            print("These are not anagrams. Their length is not the same.")
            # https://python-course.eu/python-tutorial/formatted-output.php
            # https://www.w3schools.com/python/ref_string_format.asp
            print("The first word has {a:2d} and the second word has {b:2d}  characters".format(
                a=anagram_string_1_length, b=anagram_string_2_length))
            # https://stackoverflow.com/questions/73663/how-do-i-terminate-a-script
            # will not use quit() as it will make unreacheble the next line of code
        else:
            # https://www.w3schools.com/python/python_howto_reverse_string.asp
            # https://python.land/introduction-to-python/strings
            input_string_2_reversed = input_string_2[::-1]
            index_string = 0
            for index_string in range(0, anagram_string_1_length):
                if (input_string_1[index_string] == (input_string_2_reversed[index_string])):
                    if (anagram_string_1_length-1 == index_string):
                        print("Great, this is an anagram")
                        break
                else:
                    print("Sorry, this is not an anagram")
                    break
