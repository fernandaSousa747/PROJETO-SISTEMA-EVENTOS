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

# Projeto físico do banco de dados

O banco de dados do sistema foi projetado de forma simples e eficiente, contendo uma tabela principal chamada "eventos", responsável por armazenar as informações dos eventos cadastrados.

A tabela possui os seguintes campos:

- id: identificador único do evento, definido como chave primária e com incremento automático.
- nome: armazena o nome do evento, sendo um campo obrigatório.
- data: representa a data do evento, utilizando o tipo DATE.
- local: indica onde o evento será realizado, também sendo obrigatório.
- descricao: campo opcional utilizado para detalhar o evento.
- status: indica a situação do evento, com valor padrão "Agendado".

Foram aplicadas restrições de integridade, como o uso de NOT NULL em campos essenciais e uma restrição CHECK para limitar os valores possíveis do status, garantindo maior consistência dos dados.

Essas decisões foram tomadas para garantir que a integridade, organização e confiabilidade das informações armazenadas no sistema.

## Wireframe e Sitemap

O wireframe do sistema foi desenvolvido com o objetivo de representar, de forma simples e direta, as principais telas e o fluxo de navegação do sistema de gerenciamento de eventos. Seguindo a proposta da atividade, foi optado por um modelo de baixa fidelidade (low-fidelity), priorizando a estrutura, organização das informações e usabilidade, sem foco em aspectos visuais ou estéticos.

As telas foram projetadas para ambiente desktop, inicialmente, considerando uma navegação clara e objetiva entre as funcionalidades principais do sistema.

### Telas desenvolvidas

O sistema possui quatro telas principais:

1. Tela Inicial
A tela inicial apresenta as opções principais do sistema, permitindo ao usuário escolher entre visualizar os eventos cadastrados ou cadastrar um novo evento e também saiba mais sobre as possibilidades de uso do sistema. Essa tela funciona como ponto de entrada do sistema.

2. Tela de Listagem de Eventos
Exibe os eventos cadastrados em formato de lista, contendo informações como nome, data, local e status. Também disponibiliza ações como editar e remover eventos, além da opção de cadastrar um novo evento.

3. Tela de Cadastro de Evento
Permite ao usuário inserir as informações de um novo evento, como nome, data, local, descrição e status. Após o preenchimento, o usuário pode salvar ou cancelar a operação.

4. Tela de Edição de Evento
Apresenta os dados de um evento já cadastrado, permitindo sua atualização ou exclusão. Essa tela facilita a manutenção das informações no sistema.

### Fluxo de navegação (Sitemap)

O fluxo do sistema foi pensado de forma simples e funcional, garantindo uma navegação intuitiva entre as telas:

- A partir da tela inicial, o usuário pode acessar a listagem de eventos ou o cadastro de um novo evento;
- Na tela de listagem, é possível editar, remover ou cadastrar novos eventos;
- As telas de cadastro e edição retornam à listagem após a realização das ações.

Esse fluxo garante que o usuário consiga realizar todas as operações principais do sistema de forma rápida e organizada.

### Usabilidade, consistência e acessibilidade

O wireframe foi desenvolvido com foco na clareza e facilidade de uso, utilizando uma estrutura simples e padronizada entre as telas. Os elementos foram organizados de forma consistente, mantendo a mesma lógica de navegação em todo o sistema.

A simplicidade do layout contribui para uma melhor compreensão das funcionalidades, tornando o sistema mais acessível, mesmo para usuários com pouca experiência.

### Observação

O wireframe completo do sistema está disponível no repositório no arquivo:

- wireframe e sitemap.pdf