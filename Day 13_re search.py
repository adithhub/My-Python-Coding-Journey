import re

my_text = "This text is for checking import re."
a = re.search("^This.*import.", my_text)

if a:
    print("YESSSSSS")
else:
    print("NAHHHHHHHHH.")
