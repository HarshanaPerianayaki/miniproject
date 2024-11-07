class Ticket:
    def __init__(self, ticket_id, event_name, available_seats, price):
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.available_seats = available_seats
        self.price = price

    def book_ticket(self, seats_to_book):
        if seats_to_book <= self.available_seats:
            self.available_seats -= seats_to_book
            print(f"Successfully booked {seats_to_book} seats for '{self.event_name}'!")
            return seats_to_book
        else:
            print(f"Sorry! Only {self.available_seats} seats are available for '{self.event_name}'.")
            return 0

    def __str__(self):
        return f"{self.event_name} (ID: {self.ticket_id}) - Available Seats: {self.available_seats}, Price per seat: ${self.price}"


class Booking:
    def __init__(self, user, ticket, seats_booked):
        self.user = user
        self.ticket = ticket
        self.seats_booked = seats_booked

    def __str__(self):
        return f"{self.user} booked {self.seats_booked} seats for '{self.ticket.event_name}'."


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.bookings = []

    def book_ticket(self, ticket, seats_to_book):
        booked_seats = ticket.book_ticket(seats_to_book)
        if booked_seats > 0:
            new_booking = Booking(self.name, ticket, booked_seats)
            self.bookings.append(new_booking)
            print(f"Booking confirmed! {self.name} has booked {booked_seats} seats.")
        else:
            print("Booking failed.")

    def view_bookings(self):
        if not self.bookings:
            print(f"{self.name} has no bookings.")
        else:
            print(f"Bookings for {self.name}:")
            for booking in self.bookings:
                print(booking)


class TicketBookingSystem:
    def __init__(self):
        self.tickets = []
        self.users = {}

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def register_user(self, name, email):
        if email in self.users:
            print(f"User with email {email} already registered.")
        else:
            new_user = User(name, email)
            self.users[email] = new_user
            print(f"User {name} registered successfully!")

    def display_available_tickets(self):
        if not self.tickets:
            print("No tickets available.")
        else:
            print("Available tickets:")
            for ticket in self.tickets:
                print(ticket)

    def get_user(self, email):
        return self.users.get(email)


# Demo of the ticket booking system
def main():
    # Create the system
    system = TicketBookingSystem()

    # Add tickets
    system.add_ticket(Ticket(101, "Concert A", 100, 50))
    system.add_ticket(Ticket(102, "Concert B", 150, 40))

    # Register users
    system.register_user("Alice", "alice@example.com")
    system.register_user("Bob", "bob@example.com")

    # Display available tickets
    system.display_available_tickets()

    # Book tickets for users
    user = system.get_user("alice@example.com")
    if user:
        user.book_ticket(system.tickets[0], 2)  # Alice books 2 seats for "Concert A"

    user = system.get_user("bob@example.com")
    if user:
        user.book_ticket(system.tickets[1], 3)  # Bob books 3 seats for "Concert B"

    # View user bookings
    user = system.get_user("alice@example.com")
    if user:
        user.view_bookings()

    user = system.get_user("bob@example.com")
    if user:
        user.view_bookings()

if __name__ == "__main__":
    main()
