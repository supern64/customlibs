// A simple implementation of my own library
#include "range.h"

namespace range {

	Range::Range(int start, int end): start(start), end(end){}

	bool Range::isInRange(int number)
	{
		if (number >= start && number <= end)
		{
			return true;
		} else 
		{
			return false;
		}
	}

	bool Range::isInRange(Range range)
	{
		if (range.start >= start && range.end <= range.end)
		{
			return true;
		} else
		{ 
			return false;
		}
	}

	bool Range::isOverlapping(Range range)
	{
		if (isInRange(range.start) || isInRange(range.end))
		{
			return true;
		} else
		{ 
			return false;
		}
	}
};
