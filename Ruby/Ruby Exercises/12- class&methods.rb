class Pessoa
    attr_writer :nome

    def initialize(nome)
        @nome = nome
    end

    def print_hello
        puts "olá #{@nome}."
    end
end

pss = Pessoa.new("Cristian")
pss.print_hello 
pss.nome = "João"
pss.print_hello