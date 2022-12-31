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
    bool hasCycle(ListNode *head) 
    {
        unordered_map<ListNode*, bool> hash;
        while(head != NULL)
        {
            if(hash[head])
            {
                return true;
            }
            hash[head] = true;
            head = head->next;
        }    
        return false;
    }
};