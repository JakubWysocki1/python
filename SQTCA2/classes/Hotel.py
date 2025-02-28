class Hotel():

    # private class variables
    hotel_name = ""
    hotel_address = ""
    hotel_rooms_qty = 0
    hotel_num_rooms_booked = 0
    hotel_room_price = 0
    hospitality_vat_rate = 9 # Vat rate in Ireland currently 9% for hospitality sector
    hotel_star_rating = 0

    # No unit test is needed for the constructor!
    def __init__(self, hotel_name_in="", hotel_address_in="", hotel_rooms_qty_in=100, hotel_room_price_in=99):
        self.hotel_name = hotel_name_in
        self.hotel_address = hotel_address_in
        self.hotel_num_rooms_booked = 0
        
        if hotel_rooms_qty_in >= 0:
            self.hotel_rooms_qty = hotel_rooms_qty_in
        else:
            self.hotel_rooms_qty = 0

        if hotel_room_price_in >= 0:
            self.hotel_room_price = hotel_room_price_in
        else:
            self.hotel_room_price = 0            


    # Set the star rating, if a valid star rating
    def set_star_rating(self, star_rating):
        if star_rating in [1, 2, 3, 4, 5]:
            self.__star_rating = star_rating
            return "Star Rating of Hotel:" + str(self.__star_rating)
        else:
            return "Not valid Star Rating, must be 1, 2, 3, 4 or 5"

    # Return the total price of booking rooms	
    def book_rooms(self, num_rooms):
        # if it is a valid number of rooms that can be booked?
        if num_rooms > 0 and num_rooms <= self.hotel_rooms_qty:
            # If those rooms are actually available and not already booked
            if (self.hotel_rooms_qty - self.hotel_num_rooms_booked) >= num_rooms:
                total_price = self.hotel_room_price + (self.hotel_room_price*(self.hospitality_vat_rate/100))
                return "Rooms booked, and total cost is: " + str(total_price)
            else:
                "There are not " + str(num_rooms) + " free rooms, sorry!"
        else:
            return "Invalid number entered, try again."

    # Return the cost of insuring a hotel
    def cost_of_hotel_insurance(self, base_price, year_build, hotel_rooms_qty):
        surcharge = 0

        # get surcharge based on year
        if year_build < 1951:
            surcharge += 2000
        elif year_build < 1980:
            surcharge += 1000
        elif year_build < 1999:
            surcharge += 500
        elif year_build < 2010:
            surcharge += 300            
        else:
            surcharge += 50
       
        # get surcharge based on room numbers
        if hotel_rooms_qty < 25:
            surcharge += 300
        elif hotel_rooms_qty < 51:
            surcharge += 400
        if hotel_rooms_qty < 101:
            surcharge += 650
        else:
            surcharge += 900

        # finally return base_price plus surcharge
        return base_price + surcharge

if __name__ == '__main__':
    h1 = Hotel("Hotel Marion", "Ballsbridge", 200, 200)

    print("******               *******")
    print("****** Hotels System *******")

    num_rooms = int(input("Please enter number of rooms to book: "))
    print( h1.book_rooms(num_rooms) )

    star_rating = int(input("Thank you for staying, what would you recommend the star rating of the hotel was: "))
    print( h1.set_star_rating(star_rating) )

    print("******                        *******")  
    print("****** Hotels Insurance Costs *******")  
    base_price = int(input("What is the base price of the insurance: "))
    year_built = int(input("What year was the hotel built: ")) 
    print("The insurance cost will be: " + str( h1.cost_of_hotel_insurance(base_price, year_built, h1.hotel_rooms_qty) ))  
#h1.hotel_rooms_qty20