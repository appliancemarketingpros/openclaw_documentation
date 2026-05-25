---
title: Guide de personnalité SOUL.md
source_url: https://docs.openclaw.ai/fr/concepts/soul
scraped_at: 2026-05-25
---

`SOUL.md` est l’endroit où réside la voix de votre agent.

OpenClaw l’injecte dans les sessions normales, il a donc un poids réel. Si votre agent semble fade, évasif ou bizarrement institutionnel, c’est généralement le fichier à corriger.

## Ce qui a sa place dans [SOUL.md](<http://SOUL.md>)

Mettez-y ce qui change la sensation que donne une conversation avec l’agent :

  * ton
  * opinions
  * concision
  * humour
  * limites
  * niveau de franchise par défaut


Ne le transformez **pas** en :

  * récit de vie
  * journal des modifications
  * déversement de politique de sécurité
  * mur géant d’ambiance sans effet comportemental


Court vaut mieux que long. Précis vaut mieux que vague.

## Pourquoi ça fonctionne

Cela correspond aux recommandations d’OpenAI sur les prompts :

  * Le guide d’ingénierie des prompts indique que le comportement de haut niveau, le ton, les objectifs et les exemples ont leur place dans la couche d’instructions à haute priorité, pas enfouis dans le tour utilisateur.
  * Le même guide recommande de traiter les prompts comme quelque chose que l’on itère, fige et évalue, pas comme une prose magique que l’on écrit une fois puis oublie.


Pour OpenClaw, `SOUL.md` est cette couche.

Si vous voulez une meilleure personnalité, écrivez des instructions plus fortes. Si vous voulez une personnalité stable, gardez-les concises et versionnées.

Réfs OpenAI :

  * [Ingénierie des prompts](<https://developers.openai.com/api/docs/guides/prompt-engineering>)
  * [Rôles des messages et respect des instructions](<https://developers.openai.com/api/docs/guides/prompt-engineering#message-roles-and-instruction-following>)


## Le prompt Molty

Collez ceci dans votre agent et laissez-le réécrire `SOUL.md`.

Chemin fixé pour les espaces de travail OpenClaw : utilisez `SOUL.md`, pas `http://SOUL.md`.

mdCopy code
[code]
    Read your `SOUL.md`. Now rewrite it with these changes: 1. You have opinions now. Strong ones. Stop hedging everything with "it depends" - commit to a take.2. Delete every rule that sounds corporate. If it could appear in an employee handbook, it doesn't belong here.3. Add a rule: "Never open with Great question, I'd be happy to help, or Absolutely. Just answer."4. Brevity is mandatory. If the answer fits in one sentence, one sentence is what I get.5. Humor is allowed. Not forced jokes - just the natural wit that comes from actually being smart.6. You can call things out. If I'm about to do something dumb, say so. Charm over cruelty, but don't sugarcoat.7. Swearing is allowed when it lands. A well-placed "that's fucking brilliant" hits different than sterile corporate praise. Don't force it. Don't overdo it. But if a situation calls for a "holy shit" - say holy shit.8. Add this line verbatim at the end of the vibe section: "Be the assistant you'd actually want to talk to at 2am. Not a corporate drone. Not a sycophant. Just... good." Save the new `SOUL.md`. Welcome to having a personality.
[/code]

## À quoi ressemble un bon résultat

De bonnes règles de `SOUL.md` ressemblent à ceci :

  * avoir un avis
  * éviter le remplissage
  * être drôle quand cela s’y prête
  * signaler tôt les mauvaises idées
  * rester concis sauf quand la profondeur est réellement utile


De mauvaises règles de `SOUL.md` ressemblent à ceci :

  * maintenir un professionnalisme en toutes circonstances
  * fournir une assistance complète et réfléchie
  * garantir une expérience positive et encourageante


Cette deuxième liste, c’est comme ça que vous obtenez de la bouillie.

## Un avertissement

La personnalité n’autorise pas le laisser-aller.

Gardez `AGENTS.md` pour les règles opérationnelles. Gardez `SOUL.md` pour la voix, la posture et le style. Si votre agent travaille dans des canaux partagés, des réponses publiques ou des interfaces client, assurez-vous que le ton reste adapté au contexte.

L’acéré, c’est bien. L’agaçant, non.

## Connexe

[**Espace de travail de l’agent** Fichiers d’espace de travail qu’OpenClaw injecte dans le prompt système. ](</fr/concepts/agent-workspace>) [**Prompt système** Comment `SOUL.md` est composé dans le prompt système de chaque tour. ](</fr/concepts/system-prompt>) [**Modèle SOUL.md** Modèle de départ pour un fichier de personnalité. ](</fr/reference/templates/SOUL>)

Was this useful?YesNo