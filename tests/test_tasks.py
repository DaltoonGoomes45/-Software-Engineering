import sys
import os

# Permite importar o app.py da pasta src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from app import (
    criar_tarefa,
    listar_tarefas,
    atualizar_status,
    atualizar_prioridade,
    remover_tarefa,
    resetar_dados
)


def setup_function():
    """Executa antes de cada teste"""
    resetar_dados()


def test_criar_tarefa():
    tarefa = criar_tarefa("Testar criação")

    assert tarefa["id"] == 1
    assert tarefa["titulo"] == "Testar criação"
    assert tarefa["status"] == "To Do"


def test_listar_tarefas():
    criar_tarefa("Tarefa 1")
    criar_tarefa("Tarefa 2")

    tarefas = listar_tarefas()

    assert len(tarefas) == 2
    assert tarefas[0]["titulo"] == "Tarefa 1"
    assert tarefas[1]["titulo"] == "Tarefa 2"


def test_atualizar_status():
    criar_tarefa("Tarefa para atualizar")

    tarefa_atualizada = atualizar_status(1, "Done")

    assert tarefa_atualizada is not None
    assert tarefa_atualizada["status"] == "Done"


def test_remover_tarefa():
    criar_tarefa("Tarefa para remover")
    remover_tarefa(1)

    tarefas = listar_tarefas()
    assert len(tarefas) == 0

def test_criar_tarefa_com_prioridade():
    tarefa = criar_tarefa("Tarefa com prioridade", "Alta")
    assert tarefa["prioridade"] == "Alta"


def test_atualizar_prioridade():
    tarefa = criar_tarefa("Outra tarefa", "Baixa")
    tarefa_atualizada = atualizar_prioridade(tarefa["id"], "Média")
    assert tarefa_atualizada["prioridade"] == "Média"
