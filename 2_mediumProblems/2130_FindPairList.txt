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

    int count=0;
    ListNode* middleNode(ListNode* head) 
    {
        for(ListNode *temp=head; temp->next!=nullptr; temp=temp->next)
        {
            count++;
        }
        count++;
        count /= 2;
        int rando = count;
        while(rando>0)
        {
            rando--;
            head = head->next;
        }
        return head;
    }
    int pairSum(ListNode* head) 
    {
        int ans = 0;
        ListNode* temp = head;
        temp = middleNode(temp);
        vector<int> big(count, 0);
        for(int i = 0, rando = count-1; i < count; i++, rando--)
        {
            big[i] += temp->val;
            big[rando] += head->val;
            temp = temp->next;
            head = head->next;
        }
        for(auto n : big) 
        {
            if(big[0] < n) big[0] = n;
        }
        return big[0];
    }
};