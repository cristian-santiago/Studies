# Strings in Ruby there are many methods that can be used.
name = "Cristian"
city = "Rio de Janeiro"
stack = "Ruby"
#Heredoc 1
txt = <<-MSG 
   Hi, my name is #{name},
and I live in #{city}.
Currently I'm learning #{stack}.
MSG

puts txt

#Heredoc 2 (usign 'Q' we're signing a variable, or 'q' just for a normal txt)

txt2 = %Q( 
Hi, my name is #{name},
and I live in #{city}.
Currently I'm learning #{stack}.
)

puts txt2

#checking some public methods in strings


txt.public_methods() # show all the methods for the variable used
puts txt.length() # Show the length of the sentence including the spaces.

puts txt.size() # Also show the size of the strings in the sentence.

puts txt.strip().length() #show the length of the sentence excluding the white spaces

strip_txt =  txt.strip()
puts strip_txt

puts txt.upcase() # Convert the whole txt to UPPERCASE

puts txt.downcase() # Convert the whole txt to LOWERCASE

p txt.split # Will return the sentence separately word by word

puts txt[50] # Show the letter on index 50

