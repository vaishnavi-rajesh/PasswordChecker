def StrengthCheck(password):
    has_upper=False
    has_lower=False
    has_symbol=False
    has_number=False

    for ch in password:
        if ch.isupper():
            has_upper=True
        elif ch.islower():
            has_lower=True
        elif ch.isdigit():
            has_number=True
        else:
            has_symbol=True

    length=len(password)
    if length<8:
        return "Weak password!"
    elif length>=8 and has_upper and has_lower and has_symbol and has_number:
        return "Strong password!"
    elif length>=8 and (has_lower or has_upper) and (has_number or has_symbol):
        return "Moderate strength"
    else:
        return "Weak password!"
    

password=input("Enter your password")
print(StrengthCheck(password))

    