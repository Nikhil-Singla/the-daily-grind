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
        int carry = 0; //Creating carry function
        ListNode answer; //Declaring where our answer would be stored
        ListNode *tmp = &answer; //Temp variable to work on
        while(l1||l2) //While either l1 or l2 is active
        {
            int val = carry + (l1 ? l1->val : 0) + (l2 ? l2->val : 0); //value = carry + if(l1) then l1->val else 0 + if(l2) then l2->val else 0
            carry = val/10; //Carry the tens place
            val = val%10; //Value is just the units place.
            ListNode *after = new ListNode(val); //Declare the next number as the subsequent digit in the linked list
            tmp->next = after; //Join the after variable to the answer linked list
            tmp = tmp->next; //Iterate temp one step down
            (l1 ? l1 = l1->next:0); //If l1 exists, initialize l1 one step down
            (l2 ? l2 = l2->next:0); //If l2 exists, initialize l2 one step down
        }
        if(carry) //If we have a final carry
        {
            tmp->next = new ListNode(carry); //Since no more digits, the carry is the end/start number
        }
        return answer.next; //Answer was the top of the list. The digits started from the "next"
    }
};
