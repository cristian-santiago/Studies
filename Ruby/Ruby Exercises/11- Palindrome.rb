# This method will show if the word or sentence is a palindrome one

def palindrome_word(word)
    rev = word.reverse.delete(' ').downcase #Reverse the sentence, deleting all whitespace and converting into lowcase
    if rev == word.delete(' ').downcase #Also deleting the whitespace and converting into lowcase
        puts "This word/sentence is palindrome!"
    else
        puts "It's not a palindrome!"
    end    
end

print "Type a Palindrome word or sentence: "
txt = gets.chomp
palindrome_word(txt)

