# 🧠 Sub-Agente Revisor

> Pattern de Loop Engineering: separar quem faz de quem revisa.
> "The model that wrote the code is way too nice grading its own homework." — Addy Osmani

## Quando usar
- Fluxos n8n, configs, propostas, código crítico

## Como funciona
Executor → faz o trabalho → Revisor → audita

## O que verifica (ordem)
1. 🔴 Segurança — tokens expostos? injeção?
2. 🟡 Correção — lógica certa? edge cases?
3. 🟢 Boas Práticas — padrão do projeto?
4. ⚪ Completude — faltou algo?

## Regras
- 1 erro GRAVE ou 3+ MÉDIOS → volta pro executor
- Só cosmética → aprovado
- Revisor NUNCA reescreve — só aponta problemas
