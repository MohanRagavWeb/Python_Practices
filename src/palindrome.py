#12. Check if a string is a palindrome without built-in functions.
def check_palindrome(string):
    rev = ""
    string=string.lower()
    for i in string:
        rev = i + rev
    if rev==string:
        print("Palindrome")
    else:
        print("Not a Palindrome")


string=input("Enter a String: ")


check_palindrome(string)

