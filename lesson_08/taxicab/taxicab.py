class TaxiCab:

    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer_reading = 0

    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord  

    def get_odometer(self):
        return self._odometer_reading
    
    def move_x(self, x_coord):
        self._x_coord += x_coord
        self._odometer_reading += abs(x_coord)
    
    def move_y(self, y_coord):
        self._x_coord += y_coord
        self._odometer_reading += abs(y_coord)


taxi_cab_one = TaxiCab(0,0)
taxi_cab_one.move_x(3)
taxi_cab_one.move_y(4)

print(taxi_cab_one.get_odometer())
print(taxi_cab_one.get_x_coord())
print(taxi_cab_one.get_y_coord())
