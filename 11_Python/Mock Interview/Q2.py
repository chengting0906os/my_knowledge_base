# Mock Interview — Q2
#
# 下面這段程式碼的輸出是什麼？為什麼？

def append_to(element, to=[]):
    to.append(element)
    return to

print(append_to(1))
print(append_to(2))
print(append_to(3))
