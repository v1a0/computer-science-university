"""
Examples of generators
"""


nums_list = [1, 2, 3, 4, 5]
str_list = ['python', 'generators', 'examples']


def x10(nums: list):
    for num in nums:
        yield num * 10


ex_gen = x10(nums_list)

for ex in ex_gen:
    print(ex)

# ---------------------
print('='*40)
# ---------------------


def awesome(words: list):
    for word in words:
        yield f"Awesome {word}!"


ex_gen = awesome(str_list)

for ex in ex_gen:
    print(ex)


# ---------------------
print('='*40)
# ---------------------

ex_gen = awesome(str_list)

print(next(ex_gen))
print(ex_gen.__next__())
print(next(ex_gen))
# print(next(ex_gen_1))
# Traceback (most recent call last):
#   File "computer-science-university\python\basics\generators.py", line 44, in <module>
#     print(next(ex_gen_1))
# StopIteration


# ---------------------
print('='*40)
# ---------------------


def add_some(items: list):
    for item in items:
        addon = yield
        yield addon + item


ex_gen = add_some(str_list)
addon = ''

for ex in ex_gen:
    addon = ex_gen.send(addon)
    print(addon)