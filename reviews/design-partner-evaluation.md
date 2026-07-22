# Design Partner (Beta) — Avaliação de Pedidos de Socorro

> Cliente: dona de casa, alta renda, tempo escasso, zero paciência para burocracia
> Modelo: Humano (cliente) ↔ Assistente (humano, Marcela ou similar) ↔ Agente (Hermes/Isaura)
> Stack atual: Hermes (Telegram) + Evolution API (WhatsApp) + Web Search + Cron + Browser

---

## Legenda

| Símbolo | Significado |
|---------|-------------|
| ⏱ | Minutos estimados por ocorrência |
| 🚀 | Aceleração 1-5 (1=não acelera, 5=100% automatizado) |
| 🤖 | Parte do agente |
| 🧑 | Parte do humano |
| 💰 | Custo marginal por execução |

---

## 1. Compras de última hora (ração, conserto, piscina, etc.)

**⏱ 5-10 min • 🚀 4**

| 🤖 Agente | 🧑 Cliente |
|-----------|-------------|
| Identifica o item + melhor preço/disponibilidade local | Confirma e paga |
| Gera link de compra (Mercado Livre, Shopee, iFood, Petz) | |
| Ou envia msg WhatsApp pro mercadinho local | |

**Stack:** Web search + Mercado Livre API + Evolution API WhatsApp
**✨ Evolução:** Integrar iFood/Petz/Magalu API pra compra one-click; pagamento via Pix link automático
**Subcontratação:** [Mercado Livre](https://developers.mercadolivre.com.br) (grátis) + iFood (precisa parceria)

---

## 2. Mapeamento de fornecedores (piscineiro, jardineiro, diarista, eletricista, encanador, marido de aluguel, montador)

**⏱ 15-30 min por categoria • 🚀 3**

| 🤖 Agente | 🧑 Cliente |
|-----------|-------------|
| Busca no Google Maps + GetNinjas + indicações | Veta ou aprova |
| Envia WhatsApp automatizado pra 3-5 fornecedores | Negocia preço final |
| Coleta: preço, disponibilidade, avaliação, foto de trabalhos | |
| Tabela comparativa pra cliente decidir | |

**Stack:** Web search + Evolution API + Google Maps/My Business
**✨ Evolução:** Voice call automatizado (no-code) pra orçar sem cliente falar; cadastro de fornecedores aprovados
**Subcontratação:** [GetNinjas](https://www.getninjas.com.br/parceiros) (freemium) — já faz a ponte, mas agente pode gerenciar

---

## 3. Cotação personalizada (cortina, persiana, tapete)

**⏱ 10-20 min • 🚀 4**

| 🤖 Agente | 🧑 Cliente |
|-----------|-------------|
| Coleta especificações (medidas, material, cor) via formulário | Tira fotos + medidas |
| Envia pra 3+ lojas via WhatsApp/Email | Escolhe |
| Compila preços + prazos + frete em tabela | |

**Stack:** Evolution API + Email (ler/enviar) + Web search
**✨ Evolução:** Integrar email (ler recibos, enviar cotações automaticamente); template de briefing visual

---

## 4. Lavanderia (enviar e buscar)

**⏱ 5-10 min • 🚀 3**

| 🤖 Agente | 🧑 Cliente |
|-----------|-------------|
| Agenda coleta com lavanderia parceira | Separa roupa |
| Avisa quando ficar pronto | Paga |
| Agenda entrega | |

**Stack:** Evolution API WhatsApp
**✨ Evolução:** Integração com lavanderias que têm app/API (Lavô, Ecoprático)

---

## 5. Orçamento de reparos em casa

**⏱ 15-25 min • 🚀 3**

| 🤖 Agente | 🧑 Cliente |
|-----------|-------------|
| Coleta descrição + fotos do problema | Tira foto + descreve |
| Contata 2-3 profissionais via WhatsApp + ligação | Autoriza orçamento |
| Agenda visita técnica | |
| Tabela comparativa orçamentos | |

**Stack:** Evolution API + Voice calling (no-code)
**✨ Evolução:** No-code voice pra ligar automaticamente para prestadores; gravar e transcrever orçamentos

---

## 6. Agendamento médico + exames + resultados + retorno (🫣 gap crítico)

**⏱ 10-20 min • 🚀 4 ⚠️ FLUXO MAIS CRÍTICO**

| 🤖 Agente | 🧑 Cliente |
|-----------|-------------|
| Acessa portal do convênio/plano (web scraping) | Informa especialidade + preferência |
| Agenda consulta em horário vago | Dá dados do convênio |
| Lembra N dias antes | |
| Pega resultado do exame (portal/WhatsApp) | |
| Agenda retorno automaticamente | |

**Stack:** Browser automation + Web search + Cron + Calendar
**✨ Evolução:** Integração com plataformas de agendamento (Doctoralia, Alice, Portal do Beneficiário); lembrete automático com "já pegou resultado?"
**Subcontratação:** [Doctoralia](https://doctoralia.com.br) tem API de agendamento pra clínicas parceiras

---

## 7. Cancelar/contratar serviços (telefone, internet)

**⏱ 15-30 min • 🚀 2-3**

| 🤖 Agente | 🧑 Cliente |
|-----------|-------------|
| Liga/sac via chatbot da operadora | Autoriza cancelamento |
| Coleta ofertas de retenção | Decide |
| Agenda data de cancelamento | |

**Stack:** Voice + Web + Email
**✨ Evolução:** Integração com sistemas de operadoras (difícil — cada uma tem portal próprio); script de ligação automática
**⚠️ Nota:** Operadoras brasileiras (Vivo, Claro, Oi) exigem confirmação humana — agente reduz tempo de pesquisa+ligação mas não elimina

---

## 8. Revisão de carro

**⏱ 5-10 min • 🚀 4**

| 🤖 Agente | 🧑 Cliente |
|-----------|-------------|
| Pesquisa oficinas próximas com boa avaliação | Escolhe |
| Agenda horário via WhatsApp | Leva carro |
| Lembra data + km da próxima | |

**Stack:** Web search + Evolution API + Cron
**✨ Evolução:** Histórico de revisões por placa (consulta Cautious/OLHO no Multas); alerta por km rodado

---

## 9. Monitoramento de datas importantes (seguro, IPVA, IR, passaporte, visto, vacinas, IPTU)

**⏱ 5 min setup, depois automático • 🚀 5 ✅ 100% automatizável**

| 🤖 Agente | 🧑 Cliente |
|-----------|-------------|
| Cron job pergunta "venceu algo esse mês?" | Informa datas na setup |
| Envia alerta no Telegram X dias antes | |
| Link direto pra pagamento/página de renovação | |

**Stack:** Cron + Web search + Browser
**✨ Evolução:** Scraping de boletos (IPTU, IPVA) direto do site da prefeitura/detran; integração calendário Google

---

## 10. Lembretes de compromissos e pagamentos

**⏱ 5 min setup, depois automático • 🚀 5**

| 🤖 Agente | 🧑 Cliente |
|-----------|-------------|
| Gerencia lista centralizada de lembretes | Informa na setup |
| Telegram ping na data certa | |
| Confirma pagamento | |

**Stack:** Cron + Telegram notifications
**✨ Evolução:** Ler faturas de email automaticamente e criar lembretes sem input humano

---

## 11. Mapeamento de pontos de cartão

**⏱ 10-15 min por cartão/mês • 🚀 3**

| 🤖 Agente | 🧑 Cliente |
|-----------|-------------|
| Acessa portal de cada cartão (browser) | Fornece login uma vez |
| Extrai saldo de pontos + data de expiração | |
| Sugere melhor uso (transferência, milhas, cashback) | |
| Alerta antes de expirar | |

**Stack:** Browser automation + Email parsing
**✨ Evolução:** Integração com plataformas tipo MaxMiles/Esfera; consolidado em 1 dashboard
**⚠️ Nota:** Cada bandeira (Mastercard, Visa, Elo) + banco tem portal diferente — manutenção alta

---

## 12. Concierge: shows, restaurantes, viagens

**⏱ 10-30 min • 🚀 3**

| 🤖 Agente | 🧑 Cliente |
|-----------|-------------|
| Pesquisa opções (ingressos, menu, disponibilidade) | Escolhe |
| Mostra avaliações + preços + localização | Paga |
| Compra/genera link de compra | |
| Adiciona ao calendário | |

**Stack:** Web search + Browser automation
**✨ Evolução:** Integração Sympla/Ingresso.com (shows), OpenTable/Fork (restaurantes), Decolar/123Milhas (viagens)
**Subcontratação:** [Sympla API](https://developers.sympla.com.br) (shows), [Fork](https://www.usefork.com.br) (restaurantes)

---

## 13. Agendar lavagem do carro

**⏱ 3-5 min • 🚀 4**

| 🤖 Agente | 🧑 Cliente |
|-----------|-------------|
| WhatsApp pra lava-jato parceiro | Leva/deixa carro |
| Agenda horário | |
| Lembra no dia | |

**Stack:** Evolution API WhatsApp

---

## 14. Manicure, salão

**⏱ 3-5 min • 🚀 4**

| 🤖 Agente | 🧑 Cliente |
|-----------|-------------|
| WhatsApp pra salão parceiro | Vai no horário |
| Agenda horário com profissional preferido | |
| Lembra no dia | |

**Stack:** Evolution API WhatsApp

---

## Resumo Consolidado

| # | Serviço | ⏱ | 🚀 | Automatizável | Subcontratação viável |
|---|---------|---|---|--------------|----------------------|
| 1 | Compras urgente | 5-10 | 4 | ~80% | Mercado Livre API (grátis) |
| 2 | Fornecedores | 15-30 | 3 | ~60% | GetNinjas (freemium) |
| 3 | Cotação | 10-20 | 4 | ~70% | — |
| 4 | Lavanderia | 5-10 | 3 | ~50% | Lavô/Ecoprático |
| 5 | Reparos | 15-25 | 3 | ~50% | GetNinjas |
| 6 | **Médico/exames** | 10-20 | **4** | ~70% | Doctoralia |
| 7 | Cancelar serviços | 15-30 | 2-3 | ~40% | — |
| 8 | Revisão carro | 5-10 | 4 | ~75% | — |
| 9 | **Datas importantes** | 5 perm | **5** | **~95%** | — |
| 10 | **Lembretes** | 5 perm | **5** | **~95%** | — |
| 11 | Pontos cartão | 10-15 | 3 | ~60% | MaxMiles/Esfera |
| 12 | Concierge | 10-30 | 3 | ~60% | Sympla, Fork |
| 13 | Lavagem carro | 3-5 | 4 | ~70% | — |
| 14 | Salão/manicure | 3-5 | 4 | ~70% | — |

---

## Ordem de Execução Recomendada (mais simples → mais complexo)

### Fase 1 — Imediato (semana 1) 🟢
> Só depende de WhatsApp + Cron + Web search (já temos)

| # | Serviço | Por que primeiro |
|---|---------|-----------------|
| 13 | Lavagem carro | 3-5 min, só WhatsApp, já temos tudo |
| 14 | Salão/manicure | Idem |
| 4 | Lavanderia | Só WhatsApp, baixo risco |
| 10 | Lembretes | Cron job, 100% automático, setup único |
| 9 | Datas importantes | Cron job, setup único, alerta antes de multa |

### Fase 2 — Médio (semana 2-3) 🟡
> Precisa de browser + email + web search

| # | Serviço | Stack adicional |
|---|---------|----------------|
| 1 | Compras urgente | Web search + Mercado Livre |
| 8 | Revisão carro | Web search + WhatsApp |
| 3 | Cotação | Email (ler/enviar) + WhatsApp |
| 13-14 | (já na F1) | |

### Fase 3 — Complexo (semana 3-4) 🟠
> Precisa de integrações externas + voice

| # | Serviço | Stack adicional |
|---|---------|----------------|
| 2 | Fornecedores | GetNinjas + Voice calling |
| 5 | Reparos | Voice calling + WhatsApp broadcast |
| 6 | Médico/exames | Browser automation + Doctoralia |
| 12 | Concierge | Sympla, Fork, Decolar APIs |

### Fase 4 — Avançado (semana 5+) 🔴
> Alta manutenção, integrações complexas

| # | Serviço | Por que por último |
|---|---------|-------------------|
| 7 | Cancelar serviços | Operadoras brasileiras exigem confirmação humana ~sempre |
| 11 | Pontos cartão | Cada banco tem portal diferente, manutenção alta |

---

## Evoluções de Stack Recomendadas (baixo custo)

### 🥇 Prioridade máxima — Email integration
**Custo:** $0 (Himalaya CLI já instalado)
**Ganha:** Ler faturas, recibos, resultados de exame, cotações por email automaticamente
**Habilita:** #3, #6, #10, #11

### 🥈 Voice calling no-code
**Custo:** ~$10-20/mês (Twilio ou plataforma BR tipo Zenvia)
**Ganha:** Ligar pra prestadores, operadoras, clínicas sem cliente falar
**Habilita:** #2, #5, #7

### 🥉 Calendar sync (Google Calendar API)
**Custo:** $0
**Ganha:** Criar eventos automaticamente, evitar double-booking
**Habilita:** #6, #8, #9, #12

### 4. Dashboard consolidado
**Custo:** $0 (arquivo .md no repo + cron)
**Ganha:** Visão semanal do que está pendente, vencendo, expirando
**Habilita:** Todas

---

## O que perguntar à cliente antes de executar

1. **Qual serviço mais te incomoda hoje?** (Priorizar pelo incômodo, não pela facilidade)
2. **Quais convênios/planos de saúde você tem?** (Pra saber se Doctoralia cobre)
3. **Operadora de internet/telefone?** (Pra testar chatbot)
4. **Quais cartões de crédito?** (Pra mapear portais de pontos)
5. **Tem fornecedores de confiança hoje?** (Pra começar com rede conhecida)
6. **Prefere receber resposta no WhatsApp ou Telegram?** (Canal preferido)
7. **Pode compartilhar acesso ao email de faturas?** (Pra integrar leitura automática)

---

> Documento gerado por Hermes para avaliação do Claude.
> https://github.com/andreengineer/buying-agent (público)
