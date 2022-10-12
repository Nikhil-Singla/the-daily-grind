/*
Question:

You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is 
possible to measure exactly targetCapacity liters using these two jugs.

If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.

*/

class Solution {
public:
    bool canMeasureWater(int jug1Capacity, int jug2Capacity, int targetCapacity) 
    {
        
        int x=jug1Capacity,y=jug2Capacity,z=x+y; //: X is Jug 1 Capacity, Y is Jug 2 Capacity and Z is the Total Sum of capacities.
        int steps[]={x,-x,-y,y}; //STEPS THAT CAN BE PERFORMED: //: The possible individual moves that can be taken from the two jugs
        
        queue<int> q; //: Declaring a queue
        vector<int> vis(z+1,0); // VISITED ARRAY TO KEEP NOT ITERATING THE SAME VALUES OVER AND OVER AGAIN 
        //: Vector array initialized to the size of sum of the two jugs + 1, all initialised to 0.
        
        q.push(0); // Pushing the initial water cap in the jug?
        vis[0]=1; // Visited 0
        while(!q.empty())
        {
            int node=q.front();
            q.pop();
            
            if(node==targetCapacity)
            {
                return true; // WHEN WE FIND THE TARGET CAPACITY ACHIEVED
            }
            for(int i=0;i<4;i++)
            {
                int newNode=node+steps[i];
                if(newNode>=0 && newNode<=z && vis[newNode]==0) //BOUNDARY CHECKS 
                {
                    q.push(newNode);
                    vis[newNode]=1;
                }
            }
        }
        return false; // IF TARGET CAPACITY CAN NEVER BE ACHIVED
    }
};
// SOLUTION BY akb9911 on LEETCODE, AKA ARYAN: https://leetcode.com/akb9911/
