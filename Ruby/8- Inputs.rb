# gets() and gets.chomp

# The gets() and gets will rertun \n at the end of the inserted valur
# For better resolution, we use .chomp to remove the last special character

print "Type your name: " # Using print to insert the value beside the input.
name = gets.chomp # Ruby will ask for a value to insert on the 'name' variable

print "How old are you? "
age = gets.chomp.to_i #Ruby will ask for a value to insert on the 'age' variable
# to_i  will convert the variable age in an integer number

print "Where are you from? "
addrs = gets.chomp #Ruby will ask for a value to insert on the 'addrs' variable

# Using heredoc to insert a big msg to display after using puts
txt = <<-MSG
Nice to meet you #{name}.
Good you are #{age} years old.
How's it look like living in #{addrs}?
MSG

puts txt