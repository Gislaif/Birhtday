recipient_name = input("Enter the recipient's name: ")
year_of_birth = int(input("Enter the year of birth: "))
personalized_message = input("Enter a personalized message: ")
sender_name = input("Enter your name (sender's name): ")
current_year = 2023
recipient_age = current_year - year_of_birth
print("Personalized message for", recipient_name)
print("**************************")
print(personalized_message)
print("**************************")
print("From:", sender_name)
print(recipient_name, "is", recipient_age, "years old.")