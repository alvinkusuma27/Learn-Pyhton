# =====================================================
# PYTHON OUTPUT VARIABLES
# =====================================================

# =========================
# 1. Output single variable
# =========================

x = "Python is awesome"
print(x)


# =========================
# 2. Output multiple variables (pakai koma)
# =========================

x = "Python"
y = "is"
z = "awesome"

print(x, y, z)


# =========================
# 3. Output pakai + operator (string)
# =========================

x = "Python "
y = "is "
z = "awesome"

print(x + y + z)


# =========================
# 4. + operator untuk angka (matematika)
# =========================

x = 5
y = 10

print(x + y)


# =========================
# 5. ERROR case (string + number)
# =========================

x = 5
y = "John"

# print(x + y)  # ❌ ERROR: tidak bisa gabung int + str


# =========================
# 6. Cara paling aman (recommended)
# =========================

print(x, y)  # ✅ bisa campur tipe data