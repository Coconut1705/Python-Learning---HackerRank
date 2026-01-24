print(9 + 6)
print("=======================================Arithmetic Operators=========================================")

a = 15 + 20
b = a + 80
c = b + a

print(a)
print(b)
print(c)

print("=======================================Comparison Operators=========================================")

x = 8
y = 12

print(x * y)
print(x >= y)
print(1 < x < 13)
print(2 < x and x > 7)
print(not(x > y))

print("=======================================Identity Operators=========================================")

n = ["Dell", "HP", "Asus"]
m = ["Acer", "MSI"]
z = m

print(m is n)
print(m is z)
print(m == n)
print(m == z)

print("=======================================Membership Operators=========================================")

cars = ["Ford", "Volvo", "BMW"]
if "Volvo" in cars:
    print("Có Volvo trong danh sách")
else:
    print("Không có Volvo trong danh sách")

if "Audi" not in cars:
    print("Không có Audi trong danh sách")
else:
    print("Có Audi trong danh sách")
    