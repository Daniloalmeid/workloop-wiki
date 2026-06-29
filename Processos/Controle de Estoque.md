# 📦 Controle de Estoque

## Entrada
- Cliente informa no WhatsApp
- Hermes registra no Supabase
- local no computador do cliente

## Saída
- Automática: quando procedimento é confirmado
- Manual: "saíram 2 frascos de X"

## Alertas
- Estoque mínimo → Hermes avisa no WhatsApp
- Reposição sugerida automaticamente

## Tabela no Supabase
```sql
CREATE TABLE insumos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(200) UNIQUE,
    quantidade_atual INTEGER DEFAULT 0,
    quantidade_minima INTEGER DEFAULT 5,
    unidade VARCHAR(50)
);
```
