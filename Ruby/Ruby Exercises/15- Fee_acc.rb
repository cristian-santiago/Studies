
class FeeAcc < BankAccount
    FEE = 2 
    def transfer(other_acc, value)
        super
        
        debt(FEE)  
        
    end


end 