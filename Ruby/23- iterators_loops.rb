# While loops: This loop needs to set a variable as parameter and an iterator inside the block.
'''
i = 0 # variable

while i < 10 # loop syntax
    #block content
    puts "In Looping"  # will print 10 msgs, as the variable starts from 0 and the iterator is +1.
    i += 1 # iterator
end
'''
# Each iterator: This method iterates over an array, inserting the objects inside it to an specifig variable

''' 
fruits = ["banana", "apple", "grape", "mango"] # Array

fruits.each do |f|  # iterator method syntax
   p f              # block content
end

fruits.each {|f| p f} # One line iterator method, used basically with small blocks.'''

 # For loops: This loop iterates over the collection setted on the syntax block.
 # It's better to use when necessary iterate over a  specific range of values.

''' for i in 0..10
    p i
 end'''