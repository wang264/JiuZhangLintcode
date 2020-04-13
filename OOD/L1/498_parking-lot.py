# 498. 停车场
# 中文English
# 设计一个停车场
#
# 1.一共有n层，每层m列，每列k个位置
# 2.停车场可以停摩托车，公交车，汽车
# 3.停车位分别有摩托车位，汽车位，大型停车位
# 4.每一列，摩托车位编号范围为[0,k/4)(注：包括0，不包括k/4),汽车停车位编号范围为[k/4,k/4*3)(注：不包括k/4*3),大型停车位编号范围为[k/4*3,k)(注：不包括k)
# 5.一辆摩托车可以停在任何停车位
# 6.一辆汽车可以停在一个汽车位或者大型停车位
# 7.一辆公交车可以停在一列里的连续5个大型停车位。
#
# 样例
# Example 1
#
# Input:
# level=1
# num_rows=1
# spots_per_row=11
# parkVehicle("Motorcycle_1")
# parkVehicle("Car_1")
# parkVehicle("Car_2")
# parkVehicle("Car_3")
# parkVehicle("Car_4")
# parkVehicle("Car_5")
# parkVehicle("Bus_1")
# unParkVehicle("Car_5")
# parkVehicle("Bus_1")
#
# Output:
# true
# true
# true
# true
# true
# true
# false
# true
#
# Explanation:
# Parking Lot：
# Motorcycle: 0 1
# Car:        2 3 4 5
# Bus:        6 7 8 9 10
# When "Car_5" first got to the parking lot, there is no place for it in compact spots.
# The "Car_5" has to park in Bus spot 6. So "Bus_1" cannot park until "Car_5" left.
# Example 2
#
# Input:
# level=1
# num_rows=1
# spots_per_row=14
# parkVehicle("Motorcycle_1")
# parkVehicle("Motorcycle_2")
# parkVehicle("Motorcycle_3")
# parkVehicle("Car_1")
# parkVehicle("Car_2")
# parkVehicle("Car_3")
# parkVehicle("Motorcycle_4")
# parkVehicle("Car_4")
# parkVehicle("Car_5")
# parkVehicle("Car_6")
# parkVehicle("Car_7")
# parkVehicle("Bus_1")
# unParkVehicle("Car_1")
# unParkVehicle("Motorcycle_4")
# unParkVehicle("Car_3")
# unParkVehicle("Car_6")
# parkVehicle("Bus_1")
# unParkVehicle("Car_7")
# parkVehicle("Bus_1")
#
# Output:
# true
# true
# true
# true
# true
# true
# true
# true
# true
# true
# true
# false
# false
# true

# 本参考程序来自九章算法，由 @ 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


# enum type for Vehicle
class VehicleSize:
    Motorcycle = 1
    Compact = 2
    Large = 3
    Other = 99


class Vehicle:
    # Write your code here
    def __init__(self):
        self.parking_spots = []
        self.spots_needed = 0
        self.size = None
        self.license_plate = None

    def get_spots_needed(self):
        return self.spots_needed

    def get_size(self):
        return self.size

    def park_in_spot(self, spot):
        self.parking_spots.append(spot)

    def clear_spots(self):
        for spot in self.parking_spots:
            spot.remove_vehicle()

        self.parking_spots = []

    def can_fit_in_spot(self, spot):
        raise NotImplementedError('This method should have implemented.')


class Motorcycle(Vehicle):
    # Write your code here
    def __init__(self):
        Vehicle.__init__(self)
        self.spots_needed = 1
        self.size = VehicleSize.Motorcycle

    def can_fit_in_spot(self, spot):
        return True


class Car(Vehicle):
    # Write your code here
    def __init__(self):
        Vehicle.__init__(self)
        self.spots_needed = 1
        self.size = VehicleSize.Compact

    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.Large or \
               spot.get_size() == VehicleSize.Compact


class Bus(Vehicle):
    # Write your code here
    def __init__(self):
        Vehicle.__init__(self)
        self.spots_needed = 5
        self.size = VehicleSize.Large

    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.Large


class ParkingSpot:
    # Write your code here
    def __init__(self, lvl, r, n, sz):
        self.level = lvl
        self.row = r
        self.spot_number = n
        self.spot_size = sz
        self.vehicle = None

    def is_available(self):
        return self.vehicle == None

    def can_fit_vehicle(self, vehicle):
        return self.is_available() and vehicle.can_fit_in_spot(self)

    def park(self, v):
        if not self.can_fit_vehicle(v):
            return False

        self.vehicle = v
        self.vehicle.park_in_spot(self)
        return True

    def remove_vehicle(self):
        self.level.spot_freed()
        self.vehicle = None

    def get_row(self):
        return self.row

    def get_spot_number(self):
        return self.spot_number

    def get_size(self):
        return self.spot_size


class Level:
    # Write your code here
    def __init__(self, flr, num_rows, spots_per_row):
        self.floor = flr
        self.spots_per_row = spots_per_row
        self.number_spots = 0
        self.available_spots = 0;
        self.spots = []

        for row in range(num_rows):
            for spot in range(0, spots_per_row / 4):
                sz = VehicleSize.Motorcycle
                self.spots.append(ParkingSpot(self, row, self.number_spots, sz))
                self.number_spots += 1

            for spot in range(spots_per_row / 4, spots_per_row / 4 * 3):
                sz = VehicleSize.Compact
                self.spots.append(ParkingSpot(self, row, self.number_spots, sz))
                self.number_spots += 1

            for spot in range(spots_per_row / 4 * 3, spots_per_row):
                sz = VehicleSize.Large
                self.spots.append(ParkingSpot(self, row, self.number_spots, sz))
                self.number_spots += 1

        self.available_spots = self.number_spots

    def park_vehicle(self, vehicle):
        if self.get_available_spots() < vehicle.get_spots_needed():
            return False

        spot_num = self.find_available_spots(vehicle)

        if spot_num < 0:
            return False
        return self.park_starting_at_spot(spot_num, vehicle)

    def find_available_spots(self, vehicle):
        spots_needed = vehicle.get_spots_needed()
        last_row = -1
        spots_found = 0

        for i in xrange(len(self.spots)):
            spot = self.spots[i]
            if last_row != spot.get_row():
                spots_found = 0
                last_row = spot.get_row()
            if spot.can_fit_vehicle(vehicle):
                spots_found += 1
            else:
                spots_found = 0

            if spots_found == spots_needed:
                return i - (spots_needed - 1)

        return -1

    def park_starting_at_spot(self, spot_num, vehicle):
        vehicle.clear_spots()
        success = True

        for i in range(spot_num, spot_num + vehicle.get_spots_needed()):
            success = success and self.spots[i].park(vehicle)

        if success:
            self.available_spots -= vehicle.get_spots_needed()

        return success

    def spot_freed(self):
        self.available_spots += 1

    def get_available_spots(self):
        return self.available_spots


class ParkingLot:
    # @param {int} n number of leves
    # @param {int} num_rows  each level has num_rows rows of spots
    # @param {int} spots_per_row each row has spots_per_row spots
    def __init__(self, n, num_rows, spots_per_row):
        # Write your code here
        self.levels = []
        for i in range(n):
            self.levels.append(Level(i, num_rows, spots_per_row))

    # Park the vehicle in a spot (or multiple spots)
    # Return false if failed
    def park_vehicle(self, vehicle):
        # Write your code here
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    # unPark the vehicle
    def unpark_vehicle(self, vehicle):
        # Write your code here
        vehicle.clear_spots()