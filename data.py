# data sheet to keep score of guesses from the user

guesses = r"""
Attempts left 7
+--
|
|
|
|

Attempts left 6
+--,
|
|
|
|

Attempts left 5
+--,
|  o
|
|
|

Attempts left 4
+--,
|  o
|  |
|
|

Attempts left 3
+--,
|  o
| /|
|
|

Attempts left 2
+--,
|  o
| /|\
|
|

Attempts left 1
+--,
|  o
| /|\
| /
|

Attempts left 0
+--,
|  o
| /|\
| / \
|

""".strip().split("\n\n")
# Added split strip method so that the data is interpreted as each stage as intended 