This is a simple Password Generator, it generates a password based on user's desired length of characters, However a password of less than 12 characters is not a strong password so the program suggests to choose at least 12 characters for the password. \
\
Libraries used;
1. **string**
```python
import string
Characters = string.ascii_letters + string.digits + string. punctuation
```
*String* is used to generate items for the characters list;

```python
string.ascii_letters #Generates A-Z letters both uppercase and lowercase.
string.digits #Generates digits 0-9.
string.punctuation #Generates special characters.
```
2. **random**
```python
import random
password += random.choice(characters)
```
*Random* is used with it's <u>choice</u> method  to pick a random item in the "characters" list and add it to our string "password".