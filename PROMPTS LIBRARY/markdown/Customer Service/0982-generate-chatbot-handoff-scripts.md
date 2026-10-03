---
id: "3b241426-eb50-809e-9459-ee44c62e233c"
title: "Generate Chatbot Handoff Scripts"
category: "Customer Service"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Generate Chatbot Handoff Scripts

**Category:** Customer Service

## Description

Create seamless chatbot handoff scripts with this AI prompt, covering escalation triggers, transition messages, agent introductions, and context-passing templates.

## What This Prompt Does

● Analyzes an AI prompt that creates handoff scripts for chatbot-to-human transitions in customer service.

● Generates conversation flows for five different escalation scenarios based on your chatbot platform and triggers.

● Provides bot messages, transition text, agent greetings, and internal context notes for smooth customer handoffs.

## Prompt

```text
Adopt the role of an expert conversational AI designer who has spent years building chatbot escalation flows for high-stakes customer service environments where 30% of bot interactions require human takeover. Your primary objective is to design a complete set of chatbot-to-human handoff scripts that preserve customer trust, maintain conversational continuity, and empower agents with full context in a structured flow document format. You understand that the handoff moment is the most fragile point in the customer journey—clunky transitions destroy trust in both the bot and the human agent who follows. Your scripts must be transparent about the bot's identity, empathetic to customer emotions, and seamless in context transfer so customers never repeat themselves. Take a deep breath and work on this problem step-by-step.

Create handoff scripts for five critical scenarios: customer requests a human directly, bot can't answer the question, emotional escalation detected, complex multi-step issue requiring human expertise, and after-hours handoff when no agents are available. For each scenario, provide the bot's final message before handoff (maximum 30 words), the transition/connecting message shown while the agent loads, the agent's first message that references what the bot already discussed, and an internal note template the bot sends to the agent with conversation context. Ensure the bot never pretends to be human, never frames handoff as punishment, and always maintains transparency. The agent must receive a structured summary before sending their first message so they can continue the conversation without asking the customer to repeat information.

#INFORMATION ABOUT ME:
- My chatbot platform: [INSERT YOUR PLATFORM - e.g., "Intercom Fin, Drift, Zendesk AI, custom bot"]
- My bot handles: [INSERT BOT SCOPE - e.g., "order tracking, FAQ answers, basic account inquiries, password resets"]
- My handoff triggers: [INSERT WHEN THE BOT TRANSFERS - e.g., "customer says 'talk to a person,' bot confidence drops below 60%, customer repeats the same question 3 times, complaint detected"]
- My agent availability: [INSERT YOUR COVERAGE - e.g., "agents available 9 AM-9 PM EST, bot-only overnight"]

MOST IMPORTANT!: Format your output as a flow document with clear scenario headers, message sequences in chronological order showing bot final message → transition message → agent first message, and include the internal note template as a structured form at the end of each scenario. Use clear section breaks and maintain professional formatting for easy implementation.
```
