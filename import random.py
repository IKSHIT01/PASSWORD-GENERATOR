import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the character set: letters (uppercase and lowercase), digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Main program
while True:
    try:
        # Ask the user for the desired password length
        length = int(input("Enter the desired password length: "))
        
        # Ensure the length is a positive number greater than 0
        if length <= 0:
            print("Please enter a valid length greater than 0.")
            continue
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated password: {password}")
        
        # Ask the user if they want to generate another password
        another = input("\nDo you want to generate another password? (yes/no): ").lower()
        if another != 'yes':
            print("Exiting the Password Generator. Stay secure!")
            break
    except ValueError:
        print("Please enter a valid number.")
