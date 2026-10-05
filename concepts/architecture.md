---
title: Gateway architecture
source_url: https://docs.openclaw.ai/concepts/architecture
scraped_at: 2026-10-05
---

[code]
    sequenceDiagram
        participant Client
        participant Gateway
    
        Client->>Gateway: req:connect
        Gateway-->>Client: res (ok)
        Note right of Gateway: or res error + close
        Note left of Client: payload=hello-ok<br>snapshot: presence + health
    
        Gateway-->>Client: event:presence
        Gateway-->>Client: event:tick
    
        Client->>Gateway: req:agent
        Gateway-->>Client: res:agent<br>ack {runId, status:"accepted"}
        Gateway-->>Client: event:agent<br>(streaming)
        Gateway-->>Client: res:agent<br>final {runId, status, summary}
[/code]