print("WELCOME TO THE TIP CALCULATOR")
bill= float(input("what was the total bill? Rs."))
percent= int(input("what percentage of tip you would like to give? 10, 12, or 15? "))
split= int(input("how many people to split the bill? "))
tip = percent/100
tipvalue= bill * tip
total= bill + tipvalue
each= total/split
print(f"each person should pay = {each:.2f}")
