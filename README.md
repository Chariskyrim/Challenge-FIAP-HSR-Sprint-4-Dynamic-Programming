# HealthFlow CRM — Sprint 4: Grafos e Dijkstra

**Challenge FIAP 2025 — Hospital São Rafael**  
Disciplina: Dynamic Programming | Turma: 2ESPR

---

## Sobre o Sprint

O fluxo de captação do CRM do Hospital São Rafael foi modelado como um **grafo direcionado ponderado**. O objetivo é encontrar o caminho mais eficiente, em tempo, para conduzir um lead desde a entrada no sistema até a confirmação como paciente, usando o algoritmo de Dijkstra.

---

## Estrutura do Repositório

```
├── Tarefa2.py   # Sprint 4 — Grafos e Dijkstra
└── README.md
```

---

## Tarefas Implementadas

### Tarefa 1 — Fluxo do CRM como Grafo Direcionado

O processo de captação foi mapeado em 7 etapas:

```
Lead Recebido → Primeiro Contato → Qualificação → Agendamento
             → Consulta → Proposta Comercial → Confirmação
```

Cada etapa é um nó do grafo. As arestas têm pesos representando o tempo médio em horas para avançar de uma etapa à outra. O grafo inclui caminhos alternativos, atalhos com pesos maiores que simulam atendimentos acelerados mas menos estruturados.

| Conexão | Custo |
|---|---|
| Lead Recebido → Primeiro Contato | 1h |
| Primeiro Contato → Qualificação | 2h |
| Qualificação → Agendamento | 3h |
| Agendamento → Consulta | 2h |
| Consulta → Proposta Comercial | 3h |
| Proposta Comercial → Confirmação | 2h |

---

### Tarefa 2 — Algoritmo de Dijkstra

A função `dijkstra()` encontra o menor caminho entre **Lead Recebido** e **Confirmação** usando `heapq` — fila de prioridade nativa do Python.

**Funcionamento:**
1. Inicia em `Lead Recebido` com custo 0
2. A fila de prioridade garante que o nó de menor custo acumulado é sempre processado primeiro: intuição gulosa
3. Para cada nó visitado, calcula e enfileira o custo acumulado até cada vizinho
4. Para ao atingir `Confirmação`

**Resultado:**
```
Lead Recebido → Primeiro Contato → Qualificação → Agendamento
             → Consulta → Proposta Comercial → Confirmação

Custo total: 13 horas
```

---

### Tarefa 3 — Interpretação do Resultado

A função `todos_os_caminhos()` mapeia recursivamente todas as rotas possíveis e as ordena por custo, permitindo comparar o resultado do Dijkstra com as alternativas.

O sistema encontrou **11 caminhos possíveis**. O caminho principal de 13h percorre todas as etapas do processo. Os atalhos disponíveis têm pesos altos que refletem o custo real de pular etapas: leads mal qualificados geram mais cancelamentos, e propostas sem avaliação médica têm menor taxa de conversão.

O Dijkstra descarta essas rotas automaticamente ao acumular os custos a cada passo, nunca explora um caminho caro enquanto existe um mais barato disponível na fila de prioridade.

**Conclusão:** conduzir o lead por todas as etapas do processo com qualidade é mais eficiente no total do que tentar acelerar pulando etapas essenciais.

---

## Como Executar

```bash
python Tarefa2.py
```

Necessário apenas Python 3.x, sem dependências externas.

---

## Conceitos Aplicados

| Conceito | Aplicação |
|---|---|
| Grafo direcionado ponderado | Modelagem do fluxo de captação do CRM |
| Fila de prioridade (heapq) | Núcleo do algoritmo de Dijkstra |
| Intuição gulosa | Sempre processa o menor custo disponível |
| Recursão | Mapeamento de todos os caminhos possíveis |

---

## Integrantes

| Nome | RM |
|---|---|
| Enzo Luciano | — |

---

*Challenge FIAP — Agosto/2025 — Hospital São Rafael*