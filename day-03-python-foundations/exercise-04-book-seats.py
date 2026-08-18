total_seats_booked = 0
def book_seats(n):
    global total_seats_booked
    total_seats_booked = n + total_seats_booked
    print(f"Booked {total_seats_booked} seat(s) Total booked so far: {total_seats_booked}")

def reset_bookings():
    global total_seats_booked
    total_seats_booked = 0

book_seats(3)
book_seats(5)
reset_bookings()
book_seats(2)