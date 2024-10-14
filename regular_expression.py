import re
# Example for Regular Expressions
# Go through this to understand more https://chatgpt.com/share/670d31fe-996c-8008-8bea-535b41a3edc0

## Match any one character in the string
pattern_1 = r'[abc]'  # Matches 'a', 'b', or 'c'

## Match anything in the range
pattern_2 = r'[a-z]'  # Matches any lowercase letter
pattern_3 = r'[0-9]'  # Matches any digit

## Negation
pattern_4 = r'[^abc]'  # Matches any character except 'a', 'b', or 'c'

## Grouping: Allows you to apply quantifiers to the entire group
pattern_5 = r'(abc)+'  # Matches 'abc', 'abcabc', etc.

## Capturing: Extracts matched substrings.
match = re.search(r'(\d{3})-(\d{2})-(\d{4})', '123-45-6789')
if match:
    print(match.group(0))  # Entire match
    print(match.group(1))  # First group: '123'
    print(match.group(2))  # Second group: '45'
    print(match.group(3))  # Third group: '6789'

## Named Groups: Assigns a name to a group for easier access.
pattern = r'(?P<area_code>\d{3})-(?P<number>\d{7})'
match = re.search(pattern, '123-4567890')
if match:
    print(match.group('area_code'))  # '123'
    print(match.group('number'))     # '4567890'

## Non-capturing Groups: Use (?:...) to group without capturing.
pattern = r'(?:abc)+'  # Groups 'abc' but does not capture




