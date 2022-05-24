require "./15- bank_acc_model"
require "./15- Fee_acc"
acc_person1 = FeeAcc.new("Cristian", 50)
acc_person2 = BankAccount.new('Mario', 200)




puts "Person one account"
p acc_person1.balance
puts "Person two account"
p acc_person2.balance
puts "-"*20


begin
    acc_person1.transfer(acc_person2, 30)
rescue StandardError => msg_error 
    p "Could't transfer: #{msg_error.message}"
    
end


puts "Person one account"
p acc_person1.balance
puts "Person two account"
p acc_person2.balance