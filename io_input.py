
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    print("hello3")
    return text == reverse(text)

something = raw_input("Enter text: ")
print("hello1")
if is_palindrome(something):
    print(something, 'is a palindrome')
    print("hello2")
else:
    print(something, 'is not a palindrome')
