# principle = int(input("Enter Principle Amount;"))
# rate = int(input("Enter Rate of Interest:"))
# time = int(input("Enter Time period (in years):"))

# simple_interest = (principle * rate * time) / 100
# total_amount = principle + simple_interest

# print(total_amount)


# total_cars = int(input("How many cars are there? : "))
# car_fare_per_hr = 20
# total_bikes = int(input("How many bikes are there? : "))
# bike_fare_per_hr = 10
# time = 6

# total_collection = (total_cars * car_fare_per_hr * time) + (total_bikes * bike_fare_per_hr * time)

# if (total_collection > 10000):
#     print("It is a Profitable day!")
# else:
#     print("It is not a good day :(")


# limit = int(input("Please enter the number till you want to add odd numbers: "))

# sum = 0

# for i in range(0, limit, 1):
#     if(i % 2 != 0):
#         sum += i

# print(sum)


# Lists
# names = ["prajjwal", "Subra", "Nikhil", "Rohan"]
# feedbacks = [3, 4, 4, 5]

# for i in range(0, 4, 1):
#     if (feedbacks[i] < 4):
#         print(names[i])


# We are going to take the 5 input from the users where they will provide the name of the learnr and the feedback
# At the end we will print the average of the feedback
# names = []
# feedbacks = []
# sum = 0


# def name():
#     val = input("Please enter your name: ")
#     names.append(val)


# def feedback():
#     val = int(input("Please provide your feedback: "))
#     feedbacks.append(val)


# for i in range(0, 5, 1):
#     name()
#     feedback()
#     sum += feedbacks[i]

# print(sum/len(feedbacks))

learners = []
sumOfFeedback = 0

for i in range(5):
    name = input("Please enter your name: ")
    feedback = int(input("Please provide your feedback: "))

    sumOfFeedback += feedback

    learners.append({
        "name": name,
        "feedback": feedback
    })

print(sumOfFeedback / len(learners))
