# Description
# In the Master-Slave architecture, slave server will ping master in every k seconds to tell master server he is alive.
#  If a master server didn't receive any ping request from a slave server in 2 * k seconds, the master will trigger
# an alarm (for example send an email) to administrator.
#
# Let's mock the master server, you need to implement the following three methods:
#
# initialize(slaves_ip_list, k). salves_ip_list is a list of slaves' ip addresses. k is define above.
# ping(timestamp, slave_ip). This method will be called every time master received a ping request from one of the
# slave server. timestamp is the current timestamp in seconds. slave_ip is the ip address of the slave server who
# pinged master.
# getDiedSlaves(timestamp). This method will be called periodically (it's not guaranteed how long between two calls).
# timestamp is the current timestamp in seconds, and you need to return a list of slaves' ip addresses that died.
# Return an empty list if no died slaves found.
# You can assume that when the master started, the timestamp is 0, and every method will be called with an global
#  increasing timestamp.
#
# Have you met this question in a real interview?
# Example
# Example1
#
# Input:
# initialize(["10.173.0.2", "10.173.0.3"], 10)
# ping(1, "10.173.0.2")
# getDiedSlaves(20)
# getDiedSlaves(21)
# ping(22, "10.173.0.2")
# ping(23, "10.173.0.3")
# getDiedSlaves(24)
# getDiedSlaves(42)
#
# Output:
# ["10.173.0.3"]
# ["10.173.0.2", "10.173.0.3"]
# []
# ["10.173.0.2"]
#
# Explanation:
# initialize(["10.173.0.2", "10.173.0.3"], 10)
# ping(1, "10.173.0.2")
# getDiedSlaves(20)
# >> ["10.173.0.3"]
# getDiedSlaves(21)
# >> ["10.173.0.2", "10.173.0.3"]
# ping(22, "10.173.0.2")
# ping(23, "10.173.0.3")
# getDiedSlaves(24)
# >> []
# getDiedSlaves(42)
# >> ["10.173.0.2"]


class HeartBeat:

    def __init__(self):
        # initialize your data structure here
        self.slaves_ip_list = dict()


    # @param {str[]} slaves_ip_list a list of slaves'ip addresses
    # @param {int} k an integer
    # @return nothing
    def initialize(self, slaves_ip_list, k):
        # Write your code here
        self.k = k
        for ip in slaves_ip_list:
            self.slaves_ip_list[ip] = 0


    # @param {int} timestamp current timestamp in seconds
    # @param {str} slave_ip the ip address of the slave server
    # @return nothing
    def ping(self, timestamp, slave_ip):
        # Write your code here
        if slave_ip not in self.slaves_ip_list:
            return

        self.slaves_ip_list[slave_ip] = timestamp


    # @param {int} timestamp current timestamp in seconds
    # @return {str[]} a list of slaves'ip addresses that died
    def getDiedSlaves(self, timestamp):
        # Write your code here
        results = []
        for ip, time in self.slaves_ip_list.items():
            if time <= timestamp - 2 * self.k:
                results.append(ip)
        return results