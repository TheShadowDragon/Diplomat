import email_validator
from email_validator import validate_email

email = "abcdef.com"

try:
    val = validate_email(email).email
except:
    val = "ok"
