class Pessoa
    :nome
    :idade

    def initialize nome, idade
        @nome=nome
        @idade=idade
    end 
    
    def somaAno
        @idade.idade += 1
    end 

    def to_hash
        { nome: @nome, idade: @idade }
    end
end
