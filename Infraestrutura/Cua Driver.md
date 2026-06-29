# 🖥️ Cua Driver — Computer Use

## Visão Geral
Cua Driver v0.6.8 permite controlar o PC Windows remotamente via MCP (33 ferramentas). Comunicação via SSH tunnel + JSON-RPC pipe.

## Inicialização
No PowerShell do PC:
```powershell
& "C:\Users\Dimmer 2\cua-driver\cua-driver.exe" serve
```

## Acesso via Hermes
O MCP **não carrega como tool nativa**. Usar SSH + pipe JSON-RPC:

```bash
echo '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"launch_app","arguments":{"path":"..."}}}' | sshpass -p 'senha' ssh dimmer 2@100.76.8.70 "\"C:\Users\Dimmer 2\cua-driver\cua-driver.exe\" mcp"
```

## Ferramentas Disponíveis (33)
| Categoria | Tools |
|-----------|-------|
| **Apps** | list_apps, launch_app, kill_app |
| **Janelas** | list_windows, get_window_state, bring_to_front, debug_window_info |
| **Mouse** | click, right_click, scroll |
| **Teclado** | type_text, press_key, hotkey, set_value |
| **Tela** | get_screen_size, get_cursor_position, zoom |
| **Cursor IA** | move_cursor, set_agent_cursor_enabled, set_agent_cursor_motion, set_agent_cursor_style, get_agent_cursor_state |
| **Browser** | page (execute_javascript, get_text, query_dom, click_element) |
| **Recording** | start_recording, stop_recording, get_recording_state, replay_trajectory, install_ffmpeg |
| **Sessão** | start_session, end_session |
| **Sistema** | get_config, set_config, health_report, check_permissions, check_for_update, get_accessibility_tree |

## Exemplos de Uso
### Abrir VS Code
```json
{"name":"launch_app","arguments":{"path":"C:\\Program Files\\Microsoft VS Code\\Code.exe","additional_arguments":["C:\\Users\\Dimmer 2\\Desktop\\arquivo.html"]}}
```

### Abrir Edge com URL
```json
{"name":"launch_app","arguments":{"urls":["https://google.com"]}}
```

### Digitar texto
```json
{"name":"type_text","arguments":{"pid":7692,"text":"Hello World"}}
```

## Gateway Restart
Quando precisar reiniciar o gateway (ex: para nova config):
1. `kill -9 <PID do gateway>`
2. systemd reinicia automaticamente
3. ⚠️ A sessão cai — precisa reconectar no Telegram

## Limitações
- MCP não carrega como tool nativa do Hermes (precisa pipe SSH)
- Gateway restart pode resetar config (mcp_servers)
- VS Code não abre via SSH remoto (precisa Cua Driver)
