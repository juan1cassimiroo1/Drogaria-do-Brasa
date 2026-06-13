import streamlit as st
from dotenv import load_dotenv

# Carrega as variáveis do .env imediatamente na inicialização
load_dotenv()

from src.service import MedicamentoService # noqa: E402

# Inicializa o serviço conectado ao Supabase
service = MedicamentoService()

st.set_page_config(page_title="Drogaria do Brasa", page_icon="💊", layout="centered")

st.title("💊 Drogaria do Brasa - Painel Web")
st.markdown("Consulte endereços de farmácias parceiras via CEP e registre medicamentos.")

# Interface de cadastro de Medicamentos
st.subheader("Cadastrar Novo Medicamento")
nome_med = st.text_input("Digite o nome do medicamento:", placeholder="Ex: Dipirona 500mg")
cep_input = st.text_input("Digite o CEP para busca:", placeholder="00000-000", max_chars=8)

if st.button("Buscar Endereço e Cadastrar"):
    if nome_med and cep_input:
        if len(cep_input) == 8 and cep_input.isdigit():
            with st.spinner("Buscando endereço e salvando no banco..."):
                endereco_retornado = service.buscar_cep(cep_input)
                
                if "não encontrado" in endereco_retornado.lower() or "erro" in endereco_retornado.lower():
                    st.error(endereco_retornado)
                else:
                    service.salvar_medicamento(nome=nome_med, cep=cep_input, endereco=endereco_retornado)
                    st.success(f"✅ Sucesso! '{nome_med}' cadastrado para o endereço:")
                    st.info(endereco_retornado)
                    st.rerun() # Atualiza a tela para o novo item aparecer na lista abaixo
        else:
            st.warning("Por favor, digite um CEP válido com 8 dígitos numéricos.")
    else:
        st.warning("Preencha o nome do medicamento e o CEP.")

st.markdown("---")

# Seção para listar e remover o que já foi salvo na nuvem
st.subheader("📦 Medicamentos Registrados no Banco (Nuvem)")

try:
    lista_meds = service.listar_medicamentos()
    if lista_meds:
        for item in lista_meds:
            # Cria duas colunas: uma larga para o texto e uma estreita para o botão de apagar
            col_texto, col_botao = st.columns([0.85, 0.15])
            
            with col_texto:
                st.write(f"🔹 **{item['nome']}** | CEP: {item['cep']} \n\n _{item['endereco']}_")
            
            with col_botao:
                # O botão usa o ID único do registo para saber exatamente quem apagar
                if st.button("🗑️", key=f"del_{item['id']}"):
                    with st.spinner("Removendo..."):
                        service.deletar_medicamento(item['id'])
                        st.success("Removido!")
                        st.rerun() # Recarrega a aplicação para atualizar a lista no ecrã
            st.markdown("---")
    else:
        st.write("Nenhum medicamento encontrado no banco de dados.")
except Exception as e:
    st.error(f"Erro ao ler os dados do Supabase: {e}")