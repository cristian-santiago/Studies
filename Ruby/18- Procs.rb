# Procs it's similar to lambda, but uses a specific syntax

full_name = Proc.new {|first, last| first + " " + last}

addres = Proc.new {|city, state| "City: "+ city +", State: "+ state}

p full_name["Cristian", "Santiago"]

p full_name.call("Michele", "Carvalho")

p addres["Nova Iguaçu", "Rio de Janeiro"]