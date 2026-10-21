---
name: modern-web-and-ui
description: Professional web development and UI/UX design: semantic HTML5, modern vanilla CSS tokens, WCAG 2.1 AA accessibility, Chrome DevTools performance audits, and sleek aesthetics.
---

# Modern Web, UI/UX & Frontend Engineering

A design and engineering standard for creating web applications that wow users with visual excellence, fluid interactivity, and flawless performance.

## 1. Visual Aesthetics & Design System
- **Curated Color Palettes**: Sleek dark modes with deep slate/indigo backgrounds, tailored HSL accents, and glassmorphic panels (`backdrop-filter: blur(12px)`).
- **Modern Typography**: Clear font hierarchy using Google Fonts (Inter, Outfit, Roboto) with proportional line-heights and letter-spacing.
- **Subtle Micro-Animations**: Smooth transitions on hover, modal open/close animations, and dynamic state feedback.
- **Windowed & Fullscreen Modes**: Always provide a fullscreen toggle button alongside windowed mode for dashboard and data apps.

## 2. Accessible Semantic Markup (WCAG 2.1 AA)
- Single `<h1>` per page with hierarchical `<h2>`-`<h6>` structure.
- All interactive elements must have clear focus rings, unique IDs, and keyboard navigation support.
- Proper contrast ratios (minimum 4.5:1 for regular text, 3:1 for large text).
- Correct ARIA attributes (`aria-label`, `aria-expanded`, `aria-hidden`) where semantic HTML alone is insufficient.

## 3. Web Performance & Core Web Vitals
- **LCP (Largest Contentful Paint)**: Minimize critical render-blocking CSS/JS, optimize image assets, and use inline critical styles.
- **INP (Interaction to Next Paint)**: Avoid long tasks on the main thread; debounce search inputs; use CSS transforms for animations.
- **Zero Layout Shift (CLS)**: Always reserve dimensions for images, banners, and dynamic containers.
- **Tufte Data Visualization**: High data-ink ratio, legible axis markers, and direct labeling without cluttered legends.
