# Sistema de Controle de Estoque

Sistema simples de controle de estoque via terminal, feito em Python puro (sem dependências externas).

## Funcionalidades

- **Adicionar produto** — cadastra um novo produto (nome, preço e quantidade). Se o produto já existir, soma a quantidade ao estoque atual.
- **Atualizar produto** — permite atualizar o preço ou a quantidade de um produto já cadastrado.
- **Excluir produto** — remove um produto do estoque.
- **Ver estoque** — lista todos os produtos ou busca um produto específico pelo nome.

## Como executar

```bash
python estoque.py
```

Requisito: Python 3.

## Exemplo de uso

```
=== MENU ===
[1] Adicionar produto
[2] Atualizar produto
[3] Excluir produto
[4] Ver estoque
[0] Sair
Escolha: 1
Nome do produto: teclado
Preço: 150
Quantidade: 10
Produto teclado cadastrado com sucesso
```

## Estrutura

O projeto está em um único arquivo (`estoque.py`), com o estoque armazenado em memória em um dicionário Python (os dados são perdidos ao fechar o programa).

## Possíveis melhorias futuras

- Persistência dos dados em arquivo (JSON/CSV) ou banco de dados
- Validação de valores negativos para preço e quantidade
- Testes automatizados

## Licença

Projeto livre para estudo e uso pessoal.
