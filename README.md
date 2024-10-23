Cabin Reservation CLI
The Cabin Reservation CLI is a command-line application that allows users to manage reservations for predefined cabins. Users can view available cabins, create reservations, and manage bookings for specific dates. The system ensures that cabins cannot be double-booked and provides clear feedback for any conflicts in the reservation dates.

Predefined Cabins:
Raccoon Holler
Chipmunk Ridge
Flamingos Paradise


Features
View available cabins: Users can see a list of predefined cabins that are available for booking.
Create reservations: Users can create reservations for the predefined cabins, specifying the check-in and check-out dates.
Prevent double booking: The application ensures that cabins are not double-booked by checking for date conflicts.
View all reservations: Users can view all current reservations, along with the guest names, cabin names, and reservation dates.
Delete reservations: Users can delete a reservation if needed.

Requirements
Python 3.x
SQLite (built-in with Python, no separate installation required) 


Clone the repository:
git clone <repository-url>
cd cabin_reservation

Run the application: 
The application will automatically set up the database and seed it with the predefined cabins

Usage
Once you run the application, you will be presented with a menu of options. Simply type the number of the option you want to select.


Cabin Reservation System
1. List all Cabins
2. Add a Reservation
3. List all Reservations
4. Delete a Reservation
5. Exit

Enter your choice (1-5):

1. List all Cabins
Displays a list of predefined cabins. Example:


Available Cabins:
Cabin 1: Raccoon Holler
Cabin 2: Chipmunk Ridge
Cabin 3: Flamingos Paradise

2. Add a Reservation
Allows you to create a reservation by entering your name, selecting a cabin, and specifying check-in and check-out dates. The system will check for any booking conflicts and alert you if the dates are unavailable.

Available Cabins:
1. Raccoon Holler
2. Chipmunk Ridge
3. Flamingos Paradise
Choose a cabin by number: 1
Enter guest name: John Doe
Enter check-in date (YYYY-MM-DD): 2024-11-01
Enter check-out date (YYYY-MM-DD): 2024-11-05

Reservation for 'John Doe' created for Cabin 'Raccoon Holler' from 2024-11-01 to 2024-11-05.
3. List all Reservations
Displays all current reservations, including the guest name, cabin name, and reservation dates.

Reservations:
Reservation 1: Guest John Doe, Cabin 'Raccoon Holler', From 2024-11-01 to 2024-11-05

4. Delete a Reservation
Allows you to delete an existing reservation by entering its ID.

Example:


Reservations:
Reservation 1: Guest John Doe, Cabin 'Raccoon Holler', From 2024-11-01 to 2024-11-05

Enter the ID of the reservation to delete: 1
Reservation 1 deleted.
5. Exit
Exits the application.

we have also implemented an error handling tool that will catch any conflitcing dates that the user may try to reserve.

FUTURE IMPROVEMENTS:
1. allow users to login to view their specific reservations and cabins.
2. allow users to edit their existing reservations
3. allow bookings for multiple cabins at once for larger parties. 
