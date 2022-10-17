/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
ListNode* deleteDuplicates(ListNode* head) 
    {
        ListNode* next = head;
        ListNode* ans = head;
        if(head==NULL)
        {
            return head;
        }
        while(next!=NULL)
        {
            if(head->val != next->val)
            {
                head->next = next;
                head = head->next;
            }
            next = next->next;
        }
        head->next = NULL;
        return ans;
    }
};
