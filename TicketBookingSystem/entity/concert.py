from TicketBookingSystem.entity.event import Event

class Concert(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, ticket_price, artist, concert_type):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, ticket_price, "Concert")
        self.artist = artist
        self.concert_type = concert_type

    def display_event_details(self):
        super().display_event_details()
        print(f"Artist: {self.artist}")
        print(f"Concert Type: {self.concert_type}")