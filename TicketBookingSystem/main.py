from app.TicketBookingSystem import TicketBookingSystem
from util.dbutil import DBUtil

db_conn = DBUtil.getDBConn()
ticket_booking_system = TicketBookingSystem(db_conn)
ticket_booking_system.run()





