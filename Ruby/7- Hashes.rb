# hashes são estruturas que contem chaves e valores inseridos dentro de chaves {}

# Método normal de utilizar um hash
hash = {

    "name" => "Cristian",
    "age" => 30,
    "nationality" => "Brasileiro",
    "city" => "Nova Iguaçu",
    "phone" => 123456789,
}

p hash

# Método eficiente para usar hashes combinado com simbolos (:) -> This way seems JSON structure
good_hash = {

    name: "Juan",
    age: 25,
    nationality: 'Spanish',
    city: 'Madrid',
    phone: 987654321,
}

p good_hash

p good_hash[:name] # Will call the name value from the hash

good_hash[:name] = 'Arthur' # Will update the name on that hash

p good_hash

# USefull methods

p good_hash.keys # Will take all the keys from a hash
p good_hash.values # Will take all the values
p good_hash.empty? # Will print if the hash is empty or not (Boolean)