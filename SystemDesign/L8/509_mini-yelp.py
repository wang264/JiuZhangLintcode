# Description
# Design a simple yelp system. Support the following features:
#
# 1. Add a restaurant with name and location.
# 2. emove a restaurant with id.
# 3. Search the nearby restaurants by given location.
# A location is represented by latitude and longitude, both in double. A Location class is given in code.
# Nearby is defined by distance smaller than k Km .
#
# Restaurant class is already provided and you can directly call Restaurant.create() to create a new object. Also, a Helper class is provided to calculate the distance between two location, use Helper.get_distance(location1, location2).
#
# A GeoHash class is provided to convert a location to a string. Try GeoHash.encode(location) to convert location to a geohash string and GeoHash.decode(string) to convert a string to location.
#
# Press here to Learn about GeoHash
#
# Have you met this question in a real interview?
# Example
# Example 1
#
# Input:
# addRestaurant("Lint Cafe", 10.4999999, 11.599999)
# addRestaurant("Code Cafe", 10.4999999, 11.512109)
# neighbors(10.5, 11.6, 6.7)
# removeRestaurant(1)
# neighbors(10.5, 9.6, 6.7)
#
# Output:
# 1
# 2
# ["Lint Cafe"]
# []
#
# Explanation:
# When add 2 restaurants, we return 1 and 2.
# When searching neighbors, first time we find Lint Cafe and the second time we find nothing.
# Example 2
#
# Input:
# addRestaurant("Lint Cafe", 10.4999999, 11.599999)
# addRestaurant("Code Cafe", 10.4999999, 11.512109)
# neighbors(10.5, 11.6, 6.7)
# removeRestaurant(1)
# neighbors(10.5, 11.6, 6.7)
#
# Output:
# 1
# 2
# ["Lint Cafe"]
# []
#
# Explanation
# When searching neighbors the second time, the "Lint Cafe" has been removed.

from YelpHelper import Location, Restaurant, GeoHash, Helper
from collections import defaultdict
from heapq import heappush, heappop


class MiniYelp:

    def __init__(self):
        self.errors = [2500, 630, 78, 20, 2.4, 0.61, 0.076, 0.01911]
        self.id2restaurant = dict()
        self.loc_table = defaultdict(lambda: defaultdict(set))

    # @param {str} name
    # @param {Location} location
    # @return {int} restaurant's id
    def add_restaurant(self, name, location):
        restaurant = Restaurant.create(name, location)
        r_id = restaurant.id

        self.id2restaurant[r_id] = restaurant

        geocode = GeoHash.encode(location)

        for i in range(9):
            self.loc_table[i][geocode[:i]].add(r_id)

        return r_id

    # @param {int} restaurant_id
    # @return nothing
    def remove_restaurant(self, restaurant_id):
        if restaurant_id not in self.id2restaurant:
            return

        restaurant = self.id2restaurant.pop(restaurant_id)
        geocode = GeoHash.encode(restaurant.location)
        for i in range(9):
            self.loc_table[i][geocode[:i]].remove(restaurant_id)

    # @param {Location} location
    # @param {double} k, distance smaller than k miles
    # @return {str[]} a list of restaurant's name and sort by
    # distance from near to far.
    def neighbors(self, location, k):
        code_len = self.get_code_len(k)
        geocode = GeoHash.encode(location)
        r_ids = list(self.loc_table[code_len][geocode[:code_len]])
        dist_lists = []
        for r_id in r_ids:
            restaurant = self.id2restaurant[r_id]
            dist = Helper.get_distance(restaurant.location, location)
            if dist < k:
                heappush(dist_lists, (dist, restaurant.name))

        name_lists = []
        while dist_lists:
            _, name = heappop(dist_lists)
            name_lists.append(name)

        return name_lists

    def get_code_len(self, k):

        for i, error in enumerate(self.errors):
            if k > error:
                return i
        return len(self.errors)

