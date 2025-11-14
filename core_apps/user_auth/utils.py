import random
import string
# Generate OTP with 6 digits
def generate_OTP(lenght=6)->str:
    return "".join(random.choices(string.digits,k=lenght))
