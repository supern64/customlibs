// A simple implementation of my own library
#include "range.h"

class Range
{
	public:
		int start;
		int end;
		
		Range(int start, int end)
		{
			start = start;
			end = end;
		}
		
		bool isInRange(int number)
		{
			if (number >= start && number <= end)
			{
				return true;
			} else 
			{
				return false;
			}
		}
		
		bool isInRange(Range range)
		{
			if (range.start >= start && range.end <= range.end)
			{
				return true;
			} else
			{ 
				return false;
			}
		}
		
		bool isOverlapping(Range range)
		{
			if (isInRange(range.start) || isInRange(range.end))
			{
				return true;
			} else
			{ 
				return false;
			}
		}
}