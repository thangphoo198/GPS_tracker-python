import sys

# Lấy danh sách các module đã được nạp
modules = sys.modules

# Hiển thị danh sách các module
for module_name in modules:
    print(module_name)
