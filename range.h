#ifndef RANGE_H
#define RANGE_H

namespace range
{
	class Range
	{
		private:
			int start;
			int end;
			
		public:
			Range(int start, int end);
			
			bool isInRange(int number);
			bool isInRange(Range range);
			bool isOverlapping(Range range);
			
	};
}		
			
		
#endif