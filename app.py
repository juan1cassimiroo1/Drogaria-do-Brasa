import streamlit as st
from src.service import MedicamentoService

service = MedicamentoService()

st.title("💊 Drogaria do Brasa - Painel Web")
st.markdown("Consulte endereços de farmácias parceiras via CEP.")

cep = st.text_input("Digite o CEP para busca:", placeholder="00000-000")

if st.button("Buscar Endereço"):
    if cep:
        with st.spinner("Consultando API..."):
            endereco = service.buscar_cep(cep)
            if endereco:
                st.success(f"📍 {endereco}")
            else:
                st.error("CEP não encontrado.")
    else:
        st.warning("Por favor, digite um CEP.")