# 🏥 Cliente 1 — Clínica de Estética

## 📌 Informações Básicas

| Campo | Valor |
|-------|-------|
| **Nome/Empresa** | Clínica de Estética |
| **Responsável** | — |
| **WhatsApp** | — |
| **Instagram** | — |
| **Tipo de Negócio** | Estética |
| **Status** | 🟡 Em implantação |
| **Data de Início** | Junho/2026 |

## 🖥️ Serviços

- [ ] WhatsApp Business (Evolution API) — Instância `clinica`
- [ ] Instagram — Pendente
- [ ] Supabase Database
- [ ] n8n Workflows
- [ ] Google Calendar — Pendente OAuth

## 🔧 Configurações

### WhatsApp
- **Instance ID:** `clinica`
- **API:** `https://workloop-evolution-api.s1cbdj.easypanel.host`
- **Número:** 5511968983322 (Workloop)
- **Webhook:** → n8n (MESSAGES_UPSERT)

### Database
- **Supabase:** Tabelas padrão (8 tabelas)
- **Queries:** Clientes, agendamentos, estoque

### Automações
- **Fluxo principal:** OpenAI/Agente Sofia via n8n
- **Webhook:** Evolution API → n8n → Resposta automática

## 📊 Métricas

*Em fase de implantação — métricas pendentes.*

---

> Documentação inicial — aguardando dados do cliente.
