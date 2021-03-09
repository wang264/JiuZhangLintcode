# 529. Geohash
# 中文English
# Geohash is a hash function that convert a location coordinate pair into a base32 string.
#
# Check how to generate geohash on wiki: Geohash or just google it for more details.
#
# Try http://geohash.co/.
#
# You task is converting a (latitude, longitude) pair into a geohash string.
#
# Example
# Example1
#
# Input:
# lat = 39.92816697
# lng = 116.38954991
# precision = 12
# Output: "wx4g0s8q3jf9"
# Example2
#
# Input:
# lat = -90
# lng = 180
# precision = 12
# Output: "pbpbpbpbpbpb"
# Notice
# 1 <= precision <=12


class GeoHash:
    # @param {double} latitude, longitude a location coordinate pair
    # @param {int} precision an integer between 1 to 12
    # @return {string} a base32 string
    def encode(self, latitude, longitude, precision):
        # Write your code here
        _base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
        lat_bin = self.get_bin(latitude, -90, 90)
        lng_bin = self.get_bin(longitude, -180, 180)

        hash_code, b = '', ''
        for i in range(30):
            b += lng_bin[i] + lat_bin[i]

        for i in range(0, 60, 5):
            hash_code += _base32[int(b[i:i + 5], 2)]

        return hash_code[:precision]

    def get_bin(self, value, left, right):
        b = ''
        for i in range(30):
            mid = (left + right) / 2.0
            if value > mid:
                left = mid
                b += '1'
            else:
                right = mid
                b += '0'
        return b