print("🎬 Welcome to Movie Ticket Booking System 🎬")

seats = 20
price = 150

while True:
    print("\n--------------------------------")
    print("Available Seats:", seats)
    print("Ticket Price: ₹", price)
    print("--------------------------------")

    book = int(input("Enter number of tickets to book (0 to Exit): "))

    if book == 0:
        print("Thank you for visiting! 🍿")
        break

    if book <= seats:
        total = book * price
        seats -= book

        print("\n✅ Booking Successful!")
        print("Tickets Booked:", book)
        print("Total Amount: ₹", total)
        print("Remaining Seats:", seats)

    else:
        print("\n❌ Sorry! Not enough seats available.")

print("\n🎥 Enjoy Your Movie! 🎥")