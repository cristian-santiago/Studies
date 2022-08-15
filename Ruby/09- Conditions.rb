# Conditions in Ruby allow execute different kinds of codes depending on the condition method iserted

'''
For better resolution we can use some Operators to help on conditions.
== Equal 
!= Different
>, < , <= , >= 
! Negative
&& And
|| Or
'''

print "Insert a number between 0 and 10: "
value = gets.chomp.to_i

if value > 5 && value <=10
    puts "You typed a number higher than 5."
elsif value < 5 && value >=0  
    puts "You typed a number lower than 5."
elsif value == 5
    puts "You typed the number 5!"
else
    puts "Sorry, you typed #{value}. This number is outside the range I suggested."

end

