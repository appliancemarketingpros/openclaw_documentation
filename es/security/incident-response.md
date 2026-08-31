---
title: Respuesta ante incidentes
source_url: https://docs.openclaw.ai/es/security/incident-response
scraped_at: 2026-08-31
---

Comenzar

## 1\. Detección y triaje

Las señales de seguridad provienen de:

  * Avisos de seguridad de GitHub (GHSA) e informes privados de vulnerabilidades.
  * Issues y debates públicos de GitHub cuando los informes no son confidenciales.
  * Señales automatizadas: Dependabot, CodeQL, avisos de npm y análisis de secretos.


Triaje inicial:

  1. Confirmar el componente y la versión afectados, así como el impacto en los límites de confianza.
  2. Clasificarlo como un problema de seguridad o como un caso de refuerzo/sin acción, según las reglas de alcance y exclusión del alcance de `SECURITY.md`.
  3. La persona responsable del incidente responde según corresponda.


## 2\. Gravedad

Gravedad | Definición  
---|---  
Crítica | Compromiso de un paquete, una versión o un repositorio; explotación activa; o elusión no autenticada de los límites de confianza con control de alto impacto o exposición de datos.  
Alta | Elusión verificada de los límites de confianza que requiere condiciones previas limitadas (por ejemplo, una acción autenticada pero no autorizada de alto impacto) o exposición de credenciales confidenciales propiedad de OpenClaw.  
Media | Debilidad de seguridad significativa con impacto práctico, pero con posibilidades de explotación limitadas o requisitos previos considerables.  
Baja | Hallazgos de defensa en profundidad, denegación de servicio de alcance limitado o carencias de refuerzo/paridad sin una elusión demostrada de los límites de confianza.  
  
## 3\. Respuesta

  1. Confirmar la recepción a quien envió el informe (en privado cuando sea confidencial).
  2. Reproducir el problema en las versiones compatibles y en la versión más reciente de `main`; a continuación, implementar y validar un parche con cobertura de regresión.
  3. Crítica/alta: preparar las versiones corregidas tan rápido como sea posible en la práctica.
  4. Media/baja: aplicar el parche mediante el flujo normal de publicación y documentar las pautas de mitigación.


## 4\. Comunicación y divulgación

Comunicarse mediante los avisos de seguridad de GitHub en el repositorio afectado, las notas de la versión o las entradas del registro de cambios correspondientes a las versiones corregidas, y el seguimiento directo con quien envió el informe sobre el estado y la resolución.

Los incidentes críticos o de gravedad alta requieren una divulgación coordinada y la emisión de un CVE cuando corresponda. Los hallazgos de refuerzo de bajo riesgo pueden documentarse en las notas de la versión o en avisos sin un CVE, según el impacto y la exposición de los usuarios.

## 5\. Recuperación y seguimiento

Después de publicar la corrección:

  1. Verificar las medidas correctivas en el Pipeline de CI y en los artefactos de la versión.
  2. Realizar una breve revisión posterior al incidente: cronología, causa raíz, deficiencia de detección y plan de prevención.
  3. Añadir tareas de seguimiento de refuerzo, pruebas y documentación, y supervisarlas hasta su finalización.


## Contenido relacionado

  * [Política de seguridad](<https://github.com/openclaw/openclaw/blob/main/SECURITY.md>) — alcance de los informes y modelo de confianza.
  * [Modelo de amenazas](</es/security/THREAT-MODEL-ATLAS>)


Was this useful?YesNo

Open issue