import random
import string

# Function to generate a random password
def generate_password(length):
    # Define group of characters to choose from for generating password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password by selecting random characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main function to handle user input and generate a password
def main():
    print("_______________Welcome to the Password Generator!________________") 

    try:
        # Ask the user how many passwords they want to generate
        num_passwords = int(input("How many passwords would you like to generate? "))
        # Ask the user for the length of each password
        password_length = int(input("Enter the length for each password to be generated : "))
    except ValueError:
        # Handling invalid input
        print("Please enter valid numbers.")
        return

    # Generate the specified number of passwords with the specified length of users choice
    for i in range(num_passwords):
        # Generate and print each passwords
        password = generate_password(password_length)
        print(f"Password {i+1}: {password}")

# Call the main function to start the program
main()
