# =====================================================
# PYTHON VARIABLES - MULTIPLE ASSIGNMENT & UNPACKING
# =====================================================

# =========================
# 1. Many Values to Multiple Variables
# =========================

x, y, z = "Orange", "Banana", "Cherry"

print("Many values to multiple variables:")
print(x)
print(y)
print(z)


# =========================
# 2. One Value to Multiple Variables
# =========================

x = y = z = "Orange"

print("One value to multiple variables:")
print(x)
print(y)
print(z)


# =========================
# 3. Unpacking a Collection (List)
# =========================

fruits = ["apple", "banana", "cherry"]

x, y, z = fruits

print("Unpacking a list:")
print(x)
print(y)
print(z)
