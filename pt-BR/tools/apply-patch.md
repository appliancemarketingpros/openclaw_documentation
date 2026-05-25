---
title: ferramenta apply_patch
source_url: https://docs.openclaw.ai/pt-BR/tools/apply-patch
scraped_at: 2026-05-25
---

Aplique alterações em arquivos usando um formato de patch estruturado. Isso é ideal para edições em vários arquivos ou com vários hunks, em que uma única chamada `edit` seria frágil.

A ferramenta aceita uma única string `input` que envolve uma ou mais operações de arquivo:

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## Parâmetros

  * `input` (obrigatório): Conteúdo completo do patch, incluindo `*** Begin Patch` e `*** End Patch`.


## Observações

  * Os caminhos do patch aceitam caminhos relativos (a partir do diretório do workspace) e caminhos absolutos.
  * `tools.exec.applyPatch.workspaceOnly` assume `true` como padrão (contido no workspace). Defina como `false` somente se você intencionalmente quiser que `apply_patch` grave/exclua fora do diretório do workspace.
  * Use `*** Move to:` dentro de um hunk `*** Update File:` para renomear arquivos.
  * `*** End of File` marca uma inserção somente EOF quando necessário.
  * Disponível por padrão para modelos OpenAI e OpenAI Codex. Defina `tools.exec.applyPatch.enabled: false` para desativá-lo.
  * Opcionalmente, restrinja por modelo via `tools.exec.applyPatch.allowModels`.
  * A configuração fica somente em `tools.exec`.


## Exemplo

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## Relacionados

[**Diffs** Visualizador de diff somente leitura para apresentação de alterações. ](</pt-BR/tools/diffs>) [**Exec tool** Execução de comandos de shell a partir do agente. ](</pt-BR/tools/exec>) [**Code execution** Análise remota de Python em sandbox com xAI. ](</pt-BR/tools/code-execution>)

Was this useful?YesNo