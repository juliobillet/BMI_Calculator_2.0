height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

##################################
#          COLOR PALETTE         #
##################################

class color:
   PURPLE = "\033[95m"
   CYAN = "\033[96m"
   DARKCYAN = "\033[36m"
   BLUE = "\033[94m"
   GREEN = "\033[92m"
   YELLOW = "\033[93m"
   RED = "\033[91m"
   STRONG_RED = "\033[31m"
   BOLD = "\033[1m"
   UNDERLINE = "\033[4m"
   END = "\033[0m"

##################################

bmi_result = int(weight / (height ** 2))

if bmi_result < 18.5:
  print(f"Your BMI is {bmi_result}, you are", color.YELLOW + color.BOLD + "underweight." + color.END)
elif bmi_result < 25:
  print(f"Your BMI is {bmi_result}, you are", color.GREEN + color.BOLD + "normal weight." + color.END)
elif bmi_result < 30:
  print(f"Your BMI is {bmi_result}, you are", color.YELLOW + color.BOLD + "slightly overweight." + color.END)
elif bmi_result < 35:
  print(f"Your BMI is {bmi_result}, you are", color.RED + color.BOLD + "obese." + color.END)
else:
  print(f"Your BMI is {bmi_result}, you are", color.STRONG_RED + color.BOLD + "clinically obese." + color.END)
