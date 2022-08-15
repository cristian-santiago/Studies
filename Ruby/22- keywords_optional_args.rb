# How to work with keywords and optional arguments


def registration email:, password:, **kwargs # kwargs will help to determine optional arguments for the method
    puts "Building an account for: #{email}"

    # First optional argument (role)
    if kwargs[:role]
        puts "Adding the role: #{kwargs[:role]}" 
    end
    # Second optional argument (plan)
    if kwargs[:plan]
        puts "Adding the plan: #{kwargs[:plan]}"
    end
    
end

# to use the optional argument in a method, just call it as shown below.
registration(
    email: "cristian@email.com",
    password: "aswdfasdf",
    #role: "Admin",
    #plan: "Premium"
    )