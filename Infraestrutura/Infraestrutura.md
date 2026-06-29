# 🖥️ Infraestrutura

## VPS
- **OS:** Linux
- **Gateway:** Hermes Agent via systemd (`hermes-gateway.service`)
- **Tailscale IP:** 100.95.120.79
- **Acesso:** root@VPS

## PC Remoto (Admin)
- **Usuário:** dimmer 2
- **IP Tailscale:** 100.76.8.70
- **SSH:** `sshpass -p 'senha' ssh dimmer 2@100.76.8.70`
- **Cua Driver:** `C:\Users\Dimmer 2\cua-driver\cua-driver.exe`

## Serviços Web
| Serviço | URL |
|---------|-----|
| n8n | n8n.workloop.com.br |
| Evolution API | workloop-evolution-api.s1cbdj.easypanel.host |
| Caddy | :2080/:2443 |

## Credenciais Armazenadas
- **Supabase:** `/root/.env.supabase`
- **Hermes .env:** `/root/.hermes/.env`
- **Clientes:** `/root/clientes/<id>/memoria.json`
