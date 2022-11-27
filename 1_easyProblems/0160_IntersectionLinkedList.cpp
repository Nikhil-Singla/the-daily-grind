/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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