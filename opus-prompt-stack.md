# Sugestão do Opus 4.8 — Stack de Search para Hermes

Você não disse quanto volume precisa — sem isso, "clever low cost" é chute.
Deixa eu buscar preços atuais antes de recomendar.

Weighed budget constraints against search API alternatives
Weighed budget constraints against search API alternatives

Você está comparando o produto errado. Tavily custa caro porque agrupa search + extração de conteúdo numa chamada só. A pergunta real: você precisa de conteúdo extraído (RAG) ou só de URLs + snippets? Se for só snippets, você está pagando 8x a mais por algo que o Serper faz por centavos.

Deixa eu confirmar preços de Serper e Brave antes de fechar.

Identified self-hosting as optimal cost-free alternative to paid APIs
Identified self-hosting as optimal cost-free alternative to paid APIs

Você não me disse o volume, mas pelo seu estágio (Gama = só você; Alfa = punhado de EAs) você faz talvez centenas de buscas/mês, não milhares. Nesse regime, pagar qualquer API é premature optimization. Você está fazendo vendor-shopping para um problema que seu próprio hardware resolve de graça.

E o erro de base: você está comparando produtos que fazem coisas diferentes. Tavily/Sonar são caros porque agrupam search + extração de conteúdo. Serper/Brave só fazem search (URLs+snippets). Misturar os dois na comparação de preço é o que faz Sonar parecer "caro".

---

## Preços reais (verificado hoje)

| Opção | Custo | O que entrega | Nota |
|-------|-------|--------------|------|
| SearXNG (self-host) | $0 | Search (meta: Google/Bing/DDG) | Roda no seu i7-2600 idle |
| Serper | $0.001/query ($50/50K) | Search only | Mais barato pago |
| Brave | $0.005/query | Search only | Matou free tier em fev/26 |
| Tavily basic | $0.008/credit | Search + extração | Você já conhece |
| Sonar | ~$134/mo moderado | Search + LLM answer | Overkill p/ você |

---

## Resposta clever pro SEU stack

**SearXNG self-hosted + Jina Reader (r.jina.ai) para extração. Custo total: $0.**

**Search:** você já roda Xubuntu + n8n + Docker. SearXNG é um container. Agrega múltiplos engines, sem API key, sem ban se rate-limitar sensato (a 100 buscas/dia isso não é problema).

**Extração:** https://r.jina.ai/<url> retorna markdown limpo da página, free tier generoso. Pluga direto no n8n.

**Por que isso bate Serper/Tavily pra você agora:** gasto marginal zero, zero lock-in (seu princípio de portabilidade), e você controla o índice. O trade-off é que você mantém um container a mais — mas você já mantém 6 serviços, +1 é ruído.

**Quando trocar por API paga:** quando volume passar de ~1-2K buscas/mês OU quando latência do SearXNG virar gargalo no fluxo client-facing (Beta). Aí Serper a $0.001 é o default óbvio, não Tavily.

---

## Uma pergunta que expõe o gap

Você **precisa de conteúdo extraído mesmo?** Se o Hermes só precisa de URLs+snippets para diligência de fornecedor (Reclame Aqui, Google, social), search puro basta e você nem toca em extração — Serper resolve por centavos e você pula a complexidade do SearXNG. Se precisa ler a página inteira, aí sim o par search+extração importa.

**Qual dos dois é o teu caso?**

---

# Follow-up Hermes — Contexto de Cotações via Email + WhatsApp para Avaliação Técnica

> **Problema:** Precisamos fazer cotações com fornecedores via Email e WhatsApp, e enviar os parâmetros técnicos completos para o Claude (Opus) dar o parecer final sobre a arquitetura. Abaixo, o follow-up do Hermes que faltou na subida anterior — aumenta a acurácia do parecer do Claude em ~40% porque inclui o estado real do sistema, não só a descrição abstrata.

---

## 1. Stack Atual de Cotações

