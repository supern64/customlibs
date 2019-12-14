#ifndef RANGE_H
#define RANGE_H

namespace range
{
    class Range {
        private:
            int start;
            int end;
            
        public:
            inline Range(int start, int end): start(start), end(end){};
            
            inline bool isInRange(int number)
            {
                if (number >= start && number <= end)
                {
                    return true;
                } else 
                {
                    return false;
                }
            };

            inline bool isInRange(Range range)
            {
                if (range.start >= start && range.end <= range.end)
                {
                    return true;
                } else
                { 
                    return false;
                }
            }

            inline bool isOverlapping(Range range)
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
}

#endif 