# Anagram Checker
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) != len(str2):
    print("Not Anagrams")

else:
    count = 0

    for ch in str1:
        if str1.count(ch) == str2.count(ch):
            count = count + 1

    if count == len(str1):
        print("Anagrams")
    else:
        print("Not Anagrams")

#sorted can also be used to check for anagrams