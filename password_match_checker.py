password = input("Enter your password: ")
confirm_password = input("Confirm your password: ")
if password == confirm_password:
    print("Password match successful.")
else:
    print("Passwords do not match. Please try again.")