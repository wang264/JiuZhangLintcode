/**
* 本参考程序来自九章算法，由 @安助教 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

class CoffeePack
{
private:
    int neededMilk;
	int neededSugar;

public:

	CoffeePack(int neededMilk, int neededSugar)
	{
		this->neededMilk = neededMilk;
		this->neededSugar = neededSugar;
	}

	int getNeededMilk()
	{
		return neededMilk;
	}

	int getNeededSugar()
	{
		return neededSugar;
	}
};

class Coffee
{
public:
	virtual double getCost() = 0;
	virtual string getIngredients() = 0;
};

class SimpleCoffee :public Coffee
{
public:

	double getCost()
	{
		return 2;
	}

	string getIngredients()
	{
		return "Plain Coffee";
	}
};

class CoffeeDecorator :public Coffee
{
protected:
	Coffee *decoratedCoffee;

public:

	CoffeeDecorator(Coffee *coffee)
	{
		this->decoratedCoffee = coffee;
	}

	double getCost()
	{
		return decoratedCoffee->getCost();
	}

	string getIngredients()
	{
		return decoratedCoffee->getIngredients();
	}
};

class WithMilk :public CoffeeDecorator
{
public:

	WithMilk(Coffee *coffee):CoffeeDecorator(coffee){}

	double getCost()
	{
		return CoffeeDecorator::getCost() + 0.5;
	}

	string getIngredients()
	{
		return CoffeeDecorator::getIngredients() + ", Milk";
	}
};

class WithSugar :public CoffeeDecorator
{
public:

	WithSugar(Coffee *coffee):CoffeeDecorator(coffee){}

	double getCost()
	{
		return CoffeeDecorator::getCost() + 0.5;
	}

	string getIngredients()
	{
		return CoffeeDecorator::getIngredients() + ", Sugar";
	}
};

class CoffeeMaker
{
public:
	Coffee *makeCoffee(CoffeePack *pack)
	{
		Coffee *coffee = new SimpleCoffee();

		for (int i = 0; i < pack->getNeededMilk(); i++)
		{
			coffee = new WithMilk(coffee);
		}

		for (int i = 0; i < pack->getNeededSugar(); i++)
		{
			coffee = new WithSugar(coffee);
		}
		return coffee;
	}
};