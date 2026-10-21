// ==========================================================================
// SkillLens Pro - Core Application Logic
// Pair Programming Intelligence & Skill Consolidation Engine
// ==========================================================================

// Global state
const state = {
    skills: window.SKILL_DATA ? window.SKILL_DATA.skills : [],
    analytics: window.SKILL_DATA ? window.SKILL_DATA.analytics : {},
    bundles: window.SKILL_DATA ? window.SKILL_DATA.bundles : [],
    selectedCompareIds: [],
    currentTab: 'tab-dashboard',
    catalogViewMode: 'cards', // 'cards' | 'table'
    filters: {
        search: '',
        suitability: 'high_value',
        domain: 'all',
        source: 'all'
    }
};

// Initialize Application
document.addEventListener('DOMContentLoaded', () => {
    initFullscreenToggle();
    initNavigation();
    initDashboard();
    initCatalogFilters();
    initCatalog();
    initDuplicatesView();
    initBundlesView();
    updateCompareBadge();
});

// ==========================================================================
// 1. Fullscreen & Windowed Mode (User Rule 4)
// ==========================================================================
function initFullscreenToggle() {
    const btn = document.getElementById('btn-fullscreen-toggle');
    const txt = document.getElementById('txt-fullscreen');
    const iconExpand = btn.querySelector('.icon-expand');
    const iconCompress = btn.querySelector('.icon-compress');

    function updateUiState(isFullscreen) {
        if (isFullscreen) {
            document.body.classList.add('is-fullscreen');
            txt.textContent = 'Fenstermodus';
            iconExpand.classList.add('hidden');
            iconCompress.classList.remove('hidden');
        } else {
            document.body.classList.remove('is-fullscreen');
            txt.textContent = 'Vollbild';
            iconExpand.classList.remove('hidden');
            iconCompress.classList.add('hidden');
        }
    }

    btn.addEventListener('click', () => {
        if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen().catch(err => {
                console.warn(`Fullscreen error: ${err.message}`);
                // Fallback toggle css class
                const isFs = document.body.classList.toggle('is-fullscreen');
                updateUiState(isFs);
            });
        } else {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            }
        }
    });

    document.addEventListener('fullscreenchange', () => {
        updateUiState(Boolean(document.fullscreenElement));
    });
}

// ==========================================================================
// 2. Tab Navigation
// ==========================================================================
function initNavigation() {
    const tabs = document.querySelectorAll('.nav-tab');
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const targetId = tab.getAttribute('data-tab');
            switchTab(targetId);
        });
    });
}

function switchTab(tabId) {
    state.currentTab = tabId;

    // Update nav tab buttons
    document.querySelectorAll('.nav-tab').forEach(t => {
        if (t.getAttribute('data-tab') === tabId) {
            t.classList.add('active');
        } else {
            t.classList.remove('active');
        }
    });

    // Update tab contents
    document.querySelectorAll('.tab-content').forEach(c => {
        if (c.id === tabId) {
            c.classList.add('active');
        } else {
            c.classList.remove('active');
        }
    });

    // If switching to comparator, refresh comparison view
    if (tabId === 'tab-comparator') {
        renderComparatorGrid();
    }
}

// ==========================================================================
// 3. Dashboard View Initialization
// ==========================================================================
function initDashboard() {
    // Render source breakdown
    const sourceContainer = document.getElementById('source-breakdown-list');
    const sources = state.analytics.source_distribution || {};
    const maxSourceCount = Math.max(...Object.values(sources), 1);

    sourceContainer.innerHTML = Object.entries(sources)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 7)
        .map(([name, count]) => {
            const pct = Math.round((count / state.skills.length) * 100);
            return `
                <div class="breakdown-item">
                    <div class="breakdown-meta">
                        <span class="breakdown-name">${escapeHtml(name)}</span>
                        <span class="breakdown-count">${count} (${pct}%)</span>
                    </div>
                    <div class="progress-bar-bg">
                        <div class="progress-bar-fill" style="width: ${pct}%; background: var(--accent-indigo);"></div>
                    </div>
                </div>
            `;
        }).join('');

    // Render domain breakdown
    const domainContainer = document.getElementById('domain-breakdown-list');
    const domains = state.analytics.domain_distribution || {};
    
    domainContainer.innerHTML = Object.entries(domains)
        .sort((a, b) => b[1] - a[1])
        .map(([name, count]) => {
            const pct = Math.round((count / state.skills.length) * 100);
            let barColor = 'var(--accent-indigo)';
            if (name.includes('Game')) barColor = 'var(--accent-amber)';
            if (name.includes('Frontend')) barColor = 'var(--accent-cyan)';
            if (name.includes('Quality')) barColor = 'var(--accent-emerald)';
            if (name.includes('Context')) barColor = 'var(--accent-purple)';

            return `
                <div class="breakdown-item">
                    <div class="breakdown-meta">
                        <span class="breakdown-name">${escapeHtml(name)}</span>
                        <span class="breakdown-count">${count} (${pct}%)</span>
                    </div>
                    <div class="progress-bar-bg">
                        <div class="progress-bar-fill" style="width: ${pct}%; background: ${barColor};"></div>
                    </div>
                </div>
            `;
        }).join('');
}

