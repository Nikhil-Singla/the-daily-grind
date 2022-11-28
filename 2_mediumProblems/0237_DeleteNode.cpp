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
    void deleteNode(ListNode* node) 
    {
        //We will solve this by bringing the next node to the current node and then deleting the next node.
        ListNode *temp = node->next; //Copy the link of the next node to delete later and free memory
        node->val = node->next->val; //Copy the value of the next node to this node
        node->next = node->next->next; //Overwrite the next node link from this node to the node after
        delete temp; //Free up the memory space
    }
};