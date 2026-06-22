# =====================================================
# PYTHON GLOBAL vs LOCAL VARIABLES (CATATAN)
# =====================================================


# =========================
# 1. Global Variable (akses di dalam function)
# =========================

x = "awesome"

def myfunc():
    # bisa diakses dari dalam function
    print("Python is " + x)

myfunc()

# =====================================================
# 2. Local vs Global Variable
# =====================================================

x = "awesome"  # global variable

def myfunc1():
    x = "fantastic"  # local variable (hanya di dalam function)
    print("Inside function:", x)

myfunc1()

print("Outside function:", x)

# =====================================================
# 3. Menggunakan keyword global
# =====================================================

x = "awesome"

def myfunc2():
    global x
    x = "fantastic"

myfunc2()

print("Python is " + x)