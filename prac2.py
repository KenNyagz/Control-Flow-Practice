weight = 41.50
# Ground shipping
flat_charge = 20.00
if weight <= 2.00:
 cost = weight * 1.50 + flat_charge
elif weight <= 6.00:
  cost = weight * 3.00 + flat_charge
elif weight <= 10:
  cost = weight * 4.00 + flat_charge
elif weight > 10:
  cost = weight * 4.75 + flat_charge
print (str(cost)+ " by ground shipping")

# Premium ground shipping
prem_ground_shipping = 125.00
print(str(prem_ground_shipping) +" by ground shipping premium")

# Drone shipping
if weight <= 2.00:
  cost = weight * 4.50
elif weight <= 6.00:
  cost = weight * 9.00
elif weight <= 10.00:
  cost = weight * 12.00
else:
 cost = weight * 14.25

print(str(cost) + " by drone shipping")


