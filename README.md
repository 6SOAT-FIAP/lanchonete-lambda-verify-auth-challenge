# Lambda verify auth challenge

Acionador lambda para verificar resposta do desafio de autenticação usando AWS Cognito.

## Objetivo

Há uma lanchonete de bairro que está se expandindo devido ao seu grande sucesso.

Nesse contexto, um sistema de controle de pedidos é essencial para garantir que a lanchonete possa atender os clientes
de maneira eficiente, gerenciando seus pedidos e estoques de forma adequada.

Para solucionar o problema, o projeto visa oferecer à lanchonete um sistema de autoatendimento de fast food que permite
aos clientes selecionar e fazer pedidos sem precisar interagir com um atendente.

A lambda deste repositório compõe o fluxo de cadastro e autenticação do cliente, demonstrado no diagrama abaixo:

<p align = "center">
  <img src = assets/desenho-autenticacao.svg>
</p>