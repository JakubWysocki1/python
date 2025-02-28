import unittest
from classes.Hotel import Hotel

class test_Hotel(unittest.TestCase):
    test_Hotel = Hotel()
    hotel_room_price = 200
    hotel_rooms_qty = 200
    hospitality_vat_rate = 9

    
    def setUp(self):
        self.test_Hotel = Hotel("Hotel Marion", "Ballsbridge", 200, 200)

    def tearDown(self):
        del self.test_Hotel

    def test_set_star_rating_ValidParams_returnStarRating(self):
        param = 1
        
        expected_result = "Star Rating of Hotel:" + str(param)

        actual_result = self.test_Hotel.set_star_rating(param)

        self.assertEqual(expected_result, actual_result)

    def test_set_star_rating_NotValidParams_returnError(self):
        param = 6

        expected_result = "Not valid Star Rating, must be 1, 2, 3, 4 or 5"

        actual_result = self.test_Hotel.set_star_rating(param)

        self.assertEqual(expected_result, actual_result)

    def test_book_rooms_validParam_returnPrice(self):
        valid_num_rooms = 2 
       
        price = self.hotel_room_price + (self.hotel_room_price*(self.hospitality_vat_rate/100))

        expected_result = "Rooms booked, and total cost is: " + str(price)

        actual_result = self.test_Hotel.book_rooms(valid_num_rooms)

        self.assertEqual(expected_result, actual_result)

    def test_book_rooms_invalidParam_returnError(self):
        invalid_num_rooms = 300

        expected_result = "Invalid number entered, try again."

        actual_result = self.test_Hotel.book_rooms(invalid_num_rooms)

        self.assertEqual(expected_result, actual_result)

    def test_book_rooms_validParam_noRooms_returnError(self):
        num_rooms = 155
        self.test_Hotel.book_rooms(num_rooms)

        num_rooms1= 60
        expected_result = "There are not " + str(num_rooms) + " free rooms, sorry!"

        actual_result = self.test_Hotel.book_rooms(num_rooms)
        
        self.assertEqual(expected_result, actual_result)


    def test_cost_of_hote_insurance(self):
        param_list = [
            (5000,1998,500,6400)
        
        ]

        for base_price, yr, num_room, outocme in param_list:
            with self.test