// ==========================================================================
// 4. Catalog Filters & View
// ==========================================================================
function initCatalogFilters() {
    const searchInput = document.getElementById('catalog-search');
    const searchClear = document.getElementById('catalog-search-clear');
    const filterSuitability = document.getElementById('filter-suitability');
    const filterDomain = document.getElementById('filter-domain');
    const filterSource = document.getElementById('filter-source');

    // Populate source dropdown
    const sources = state.analytics.source_distribution || {};
    Object.keys(sources).sort().forEach(src => {
        const opt = document.createElement('option');
        opt.value = src;
        opt.textContent = `${src} (${sources[src]})`;
        filterSource.appendChild(opt);
    });

    // Search events
    searchInput.addEventListener('input', (e) => {
        state.filters.search = e.target.value.trim().toLowerCase();
        searchClear.classList.toggle('hidden', state.filters.search.length === 0);
        renderCatalog();
    });

    searchClear.addEventListener('click', () => {
        searchInput.value = '';
        state.filters.search = '';
        searchClear.classList.add('hidden');
        renderCatalog();
    });

    filterSuitability.addEventListener('change', (e) => {
        state.filters.suitability = e.target.value;
        renderCatalog();
    });

    filterDomain.addEventListener('change', (e) => {
        state.filters.domain = e.target.value;
        renderCatalog();
    });

    filterSource.addEventListener('change', (e) => {
        state.filters.source = e.target.value;
        renderCatalog();
    });

    // View toggle (Cards vs Table)
    const btnCards = document.getElementById('btn-view-cards');
    const btnTable = document.getElementById('btn-view-table');

    btnCards.addEventListener('click', () => {
        state.catalogViewMode = 'cards';
        btnCards.classList.add('active');
        btnTable.classList.remove('active');
        document.getElementById('catalog-cards-container').classList.remove('hidden');
        document.getElementById('catalog-table-container').classList.add('hidden');
    });

    btnTable.addEventListener('click', () => {
        state.catalogViewMode = 'table';
        btnTable.classList.add('active');
        btnCards.classList.remove('active');
        document.getElementById('catalog-cards-container').classList.add('hidden');
        document.getElementById('catalog-table-container').classList.remove('hidden');
    });
}

function initCatalog() {
    renderCatalog();
}

function getFilteredSkills() {
    return state.skills.filter(s => {
        // Suitability filter
        if (state.filters.suitability === 'high_value' && s.suitability !== 'high_value') return false;
        if (state.filters.suitability === 'unsuitable_ballast' && s.suitability !== 'unsuitable_ballast') return false;
        if (state.filters.suitability === 'specialized' && s.suitability !== 'specialized') return false;
        if (state.filters.suitability === 'duplicates_only' && (!s.exact_duplicates || s.exact_duplicates.length === 0)) return false;

        // Domain filter
        if (state.filters.domain !== 'all' && s.domain !== state.filters.domain) return false;

        // Source filter
        if (state.filters.source !== 'all' && s.source_group !== state.filters.source) return false;

        // Search text
        if (state.filters.search) {
            const query = state.filters.search;
            const matchName = s.name.toLowerCase().includes(query);
            const matchDesc = (s.description || '').toLowerCase().includes(query);
            const matchPath = s.path.toLowerCase().includes(query);
            const matchHeadings = (s.headings || []).some(h => h.toLowerCase().includes(query));
            if (!matchName && !matchDesc && !matchPath && !matchHeadings) return false;
        }

        return true;
    });
}

