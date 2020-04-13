/**
* 本参考程序来自九章算法，由 @安助教 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

const char* names[] = { "epub","pdf","mobi" };

enum Format { EPUB, PDF, MOBI };



class Book
{
private:

    Format format;

public:

	Book(Format format)
	{
		this->format = format;
	}

	Format getFormat()
	{
		return format;
	}
};

class EBookReader
{
protected:
	Book *book;

public:

	EBookReader(Book *b)
	{
		this->book = b;
	}

	virtual string readBook() = 0;
	virtual string displayReaderType() = 0;
};



class EpubReader :public EBookReader
{
public:

	EpubReader(Book *b):EBookReader(b){}

	string readBook()
	{
		return names[book->getFormat()];
	}

	string displayReaderType()
	{
		return "Using EPUB reader";
	}
};

class MobiReader :public EBookReader
{
public:

	MobiReader(Book *b):EBookReader(b){}

	string readBook()
	{
		return names[book->getFormat()];
	}

	string displayReaderType()
	{
		return "Using MOBI reader";
	}
};

class PdfReader :public EBookReader
{
public:

	PdfReader(Book *b):EBookReader(b){}

	string readBook()
	{
		return names[book->getFormat()];
	}

	string displayReaderType()
	{
		return "Using PDF reader";
	}
};

class EBookReaderFactory
{
public:

	EBookReader *createReader(Book *b)
	{
		if (b->getFormat() == EPUB)
		{
			return new EpubReader(b);
		}
		else if (b->getFormat() == MOBI)
		{
			return new MobiReader(b);
		}
		else if (b->getFormat() == PDF)
		{
			return new PdfReader(b);
		}
		else
		{
			return NULL;
		}
	}
};

class Kindle
{
private:

	vector<Book *> *books;
	EBookReaderFactory *readerFactory;

public:

	Kindle()
	{
		books = new vector<Book *>;
		readerFactory = new EBookReaderFactory;
	}

	string readBook(Book *book)
	{
		EBookReader *reader = readerFactory->createReader(book);
		return reader->displayReaderType() + ", book content is: " + reader->readBook();
	}

	void downloadBook(Book *b)
	{
		books->push_back(b);
	}

	void uploadBook(Book *b)
	{
		books->push_back(b);
	}

	void deleteBook(Book *b)
	{
		vector<Book *>::iterator it;
		for (it = books->begin(); it != books->end(); it++)
		{
			if ((*it)->getFormat() == b->getFormat())
			{
				books->erase(it);
				return;
			}
		}
	}
};