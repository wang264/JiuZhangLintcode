# Description
# Support two basic uber features:
#
# Drivers report their locations.
# Rider request a uber, return a matched driver.
# When rider request a uber, match a closest available driver with him, then mark the driver not available.
#
# When next time this matched driver report his location, return with the rider's information.
#
# You can implement it with the following instructions:
#
# report(driver_id, lat, lng)
# return null if no matched rider.
# return matched trip information.
# request(rider_id, lat, lng)
# create a trip with rider's information.
# find a closest driver, mark this driver not available.
# fill driver_id into this trip.
# return trip
# This is the definition of Trip in Java:
#
# public class Trip {
#     public int id; // trip's id, primary key
#     public int driver_id, rider_id; // foreign key
#     public double lat, lng; // pick up location
# }
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input:
#   report(1, 36.1344, 77.5672)
#   report(2, 45.1344, 76.5672)
#   request(2, 39.1344, 76.5672)
#   report(1, 38.1344, 75.5672)
#   report(2, 45.1344, 76.5672)
# Output:
#   null
#   null
#   Trip(rider_id: 2, driver_id: 1, lat: 39.1344, lng: 76.5672)
#   Trip(rider_id: 2, driver_id: 1, lat: 39.1344, lng: 76.5672)
#   null
# Example 2:
#
# Input:
#   report(1, 36.1344, 77.5672)
#   report(2, 45.1344, 76.5672)
#   request(2, 39.1344, 76.5672)
#   request(3, 78.1344, 134.5672)
# Output:
#   null
#   null
#   LOG(INFO): Trip(rider_id: 2, driver_id: 1, lat: 39.1344, lng: 76.5672)
#   LOG(INFO): Trip(rider_id: 3, driver_id: 2, lat: 78.1344, lng: 134.5672)

#
# 需要使用两个映射, 分别是 司机id -> 司机位置, 司机id -> trip.
#
# 大多语言都提供了这样的数据结构, Java HashMap, C++ map, python dict.
#
# report(dirver_id, lat, lng)
# 如果在 dirver_id -> trip 的映射中查找到对应的trip, 直接返回
# 没有查找到trip, 更新 dirver_id -> location 中的位置信息
# request(rider_id, lat, lng)
#
# 遍历 driver_id -> location , 选择距离最近的司机
# 建立 trip 并添加至 driver_id -> trip
# 将该司机从 dirver_id -> location 中删除
# 即司机id->司机位置这个映射中保存的是可用的司机.

'''
Definition of Trip:
class Trip:
    self.id; # trip's id, primary key
    self.driver_id, self.rider_id; # foreign key
    self.lat, self.lng; # pick up location

    def __init__(self, rider_id, lat, lng):

Definition of Helper
class Helper:
    @classmethod
    def get_distance(cls, lat1, lng1, lat2, lng2):
        # return calculate the distance between (lat1, lng1) and (lat2, lng2)
'''
from Trip import Trip, Helper


class Location:

    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng


class MiniUber:

    def __init__(self):
        # initialize your data structure here.
        self.driver2Location = {}
        self.driver2Trip = {}

    # @param {int} driver_id an integer
    # @param {double} lat, lng driver's location
    # return {trip} matched trip information if there have matched rider or null
    def report(self, driver_id, lat, lng):
        # Write your code here
        if driver_id in self.driver2Trip:
            return self.driver2Trip[driver_id]

        if driver_id in self.driver2Location:
            self.driver2Location[driver_id].lat = lat
            self.driver2Location[driver_id].lng = lng
        else:
            self.driver2Location[driver_id] = Location(lat, lng)

        return None

    # @param rider_id an integer
    # @param lat, lng driver's location
    # return a trip
    def request(self, rider_id, lat, lng):
        # Write your code here
        trip = Trip(rider_id, lat, lng)
        distance, driver_id = -1, -1

        for key, value in self.driver2Location.items():
            dis = Helper.get_distance(value.lat, value.lng, lat, lng);
            if distance < 0 or distance > dis:
                driver_id = key
                distance = dis

        if driver_id != -1:
            del self.driver2Location[driver_id]

        trip.driver_id = driver_id;
        self.driver2Trip[driver_id] = trip

        return trip