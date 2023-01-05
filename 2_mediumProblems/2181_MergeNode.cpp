// Much faster solution
class Solution {
public:
    ListNode* mergeNodes(ListNode* head) 
    {
        head = head->next;
        ListNode *result = head->next;
        ListNode *ret = result;
        uint sum = 0;
        while(head)
        {
            sum += head->val;
            if(head->val == 0)
            {
                if(!head->next)
                {
                    result->val = sum;
                    break;
                }
                result->val = sum;
                result = result->next;
                sum = 0;
            }
            head = head->next;
        }
        result->next = nullptr;
        return ret;
    }
};

// BRUTE FORCE
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