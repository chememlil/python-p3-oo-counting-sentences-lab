#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        # Verify that the value is a string
        self.value = value if isinstance(value, str) else ''

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        # Check if the value ends with a period
        return self.value.endswith('.')

    def is_question(self):
        # Check if the value ends with a question mark
        return self.value.endswith('?')

    def is_exclamation(self):
        # Check if the value ends with an exclamation mark
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the value by sentence-ending punctuation, and count the number of non-empty sentences
        import re
        sentences = re.split(r'[.!?]+', self.value)
        return len([s for s in sentences if s.strip()])

# Example usage
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.is_sentence())    # Output: False
print(string.is_question())    # Output: True
print(string.is_exclamation()) # Output: False
print(string.count_sentences())# Output: 3

