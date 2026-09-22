while True:
  password=input("Enter password (or 'stop' to exit):")
  if password.lower == "stop":
     break
  upper=False
  lower=False
  digit=False

  for ch in password:
       if ch.isupper():
          upper=True
       elif ch.islower():
          lower=True
       elif ch.isdigit():
          digit=True

  if len(password)>=10 and upper and lower and digit:
     print("Strong password")
  else:
     print("Weak password")