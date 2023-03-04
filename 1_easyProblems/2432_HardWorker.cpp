//Small Improvements in time
class Solution {
public:
    int hardestWorker(int n, vector<vector<int>>& logs) 
    {
        int id_min = 600, time_max = 0, prev_time = 0;
        for(auto const &c : logs)
        {
            if((c[1] - prev_time) > time_max)
            {
                id_min = c[0];
                time_max = c[1] - prev_time;
            }
            else if((c[1] - prev_time) == time_max)
            {
                id_min = min(id_min, c[0]);
            }
            prev_time = c[1];
        }
        return id_min;
    }
};

//Easier to Understand
class Solution {
public:
    int hardestWorker(int n, vector<vector<int>>& logs) 
    {
        int id_min = 600, time_max = 0, prev_time = 0;
        for(auto c : logs)
        {
            int time = c[1];
            int task_time = time - prev_time;
            if(task_time > time_max)
            {
                id_min = c[0];
                time_max = task_time;
            }
            else if(task_time == time_max)
            {
                id_min = min(id_min, c[0]);
            }
            prev_time = time;
        }
        return id_min;
    }
};