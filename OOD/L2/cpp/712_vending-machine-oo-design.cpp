/**
* 本参考程序来自九章算法，由 @MARK管理员 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

class VendingMachine;

class State
{
public:

    virtual void selectItem(string selection) = 0;
	virtual void insertMoney(int value) = 0;
	virtual void executeTransaction() = 0;
	virtual int cancelTransaction()=0;
	virtual string toString() = 0;
};

class AbstractState :public State
{
protected:
	VendingMachine *vendingMachine;

public:

	AbstractState(VendingMachine *vendingMachine)
	{
		this->vendingMachine = vendingMachine;
	}

};

class NoSelectionState :public AbstractState
{
public:

	NoSelectionState(VendingMachine *vendingMachine) :AbstractState(vendingMachine) {}

	void selectItem(string selection);

	void insertMoney(int value)
	{
		//cout << "Please make a selection first" << endl;
	}

	void executeTransaction()
	{
	//	cout << "Please make a selection first" << endl;
	}

	int cancelTransaction()
	{
		//cout << "Please make a selection first" << endl;
		return 0;
	}

	string toString()
	{
		return "NoSelection";
	}
};

class HasSelectionState :public AbstractState
{
public:

	HasSelectionState(VendingMachine *vendingMachine) :AbstractState(vendingMachine) {}

	void selectItem(string selection);

	void insertMoney(int value);

	void executeTransaction()
	{
		//cout << "You need to insert money first" << endl;
	}

	int cancelTransaction();

	string toString()
	{
		return "HasSelection";
	}

};

class InsertedMoneyState :public AbstractState
{
public:

	InsertedMoneyState(VendingMachine *vendingMachine) :AbstractState(vendingMachine) {}

	void selectItem(string selection)
	{
		//cout << "Already has a selection, please cancel transaction to make a new selection" << endl;
	}

	void insertMoney(int value);

	void executeTransaction();

	int cancelTransaction();

	string toString()
	{
		return "InsertedMoney";
	}
};

class VendingMachine
{
private:

	string currentSelectedItem;
	int currentInsertedMoney;
	AbstractState *state;
	NoSelectionState *noSelectionState;
	HasSelectionState *hasSelectionState;
	InsertedMoneyState *insertedMoneyState;
	map<string, int> *itemPrice;

public:

	VendingMachine()
	{
		currentInsertedMoney = 0;
		currentSelectedItem = "null";
		noSelectionState = new NoSelectionState(this);
		hasSelectionState = new HasSelectionState(this);
		insertedMoneyState = new InsertedMoneyState(this);
		state = noSelectionState;

		itemPrice = new map<string, int>;
		(*itemPrice)["Coke"] = 199;
		(*itemPrice)["Sprite"] = 299;
		(*itemPrice)["MountainDew"] = 399;
	}

	void setSelectedItem(string item)
	{
		this->currentSelectedItem = item;
	}

	string getSelectedItem()
	{
		return currentSelectedItem;
	}

	void insertMoney(int amount)
	{
		this->currentInsertedMoney += amount;
	}

	void emptyInsertedMoney()
	{
		this->currentInsertedMoney = 0;
	}

	int getInsertedMoney()
	{
		return currentInsertedMoney;
	}

	int getSalePrice()
	{
		if (currentSelectedItem == "null")
		{
			//cout << "Please make a selection before asking price" << endl;
			return 0;
		}
		else
		{
			return (*itemPrice)[currentSelectedItem];
		}
	}

	void changeToNoSelectionState()
	{
		state = noSelectionState;
	}

	void changeToHasSelectionState()
	{
		state = hasSelectionState;
	}

	void changeToInsertedMoneyState()
	{
		state = insertedMoneyState;
	}

	void selectItem(string selection)
	{
		state->selectItem(selection);
	}

	void addMoney(int value)
	{
		state->insertMoney(value);
	}

	void executeTransaction()
	{
		state->executeTransaction();
	}

	int cancelTransaction()
	{
		return state->cancelTransaction();
	}

	string printState()
	{
		string res = "";
		res = "Current selection is: " + currentSelectedItem + ", current inserted money: " + to_string(currentInsertedMoney)
			+ ", current state is : " + state->toString();
		return res;
	}
};

void NoSelectionState::selectItem(string selection)
{
	vendingMachine->setSelectedItem(selection);
	vendingMachine->changeToHasSelectionState();
}

void HasSelectionState::selectItem(string selection)
{
	vendingMachine->setSelectedItem(selection);
}

void HasSelectionState::insertMoney(int value)
{
	vendingMachine->insertMoney(value);
	vendingMachine->changeToInsertedMoneyState();
}

int HasSelectionState::cancelTransaction()
{
	//cout << "Transaction canceled" << endl;
	vendingMachine->setSelectedItem(NULL);
	vendingMachine->changeToNoSelectionState();
	return 0;
}

void InsertedMoneyState::insertMoney(int value)
{
	vendingMachine->insertMoney(value);
}

void InsertedMoneyState::executeTransaction()
{
	int diff = vendingMachine->getInsertedMoney() - vendingMachine->getSalePrice();

	if (diff >= 0)
	{
		//cout << "Executing transaction, will return you : " + to_string(diff) +
		//	" money and item: " + vendingMachine->getSelectedItem() << endl;
		vendingMachine->setSelectedItem("null");
		vendingMachine->emptyInsertedMoney();
		vendingMachine->changeToNoSelectionState();
	}
	else
	{
		//cout << "Not enough money, please insert " + to_string(-diff) + " more." << endl;
	}
}

int InsertedMoneyState::cancelTransaction()
{
	int insertedMoney = vendingMachine->getInsertedMoney();
	vendingMachine->setSelectedItem(NULL);
	vendingMachine->emptyInsertedMoney();
	vendingMachine->changeToNoSelectionState();
	return insertedMoney;
}