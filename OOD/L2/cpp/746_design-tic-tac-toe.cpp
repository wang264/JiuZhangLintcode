/**
* 本参考程序来自九章算法，由 @九章算法助教团队 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

/*
先初始化井字棋盘，操作函数根据题目要求，依次判断游戏是否于上一轮结束，该位置是否被选择，是否满足胜利条件，
根据结果进行对应的抛出或打印操作，若无特殊操作，交换行动玩家。
*/
class GameEndException
{
public:
    string what()
	{
		return "Game has been ended, cannot make any more moves";
	}
}gameEndException;

class AlreadyTakenException
{
public:
	string what()
	{
		return "This place has been taken";
	}
}alreadyTakenException;

class TicTacToe
{
private:

	char board[3][3];
	char currentPlayerMark;
	bool gameEnd;

public:

	TicTacToe()
	{
		initialize();
	}

	char getCurrentPlayer()
	{
		return currentPlayerMark;
	}

	void initialize()
	{
		gameEnd = false;
		currentPlayerMark = 'x';

		for (int i = 0; i < 3; i++)
		{
			for (int j = 0; j < 3; j++)
			{
				board[i][j] = '-';
			}
		}
	}

	bool isBoardFull()
	{
		for (int i = 0; i < 3; i++)
		{
			for (int j = 0; j < 3; j++)
			{
				if (board[i][j] == '-')
				{
					return false;
				}
			}
		}
		gameEnd = true;
		return true;
	}

	void changePlayer()
	{
		if (currentPlayerMark == 'x')
		{
			currentPlayerMark = 'o';
		}
		else
		{
			currentPlayerMark = 'x';
		}
	}

	bool move(int row, int col)
	{
		if (gameEnd)
		{
			throw gameEndException;
		}
		if (board[row][col] != '-')
		{
			throw alreadyTakenException;
		}
		board[row][col] = currentPlayerMark;
		bool win;
		//check row
		win = true;
		for (int i = 0; i < 3; i++)
		{
			if (board[row][i] != currentPlayerMark)
			{
				win = false;
				break;
			}
		}
		if (win)
		{
			gameEnd = true;
			return win;
		}
		//check column
		win = true;
		for (int i = 0; i < 3; i++)
		{
			if (board[i][col] != currentPlayerMark)
			{
				win = false;
				break;
			}
		}
		if (win)
		{
			gameEnd = true;
			return win;
		}
		//check back diagonal
		win = true;
		for(int i = 0; i < 3; i++)
		{
			if (board[i][i] != currentPlayerMark)
			{
				win = false;
				break;
			}
		}
		if (win)
		{
			gameEnd = true;
			return win;
		}
		//check forward diagonal
		win = true;
		for (int i = 0; i < 3; i++)
		{
			if (board[i][3 - i - 1] != currentPlayerMark)
			{
				win = false;
				break;
			}
		}
		if (win)
		{
			gameEnd = true;
            return win;
		}
		changePlayer();
		return win;
	}
};