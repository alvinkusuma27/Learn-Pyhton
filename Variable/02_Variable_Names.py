# =====================================================
# PYTHON VARIABLES - RULES (BENAR vs SALAH)
# =====================================================

# 1. Harus mulai dengan huruf atau underscore (_)

name = "Alvin"      # ✅ BENAR
_age = 27           # ✅ BENAR

# 1name = "Alvin"   # ❌ SALAH (tidak boleh mulai angka)


# =====================================================
# 2. Tidak boleh mulai dengan angka
# =====================================================

age1 = 25           # ✅ BENAR
user2 = "Budi"      # ✅ BENAR

# 2age = 25         # ❌ SALAH


# =====================================================
# 3. Hanya boleh huruf, angka, dan underscore (_)
# =====================================================

user_name = "Alvin"     # ✅ BENAR
total_price2 = 150000   # ✅ BENAR

# user-name = "Alvin"   # ❌ SALAH (tidak boleh pakai -)
# user name = "Alvin"   # ❌ SALAH (tidak boleh pakai spasi)


# =====================================================
# 4. Case-sensitive (huruf besar kecil beda)
# =====================================================

age = 25
Age = 30
AGE = 40

# Semua ini berbeda variable

print("age:", age)   # 25
print("Age:", Age)   # 30
print("AGE:", AGE)   # 40


# =====================================================
# 5. Tidak boleh pakai keyword Python
# =====================================================

# print = 10        ❌ SALAH (menimpa fungsi print)
# class = "A"       ❌ SALAH (keyword Python)
# if = 5            ❌ SALAH (keyword Python)

# Solusi jika ingin tetap pakai kata tersebut:
class_ = "A"        # ✅ BENAR
if_value = 5        # ✅ BENAR


# =====================================================
# OUTPUT CONTOH
# =====================================================

print("name:", name)
print("class_:", class_)
print("if_value:", if_value)