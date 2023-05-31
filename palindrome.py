#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def is_palindrome(word):
    # Remove whitespace and convert to lowercase
    word = word.replace(' ', '').lower()
    # Reverse the word
    reversed_word = word[::-1]
    # Check if the word and its reverse are the same
    if word == reversed_word:
        return True
    else:
        return False

# Example usage
word = input("Enter a word: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")


# In[ ]:




