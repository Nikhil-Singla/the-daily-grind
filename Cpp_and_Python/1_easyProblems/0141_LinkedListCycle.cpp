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
        ListNode *slow, *fast;
        slow = fast = head;
        while(fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast)
            {
                return true;
            }
        }
        return false;
    }
};

class Solution {
public:
    bool hasCycle(ListNode *head) 
    {
        set<ListNode*> list_node;
        while(head != NULL)
        {
            if(list_node.find(head) != list_node.end())
            {
                return true;
            }
            list_node.insert(head);
            head = head->next;
        }    
        return false;
    }
};

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