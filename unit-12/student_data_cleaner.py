name = "  nAomi omOtOsho  "
email = "  NAOMIOMOTOSHO@GMAIL.COM  "
phone = "  080-123-456-788  "

clean_name = name.strip().title()
clean_email = email.strip().lower()
clean_phone = phone.strip().replace("-", "")

print("STUDENT REGISTATION PROFILE")
print("----------------------------")
print("Name: " + clean_name)
print("Email: " + clean_email)
print("Phone: " + clean_phone)

print("\nVALIDATION")
print("Name length:", len(clean_name))
print("Email contains @:", "@" in clean_email)
print("Phone length:", len(clean_phone))
