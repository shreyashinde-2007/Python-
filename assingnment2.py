#weight on earth and moon 

def weight(mass, gravity):
    return mass * gravity

mass = float(input("Enter mass : "))

earth = weight(mass, 9.8)
moon = weight(mass, 1.62)

print("weight on earth = ", earth,"N")
print("weight on moon = ", moon, "N")