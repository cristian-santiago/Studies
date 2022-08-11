# Lambda is similar to Procs, we can use the same syntax or a simplest one, more used in Rails projects

full_name = lambda {|first, last| first + " " + last} # This syntax is similar to the Proc

address = ->(city, state) {"City: "+ city + ". State: " + state } # This syntax is

p full_name["Cristian", "Santiago"]

p address.call("Nova Iguaçu", "Rio de Janeiro")