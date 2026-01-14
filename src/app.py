tasks = []
next_id = 1


def criar_tarefa(titulo, prioridade="Média"):
    global next_id
    tarefa = {
        "id": next_id,
        "titulo": titulo,
        "status": "To Do",
        "prioridade": prioridade
    }
    tasks.append(tarefa)
    next_id += 1
    return tarefa


def listar_tarefas():
    return tasks


def atualizar_status(tarefa_id, novo_status):
    for tarefa in tasks:
        if tarefa["id"] == tarefa_id:
            tarefa["status"] = novo_status
            return tarefa
    return None


def atualizar_prioridade(tarefa_id, nova_prioridade):
    for tarefa in tasks:
        if tarefa["id"] == tarefa_id:
            tarefa["prioridade"] = nova_prioridade
            return tarefa
    return None


def remover_tarefa(tarefa_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != tarefa_id]


def resetar_dados():
    global tasks, next_id
    tasks = []
    next_id = 1


if __name__ == "__main__":
    criar_tarefa("Criar repositório no GitHub", "Alta")
    criar_tarefa("Configurar Kanban", "Média")

    atualizar_prioridade(2, "Alta")

    print(listar_tarefas())
