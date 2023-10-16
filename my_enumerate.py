'''
Writing my own generator function that works like the built-in function "enumerate"
'''


def my_enumerate(iterable, start=0):
    n = start
    for element in iterable:
        yield n, element
        n += 1
    
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

# Test 1
for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
    
# Test 2
for i, lesson in my_enumerate(['a','b','c'], 6):
    print("Lesson {}: {}".format(i, lesson))

# Test 3    
for i, lesson in my_enumerate(['a','b','c']):
    print("Lesson {}: {}".format(i, lesson))  