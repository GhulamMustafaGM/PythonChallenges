
("Welcome to the MPH to MPS Conversion App")

#Gather user input
mph = float(input("\nWhat is your speed in miles per hour: "))

#Convert to mps
mps = mph*0.4474
mps = round(mps, 2)

print("Your speed in meters per second is " + str(mps) + ".")


# output 

# What is your speed in miles per hour: 60
# Your speed in meters per second is 26.84.