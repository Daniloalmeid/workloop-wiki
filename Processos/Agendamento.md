# 📅 Fluxo de Agendamento

## Responsabilidades
| Quem | O que faz |
|---|---|
| **n8n** | Conversa com paciente, consulta Google Calendar, agenda |
| **Hermes** | Só consulta depois (não participa ao vivo) |

## Como funciona
1. Paciente envia mensagem sobre agendamento
2. n8n detecta intenção → assume conversa
3. n8n pergunta: procedimento, dia, horário
4. n8n consulta Google Calendar → oferece opções
5. Paciente confirma
6. n8n salva no Google Calendar + Supabase
7. n8n notifica Hermes

## Lembretes
- Automáticos 24h antes
- n8n dispara, Hermes personaliza a mensagem
