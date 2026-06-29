---
title: प्रवाह (रीडायरेक्ट)
source_url: https://docs.openclaw.ai/hi/cli/flows
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw tasks flow`

शीर्ष-स्तरीय `openclaw flows` कमांड नहीं है। स्थायी TaskFlow निरीक्षण `openclaw tasks flow` के अंतर्गत है।

## उपकमांड

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

उपकमांड | विवरण | आर्ग्युमेंट / विकल्प  
---|---|---  
`list` | ट्रैक किए गए TaskFlow सूचीबद्ध करें। | `--json` मशीन-पठनीय आउटपुट; `--status <name>` फ़िल्टर (नीचे स्थिति मान देखें)।  
`show` | एक TaskFlow दिखाएं। | `<lookup>` flow id या स्वामी कुंजी; `--json` मशीन-पठनीय आउटपुट।  
`cancel` | चल रहे TaskFlow को रद्द करें। | `<lookup>` flow id या स्वामी कुंजी।  
  
`<lookup>` flow id (`list` / `show` द्वारा लौटाया गया) या flow की स्वामी कुंजी (वह स्थिर पहचानकर्ता जिसे स्वामित्व वाला सबसिस्टम flow को ट्रैक करने के लिए उपयोग करता है) में से किसी एक को स्वीकार करता है।

### स्थिति फ़िल्टर मान

`list` पर `--status` इनमें से एक स्वीकार करता है:

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## उदाहरण

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

पूर्ण TaskFlow अवधारणाओं और ऑथरिंग के लिए [TaskFlow](</hi/automation/taskflow>) देखें। पैरेंट `tasks` कमांड के लिए [tasks CLI संदर्भ](</hi/cli/tasks>) देखें।

## संबंधित

  * [CLI संदर्भ](</hi/cli>)
  * [ऑटोमेशन](</hi/automation>)
  * [TaskFlow](</hi/automation/taskflow>)


Was this useful?YesNo

Open issue