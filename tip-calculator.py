bill = int(input("How much is your bill?"))
service_ans = input("NB:Can either be good,great or terrible. How was your service? ")
service = service_ans.lower()

print(service)

if service == "good":
    tip = bill*0.15
elif service == "great":
    tip = bill*0.2
else:
    tip = 0

full_amount = bill+tip

print("Your bill is "+str(full_amount)+". Thank you for purchasing.")
