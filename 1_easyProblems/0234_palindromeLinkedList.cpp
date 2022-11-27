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

//Use idea's from Reversing List and Pallindrome number
class Solution {
public:
    bool isPalindrome(ListNode* head) 
    {
        ListNode* tempHead = head;
        ListNode* reverse = new ListNode(tempHead->val);
        tempHead = tempHead->next;
        while(tempHead != NULL)
        {
            ListNode* temp = new ListNode(tempHead->val);
            temp->next = reverse;
            reverse = temp;
            tempHead = tempHead->next;
        }

        while(head != NULL)
        {
            if(reverse->val != head->val)
            {
                return false;
            }
            reverse = reverse->next;
            head = head->next;
        }
        return true;
    }
};