tasks = []
next_id = 1


def criar_tarefa(titulo):
    global next_id
    tarefa = {
        "id": next_id,
        "titulo": titulo,
        "status": "To Do"
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


def remover_tarefa(tarefa_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != tarefa_id]


if __name__ == "__main__":
    criar_tarefa("Criar repositório no GitHub")
    criar_tarefa("Configurar Kanban")

    print(listar_tarefas())
