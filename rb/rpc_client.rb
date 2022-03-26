require 'xmlrpc/client'
require 'pp'
require './Pessoa.rb'

client = XMLRPC::Client.new('localhost', '/rpc' , 8000)

pessoa = Pessoa.new 'luiz', 23

# result = client.call2 'somar', 3,5
result = client.call2 'adicionaAno', pessoa.to_hash

puts result[1].values[1]
