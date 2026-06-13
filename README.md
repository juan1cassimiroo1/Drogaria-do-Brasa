# 💊 Drogaria do Brasa (v2.0.0)

Sistema web para gerenciamento de estoque de medicamentos e consulta de farmácias parceiras integrada à nuvem.

## 📌 O Problema
A interrupção de tratamentos médicos é um problema crítico de saúde pública. Estima-se que uma parcela significativa de pacientes com doenças crônicas (como hipertensão e diabetes) esqueça de renovar seu estoque de medicamentos, levando a crises e internações. As rotinas intensas fazem com que o controle manual seja falho e ineficiente.

## 💡 A Solução
O **Drogaria do Brasa** evoluiu de uma ferramenta de linha de comando para uma **Aplicação Web interativa**. O painel permite que o usuário consulte endereços de farmácias parceiras automaticamente via CEP (consumindo a API do ViaCEP) e registre os medicamentos diretamente em um banco de dados relacional na nuvem. 

O sistema impede erros humanos, garante validação rigorosa de dados e centraliza as informações de forma segura e persistente.

---

## 🛠️ Tecnologias e Boas Práticas
* **Python 3.12**
* **Streamlit** (Interface Web amigável e reativa)
* **Supabase / PostgreSQL** (Persistência de dados em nuvem em tempo real)
* **HTTPX** (Consumo assíncrono da API externa ViaCEP)
* **Arquitetura em Camadas** (Separação clara entre a interface de visualização e a lógica de serviços/banco)

---

## 🚀 Qualidade e Automação
* **Testes Automatizados:** Cobertura de casos lógicos e limites utilizando o framework `Pytest`.
* **Integração Contínua (CI):** Pipeline automatizada via `GitHub Actions` que executa os testes a cada Pull Request ou Push, garantindo a estabilidade do código.
* **Linting & Estilo:** Código rigorosamente padronizado de acordo com a PEP 8 através do `Ruff`.

---

## 💻 Como Instalar e Rodar

Siga os passos abaixo para configurar e executar o projeto localmente:

### 1. Instale as dependências
Certifique-se de ter o Python instalado e execute no terminal:
```bash
pip install -r requirements.txt

### 2. Configure as Variaveis de Ambiente
SUPABASE_URL="[https://seu-projeto.supabase.co](https://seu-projeto.supabase.co)"
SUPABASE_KEY="sua-chave-anon-public-key"

### 3. Execute o comando do Streamlit
Bash : streamlit run app.py

## 🌍 Entrega Intermediária - Links Rápidos
* **Aplicação Online:** [AQUI](https://drogaria-do-brasa-7jrapicmsnawq8nabtx47k.streamlit.app)

---
**Desenvolvido por:** Juan Cassimiro
