Sorting Hat - Projeto em Python

Este projeto foi desenvolvido com base na aula de Object-Oriented Programming (OOP) do curso CS50P - Python Introduction da Harvard.
Trata-se de um projeto simples que demonstra como a programação orientada a objetos pode tornar o código mais robusto, organizado e fácil de entender.

Descrição do Projeto

O objetivo do código é simular o Chapéu Seletor (Sorting Hat) de Harry Potter, atribuindo uma casa de Hogwarts (Gryffindor, Hufflepuff, Ravenclaw ou Slytherin) a um usuário de forma aleatória.

Como funciona o código?

O projeto utiliza uma classe chamada Hat, que armazena uma lista de casas de Hogwarts.
A classe utiliza o método de classe (@classmethod) chamado sort, que seleciona uma casa aleatória da lista com a ajuda da biblioteca random.
O usuário é solicitado a inserir seu nome, e o código retorna o nome do usuário junto com a casa à qual ele foi designado.
Detalhes Técnicos

Classe Hat

A classe Hat contém um atributo houses, que é uma lista das quatro casas de Hogwarts.
O método sort é declarado como um @classmethod, o que permite que ele acesse o atributo da classe diretamente usando cls.

Método @classmethod

O @classmethod é usado para criar um método que pertence à classe e não a instâncias dela. Isso significa que você não precisa criar um objeto do tipo Hat para usar o método sort.
O prefixo cls dentro do método representa a própria classe, permitindo o acesso a atributos ou métodos da classe.

Execução do Código

O usuário é solicitado a inserir seu nome:
Insert your name to find out which house is yours:

A função Hat.sort escolhe uma casa de forma aleatória e imprime o resultado:
Harry is in Gryffindor


Conclusão

Apesar de ser um projeto simples, ele demonstra conceitos importantes de POO, como:

- A utilização de classes para encapsular dados e comportamentos.
- A aplicação de métodos de classe para manipular atributos de classe.
