# Splat arguments allows to insert an ilimited amount of arguments, just using *.
# In the example below, the argument will receive many differents data, all will be stored in yje array customers.
def customer_assignment *customers 
    # As an exemple, to use the method upcase, it's necessary iterate over the array.
    customers.each do |customer|
        puts customer.upcase
    end

    #puts customers
end
customer_assignment("Apple", "Google", "Facebook")