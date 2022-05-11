tabby_cat = "\vI'm tabbed in." #\t tabs the word (adding a space)
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat." #\\ is a backslash(\)
#a list where the content is tabbed (indented) with stars as unordered list (bullet points)
fat_cat = """
\vI'll do a list:
\t* \"Cat food\"
\t* fishies
\t* \vCatnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("Hello\vWorld")#ASCII vertical tab not working
