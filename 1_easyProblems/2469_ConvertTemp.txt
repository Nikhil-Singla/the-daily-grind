class Solution {
public:
    vector<double> convertTemperature(double C) 
    {
        return {C + 273.15, C*1.80 + 32.00};
    }
};

class Solution {
public:
    vector<double> convertTemperature(double C) 
    {
        double F = 0.0, K = 0.0;
        K = C + 273.15;
        F = C*1.80 + 32.00;
        return {K, F};
    }
};