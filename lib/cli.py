from models import Cabin, Reservation
from databases import create_tables, seed_cabins
from datetime import datetime

def display_menu():
    print("\nCabin Reservation System")
    print("1. List all Cabins")
    print("2. Add a Reservation")
    print("3. List all Reservations")
    print("4. Delete a Reservation")
    print("5. Exit")

def get_user_choice():
    choice = input("\nEnter your choice (1-5): ")
    return choice

def list_cabins():
    cabins = Cabin.get_all()
    if cabins:
        print("\nAvailable Cabins:")
        for cabin in cabins:
            print(f"Cabin {cabin[0]}: {cabin[1]}")
    else:
        print("No cabins available.")

def add_reservation():
    guest_name = input("Enter guest name: ")

    
    cabins = Cabin.get_all()
    print("\nAvailable Cabins:")
    for i, cabin in enumerate(cabins, 1):
        print(f"{i}. {cabin[1]}")

    cabin_choice = int(input("Choose a cabin by number: "))
    
    if 1 <= cabin_choice <= len(cabins):
        cabin_id = cabins[cabin_choice - 1][0]
    else:
        print("Invalid cabin choice.")
        return

    
    check_in = input("Enter check-in date (YYYY-MM-DD): ")
    check_out = input("Enter check-out date (YYYY-MM-DD): ")

    
    try:
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d").date()
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d").date()

        
        if check_in_date >= check_out_date:
            print("Error: Check-out date must be after check-in date.")
            return
    except ValueError:
        print("Error: Invalid date format. Please enter the date as YYYY-MM-DD.")
        return

    
    existing_reservations = Reservation.get_by_cabin_id(cabin_id)
    for reservation in existing_reservations:
        existing_check_in = datetime.strptime(reservation[3], "%Y-%m-%d").date()
        existing_check_out = datetime.strptime(reservation[4], "%Y-%m-%d").date()

        
        if (check_in_date < existing_check_out) and (check_out_date > existing_check_in):
            print(f"Error: Cabin is already booked from {existing_check_in} to {existing_check_out}.")
            return

   
    reservation = Reservation(guest_name=guest_name, cabin_id=cabin_id, check_in=check_in, check_out=check_out)
    reservation.create()
    print(f"\nReservation for '{guest_name}' created for {cabins[cabin_choice - 1][1]} from {check_in} to {check_out}.")


def list_reservations():
    reservations = Reservation.get_all()
    if reservations:
        print("\nReservations:")
        for reservation in reservations:
            print(f"Reservation {reservation[0]}: Guest: {reservation[1]}, Cabin: {reservation[2]}, From: {reservation[3]} to {reservation[4]}")
    else:
        print("No reservations available.")

def delete_reservation():
    list_reservations()
    reservation_id = input("\nEnter the ID of the reservation to delete: ")
    Reservation.delete(reservation_id)
    print(f"Reservation {reservation_id} deleted.")

def main():
    create_tables()  
    seed_cabins()    

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            list_cabins()
        elif choice == '2':
            add_reservation()
        elif choice == '3':
            list_reservations()
        elif choice == '4':
            delete_reservation()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-5).")

if __name__ == '__main__':
    main()
