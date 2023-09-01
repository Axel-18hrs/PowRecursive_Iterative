def pow_iterative(x, y):
    result = 1
    for pow in range(y):
        result *= x
    print(result)

def pow_recursive(x, y):
    if y == 0:
        return 1
    return x * pow_recursive(x, y - 1)

choice = int(input("// Choose an option:" +
      "\n[1]: iterative pow" +
      "\n[2]: recursive pow\n"))

if choice == 1:
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    pow_iterative(x, y)

if choice == 2:
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    pow_recursive(x, y)