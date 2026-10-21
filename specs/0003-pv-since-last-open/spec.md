---
name: spec
description: Contract for PalantirView "since last open" chat summaries — thresholds, cache, format, latency, privacy routing, memory. Pull when working on PalantirView (self-org lane).
alwaysApply: false
---

# Spec — PalantirView: summary since last open

> **Source of truth.** Status: draft. Lane: self-org (30% cap). Owner: Codex on lat. Code lives in the
> PalantirView repo on lat; this file is the contract.

## Summary
When André opens a chat or group in PalantirView, he sees a short summary of everything that
arrived since he last opened it, sized to how much he missed.

## Acceptance criteria

### AC-1: summary size follows unread volume
- **Given** a chat with N messages after `last_opened_ts`
- **When** André opens it
- **Then** N ≥ 50 → full summary; 10 ≤ N ≤ 49 → 3-line digest; N < 10 → no summary

### AC-2: cached reopen costs nothing
- **Given** a summary was generated up to message M
- **When** the chat is reopened with no message after M
- **Then** the cached summary is shown and 0 model calls are made

### AC-3: fixed format
- **Then** a full summary has at most 12 lines in this order: TL;DR (3 bullets) · Decisions ·
  Asks for André (who, what, by when) · Dates and events · Money mentioned (R$) · Links and files ·
  a conflict flag only when there is one

### AC-4: fast enough to read on open
- **Given** 50 to 300 new messages
- **Then** the summary renders in under 30 s; above 300 messages a progress line appears within 3 s

### AC-5: message content goes only to Claude or GPT
- **Given** any summary call
- **Then** the only outbound destinations are the configured Claude or OpenAI endpoints;
  any other destination fails the call and logs it

### AC-6: low memory
- **Given** a chat with 5,000 messages
- **Then** summarizing streams in chunks and peak RSS stays under 300 MB

### AC-7: mark as read
- **When** André taps "mark read"
- **Then** `last_opened_ts` moves to now and the next open shows no summary until new messages arrive

## Method (non-binding)
Map-reduce: chunks of 40 messages → chunk notes → merge. Cache key = (chat_id, last message id).

## Edge cases
- Media-only messages → counted, summarized as "N photos / N audios" with sender.
- Edited or deleted messages after summary → ignored until the next new message.
- Group with > 2,000 unread → summarize the latest 2,000, say how many were skipped.

## Out of scope
- Sending messages, auto-replies, reactions.
- Any non-Claude/GPT model for message content.
- Cross-chat digests (one chat at a time).

## Traceability
- Tasks: [tasks.md](./tasks.md) · Week plan: [../0002-family-cohort-w1/plan.md](../0002-family-cohort-w1/plan.md)
