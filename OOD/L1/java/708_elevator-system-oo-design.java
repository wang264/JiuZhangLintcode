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


enum Direction {
    UP, DOWN
}

enum Status {
	UP, DOWN, IDLE
}

class Request {
	private int level;

	public Request(int l)
	{
		level = l;
	}

	public int getLevel()
	{
		return level;
	}
}

class ElevatorButton {
	private int level;
	private Elevator elevator;

	public ElevatorButton(int level, Elevator e)
	{
		this.level = level;
		this.elevator = e;
	}

	public void pressButton()
	{
		InternalRequest request = new InternalRequest(level);
		elevator.handleInternalRequest(request);
	}
}

class ExternalRequest extends Request{

	private Direction direction;

	public ExternalRequest(int l, Direction d) {
		super(l);
		// TODO Auto-generated constructor stub
		this.direction = d;
	}

	public Direction getDirection()
	{
		return direction;
	}
}

class InternalRequest extends Request{

	public InternalRequest(int l) {
		super(l);
		// TODO Auto-generated constructor stub
	}
}

public class Elevator {

	private List<ElevatorButton> buttons;

	private List<Boolean> upStops;
	private List<Boolean> downStops;

	private int currLevel;
	private Status status;

	public Elevator(int n)
	{
		buttons = new ArrayList<ElevatorButton>();
		upStops = new ArrayList<Boolean>();
		downStops = new ArrayList<Boolean>();
		currLevel = 0;
		status = Status.IDLE;

		for(int i = 0; i < n; i++)
		{
			upStops.add(false);
			downStops.add(false);
		}
	}

	public void insertButton(ElevatorButton eb)
	{
		buttons.add(eb);
	}

	public void handleExternalRequest(ExternalRequest r)
	{
		if(r.getDirection() == Direction.UP)
		{
			upStops.set(r.getLevel() - 1, true);
			if(noRequests(downStops))
			{
				status = Status.UP;
			}
		}
		else
		{
			downStops.set(r.getLevel() - 1, true);
			if(noRequests(upStops))
			{
				status = Status.DOWN;
			}
		}
	}

	public void handleInternalRequest(InternalRequest r)
	{
		// check valid
		if(status == Status.UP)
		{
			if(r.getLevel() >= currLevel + 1)
			{
				upStops.set(r.getLevel() - 1, true);
			}
		}
		else if(status == Status.DOWN)
		{
			if(r.getLevel() <= currLevel + 1)
			{
				downStops.set(r.getLevel() - 1, true);
			}
		}
	}

	public void openGate() throws Exception
	{
		if(status == Status.UP)
		{
			for(int i = 0; i < upStops.size(); i++)
			{
				int checkLevel = (currLevel + i) % upStops.size();
				if(upStops.get(checkLevel))
				{
					currLevel = checkLevel;
					upStops.set(checkLevel, false);
					break;
				}
			}
		}
		else if(status == Status.DOWN)
		{
			for(int i = 0; i < downStops.size(); i++)
			{
				int checkLevel = (currLevel + downStops.size() - i) % downStops.size();
				if(downStops.get(checkLevel))
				{
					currLevel = checkLevel;
					downStops.set(checkLevel, false);
					break;
				}
			}
		}
	}

	public void closeGate()
	{
		if(status == Status.IDLE)
		{
			if(noRequests(downStops))
			{
				status = Status.UP;
				return;
			}
			if(noRequests(upStops))
			{
				status = Status.DOWN;
				return;
			}
		}
		else if(status == Status.UP)
		{
			if(noRequests(upStops))
			{
				if(noRequests(downStops))
				{
					status = Status.IDLE;
				}
				else status = Status.DOWN;
			}
		}
		else {
			if(noRequests(downStops))
			{
				if(noRequests(upStops))
				{
					status = Status.IDLE;
				}
				else status = Status.UP;
			}
		}
	}

	private boolean noRequests(List<Boolean> stops)
	{
		for(int i = 0; i < stops.size(); i++)
		{
			if(stops.get(i))
			{
				return false;
			}
		}
		return true;
	}

	public String elevatorStatusDescription()
	{
		String description = "Currently elevator status is : " + status
				+ ".\nCurrent level is at: " + (currLevel + 1)
				+ ".\nup stop list looks like: " + upStops
				+ ".\ndown stop list looks like:  " + downStops
				+ ".\n*****************************************\n";
		return description;
	}
}