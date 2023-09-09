"""The program that you create for this exercise will begin by reading the cost of a meal ordered
 at a restaurant from the user. Then your program will compute the tax and tip for the meal.
 Use your local tax rate when computing the amount of tax owing. Compute the tip as 10 percent
 of the meal amount (without the tax). The output from your program should include the tax amount,
the tip amount, and the grand total for the meal including both the tax and the tip.
 Format the output so that all, of the values are displayed using two decimal places.

 Local Tax = 5%

For example:

Thank you for dining at Malai Cha Restaurant

Enter the cost of your meal: 45
The cost of your meal is: $45.00
Local Tax = 5%
Tip = 18%

[Total Amount due is: 45.00 + (0.18 *45.00) + ( 0.05* 45) =45.00 + 8.10 + 2.25 = 55.35]

Total Amount due is : $55.35 """

#A greetings
print("Thank you for dining at 'Malai Cha Restaurant'")

#cost rate from user
meal_cost = float(input("What is your meal rate? "))
print(f"The cost of your meal rate is ${meal_cost:.2f}")

#calculating tax and tip and total cost
tax = meal_cost*(5/100)
print(f"Your total tax is:${tax:.2f}")

tip = meal_cost*(10/100)
print(f"Your total tip is: ${tip:.2f}")

#printing total cost for meal tax and tip
total_cost = meal_cost+tax+tip
print(f"You have to pay ${total_cost:.2f}")