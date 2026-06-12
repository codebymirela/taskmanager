class Tarefa:
    """Representa uma tarefa do gerenciador."""

    PRIORIDADES_VALIDAS = ["baixa", "média", "alta"]

    def __init__(self, titulo, prioridade="média", categoria="geral", concluida=False):
        titulo = titulo.strip()

        if not titulo:
            raise ValueError("O título da tarefa não pode ficar vazio.")

        prioridade = prioridade.strip().lower()
        categoria = categoria.strip().lower()

        if prioridade not in self.PRIORIDADES_VALIDAS:
            prioridade = "média"

        if not categoria:
            categoria = "geral"

        self.titulo = titulo
        self.prioridade = prioridade
        self.categoria = categoria
        self.concluida = concluida

    def marcar_como_concluida(self):
        self.concluida = True

    def transformar_em_dicionario(self):
        return {
            "titulo": self.titulo,
            "prioridade": self.prioridade,
            "categoria": self.categoria,
            "concluida": self.concluida
        }

    @classmethod
    def criar_de_dicionario(cls, dados):
        return cls(
            titulo=dados["titulo"],
            prioridade=dados.get("prioridade", "média"),
            categoria=dados.get("categoria", "geral"),
            concluida=dados.get("concluida", False)
        )