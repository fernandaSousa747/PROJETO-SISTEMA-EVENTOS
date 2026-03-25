## PROJETO SISTEMA DE EVENTOS

# Entregável P1

## Estrutura do projeto

O projeto está organizado de forma simples, contendo um arquivo principal responsável pela execução do sistema:

- **main.py**: arquivo principal onde estão implementadas as classes e a lógica do sistema de gerenciamento de eventos.


## Explicação sobre as classes usadas no projeto

O sistema foi desenvolvido utilizando Programação Orientada a Objetos, com duas classes principais:

 1º Evento
Representa um evento dentro do sistema, contendo atributos como id, nome, data, local, descrição e status.  
Essa classe tem como objetivo organizar as informações relacionadas a cada evento cadastrado, permitindo sua identificação e visualização de forma clara.

 2º GerenciadorEventos
Responsável por gerenciar os eventos do sistema.  
Essa classe permite cadastrar, listar, buscar, atualizar e remover eventos.

Além disso, possui funcionalidades extras como busca por nome e filtragem por status, facilitando a organização e o acesso às informações.


## Como as classes principais foram implementadas

As classes principais do sistema foram implementadas com base na modelagem de um sistema de gerenciamento de eventos, utilizando a linguagem de programação Python e os conceitos de Programação Orientada a Objetos (POO).

A classe Evento foi desenvolvida para representar cada evento cadastrado no sistema, contendo atributos como id, nome, data, local, descrição e status. Essa estrutura permite armazenar e organizar as informações essenciais de cada evento.

A classe GerenciadorEventos foi criada para ser responsável pelo gerenciamento geral do sistema. Ela armazena os eventos em uma lista e disponibiliza métodos para realizar operações como cadastro, listagem, busca por ID, atualização e remoção de eventos.

Além disso, foram implementadas funcionalidades adicionais, como busca por nome e listagem por status, tornando o sistema mais completo e funcional.

Durante o desenvolvimento, foi adotada uma abordagem baseada no conceito de Produto Mínimo Viável (MVP), priorizando a implementação das funcionalidades principais exigidas.

Também foi realizada a separação entre a lógica do sistema e a exibição das informações, utilizando métodos que retornam dados e centralizando a saída no bloco principal do programa.

O código-fonte do projeto foi organizado de forma clara e disponibilizado em um repositório no GitHub, facilitando o versionamento, compartilhamento e acesso ao sistema desenvolvido.


## Princípios e práticas de POO utilizadas

O desenvolvimento do projeto foi baseado nos principais conceitos da Programação Orientada a Objetos (POO), buscando organizar o sistema de forma clara, estruturada e de fácil manutenção.

Um dos princípios mais presentes foi o encapsulamento, já que cada classe é responsável por concentrar seus próprios dados e comportamentos. A classe Evento armazena as informações dos eventos, enquanto a classe GerenciadorEventos gerencia as operações realizadas sobre esses dados.

Também foi aplicado o conceito de abstração, ao representar elementos do mundo real, como eventos, de forma simplificada dentro do sistema, sem expor detalhes desnecessários.

Outro ponto importante foi o baixo acoplamento, já que cada classe possui uma responsabilidade bem definida, o que facilita a compreensão do código e futuras modificações.

Além disso, o sistema utiliza o relacionamento entre objetos, onde o gerenciador mantém uma coleção de eventos, permitindo que o sistema funcione de forma integrada e organizada.

Dessa forma, a aplicação dos conceitos de POO permitiu o desenvolvimento de um sistema simples, mas bem estruturado e preparado para possíveis evoluções.

## Possíveis usos da nossa solução

O sistema de gerenciamento de eventos pode ser utilizado por pessoas ou organizações que desejam organizar melhor seus compromissos, atividades e eventos, permitindo um controle mais eficiente das informações cadastradas.

Além do uso individual, a solução pode ser aplicada em contextos educacionais, institucionais ou empresariais, auxiliando no planejamento de palestras, reuniões, workshops e outros tipos de eventos. Nesse cenário, o sistema contribui para a organização, acompanhamento e atualização das atividades.

Em um contexto mais amplo, pequenas empresas, organizadores de eventos ou instituições de ensino podem utilizar uma ferramenta semelhante para gerenciar sua agenda de eventos, melhorar a comunicação e evitar conflitos de datas ou informações.

Esse projeto surge a partir da necessidade de organização e controle de atividades em uma rotina que envolve estudo, trabalho e outras responsabilidades, demonstrando como uma solução simples pode contribuir para melhorar o gerenciamento do tempo e das tarefas do dia a dia.