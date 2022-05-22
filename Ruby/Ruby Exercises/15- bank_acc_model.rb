class BankAccount
    def initialize(owner, initial_value)
        @owner = owner
        @value = initial_value
    end

    def balance
        @value
    end


    def transfer(other_acc, val_trans)
    
        if balance >= val_trans
            debt(val_trans)
            other_acc.deposit(val_trans)
            puts "You've transfer #{val_trans}! Check your balance."
        else
            puts "You're trying to transfer $#{val_trans}"
            raise "Couldn't make the transfer. Not enough balance."
            
        end
    
    end

    
    private

    def debt(val_debt)
        @value -= val_debt
    end

    protected 

    def deposit(val_deposit)
        @value += val_deposit
    end



end