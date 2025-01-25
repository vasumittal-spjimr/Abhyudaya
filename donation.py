import os
import json

# File to store user and donation data
data_file = "ngo_donations.json"

def load_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return {"users": {}, "donations": []}

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

def register_user(data):
    print("\n--- Register ---")
    email = input("Enter your email: ")
    if email in data["users"]:
        print("User already exists. Try logging in.")
        return
    name = input("Enter your name: ")
    password = input("Set your password: ")
    data["users"][email] = {"name": name, "password": password}
    save_data(data)
    print("Registration successful! You can now log in.")

def login_user(data):
    print("\n--- Login ---")
    email = input("Enter your email: ")
    if email not in data["users"]:
        print("No account found. Please register first.")
        return None
    password = input("Enter your password: ")
    if data["users"][email]["password"] != password:
        print("Incorrect password. Try again.")
        return None
    print(f"Welcome back, {data['users'][email]['name']}!")
    return email

def make_donation(data, email):
    print("\n--- Make a Donation ---")
    amount = float(input("Enter the donation amount: "))
    message = input("Enter a message for the NGO (optional): ")
    donation = {"email": email, "amount": amount, "message": message}
    data["donations"].append(donation)
    save_data(data)
    print("Thank you for your generous donation!")

def view_donations(data):
    print("\n--- Donations Summary (Admin) ---")
    total_amount = 0
    for donation in data["donations"]:
        print(f"Donor: {donation['email']}, Amount: {donation['amount']}, Message: {donation['message']}")
        total_amount += donation["amount"]
    print(f"\nTotal Donations: {total_amount}")

def main():
    data = load_data()

    while True:
        print("\n--- NGO Donation Portal ---")
        print("1. Register")
        print("2. Login")
        print("3. View Donations (Admin)")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            register_user(data)
        elif choice == "2":
            email = login_user(data)
            if email:
                make_donation(data, email)
        elif choice == "3":
            password = input("Enter admin password: ")
            if password == "admin123":
                view_donations(data)
            else:
                print("Incorrect admin password.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
