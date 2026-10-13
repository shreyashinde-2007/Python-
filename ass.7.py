def calculate_calories(carbs,fats,proteins):
    total_calories = (carbs*4) + (fats*9) + (proteins*4)
    return total_calories

# Input grams of nutrients consumed in a day
carbs = float(input("Enter grams of carbohydrates: "))
fats = float(input("Enter grams of fats: "))
proteins = float(input("Enter grams of proteins: "))

#Calculate and display total calories
total = calculate_calories(carbs, fats, proteins)

print("Total daily calaric intake:", total, "calories")
    
