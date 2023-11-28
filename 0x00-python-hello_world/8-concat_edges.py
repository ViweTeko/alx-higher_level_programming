#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-orientated programming\
        language that combines remarkable power with very clear syntax"
str = str[39:69] + str[str.find("with"):str.find("with") + 5] + str[:6]
print(str)
