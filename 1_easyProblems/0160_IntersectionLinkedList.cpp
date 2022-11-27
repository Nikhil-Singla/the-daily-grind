/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

//Using hashmap and O(n) space with O(m + n) time complexity
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) 
    {
        unordered_map<ListNode*, int> hash_map;
        while(headB != NULL)
        {
            hash_map[headB]++;
            headB = headB->next;
        }
        while(headA != NULL)
        {
            if(hash_map[headA] == 1)
            {
                return headA;
            }
            headA = headA->next;
        }
        
        return NULL;
    }
};

// ACCEPTED BRUTE FORCE APPROACH
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) 
    {
        ListNode* temp;
        while(headA != NULL)
        {
            temp = headB;
            while(temp != NULL)
            {
                if(temp == headA)
                {
                    return temp;
                }
                temp = temp->next;
            }
            headA = headA->next;
        }
        return NULL;
    }
};

//Using solution to find the difference between the lists.
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) 
    {
        int lenA = 0;
        int lenB = 0;
        ListNode* tempA = headA;
        ListNode* tempB = headB;
        while(tempA != NULL)
        {
            lenA++;
            tempA = tempA->next;
        }
        while(tempB != NULL)
        {
            lenB++;
            tempB = tempB->next;
        }
        int diff = abs(lenA - lenB);
        if(lenA > lenB)
        {
            while(diff)
            {
                headA = headA->next;
                diff--;
            }
        }
        else
        {
            while(diff)
            {
                headB = headB->next;
                diff--;
            }
        }
        while(headA != NULL)
        {
            if(headA == headB)
            {
                return headA;
            }
            headA = headA->next;
            headB = headB->next;
        }
        return NULL;
    }
};

