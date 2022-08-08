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