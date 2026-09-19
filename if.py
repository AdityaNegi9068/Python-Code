import random

is_client = random.choice([True, False])
status = "Active" if is_client else "Inactive"
print(status)