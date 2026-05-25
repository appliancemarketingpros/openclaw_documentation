---
title: Criando Skills
source_url: https://docs.openclaw.ai/pt-BR/tools/creating-skills
scraped_at: 2026-05-25
---

Skills ensinam ao agente como e quando usar ferramentas. Cada Skill é um diretório contendo um arquivo `SKILL.md` com frontmatter YAML e instruções em markdown.

Para saber como Skills são carregadas e priorizadas, consulte [Skills](</pt-BR/tools/skills>).

## Crie sua primeira Skill

* ### Crie o diretório da Skill

Skills ficam no seu workspace. Crie uma nova pasta:

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
[/code]

* ### Escreva SKILL.md

Crie `SKILL.md` dentro desse diretório. O frontmatter define os metadados, e o corpo em markdown contém instruções para o agente.

markdownCopy code
[code]
    ---name: hello-worlddescription: A simple skill that says hello.--- # Hello World Skill When the user asks for a greeting, use the `echo` tool to say"Hello from your custom skill!".
[/code]

Use formato com hífens, letras minúsculas, dígitos e hífens para o `name` da Skill. Mantenha o nome da pasta alinhado ao `name` do frontmatter.

* ### Adicione ferramentas (opcional)

Você pode definir esquemas de ferramentas personalizados no frontmatter ou instruir o agente a usar ferramentas do sistema existentes (como `exec` ou `browser`). Skills também podem ser distribuídas dentro de plugins junto com as ferramentas que documentam.

* ### Carregue a Skill

Inicie uma nova sessão para que o OpenClaw detecte a Skill:

bashCopy code
[code]
    # From chat/new # Or restart the gatewayopenclaw gateway restart
[/code]

Verifique se a Skill foi carregada:

bashCopy code
[code]
    openclaw skills list
[/code]

* ### Teste-a

Envie uma mensagem que deve acionar a Skill:

bashCopy code
[code]
    openclaw agent --message "give me a greeting"
[/code]

Ou apenas converse com o agente e peça uma saudação.

## Referência de metadados da Skill

O frontmatter YAML aceita estes campos:

Campo | Obrigatório | Descrição  
---|---|---  
`name` | Sim | Identificador único usando letras minúsculas, dígitos e hífens  
`description` | Sim | Descrição de uma linha mostrada ao agente  
`metadata.openclaw.os` | Não | Filtro de SO (`["darwin"]`, `["linux"]`, etc.)  
`metadata.openclaw.requires.bins` | Não | Binários obrigatórios no PATH  
`metadata.openclaw.requires.config` | Não | Chaves de configuração obrigatórias  
  
## Práticas recomendadas

  * **Seja conciso** — instrua o modelo sobre _o que_ fazer, não sobre como ser uma IA
  * **Segurança em primeiro lugar** — se sua Skill usa `exec`, garanta que os prompts não permitam injeção arbitrária de comandos a partir de entrada não confiável
  * **Teste localmente** — use `openclaw agent --message "..."` para testar antes de compartilhar
  * **Use ClawHub** — navegue e contribua com Skills em [ClawHub](<https://clawhub.ai>)


## Onde Skills ficam

Localização | Precedência | Escopo  
---|---|---  
`\<workspace\>/skills/` | Mais alta | Por agente  
`\<workspace\>/.agents/skills/` | Alta | Agente por workspace  
`~/.agents/skills/` | Média | Perfil de agente compartilhado  
`~/.openclaw/skills/` | Média | Compartilhado (todos os agentes)  
Incluído (distribuído com o OpenClaw) | Baixa | Global  
`skills.load.extraDirs` | Mais baixa | Pastas compartilhadas personalizadas  
  
## Relacionado

  * [Referência de Skills](</pt-BR/tools/skills>) — regras de carregamento, precedência e controle
  * [Configuração de Skills](</pt-BR/tools/skills-config>) — esquema de configuração `skills.*`
  * [ClawHub](</pt-BR/clawhub>) — registro público de Skills
  * [Criação de Plugins](</pt-BR/plugins/building-plugins>) — plugins podem distribuir Skills


Was this useful?YesNo