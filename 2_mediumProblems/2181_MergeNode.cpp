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
    ListNode* mergeNodes(ListNode* head) 
    {
        head = head->next;
        ListNode *result;
        result = new ListNode(0);
        ListNode *refer = result;
        uint sum = 0;
        while(head)
        {
            sum += head->val;
            if(head->val == 0)
            {
                ListNode *temp;
                temp = new ListNode(sum);
                refer->next = temp;
                refer = refer->next;
                sum = 0;
            }
            head = head->next;
        }
        return result->next;
    }
};