from prettytable import PrettyTable
import random
import time

class PasswordGenerator:
    def __init__(self):
        self.characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&amp;*1234567890"
        self.x = PrettyTable()
        self.password_dict = {}

    def generate_passwords(self, no_of_passwords, password_length):
        count = 1
        while count <= no_of_passwords:
            password = ""
            for _ in range(password_length):
                password += random.choice(self.characters)
            self.password_dict[count] = password
            count += 1

    def display_passwords(self):
        self.x.field_names = ["Generated Passwords"]
        for key, value in self.password_dict.items():
            self.x.add_row([f"{key} | {value}"])
        print(self.x)

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            [file.write(f"{i}----{j}\n") for i, j in self.password_dict.items()]

def main():
    print("\n*** Password Generator App ***")
    
    password_generator = PasswordGenerator()

    while True:
        print("\n1: Generate passwords")
        print("2: Display generated passwords")
        print("3: Save passwords to file")
        print("4: Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            no_of_passwords = int(input("\nHow many passwords do you want to generate? "))
            password_length = int(input("\nEnter the length of each password: "))
            print("\nGenerating passwords...")
            password_generator.generate_passwords(no_of_passwords, password_length)
            print("\nPassword generation complete.")
        
        elif choice == "2":
            if password_generator.password_dict:
                password_generator.display_passwords()
            else:
                print("\nNo passwords generated yet.")
        
        elif choice == "3":
            if password_generator.password_dict:
                filename = "password.txt"
                password_generator.save_to_file(filename)
                print(f"\nGenerated passwords have been saved to {filename}")
            else:
                print("\nNo passwords generated to save.")
        
        elif choice == "4":
            print("\nExiting the Password Generator App.")
            break
        
        else:
            print("\nInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()