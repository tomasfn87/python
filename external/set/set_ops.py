
a = {1,2,3,4,5}
print(f"Starting a = {a}")
b = {3,5,6,7,8,9,10}
print(f"Starting b = {b}")

# Union, preserves a and b and returns the result
# print(f"a.union(b) = {a.union(b)}")
print(f"\na | b or a.union(b) = {a | b}") # interchangeable

# Union, a receives the operation's result
print("\nrunning a |= b or a.update(b)")
# a |= b # interchangeable
a.update(b)
print(f"and printing a = {a}")

print("\nrestarting a and b...")
a = {1,2,3,4,5}
b = {3,5,6,7,8,9,10}

print(f"\na - b or a.difference(b) = {a - b}")
# print(f"\na - b or a.difference(b) = {a.difference(b)}")
print(f"b - a or b.difference(a) = {b - a}")
a -= b
print(f"\nrunning a -= b or a.difference_update(b) and printing a = {a}")

print("\nrestarting a and b...")
a = {1,2,3,4,5}
b = {3,5,6,7,8,9,10}

print(f"\na ^ b or a.symmetric_difference(b) = {a ^ b}")
# print(f"\na ^ b or a.symmetric_difference(b) = {a.symmetric_difference(b)}")
# a ^= b
a.symmetric_difference_update(b)
print(f"running a ^= b or a.symmetric_difference_update(b) and printing a = {a}")

print("\nrestarting a and b, starting c...")
a = {1,2,3,4,5}
b = {3,5,6,7,8,9,10}
c = {3,5}
print(f"c = {c}")
print(f"\nc <= a or c.issubset(a) = {c <= a}")
# print(f"\nc <= a or c.issubset(a) = {c.issubset(a)}")
print(f"b >= c or b.issuperset(c) = {b >= c}")
# print(f"b >= c or b.issuperset(c) = {b.issuperset(c)}")


print(f"\na > c (same as a >= c and a != c) = {a > c}")
print(f"c < b (same as c <= b and c != b) = {c < b}")

