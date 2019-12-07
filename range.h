#ifndef LIBRANGE_H
#define LIBRANGE_H

namespace LibRange
{
	class Range
	{
		public:
		
			Range(int start, int end);
			
			bool isInRange(int number);
			bool isInRange(Range range);
			bool isOverlapping(Range range);
			
		private:
			int start;
			int end;
	};
			
			
		
#endif