nature_figure = int(input("1つの自然数を入れてね: "))

# print(nauture_figure)

if nature_figure % 15 == 0:
    print("fizzbuzz")
elif nature_figure % 3 == 0:
    print("fizz")
elif nature_figure % 5 == 0:
    print("buzz")
else:
    print(nature_figure)
