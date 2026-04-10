import json
import os
from typing import List
from .models import Medicamento

class MedicamentoService:
    def __init__(self):
        self.file_path = "database.json"
        self.db: List[Medicamento] = self._carregar_dados()

    def _carregar_dados(self) -> List[Medicamento]:
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r") as f:
            dados = json.load(f)
            return [Medicamento(**item) for item in dados]

    def _salvar_dados(self):
        with open(self.file_path, "w") as f:
            # Convertemos UUID para string para o JSON aceitar
            json.dump([json.loads(m.json()) for m in self.db], f, indent=4)

    def adicionar(self, med: Medicamento) -> Medicamento:
        self.db.append(med)
        self._salvar_dados()
        return med

    def listar(self) -> List[Medicamento]:
        self.db = self._carregar_dados() # Atualiza antes de listar
        return self.db

    def remover(self, nome: str) -> bool:
        tamanho_inicial = len(self.db)
        self.db = [m for m in self.db if m.nome.lower() != nome.lower()]
        if len(self.db) < tamanho_inicial:
            self._salvar_dados()
            return True
        return False