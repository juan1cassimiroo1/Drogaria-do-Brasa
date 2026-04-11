# Drogaria do Brasa

> Gerenciamento pessoal de estoque de medicamentos.

## O Problema
A interrupção de tratamentos médicos é um problema crítico de saúde pública. Estima-se que uma parcela significativa de pacientes com doenças crônicas (como hipertensão e diabetes) esquece de renovar seu estoque de medicamentos, levando a crises e internações. As rotinas intensas faz com que o controle manual seja falho e ineficiente.

## A Solução
O **Drogaria do Brasa** é uma ferramenta de linha de comando (CLI) desenvolvida para simplificar o monitoramento de medicamentos. Ele oferece uma interface onde o usuário pode cadastrar, listar e remover medicamentos com rigorosa validação de dados. 

Diferente de uma lista comum, o sistema impede erros humanos (como estoques negativos) e garante que as informações persistam de forma segura em um banco de dados estruturado.

## Tecnologias e Boas Práticas

* **Python 3.12.10
* **Pydantic V2**
* **Typer & Rich**
* **Persistência em JSON**
* **Arquitetura em Camadas**

## Qualidade e Automação
* **Testes Automatizados**: Cobertura de casos reais, inválidos e limites usando `Pytest`.
* **Integração Contínua (CI)**: Pipeline automatizada via GitHub Actions que valida cada alteração no código.
* **Linting & Estilo**: Código padronizado de acordo com a PEP 8 através do `Ruff`.

## Como Instalar e Rodar
1. Instale as dependências: `pip install -r requirements.txt`
2. Adicione um medicamento: `python -m src.main add "Metformina" "500mg" 60`
3. Consulte seu estoque: `python -m src.main list`

---
**Desenvolvido por:** Juan Cassimiro 🇧🇷
