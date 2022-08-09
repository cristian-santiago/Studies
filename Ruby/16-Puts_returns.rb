# What method returns?

def num_list
    # This method don't use return, as it's not necessary on Ruby
    [1,2,3,4]
end

def num_list_2
    # This method is using return, as long this is separating two logics, only will return if x==1
    
    x = 1
    [1,2,3,4]
    return [5,6,7,8] if x == 1
    # This function also works without using return method
    #[5,6,7,8] if x == 1
end

p num_list
p num_list_2