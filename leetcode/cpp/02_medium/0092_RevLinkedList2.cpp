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

    ListNode* reverseBetween(ListNode* head, int l, int right)
    {
        if(!head || l == right)
        {return head;}

        ListNode* newNode = new ListNode(0);
        newNode->next = head;
        ListNode* left = newNode;

        for(int i = 0; i < l - 1; i++)
        {left = left->next;}

        ListNode* iterator = left->next;

        for(int i = 0; i < right-l; i++)
        {
            ListNode* temp = iterator->next;
            iterator->next = temp->next;
            temp->next = left->next;
            left->next = temp;
        }

        return newNode->next;

    }
};