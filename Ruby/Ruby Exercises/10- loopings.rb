
value = 10

while value > 0
    puts "Number #{value}"
    value -= 1
end

list = ["a", "b", "c", "d", "e", "f"]

for i in list
    puts "The letter using for is #{i}"
end

list.each do |letter|
    puts "The letter using each is #{letter}"
end

a = 0
until a == 10
    puts "Value #{a}"
    a += 1
end

# Lace using hashes

h ={

    "name" => "Cristian",
    "age" => 30,
    "nationality" => "Brasileiro",
    "city" => "Nova Iguaçu",
    "phone" => 123456789,
    
}

h.each do |key, value|
    puts "My #{key} is #{value}."
end