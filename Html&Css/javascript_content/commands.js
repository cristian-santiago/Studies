// Variables

var nome  = "Cristian Santiago da Silva";
var idade = 30;
var city = "Nova Iguaçu";

console.log(nome); // add the name on the console log on browser
console.log(nome.replace("da Silva", "Carvalho")); // changes the strings from var name to another one
console.log(nome.toUpperCase());
console.log(nome.toLowerCase());

// Array

var listFruit = ["apple", "grape", "orange"];

listFruit.push("banana"); // This method will add 'banana' at the end of the list;

listFruit.pop(); // This method will delete the last element of the list ('banana');

listFruit.length(); // This method shows the length of the list;

listFruit.reverse(); // This method makes the list reverse, changing the position of each element;

listFruit.toString(); // This method make the output from the list became string

listFruit.join(" - "); // This method also make the output as string, but also add " - " between each element from the list

// Dictionary

var dictFruit = {name: "aple", color:"red"}; // Dictionaries keep the patern of "key and value" style

// List & Dictionary

var dictListFruit = [
    {name: "apple", color: "red"},
    {name: "grape", color: "purple"},
    {name: "orange", color: "orange"}
];