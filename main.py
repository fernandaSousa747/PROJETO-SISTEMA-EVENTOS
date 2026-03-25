class Evento:
    def __init__(self, id, nome, data, local, descricao, status="Agendado"):
        self.id = id
        self.nome = nome
        self.data = data
        self.local = local
        self.descricao = descricao
        self.status = status

    def __str__(self):
        return f"{self.id} - {self.nome} | {self.data} | {self.local} | {self.status}"


class GerenciadorEventos:
    def __init__(self):
        self.eventos = []
        self.proximo_id = 1  # ID automático

    def cadastrar_evento(self, nome, data, local, descricao, status="Agendado"):
        evento = Evento(self.proximo_id, nome, data, local, descricao, status)
        self.eventos.append(evento)
        self.proximo_id += 1
        return evento

    def listar_eventos(self):
        return self.eventos

    def buscar_evento(self, id):
        for e in self.eventos:
            if e.id == id:
                return e
        return None

    def buscar_por_nome(self, nome):
        return [e for e in self.eventos if nome.lower() in e.nome.lower()]

    def listar_por_status(self, status):
        return [e for e in self.eventos if e.status.lower() == status.lower()]

    def atualizar_evento(self, id, nome, data, local, descricao, status):
        evento = self.buscar_evento(id)
        if evento:
            evento.nome = nome
            evento.data = data
            evento.local = local
            evento.descricao = descricao
            evento.status = status
            return True
        return False

    def remover_evento(self, id):
        self.eventos = [e for e in self.eventos if e.id != id]


# Execução do sistema
if __name__ == "__main__":
    sistema = GerenciadorEventos()

    # Cadastro de eventos
    sistema.cadastrar_evento("Palestra de Tecnologia", "10/04", "UFCA", "Evento sobre inovação")
    sistema.cadastrar_evento("Workshop de Python", "12/04", "Online", "Introdução ao Python", "Finalizado")

    print("Lista de eventos:")
    for e in sistema.listar_eventos():
        print(e)

    print("\nBuscar evento por nome 'Python':")
    resultados = sistema.buscar_por_nome("Python")
    for e in resultados:
        print(e)

    print("\nEventos finalizados:")
    finalizados = sistema.listar_por_status("Finalizado")
    for e in finalizados:
        print(e)

    print("\nAtualizando evento ID 1...")
    sistema.atualizar_evento(1, "Palestra de IA", "15/04", "UFCA", "Evento sobre Inteligência Artificial", "Agendado")

    print("\nRemovendo evento ID 2...")
    sistema.remover_evento(2)

    print("\nLista final de eventos:")
    for e in sistema.listar_eventos():
        print(e)