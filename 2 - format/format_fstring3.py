from datetime import datetime

now = datetime.now()
print(f"{now:%d/%m/%y (%H:%M)}")
print(f"{now:%c}")
print(f"{now:%I:%M %p}")

format_check = "%d/%m/%y (%H:%M)"
print(f"{now:{format_check}}")

# Resultado:
# 26/10/24 (10:32)
# Sat Oct  26 10:32:55 2024
# 07:36 PM
# 26/10/24 (10:34)
