/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:

    Node* copyRandomList(Node* head) 
    {
        if(!head)
        {
            return nullptr;
        }

        unordered_map<Node*, Node*> hashMap;

        Node* tempHead = head;
        while(tempHead)
        {
            hashMap[tempHead] = new Node(tempHead->val);
            tempHead = tempHead->next;
        }

        tempHead = head;

        while(tempHead)
        {
            hashMap[tempHead]->next = hashMap[tempHead->next];
            hashMap[tempHead]->random = hashMap[tempHead->random];
            tempHead = tempHead->next;
        }

        return hashMap[head];

    }
};