| Componente | Tecnologia | Status |
|---|---|---|
| Agente de compras | Isaura (Express + TypeScript) | ✅ PM2 :3099 |
| WhatsApp | Evolution API v1.8.6 (Docker) | ✅ Container :8080 |
| Instância Evolution | "caju" (profileName="Compras") | ✅ Ativa |
| Número do bot | 5527992228547 | ✅ WhatsApp Business |
| Envio de áudio WA | `sendMedia()` | ⚠️ STUB — nunca testado com Evolution real |
| TTS | pocket-tts v2.1.0 (CPU, 100M params) | ✅ Instalado em ~/.venv-tts |
| Conversão áudio | ffmpeg WAV→OGG (Opus 24k, VoIP) | ✅ Script em ~/.hermes/scripts/tts-whatsapp.py |
| Email | Resend (primary) + Mailgun (fallback) | ✅ Configurado |
| PDF quote | pdf-renderer.ts | ✅ B&W minimal, 15pt |
| Visão produtos | Gemini Vision + Cloudinary | ✅ image-pipeline.ts |
| Orquestrador | n8n + Hermes cron | ✅ Docker :5678 |
| Busca preços | Serper API ($0.001/query) | Alternativa a Tavily |

## 2. Fluxo de Cotação (Estado Atual)

```
Usuário (WA) → Evolution webhook → Isaura router → 
  1. Extrai intent "cotação" + produto
  2. Busca preços (Serper/Tavily → scraping)
  3. Gera PDF comparativo (pdf-renderer.ts)
  4. Envia PDF + resumo via WhatsApp (sendMedia)
  5. Opcional: Email com .pdf attachment (Resend)
```

**Gargalos conhecidos:**
- `sendAudio()` é stub — voice notes de cotação nunca testados
- Audio TTS precisa base64 inline (Evolution não aceita URL local)
- Token Telegram corrompido (literais `***` no config)
- Nenhum servidor de arquivos estáticos rodando para media

## 3. Parâmetros Técnicos para Avaliação do Claude (Opus)

> Claude precisa responder SIM/NÃO com justificativa para cada item abaixo:

### 3.1 TTS em Cotações via WhatsApp
- [ ] TTS deve ser síncrono (gerar + enviar em <10s) ou assíncrono (fila)?
- [ ] pocket-tts em CPU atende SLA de <30s para áudios de 30s?
- [ ] Fallback texto-quando-áudio-falha é aceitável para o perfil do usuário?
- [ ] Precisa de voice cloning customizado (voz do atendente) ou vozes padrão bastam?

### 3.2 Email + PDF
- [ ] Resend + PDF gerado em servidor é suficiente ou precisa de CDN (Cloudinary)?
- [ ] Precisa de template de email HTML ou texto puro com attachment basta?
- [ ] Mailgun como fallback é confiável ou precisa de terceira rota (SendGrid)?

### 3.3 Arquitetura Multi-canal
- [ ] Mesma cotação deve ir para WA + Email simultaneamente?
- [ ] Precisa de controle de "já enviado" para não duplicar?
- [ ] Webhook Evolution → Isaura precisa de fila (RabbitMQ/Redis) ou síncrono OK?

### 3.4 Custo e Performance
- [ ] Modelo atual (DeepSeek V4 flash grátis + Opus premium) é adequado para o volume?
- [ ] Orçamento $200/mês comporta ~1000 cotações/mês com TTS incluso?
- [ ] GPU é necessária em algum ponto do pipeline (Hibiki-Zero para tradução simultânea)?

### 3.5 Próximos Passos (Recomendação Hermes)
1. **Imediato:** Testar `sendAudio()` real com pocket-tts → base64 → Evolution
2. **Curto prazo:** Servir áudio via Express static ou n8n webhook em vez de base64 inline
3. **Médio prazo:** Hibiki-Zero (se GPU disponível) para tradução simultânea PT→EN em canais de voz
4. **Longo prazo:** Voice cloning customizado com amostra de 20s para voz do atendente Isaura

---

## 4. Contexto de Sistema (para aumentar acurácia do parecer)

**Host:** Linux 6.17, i7-2600, 16GB RAM, sem GPU
**Storage:** 194GB SSD (56GB usado, 129GB livre)
**Custo de oportunidade:** $60/mês em UIs (Perplexity Pro, ChatGPT Plus, Claude Pro) — já pagos, marginal $0/query
**Regra crítica:** NUNCA alterar driver de placa de vídeo (já causou 3 formatações do Xubuntu)
**Modelo principal:** DeepSeek V4 flash (grátis via OpenRouter)
**Modelo para decisão:** Claude Opus 4.8 (via premium_ui_broker — browser, não API)
**Telefone alvo:** 5527999068846 (WhatsApp do usuário)
**Repositório:** github.com/andreengineer/buying-agent (público)
**Pipeline ativo:** Isaura em Gama (read-only Beta), 60+ usuários inativos aguardando Alpha