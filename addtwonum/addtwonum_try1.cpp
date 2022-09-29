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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode head;
        ListNode *tmp = &head;
        while(l1||l2)
        {
            int val = carry + (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
            carry = val/10;
            val = val%10;
            ListNode *after = new ListNode(val);
            tmp->next = after;
            tmp = tmp->next;
            (l1 ? l1 = l1->next:0);
            (l2 ? l2 = l2->next:0);
        }
        if(carry)
        {
            tmp->next = new ListNode(carry);
        }
        return head.next;
    }
};
