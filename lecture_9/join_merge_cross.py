# Множини: Створіть програму, яка зчитує два списки від користувача
# та повертає їх перетин, об'єднання та різницю у вигляді множин.

set1 = {"a", "b", "c", "d"}
set2 = {"c", "d", "e"}

print(f"union {set1.union(set2)}")

print(f"difference {set2.difference(set1).union(set1.difference(set2))}")

print(f"intersection {set2.intersection(set1)}")