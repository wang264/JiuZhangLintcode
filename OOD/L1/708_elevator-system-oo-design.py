# 708. 电梯系统 OO Design
# 中文English
# 题目：为一栋大楼设计电梯系统
#
# 1.不需要考虑超重的情况
# 2.该电梯系统目前只有1台电梯, 该楼共有n层
# 3.每台电梯有三种状态：上升，下降，空闲
# 4.当电梯往一个方向移动时，在电梯内无法按反向的楼层

# 我们提供了其他几个已经实现好的类，你只需要实现Elevator Class内的部分函数即可。
# 注意：
# Currently elevator status is : DOWN.
# 是指现在正在执行 down stop list里的命令
# Currently elevator status is : UP.
# 是指现在正在执行 up stop list里的命令
#
# 样例
# Example 1
#
# Input:
# 5
# ExternalRequest(3, "Down")
# ExternalRequest(1, "Up")
# openGate()
# closeGate()
# openGate()
# closeGate()
#
# Output:
# Currently elevator status is : DOWN.
# Current level is at: 1.
# up stop list looks like: [false, false, false, false, false].
# down stop list looks like:  [false, false, true, false, false].
# *****************************************
# Currently elevator status is : DOWN.
# Current level is at: 1.
# up stop list looks like: [true, false, false, false, false].
# down stop list looks like:  [false, false, true, false, false].
# *****************************************
# Currently elevator status is : DOWN.
# Current level is at: 3.
# up stop list looks like: [true, false, false, false, false].
# down stop list looks like:  [false, false, false, false, false].
# *****************************************
# Currently elevator status is : UP.
# Current level is at: 3.
# up stop list looks like: [true, false, false, false, false].
# down stop list looks like:  [false, false, false, false, false].
# *****************************************
# Currently elevator status is : UP.
# Current level is at: 1.
# up stop list looks like: [true, false, false, false, false].
# down stop list looks like:  [false, false, false, false, false].
# *****************************************
# Currently elevator status is : IDLE.
# Current level is at: 1.
# up stop list looks like: [false, false, false, false, false].
# down stop list looks like:  [false, false, false, false, false].
# *****************************************
# Example 2
#
# Input:
# 5
# ExternalRequest(3, "Down")
# ExternalRequest(2, "Up")
# openGate()
# InternalRequest(1)
# closeGate()
# openGate()
# closeGate()
# openGate()
# closeGate()
#
# Output:
# Currently elevator status is : DOWN.
# Current level is at: 1.
# up stop list looks like: [false, false, false, false, false].
# down stop list looks like:  [false, false, true, false, false].
# *****************************************
#
# Currently elevator status is : DOWN.
# Current level is at: 1.
# up stop list looks like: [false, true, false, false, false].
# down stop list looks like:  [false, false, true, false, false].
# *****************************************
#
# Currently elevator status is : DOWN.
# Current level is at: 3.
# up stop list looks like: [false, true, false, false, false].
# down stop list looks like:  [false, false, false, false, false].
# *****************************************
#
# Currently elevator status is : DOWN.
# Current level is at: 3.
# up stop list looks like: [false, true, false, false, false].
# down stop list looks like:  [true, false, false, false, false].
# *****************************************
#
# Currently elevator status is : DOWN.
# Current level is at: 3.
# up stop list looks like: [false, true, false, false, false].
# down stop list looks like:  [true, false, false, false, false].
# *****************************************
#
# Currently elevator status is : DOWN.
# Current level is at: 1.
# up stop list looks like: [false, true, false, false, false].
# down stop list looks like:  [false, false, false, false, false].
# *****************************************
#
# Currently elevator status is : UP.
# Current level is at: 1.
# up stop list looks like: [false, true, false, false, false].
# down stop list looks like:  [false, false, false, false, false].
# *****************************************
#
# Currently elevator status is : UP.
# Current level is at: 2.
# up stop list looks like: [false, false, false, false, false].
# down stop list looks like:  [false, false, false, false, false].
# *****************************************
#
# Currently elevator status is : IDLE.
# Current level is at: 2.
# up stop list looks like: [false, false, false, false, false].
# down stop list looks like:  [false, false, false, false, false].
# *****************************************
# 注意事项
# 每行命令之后我们都会调用elevatorStatusDescription 函数，用于测试你是否处于一个正确的状态。

