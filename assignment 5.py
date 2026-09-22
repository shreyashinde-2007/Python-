percentage= float(input("Enter percentage: "))

if percentage>90:
   print("Grade A")
elif percentage>80 and percentage<90:
   print("Grade B") 
elif percentage>70 and percentage<80:
   print("Grade C")
elif percentage>60 and percentage<70:
   print("Grade D")
elif percentage>50 and percentage<60:
   print("Grade E")   
else:
   print("Fail")    