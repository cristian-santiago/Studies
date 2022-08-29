db.pokemon.find(
{
    $or:
    [
        {
            "Defense":
            {
                $gte:60,
                $gte:80,
            },
            
        },
        {
            "Defense":100
        },        
    ],
},
{_id:0, "Name":1, "Defense":1});


db.pokemon.find({$or:[{"Attack":{$gte:100}},{"Speed":{$gte:100}},],},{_id:0, "Name":1, "Attack":1, "Speed":1})


db.pokemon.find(
{
    $or:
    [
        {
            "Attaack":
            {
                $gte:100
            },
            "Speed":
            {
                $gte:100
            }
            
        },
        {
            "Defense":
            {
                $gte:100
            },
            "HP":
            {
                $gte:100
            },
        }        
    ],
})

-- This query below will set another field called StartsWithO inside the first document that matches with the name O.
db.pokemon.updateOne({"name": /^O/},{$set:{"StartsWithO": true}})

db.pokemon.updateMany({"name": /^O/},{$set:{"StartsWithO": true}})

-- Updates - 90. Removing fields with $unset

db.pokemon.updateOne({"name": /^O/},{$unset:{"StartsWithO": true}})

db.pokemon.updateMany({"name": /^O/},{$unset:{"StartsWithO": true}})

-- Increment with $inc and $mul


db.pokemon.updateMany({"types" : "Fire"}, {$inc : {"attack": 10 }}) -- Increment 10 points on every Fire Pokemon atk (- to decrease)


db.pokemon.updateMany({"types" : "Fire"}, {$mul : {"attack" : 3 }}) -- Multiply every Fire Pokemon atk for 3 ( to divide use )

-- Limits with $min and $max

-- Set the Pokemon with atk over 150pts with min value of 150pts ()
db.pokemon.updateMany({"types" "Fire", {$min : {"attack":150}}})

-- Set all the Pokemons with atk below 75 with the max value of 75
db.pokemon.updateMany({}, {$max : {"attack": 75}})
