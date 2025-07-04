// Optimized 
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) 
    {
        ListNode* dummy = new ListNode;
        dummy -> next = head;
        ListNode* curr = dummy;
        
        while(curr -> next) 
        {
            if(curr -> next -> val == val) 
            {
                curr -> next = curr -> next -> next;
            } 
            else 
            {
                curr = curr -> next;
            }
        }
        
        return dummy -> next;
    }
};

//MEMORY EFFICIENT SOLUTION
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) 
    {
        while(head != NULL && head->val == val)
        {
            head = head->next;
        }
        ListNode *temp = head;

        while(temp != NULL && temp->next != NULL)
        {
            if(temp->next->val == val)
            {
                temp->next = temp->next->next;
            }
            else
            {
                temp = temp->next;
            }
        }

        return head;
    }
};

//INEFFICIENT BRUTE FORCE SOLUTION 
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) 
    {
        while(head != NULL && head->val == val)
        {
            head = head->next;
        }

        ListNode *temp = head;
        while(temp != NULL)
        {
            if(temp->next != NULL && temp->next->val == val)
            {
                ListNode *iterator = temp->next;
                while(iterator != NULL && iterator->val == val)
                {
                    iterator = iterator->next;
                }
                temp->next = iterator;
            }
            temp = temp->next;
        }

        return head;
    }
};