# 📦 Sistema de Controle de Estoque

Sistema simples de controle de estoque via terminal, feito em **Python puro** (sem dependências externas).

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Licença](https://img.shields.io/badge/licença-livre-green)

---

## 📋 Funcionalidades

- ➕ **Adicionar produto** — cadastra um novo produto (nome, preço e quantidade). Se o produto já existir, soma a quantidade ao estoque atual.
- ✏️ **Atualizar produto** — permite atualizar o preço ou a quantidade de um produto já cadastrado.
- 🗑️ **Excluir produto** — remove um produto do estoque.
- 🔍 **Ver estoque** — lista todos os produtos ou busca um produto específico pelo nome.

---

## 🚀 Como executar

```bash
python estoque.py
```

**Requisito:** Python 3

---

## 💻 Exemplo de uso

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

---

## 🗂️ Estrutura

O projeto está em um único arquivo (`estoque.py`), com o estoque armazenado em memória em um dicionário Python (os dados são perdidos ao fechar o programa).

---

## 🔧 Possíveis melhorias futuras

- [ ] Persistência dos dados em arquivo (JSON/CSV) ou banco de dados
- [ ] Validação de valores negativos para preço e quantidade
- [ ] Testes automatizados

---

## 📄 Licença

Projeto livre para estudo e uso pessoal.

---

## 📬 Contato

<p>
  <a href="https://github.com/LuizPauloSoares" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
  <a href="https://linkedin.com/in/luiz-paulo-soares/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  <a href="https://instagram.com/lu1z_st" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"/>
  </a>
</p>

Desenvolvido por **Luiz Paulo Soares** 🚀
