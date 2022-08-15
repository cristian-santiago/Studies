# Comprehensive guide to method arguments


# 1- Basic Argument Syntax

def full_name first_name, last_name
   puts first_name + " " + last_name
end

full_name "Cristian", "Santiago"




# 2- Named Arguments
# Used to avoid mistakes while passing the data into the arguments

def user_address city:, state:, zipcode:
    puts city
    puts state
    puts zipcode

end
# The order from the named arguments doesn't matter, as long as the name from the argument correspond to the data.
# The output order will correspond to the method logic used.
user_address city:"NI", state:"RJ", zipcode:12345
user_address state: "RJ", zipcode: 12345, city: "NI"


# 3- Default Arguments
# Default arguments are used to set a default data value, as in the example below, isn't necessary set "ENG" as language because the default value is "ENG"
# But it can be changed just setting another data into the argument, as shown, the "PT" language overrides the default one.

def movie title:, language: "ENG" # default language set on the language argument.
    puts title
    puts language
end

movie title: "Jurassic Park", language: "PT"