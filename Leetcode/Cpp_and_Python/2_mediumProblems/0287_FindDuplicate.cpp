// Daily Problem Solution 
class Solution {
public:
    int findDuplicate(vector<int>& nums) 
    {
		int slow = nums[0];
		int fast = nums[nums[0]];
        while(slow != fast)
        {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }    
        int entryPoint = 0;
        while (entryPoint != slow)
		{
			entryPoint = nums[entryPoint];
			slow = nums[slow];
		}
		return slow;

    }
};

class Solution {
public:
    int findDuplicate(vector<int>& nums) 
    {
        unordered_map<int, int> map;
        for(int i=0; i<nums.size(); i++)
        {
            if(map[nums[i]] == nums[i])
            {return nums[i];}
            map[nums[i]] = nums[i];
        }
        return -1;    
    }
};

// ALTERNATE SOLUTION INVOLVES TORTOISE AND HARE ALGORITHM
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int fast = 0, slow = 0;
        do
        {
            fast = nums[nums[fast]];
            slow = nums[slow];
        }
        while (fast != slow);
        slow = 0; //Restart to find the breakpoint as we have completed on of the cycles
        // Thus guaranteed that the next hit of the cycle would be at the repeated element.
        while (fast != slow)
        {
            fast = nums[fast];
            slow = nums[slow];
        }
        return slow;
    }
};

// Explanation by: lf963 on Leetcode

/*
If there is duplicate in the array, the mapping function is many-to-one.
For example, let's assume
nums = [2,1,3,1], then the mapping function is 0->2, {1,3}->1, 2->3. Then the sequence we get definitely has a cycle. 0->2->3->1->1->1->1->1->........ The starting point of this cycle is the duplicate number.
We can use Floyd's Tortoise and Hare Algorithm to find the starting point.

According to Floyd's algorithm, first step, if a cycle does exist, and you advance the tortoise one node each unit of time but the hare two nodes each unit of time, then they will eventually meet. This is what the first while loop does. The first while loop finds their meeting point.

*Second step, take tortoise or hare to the start point of the list (i.e. let one of the animal be 0) and keep the other one staying at the meeting point. Now, advance 
both of the animals one node each unit of time, the meeting point is the starting point of the cycle. This is what the second while loop does. 
The second while loop finds their meeting point.

*Proof of second step:
Distance traveled by tortoise while meeting = x + y
Distance traveled by hare while meeting = (x + y + z) + y = x + 2y + z
Since hare travels with double the speed of tortoise,
so 2(x+y)= x+2y+z => x+2y+z = 2x+2y => x=z
Hence by moving tortoise to start of linked list, and making both animals to move one node at a time, they both have same distance to cover .
They will reach at the point where the loop starts in the linked list 
*/