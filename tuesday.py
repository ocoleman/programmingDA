import datetime

today = datetime.datetime.today()
dayofweek = today.weekday()

print("Lets check if it's Tuesday.")

if dayofweek == 1:
    print("It's Tuesday!")
elif dayofweek == 0:
    print("It's not Tuesday.")
    print("Luckily it will be Tuesday tomorrow!")
else:
    print("Unfortunatley, it's not Tuesday.")