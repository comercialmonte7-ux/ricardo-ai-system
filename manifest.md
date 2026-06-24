# 📄 Ricardo AI System - Manifest & Backup
**Estado actual del ecosistema de agentes**

---

## 🚀 Información del Proyecto
- **Nombre:** Ricardo AI System
- **Versión Actual:** 1.1.0
- **Última Actualización:** 2026-06-24
- **Ubicación Local:** `/Users/ricardomarimodinger/.gemini/antigravity/scratch/ricardo-ai-system`
- **Repositorio:** `https://github.com/comercialmonte7-ux/ricardo-ai-system.git` (rama `main`)

---

## 🗺️ Estructura del Proyecto (post-reorganización 2026-06-24)

```
ricardo-ai-system/
├── index.html              # ROUTER Command Center v2.0 (página viva / GitHub Pages)
├── manifest.md             # Este archivo
├── config.js               # Config local con API keys (IGNORADO por .gitignore)
├── router_dashboard_hero.png
├── agents/                 # Definición de agentes del ecosistema
├── cognitive-map/          # Identidad y mapa cognitivo de Ricardo
├── memory/                 # Patrones e insights persistentes
├── data/                   # Datos operativos del negocio
│   └── router_seguridad/
│       ├── bitacora/       # Bitácora cronológica (cotizaciones, informes, guiones)
│       ├── alessandri_fndr/
│       ├── emails/
│       └── whatsapp/
├── images/                 # Recursos visuales del dashboard y presentaciones
├── scripts/                # Scripts Python/JS (generadores de PPTX, web manager, tests)
└── legacy/                 # Versiones anteriores conservadas como respaldo
```

---

## 🛠️ Estructura y Componentes

### 1. Capa de Identidad (Cognitive Map)
- [x] **Identidad Humana:** Definida en `cognitive-map/identidad_ricardo.md`.
- [ ] **Mapeo de Relaciones:** Pendiente en `cognitive-map/mapa_cognitivo.md` (placeholder vacío).

### 2. Agentes (Agents)
- [ ] **Core Agent:** `agents/ricardo_core_agent.md` (Estado: Inicializado)
- [ ] **Gmail Agent:** `agents/gmail_agent.md` (Estado: Placeholder vacío)
- [ ] **WhatsApp Agent:** `agents/whatsapp_agent.md` (Estado: Placeholder vacío)
- [x] **Business Agent (ROUTER):** `agents/router_business_agent.md` (Estado: Activo)
- [x] **Subagentes:** `agents/subagentes_config.md` (Diseño, Marketing, Contabilidad, Competencia, Captación)

### 3. Memoria (Memory)
- [x] **Patrones:** `memory/patrones.md`
- [ ] **Insights:** `memory/insights.md` (placeholder vacío)

---

## 🌐 Aplicaciones Activas
- **ROUTER Command Center v2.0** → `index.html` (servida vía GitHub Pages).
  - Versión anterior conservada en `legacy/dashboard_v1.html`.

---

## 📒 Bitácora ROUTER Seguridad (`data/router_seguridad/bitacora/`)
Registro cronológico de cotizaciones, informes y guiones. Cobertura activa: **marzo–junio 2026**.
Clientes/proyectos recientes: Municipalidad de Lebu, Interenergy Colhue, Clínica Leufu,
Liceo Isidora Ramos, Gimnasio Olimpus, Botillería Nataly, Villa Alessandri, Vista al Mar,
Nuevo Amanecer, entre otros.

> Cada documento se nombra como `YYYY-MM-DD_tipo_descriptor.ext`.

---

## 🧹 Historial de Mantenimiento

### 2026-06-24 — Reorganización del proyecto
- Eliminados `.DS_Store`.
- `dashboard.html` movido a `legacy/dashboard_v1.html` (la página viva es `index.html`).
- Eliminados duplicados verificados (md5 idéntico) de la raíz: presentaciones de
  Villa Alessandri y Vista al Mar (ya existían en `bitacora/` con fecha).
- Presentación de Nuevo Amanecer (versión 2026-06-11, más nueva) movida a `bitacora/`.
- `test_playwright.js` reubicado en `scripts/`.
- Placeholders vacíos (gmail, whatsapp, insights, mapa_cognitivo) conservados:
  son andamiaje intencional referenciado en este manifest.

---

## 🔄 Notas de Continuidad (Backup)
*Este bloque es para que cualquier IA que tome este proyecto sepa exactamente dónde estamos.*

**Hito Actual:**
La línea ROUTER Seguridad está operacionalmente activa, con bitácora densa y cotizaciones
recientes (última: Botillería Nataly, 2026-06-23). El Command Center v2.0 está publicado.
El Agente de Negocio ROUTER coordina 5 subagentes. Los agentes de Gmail y WhatsApp siguen
como placeholders pendientes de implementar.

**Próximo Paso Inmediato:**
Definir si se avanza en (a) implementar los agentes Gmail/WhatsApp pendientes, (b) completar
el mapa cognitivo de relaciones, o (c) continuar con el flujo de cotizaciones del negocio.

---
*Mantén este archivo siempre actualizado para "continuar donde sea".*