function renderCatalog() {
    const filtered = getFilteredSkills();
    document.getElementById('catalog-count').textContent = filtered.length;

    const cardsContainer = document.getElementById('catalog-cards-container');
    const tableBody = document.getElementById('catalog-table-body');

    // Render Cards
    cardsContainer.innerHTML = filtered.map(skill => {
        const isSelected = state.selectedCompareIds.includes(skill.id);
        const hasDupes = skill.exact_duplicates && skill.exact_duplicates.length > 0;
        
        // Suitability badge
        let badgeClass = 'badge-high';
        let badgeText = 'Hohe Relevanz';
        if (skill.suitability === 'unsuitable_ballast') {
            badgeClass = 'badge-ballast';
            badgeText = 'Gaming-Ballast';
        } else if (skill.suitability === 'specialized') {
            badgeClass = 'badge-specialized';
            badgeText = 'Spezialisiert (Qt)';
        }

        return `
            <div class="skill-card ${isSelected ? 'is-selected' : ''}" id="card-${skill.id}">
                <div class="card-top">
                    <div class="card-title-group">
                        <div class="card-title" title="${escapeHtml(skill.name)}">${escapeHtml(skill.name)}</div>
                        <div class="card-badges">
                            <span class="badge ${badgeClass}">${badgeText}</span>
                            <span class="badge badge-domain">${escapeHtml(skill.domain)}</span>
                            ${hasDupes ? `<span class="badge badge-duplicate">Duplikat (${skill.exact_duplicates.length})</span>` : ''}
                        </div>
                    </div>
                </div>

                <div class="card-desc">${escapeHtml(skill.description || 'Keine Beschreibung vorhanden.')}</div>

                <div class="card-headings-preview">
                    ${(skill.headings || []).slice(0, 3).map(h => `<span class="heading-tag"># ${escapeHtml(h)}</span>`).join('')}
                </div>

                <div class="card-footer">
                    <label class="compare-checkbox-label">
                        <input type="checkbox" onchange="toggleCompareSkill('${skill.id}')" ${isSelected ? 'checked' : ''}>
                        <span>Vergleichen</span>
                    </label>
                    <button class="btn btn-sm btn-outline" onclick="openSkillDetailModal('${skill.id}')">Details</button>
                </div>
            </div>
        `;
    }).join('');

    // Render Table Rows
    tableBody.innerHTML = filtered.map(skill => {
        const isSelected = state.selectedCompareIds.includes(skill.id);
        return `
            <tr>
                <td>
                    <input type="checkbox" onchange="toggleCompareSkill('${skill.id}')" ${isSelected ? 'checked' : ''}>
                </td>
                <td><strong>${escapeHtml(skill.name)}</strong></td>
                <td>${escapeHtml(skill.domain)}</td>
                <td><small>${escapeHtml(skill.source_group)}</small></td>
                <td>
                    <span class="badge ${skill.suitability === 'high_value' ? 'badge-high' : 'badge-ballast'}">
                        ${skill.suitability === 'high_value' ? 'Hohe Relevanz' : 'Ballast/Spezial'}
                    </span>
                </td>
                <td>${escapeHtml(skill.target_bundle || '-')}</td>
                <td>${skill.line_count}</td>
                <td>
                    <button class="btn btn-sm btn-outline" onclick="openSkillDetailModal('${skill.id}')">Details</button>
                </td>
            </tr>
        `;
    }).join('');
}

// ==========================================================================
// 5. Side-by-Side Comparator Logic
// ==========================================================================
function toggleCompareSkill(skillId) {
    const idx = state.selectedCompareIds.indexOf(skillId);
    if (idx > -1) {
        state.selectedCompareIds.splice(idx, 1);
    } else {
        if (state.selectedCompareIds.length >= 3) {
            alert('Sie können maximal 3 Skills gleichzeitig vergleichen. Bitte entfernen Sie zuerst einen Skill.');
            return;
        }
        state.selectedCompareIds.push(skillId);
    }

    updateCompareBadge();
    renderCatalog();
    if (state.currentTab === 'tab-comparator') {
        renderComparatorGrid();
    }
}

function updateCompareBadge() {
    const count = state.selectedCompareIds.length;
    document.getElementById('compare-count-badge').textContent = count;
    
    const hint = document.getElementById('comparator-hint');
    const namesSpan = document.getElementById('selected-compare-names');
    const openBtn = document.getElementById('btn-open-comparator');

    if (count > 0) {
        const names = state.selectedCompareIds
            .map(id => state.skills.find(s => s.id === id)?.name)
            .filter(Boolean)
            .join(', ');
        namesSpan.textContent = names;
        openBtn.style.display = 'inline-flex';
    } else {
        namesSpan.textContent = 'Keine';
        openBtn.style.display = 'none';
    }
}

function loadComparisonPreset(skillNames) {
    state.selectedCompareIds = [];
    skillNames.forEach(name => {
        const found = state.skills.find(s => s.name.toLowerCase().replace('_', '-') === name.toLowerCase().replace('_', '-'));
        if (found && !state.selectedCompareIds.includes(found.id)) {
            state.selectedCompareIds.push(found.id);
        }
    });

    updateCompareBadge();
    switchTab('tab-comparator');
    renderComparatorGrid();
}

function renderComparatorGrid() {
    const emptyState = document.getElementById('comparator-empty-state');
    const grid = document.getElementById('comparator-grid');

    if (state.selectedCompareIds.length === 0) {
        emptyState.classList.remove('hidden');
        grid.classList.add('hidden');
        return;
    }

    emptyState.classList.add('hidden');
    grid.classList.remove('hidden');

    const compareSkills = state.selectedCompareIds.map(id => state.skills.find(s => s.id === id)).filter(Boolean);

    grid.innerHTML = compareSkills.map(skill => {
        return `
            <div class="compare-column">
                <div class="compare-col-header">
                    <div>
                        <h3>${escapeHtml(skill.name)}</h3>
                        <small class="badge badge-source">${escapeHtml(skill.source_group)}</small>
                    </div>
                    <button class="btn btn-sm btn-outline" onclick="toggleCompareSkill('${skill.id}')">&times; Entfernen</button>
                </div>
                <div class="compare-col-body">
                    <div class="compare-meta-item">
                        <div class="compare-meta-label">Dateipfad</div>
                        <div class="compare-meta-val">${escapeHtml(skill.path)}</div>
                    </div>

                    <div class="compare-meta-item">
                        <div class="compare-meta-label">Domäne & Eignung</div>
                        <div>
                            <span class="badge badge-domain">${escapeHtml(skill.domain)}</span>
                            <span class="badge ${skill.suitability === 'high_value' ? 'badge-high' : 'badge-ballast'}">
                                ${skill.suitability === 'high_value' ? 'Arbeits-Relevant' : 'Ballast/Spezial'}
                            </span>
                        </div>
                    </div>

                    <div class="compare-meta-item">
                        <div class="compare-meta-label">Kennzahlen</div>
                        <div style="font-size:0.8rem; color:var(--text-secondary);">
                            <strong>${skill.line_count}</strong> Zeilen | <strong>${skill.char_count}</strong> Zeichen
                        </div>
                    </div>

                    <div class="compare-meta-item">
                        <div class="compare-meta-label">Beschreibung</div>
                        <div style="font-size:0.8rem; line-height:1.4;">${escapeHtml(skill.description || 'Keine Beschreibung.')}</div>
                    </div>

                    <div class="compare-meta-item">
                        <div class="compare-meta-label">Struktur & Überschriften</div>
                        <div style="display:flex; flex-direction:column; gap:0.25rem;">
                            ${(skill.headings || []).map(h => `<span class="heading-tag"># ${escapeHtml(h)}</span>`).join('')}
                        </div>
                    </div>

                    <div class="compare-meta-item">
                        <div class="compare-meta-label">Inhalt (Auszug)</div>
                        <pre class="code-preview-box"><code>${escapeHtml(skill.content_preview || 'Keine Vorschau verfügbar.')}</code></pre>
                    </div>
                </div>
            </div>
        `;
    }).join('');
}

// ==========================================================================
// 6. Duplicates Detector View
// ==========================================================================
function initDuplicatesView() {
    const container = document.getElementById('duplicate-groups-container');
    const dupeGroups = state.analytics.exact_duplicate_groups || [];

    if (dupeGroups.length === 0) {
        container.innerHTML = '<div class="empty-state"><h3>Keine Duplikate gefunden.</h3></div>';
        return;
    }

    container.innerHTML = dupeGroups.map((group, idx) => {
        return `
            <div class="card" style="margin-bottom: 1rem;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.75rem;">
                    <div>
                        <h4 style="font-size:1.05rem; color:var(--text-primary); margin-bottom:0.25rem;">
                            ${escapeHtml(group.name)} <span class="badge badge-duplicate">${group.count} identische Kopien</span>
                        </h4>
                        <div style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">
                            SHA256: ${group.hash.substring(0, 16)}...
                        </div>
                    </div>
                    <button class="btn btn-sm btn-outline" onclick="compareDuplicateGroup('${group.hash}')">
                        Nebeneinander vergleichen
                    </button>
                </div>
                <div style="display:flex; flex-direction:column; gap:0.4rem;">
                    ${group.instances.map((inst, i) => `
                        <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(255,255,255,0.02); padding:0.4rem 0.75rem; border-radius:4px; font-size:0.8rem; border:1px solid var(--border-subtle);">
                            <span style="font-family:var(--font-mono); color:${i === 0 ? 'var(--accent-emerald)' : 'var(--text-muted)'};">
                                ${i === 0 ? '✓ [Empfohlenes Original]' : '✗ [Redundante Kopie]'}: ${escapeHtml(inst.path)}
                            </span>
                            <span class="badge badge-source">${escapeHtml(inst.source)}</span>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }).join('');
}

function compareDuplicateGroup(hash) {
    const group = (state.analytics.exact_duplicate_groups || []).find(g => g.hash === hash);
    if (!group) return;

    state.selectedCompareIds = group.instances.slice(0, 3).map(i => i.id);
    updateCompareBadge();
    switchTab('tab-comparator');
    renderComparatorGrid();
}

// ==========================================================================
// 7. Master Bundles (Consolidation) View
// ==========================================================================
function initBundlesView() {
    const container = document.getElementById('master-bundles-container');

    container.innerHTML = state.bundles.map(bundle => {
        return `
            <div class="bundle-card">
                <div class="bundle-top">
                    <div class="bundle-icon-wrap" style="background: ${bundle.color}20; color: ${bundle.color}; border: 1px solid ${bundle.color}50;">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
                            <polyline points="2 17 12 22 22 17"></polyline>
                            <polyline points="2 12 12 17 22 12"></polyline>
                        </svg>
                    </div>
                    <div>
                        <div class="bundle-title">${escapeHtml(bundle.title)}</div>
                        <div class="bundle-tagline">${escapeHtml(bundle.tagline)}</div>
                        <div style="font-size:0.75rem; color:var(--accent-cyan); font-family:var(--font-mono); margin-top:0.25rem;">Trigger: ${escapeHtml(bundle.triggers || '')}</div>
                    </div>
                </div>

                <div class="bundle-summary">${escapeHtml(bundle.summary)}</div>

                <div class="bundle-included-box">
                    <div class="bundle-included-label">Konsolidiert diese ${bundle.skills_included.length} Einzel-Skills:</div>
                    <div class="bundle-chips">
                        ${bundle.skills_included.map(s => `<span class="bundle-chip">${escapeHtml(s)}</span>`).join('')}
                    </div>
                </div>

                <ul class="bundle-benefits-list">
                    ${bundle.benefits.map(b => `<li>${escapeHtml(b)}</li>`).join('')}
                </ul>

                <div class="bundle-footer">
                    <span style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">
                        ${bundle.is_automatic_layer ? 'rules/context-and-token-efficiency.md & hooks/hooks.json' : `consolidated-skills/${bundle.id}/SKILL.md`}
                    </span>
                    <button class="btn btn-sm btn-primary" onclick="showBundleSkillContent('${bundle.id}')">
                        ${bundle.is_automatic_layer ? 'Regel & Hook ansehen' : 'Instruktion ansehen'}
                    </button>
                </div>
            </div>
        `;
    }).join('');
}

function showBundleSkillContent(bundleId) {
    const bundle = state.bundles.find(b => b.id === bundleId);
    if (!bundle) return;

    const modal = document.getElementById('modal-skill-detail');
    document.getElementById('modal-skill-title').textContent = bundle.title;
    
    if (bundle.is_automatic_layer) {
        document.getElementById('modal-skill-source').textContent = 'Automatische System-Regel & SessionStart-Hook (Immer aktiv)';
        document.getElementById('modal-skill-body').innerHTML = `
            <div style="background: rgba(245, 158, 11, 0.1); border-left: 3px solid var(--accent-amber); padding: 0.85rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.85rem;">
                <strong>Architektur-Vorteil:</strong> Dieser Skill muss von keinem Mitarbeiter manuell aufgerufen werden. Er greift über <code>rules/context-and-token-efficiency.md</code> automatisch bei jedem Prompt und über <code>hooks/hooks.json</code> einmalig bei jedem Projektstart!
            </div>
            <div style="margin-bottom:1rem;">
                <p><strong>Ersetzt & automatisiert folgende 10 Einzel-Skills:</strong></p>
                <div class="bundle-chips" style="margin-top:0.5rem;">
                    ${bundle.skills_included.map(s => `<span class="bundle-chip">${escapeHtml(s)}</span>`).join('')}
                </div>
            </div>
            <p><strong>Automatisierungs-Vorteile für das Team:</strong></p>
            <ul class="bundle-benefits-list" style="margin-bottom:1rem;">
                ${bundle.benefits.map(b => `<li>${escapeHtml(b)}</li>`).join('')}
            </ul>
            <p><strong>Regeldatei (Dauerhaft im Hintergrund):</strong></p>
            <pre class="code-box"><code>rules/context-and-token-efficiency.md</code></pre>
            <p style="margin-top:0.75rem;"><strong>Hook-Konfiguration (Einmalig bei SessionStart):</strong></p>
            <pre class="code-box"><code>hooks/hooks.json</code></pre>
        `;
    } else {
        document.getElementById('modal-skill-source').textContent = `Konsolidierter Master-Skill (consolidated-skills/${bundle.id}/SKILL.md)`;
        document.getElementById('modal-skill-body').innerHTML = `
            <div style="margin-bottom:1rem;">
                <p><strong>Ersetzt folgende Einzel-Skills:</strong></p>
                <div class="bundle-chips" style="margin-top:0.5rem;">
                    ${bundle.skills_included.map(s => `<span class="bundle-chip">${escapeHtml(s)}</span>`).join('')}
                </div>
            </div>
            <p><strong>Team-Vorteile:</strong></p>
            <ul class="bundle-benefits-list" style="margin-bottom:1rem;">
                ${bundle.benefits.map(b => `<li>${escapeHtml(b)}</li>`).join('')}
            </ul>
            <p><strong>SKILL.md Pfad im Projekt:</strong></p>
            <pre class="code-box"><code>consolidated-skills/${bundle.id}/SKILL.md</code></pre>
        `;
    }

    document.getElementById('modal-btn-compare').style.display = 'none';
    modal.classList.remove('hidden');
}

// ==========================================================================
// 8. Modals Management
// ==========================================================================
function openSkillDetailModal(skillId) {
    const skill = state.skills.find(s => s.id === skillId);
    if (!skill) return;

    const modal = document.getElementById('modal-skill-detail');
    document.getElementById('modal-skill-title').textContent = skill.name;
    document.getElementById('modal-skill-source').textContent = `${skill.source_group} • ${skill.path}`;

    document.getElementById('modal-skill-body').innerHTML = `
        <div style="margin-bottom:1rem;">
            <div style="font-size:0.75rem; color:var(--text-muted); margin-bottom:0.25rem;">BESCHREIBUNG:</div>
            <p style="font-size:0.9rem; line-height:1.4;">${escapeHtml(skill.description || 'Keine Beschreibung vorhanden.')}</p>
        </div>

        <div style="margin-bottom:1rem; display:flex; gap:1rem;">
            <div>
                <div style="font-size:0.75rem; color:var(--text-muted);">DOMÄNE</div>
                <div><span class="badge badge-domain">${escapeHtml(skill.domain)}</span></div>
            </div>
            <div>
                <div style="font-size:0.75rem; color:var(--text-muted);">EIGNUNG FÜR ARBEIT</div>
                <div>
                    <span class="badge ${skill.suitability === 'high_value' ? 'badge-high' : 'badge-ballast'}">
                        ${skill.suitability === 'high_value' ? 'Hohe Relevanz' : 'Ballast/Spezial'}
                    </span>
                </div>
            </div>
            <div>
                <div style="font-size:0.75rem; color:var(--text-muted);">GRÖSSE</div>
                <div style="font-size:0.85rem; font-family:var(--font-mono);">${skill.line_count} Zeilen</div>
            </div>
        </div>

        <div style="margin-bottom:1rem;">
            <div style="font-size:0.75rem; color:var(--text-muted); margin-bottom:0.25rem;">EINSCHÄTZUNG / GRUND:</div>
            <div style="font-size:0.85rem; color:var(--text-secondary); background:rgba(255,255,255,0.03); padding:0.5rem; border-radius:4px;">
                ${escapeHtml(skill.suitability_reason || 'Keine spezifische Anmerkung.')}
            </div>
        </div>

        <div style="margin-bottom:1rem;">
            <div style="font-size:0.75rem; color:var(--text-muted); margin-bottom:0.25rem;">INHALT-VORSCHAU:</div>
            <pre class="code-box"><code>${escapeHtml(skill.content_preview)}</code></pre>
        </div>
    `;

    const compareBtn = document.getElementById('modal-btn-compare');
    compareBtn.style.display = 'inline-flex';
    compareBtn.onclick = () => {
        toggleCompareSkill(skill.id);
        closeSkillDetailModal();
    };

    modal.classList.remove('hidden');
}

function closeSkillDetailModal() {
    document.getElementById('modal-skill-detail').classList.add('hidden');
}

function openCleanupModal() {
    const modal = document.getElementById('modal-cleanup');
    const scriptBox = document.getElementById('cleanup-script-content');

    const psScript = `# =====================================================================
# PowerShell Bereinigungs-Skript: Redundante Skills entfernen & sichern
# Erstellt von SkillLens Pro am ${new Date().toLocaleDateString('de-DE')}
# =====================================================================

Write-Host "Starte Bereinigung von redundanten Skill-Kopien..." -ForegroundColor Cyan

# 1. Backup-Ordner anlegen
$backupDir = "$HOME\\.gemini\\skills_backup_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
New-Item -ItemType Directory -Path $backupDir -Force | Out-Null
Write-Host "Backup-Verzeichnis erstellt: $backupDir" -ForegroundColor Green

# 2. Redundante Kopien aus .openclaw entfernen (exakte Clones des Hauptplugins)
$openclawDir = "$HOME\\.gemini\\config\\plugins\\ponytail\\.openclaw"
if (Test-Path $openclawDir) {
    Write-Host "Sichere und bereinige .openclaw Duplikate..." -ForegroundColor Yellow
    Copy-Item -Path $openclawDir -Destination "$backupDir\\openclaw" -Recurse -Force
    Remove-Item -Path $openclawDir -Recurse -Force
    Write-Host ".openclaw Duplikate erfolgreich entfernt!" -ForegroundColor Green
}

# 3. Doppel-Dateien mit Unterstrich in data-agent-kit bereinigen (bigquery_*.md)
$dakDir = "$HOME\\.gemini\\config\\plugins\\data-agent-kit-plugin\\skills"
if (Test-Path $dakDir) {
    Get-ChildItem -Path $dakDir -Directory -Filter "*_*" | ForEach-Object {
        Write-Host "Bereinige redundantes Namens-Duplikat: $($_.Name)" -ForegroundColor Yellow
        Copy-Item -Path $_.FullName -Destination "$backupDir\\$($_.Name)" -Recurse -Force
        Remove-Item -Path $_.FullName -Recurse -Force
    }
}

Write-Host "Bereinigung abgeschlossen! Alle Originale wurden im Backup gesichert." -ForegroundColor Green
`;

    scriptBox.textContent = psScript;
    modal.classList.remove('hidden');
}

function closeCleanupModal() {
    document.getElementById('modal-cleanup').classList.add('hidden');
}

function copyCleanupScript() {
    const text = document.getElementById('cleanup-script-content').textContent;
    navigator.clipboard.writeText(text).then(() => {
        alert('PowerShell-Skript erfolgreich in die Zwischenablage kopiert!');
    });
}

// Utility: HTML escape
function escapeHtml(str) {
    if (!str) return '';
    return str
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}
