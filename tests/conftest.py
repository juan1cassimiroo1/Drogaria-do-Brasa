import os
import pytest

@pytest.fixture(autouse=True)
def gerenciar_ambiente_testes():
    """
    Injeta chaves fictícias no ambiente antes de rodar os testes.
    Isso impede que o MedicamentoService estoure ValueError no GitHub Actions.
    """
    os.environ["SUPABASE_URL"] = "https://mock-projeto.supabase.co"
    os.environ["SUPABASE_KEY"] = "mock-chave-secreta-para-passar-no-github-actions"