# 本参考程序来自九章算法，由 @MARK管理员 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Direction:
    UP = 'UP'
    DOWN = 'DOWN'


class Status:
    UP = 'UP'
    DOWN = 'DOWN'
    IDLE = 'IDLE'


class Request:
    def __init__(self, l=0):
        self.level = l

    def getLevel(self):
        return self.level


class ElevatorButton:
    def __init__(self, level, e):
        self.level = level
        self.elevator = e

    def pressButton(self):
        request = InternalRequest(self.level)
        self.elevator.handleInternalRequest(request);


class ExternalRequest(Request):
    def __init__(self, l=0, d=None):
        Request.__init__(self, l)
        self.direction = d

    def getDirection(self):
        return self.direction


class InternalRequest(Request):
    def __init__(self, l=None):
        Request.__init__(self, l)


class Elevator:
    def __init__(self, n):
        # Keep them, don't modify.
        self.buttons = []
        self.upStops = []
        self.downStops = []
        for i in xrange(n):
            self.upStops.append(False)
            self.downStops.append(False)
        self.currLevel = 0
        self.status = Status.IDLE

    def insertButton(self, eb):
        self.buttons.append(eb)

    def handleExternalRequest(self, r):
        # Write your code here
        if r.getDirection() == Direction.UP:
            self.upStops[r.getLevel() - 1] = True
            if self.noRequests(self.downStops):
                self.status = Status.UP
        else:
            self.downStops[r.getLevel() - 1] = True
            if self.noRequests(self.upStops):
                self.status = Status.DOWN

    def handleInternalRequest(self, r):
        # Write your code here
        if self.status == Status.UP:
            if r.getLevel() >= self.currLevel + 1:
                self.upStops[r.getLevel() - 1] = True

        elif self.status == Status.DOWN:
            if r.getLevel() <= self.currLevel + 1:
                self.downStops[r.getLevel() - 1] = True

    def openGate(self):
        # Write your code here
        if self.status == Status.UP:
            for i in xrange(len(self.upStops)):
                checkLevel = (self.currLevel + i) % len(self.upStops)
                if self.upStops[checkLevel]:
                    self.currLevel = checkLevel
                    self.upStops[checkLevel] = False
                    break

        elif self.status == Status.DOWN:
            for i in xrange(len(self.downStops)):
                checkLevel = (self.currLevel + len(self.downStops) - i) % len(self.downStops)
                if self.downStops[checkLevel]:
                    self.currLevel = checkLevel
                    self.downStops[checkLevel] = False
                    break

    def closeGate(self):
        # Write your code here
        if self.status == Status.IDLE:
            if self.noRequests(self.downStops):
                self.status = Status.UP
                return

            if self.noRequests(self.upStops):
                self.status = Status.DOWN
                return

        elif self.status == Status.UP:
            if self.noRequests(self.upStops):
                if self.noRequests(self.downStops):
                    self.status = Status.IDLE
                else:
                    self.status = Status.DOWN
        else:
            if self.noRequests(self.downStops):
                if self.noRequests(self.upStops):
                    self.status = Status.IDLE
                else:
                    self.status = Status.UP

    def noRequests(self, stops):
        for stop in stops:
            if stop:
                return False
        return True

    def elevatorStatusDescription(self):
        description = "Currently elevator status is : " + self.status + \
                      ".\nCurrent level is at: " + str(self.currLevel + 1) + \
                      ".\nup stop list looks like: " + self.toString(self.upStops) + \
                      ".\ndown stop list looks like:  " + self.toString(self.downStops) + \
                      ".\n*****************************************\n"
        return description

    @classmethod
    def toString(cls, stops):
        return str(stops).replace("False", "false").replace("True", "true")