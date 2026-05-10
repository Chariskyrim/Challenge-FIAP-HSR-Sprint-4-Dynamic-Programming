# HealthFlow CRM — Hospital São Rafael
# Sprint 4 — Grafos e Dijkstra | Dynamic Programming

import heapq
import os
os.system('cls')

# ============================================================
# TAREFA 1 — Fluxo do CRM como Grafo Direcionado
# ============================================================
# Nós    = etapas do processo de captação do HSR
# Arestas = transições entre etapas
# Pesos  = tempo médio em horas para avançar de uma etapa à outra
#
# Caminhos alternativos representam situações reais:
#   - Atalhos: atendimento acelerado, mas menos estruturado (custo alto)
#   - Caminho principal: todas as etapas, qualidade máxima (custo total menor)

grafo_crm = {
    "Lead Recebido": [
        ("Primeiro Contato", 1),     # operador entra em contato rapidamente
        ("Qualificação", 5),         # atalho: pula contato, menos personalizado
    ],
    "Primeiro Contato": [
        ("Qualificação", 2),         # coleta informações e avalia o lead
        ("Agendamento", 9),          # atalho direto, pula qualificação
    ],
    "Qualificação": [
        ("Agendamento", 3),          # lead qualificado, agenda consulta
        ("Proposta Comercial", 8),   # atalho: pula consulta, mais arriscado
    ],
    "Agendamento": [
        ("Consulta", 2),             # paciente comparece à consulta
        ("Confirmação", 14),         # atalho extremo, custo muito alto
    ],
    "Consulta": [
        ("Proposta Comercial", 3),   # médico avalia e gera proposta
        ("Confirmação", 7),          # atalho: fecha sem proposta formal
    ],
    "Proposta Comercial": [
        ("Confirmação", 2),          # paciente aceita e confirma
    ],
    "Confirmação": []
}


def exibir_grafo(grafo):
    print("  Etapas e conexões do fluxo CRM:\n")
    for no, vizinhos in grafo.items():
        if vizinhos:
            for vizinho, custo in vizinhos:
                print(f"    {no} --({custo}h)--> {vizinho}")
    print()


print("=" * 65)
print("TAREFA 1 — Fluxo do CRM como Grafo Direcionado")
print("=" * 65)
exibir_grafo(grafo_crm)


# ============================================================
# TAREFA 2 — Algoritmo de Dijkstra
# ============================================================
# Encontra o menor caminho (em horas) entre Lead Recebido
# e Confirmação usando fila de prioridade.
#
# A fila garante que o nó de menor custo acumulado é sempre
# processado primeiro -> intuição gulosa do algoritmo.

def dijkstra(grafo, inicio, destino):
    # Fila: (custo_acumulado, nó_atual, caminho_percorrido)
    fila = [(0, inicio, [inicio])]

    # Menor custo já confirmado para cada nó visitado
    visitados = {}

    while fila:
        # Retira sempre o nó de menor custo da fila
        custo_atual, no_atual, caminho = heapq.heappop(fila)

        # Nó já processado com custo menor anteriormente -> ignora
        if no_atual in visitados:
            continue

        visitados[no_atual] = custo_atual

        # Destino atingido -> retorna resultado
        if no_atual == destino:
            return custo_atual, caminho

        # Explora vizinhos e calcula custo acumulado
        for vizinho, peso in grafo.get(no_atual, []):
            if vizinho not in visitados:
                heapq.heappush(fila, (
                    custo_atual + peso,
                    vizinho,
                    caminho + [vizinho]
                ))

    return float('inf'), []


print("=" * 65)
print("TAREFA 2 — Dijkstra: Menor Caminho Lead → Confirmação")
print("=" * 65)

custo, caminho = dijkstra(grafo_crm, "Lead Recebido", "Confirmação")

print("  Caminho encontrado:\n")
for i, etapa in enumerate(caminho):
    if i < len(caminho) - 1:
        print(f"    {i+1}. {etapa} →")
    else:
        print(f"    {i+1}. {etapa} ✓")

print(f"\n  Custo total: {custo} horas")
print()


# ============================================================
# TAREFA 3 — Interpretação e Comparação de Caminhos
# ============================================================
# Mapeia todos os caminhos possíveis recursivamente e compara
# com o resultado do Dijkstra para justificar a escolha.

def todos_os_caminhos(grafo, atual, destino, caminho_atual=None, custo_atual=0):
    if caminho_atual is None:
        caminho_atual = [atual]

    if atual == destino:
        return [(custo_atual, list(caminho_atual))]

    resultado = []
    for vizinho, peso in grafo.get(atual, []):
        if vizinho not in caminho_atual:  # evita ciclos
            caminho_atual.append(vizinho)
            sub = todos_os_caminhos(grafo, vizinho, destino, caminho_atual, custo_atual + peso)
            resultado.extend(sub)
            caminho_atual.pop()

    return resultado


print("=" * 65)
print("TAREFA 3 — Interpretação e Comparação de Caminhos")
print("=" * 65)

caminhos = todos_os_caminhos(grafo_crm, "Lead Recebido", "Confirmação")
caminhos.sort(key=lambda x: x[0])

print(f"  Total de caminhos possíveis encontrados: {len(caminhos)}\n")
print("  Ranking do mais eficiente ao menos eficiente:\n")

for i, (c, cam) in enumerate(caminhos):
    if i == 0:
        print(f"  ★ MELHOR  [{c}h]")
        print(f"    " + " → ".join(cam))
    else:
        print(f"      #{i+1}    [{c}h]  " + " → ".join(cam))

print()
print("  ─" * 32)
print()
print("  Por que esse é o caminho mais eficiente?")
print()
print(f"  O caminho ótimo percorre {len(caminho)} etapas em {custo} horas.")
print("  Os atalhos disponíveis parecem mais rápidos individualmente,")
print("  mas têm pesos altos que refletem o custo real de pular etapas:")
print("  retrabalho, leads mal qualificados e maior taxa de cancelamento.")
print()
print("  O Dijkstra descarta essas rotas automaticamente ao acumular")
print("  os custos a cada passo — nunca explora um caminho caro enquanto")
print("  existe um mais barato disponível na fila de prioridade.")
print()
print("  Conclusão: no CRM do HSR, conduzir o lead por todas as etapas")
print("  do processo é mais eficiente no total do que tentar acelerar")
print("  pulando etapas essenciais de qualificação e consulta.")