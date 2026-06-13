import os
import httpx

class MedicamentoService:
    def __init__(self):
        """
        Inicializa o serviço capturando a URL base e a chave do arquivo .env.
        """
        self.url = os.environ.get("SUPABASE_URL")
        self.key = os.environ.get("SUPABASE_KEY")
        
        if not self.url or not self.key:
            raise ValueError("As variáveis SUPABASE_URL e SUPABASE_KEY não foram configuradas!")
            
        # Garante que a URL não termine com barra para não duplicar rotas nas requisições
        self.url = self.url.rstrip("/")

    def buscar_cep(self, cep: str) -> str:
        """Consome a API do ViaCEP para retornar o endereço formatado."""
        try:
            url_viacep = f"https://viacep.com.br/ws/{cep}/json/"
            resposta = httpx.get(url_viacep)
            if resposta.status_code == 200:
                dados = resposta.json()
                if "erro" not in dados:
                    logradouro = dados.get("logradouro", "")
                    bairro = dados.get("bairro", "")
                    localidade = dados.get("localidade", "")
                    uf = dados.get("uf", "")
                    return f"{logradouro}, {bairro} - {localidade}/{uf}"
            return "CEP não encontrado ou inválido."
        except Exception:
            return "Erro ao conectar ao serviço do ViaCEP."

    def salvar_medicamento(self, nome: str, cep: str, endereco: str):
        """
        Salva o medicamento enviando uma requisição direta para a API do Supabase.
        """
        url_tabela = f"{self.url}/rest/v1/medicamentos"
        
        headers = {
            "apikey": self.key,
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        }
        
        dados_insercao = {
            "nome": nome,
            "cep": cep,
            "endereco": endereco
        }
        
        with httpx.Client() as client:
            resposta = client.post(url_tabela, json=dados_insercao, headers=headers)
            if resposta.status_code not in [200, 201]:
                raise Exception(f"Erro no Supabase: {resposta.status_code} - {resposta.text}")
            return resposta.json()

    def listar_medicamentos(self) -> list:
        """Busca e retorna todos os registros salvos diretamente na API do Supabase."""
        url_tabela = f"{self.url}/rest/v1/medicamentos"
        
        headers = {
            "apikey": self.key,
            "Authorization": f"Bearer {self.key}"
        }
        
        with httpx.Client() as client:
            resposta = client.get(url_tabela, headers=headers)
            if resposta.status_code == 200:
                return resposta.json()
            return []

    def deletar_medicamento(self, id_medicamento: int):
        """
        Remove um medicamento do banco de dados na nuvem usando o ID único dele.
        """
        # Filtra a rota direto no parâmetro da URL usando a sintaxe do PostgREST (id=eq.X)
        url_deletar = f"{self.url}/rest/v1/medicamentos?id=eq.{id_medicamento}"
        
        headers = {
            "apikey": self.key,
            "Authorization": f"Bearer {self.key}"
        }
        
        with httpx.Client() as client:
            resposta = client.delete(url_deletar, headers=headers)
            if resposta.status_code not in [200, 204]:
                raise Exception(f"Erro ao deletar no Supabase: {resposta.status_code} - {resposta.text}")
            return True