---
title: Creación de Skills
source_url: https://docs.openclaw.ai/es/tools/creating-skills
scraped_at: 2026-05-25
---

Skills enseña al agente cómo y cuándo usar herramientas. Cada skill es un directorio que contiene un archivo `SKILL.md` con frontmatter YAML e instrucciones en markdown.

Para saber cómo se cargan y priorizan las skills, consulta [Skills](</es/tools/skills>).

## Crea tu primera skill

* ### Crea el directorio de la skill

Las Skills viven en tu espacio de trabajo. Crea una carpeta nueva:

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
[/code]

* ### Escribe SKILL.md

Crea `SKILL.md` dentro de ese directorio. El frontmatter define los metadatos, y el cuerpo markdown contiene instrucciones para el agente.

markdownCopy code
[code]
    ---name: hello-worlddescription: A simple skill that says hello.--- # Hello World Skill When the user asks for a greeting, use the `echo` tool to say"Hello from your custom skill!".
[/code]

Usa formato con guiones y letras minúsculas, dígitos y guiones para el `name` de la skill. Mantén alineados el nombre de la carpeta y el `name` del frontmatter.

* ### Agrega herramientas (opcional)

Puedes definir esquemas de herramientas personalizados en el frontmatter o indicar al agente que use herramientas del sistema existentes (como `exec` o `browser`). Las Skills también pueden incluirse dentro de plugins junto con las herramientas que documentan.

* ### Carga la skill

Inicia una sesión nueva para que OpenClaw detecte la skill:

bashCopy code
[code]
    # From chat/new # Or restart the gatewayopenclaw gateway restart
[/code]

Verifica que la skill se haya cargado:

bashCopy code
[code]
    openclaw skills list
[/code]

* ### Pruébala

Envía un mensaje que debería activar la skill:

bashCopy code
[code]
    openclaw agent --message "give me a greeting"
[/code]

O simplemente chatea con el agente y pídele un saludo.

## Referencia de metadatos de skills

El frontmatter YAML admite estos campos:

Campo | Obligatorio | Descripción  
---|---|---  
`name` | Sí | Identificador único que usa letras minúsculas, dígitos y guiones  
`description` | Sí | Descripción de una línea que se muestra al agente  
`metadata.openclaw.os` | No | Filtro de SO (`["darwin"]`, `["linux"]`, etc.)  
`metadata.openclaw.requires.bins` | No | Binarios requeridos en PATH  
`metadata.openclaw.requires.config` | No | Claves de configuración requeridas  
  
## Buenas prácticas

  * **Sé conciso** — indica al modelo _qué_ hacer, no cómo ser una IA
  * **La seguridad primero** — si tu skill usa `exec`, asegúrate de que los prompts no permitan inyección arbitraria de comandos desde entradas no confiables
  * **Prueba localmente** — usa `openclaw agent --message "..."` para probar antes de compartir
  * **Usa ClawHub** — explora y contribuye skills en [ClawHub](<https://clawhub.ai>)


## Dónde viven las skills

Ubicación | Precedencia | Alcance  
---|---|---  
`\<workspace\>/skills/` | Más alta | Por agente  
`\<workspace\>/.agents/skills/` | Alta | Agente por espacio de trabajo  
`~/.agents/skills/` | Media | Perfil de agente compartido  
`~/.openclaw/skills/` | Media | Compartido (todos los agentes)  
Incluidas (enviadas con OpenClaw) | Baja | Global  
`skills.load.extraDirs` | Más baja | Carpetas compartidas personalizadas  
  
## Relacionado

  * [Referencia de Skills](</es/tools/skills>) — carga, precedencia y reglas de control
  * [Configuración de Skills](</es/tools/skills-config>) — esquema de configuración `skills.*`
  * [ClawHub](</es/clawhub>) — registro público de skills
  * [Creación de Plugins](</es/plugins/building-plugins>) — los plugins pueden incluir skills


Was this useful?YesNo