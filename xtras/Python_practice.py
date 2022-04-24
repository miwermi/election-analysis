#print("Hello World")

# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# if counties[3] != 'Jefferson':
#   print(counties[2])

# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#    print("Turn on the AC.")
# else:
#    print("Open the windows.")

#How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
#Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
#Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("You received " + str(percentage_votes)+"% of the total votes.")

#What is the score?
# score = int(input("What is your test score? "))

#Determine the grade.
# if score >= 90:
#    print('Your grade is an A.')
# else:
#   if score >= 80:
#        print('Your grade is a B.')
#    else:
#        if score >= 70:
#           print('Your grade is a C.')
#        else:
#            if score >= 60:
#                print('Your grade is a D.')
#            else:
#                print('Your grade is an F.')


counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# if "Arapahoe" in counties and "El Paso" not in counties:
#     print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# for county in counties:
#    print(county)

# numbers = [0, 1, 2, 3, 4]
# for num in numbers:
#     print(num)

for num in range(5):
    print(num)

# for i in range(len(counties)):
#    print(counties[i]) 

# counties_tuples = ("Arapahoe","Denver","Jefferson")

# for i in range(len(counties_tuples)):
#      print(counties_tuples[i])

# for county in counties_tuples:
#      print(county)


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)

for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print(county and "has" and voters and "registered voters")