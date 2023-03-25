class ParkingSystem {
public:
    
    int spaces[3];
    int occupied[3];
    
    ParkingSystem(int big, int medium, int small) 
    {
        spaces[0] = big;
        spaces[1] = medium;
        spaces[2] = small;
        for(auto &c : occupied)
        {
            c = 0;
        }
    }
    
    bool addCar(int carType) 
    {
        int index = carType-1;
        if(occupied[index] >= spaces[index])
        {
            return false;
        }
        else
        {
            occupied[index]++;
            return true;
        }
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */