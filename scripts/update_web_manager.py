import re

with open('/Users/ricardomarimodinger/.gemini/antigravity/scratch/ricardo-ai-system/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "// --- Web Page Manager & File System Sync Module ---"
end_marker = "// --- Interactive 3.0x Calculator Module ---"

new_module = r"""// --- Web Page Manager & File System Sync Module ---
        let webProjects = [];
        let activeProjectId = null;
        let activeProjectHandle = null;

        function initWebManagerConnection() {
            try {
                const data = localStorage.getItem('dashboard_web_projects');
                if (data) {
                    webProjects = JSON.parse(data);
                } else {
                    webProjects = [{
                        id: 'router_website',
                        name: 'Router Seguridad',
                        url: 'https://router-seguridad-tecnologia.vercel.app',
                        hosting: 'Vercel',
                        username: 'hostalplazalebu',
                        password: '',
                        hasAuraNews: true
                    }];
                    saveWebProjects();
                }
            } catch(e) {}
        }
        initWebManagerConnection();

        function saveWebProjects() {
            try { localStorage.setItem('dashboard_web_projects', JSON.stringify(webProjects)); } catch(e) {}
        }

        function openWebManager() {
            const overlay = document.getElementById('drawer-overlay');
            const drawer = document.getElementById('drawer');
            const drawerTitle = document.getElementById('drawer-title');
            const content = document.getElementById('drawer-content');

            if (!overlay || !drawer) return;

            drawerTitle.textContent = "Hub Central de Páginas Web";

            if (!document.getElementById('web-manager-styles')) {
                const style = document.createElement('style');
                style.id = 'web-manager-styles';
                style.innerHTML = `
                    .web-manager-wrapper { padding: 5px; color: var(--color-text-dark); }
                    .web-manager-card {
                        background: #fff;
                        border: 1px solid #e2e8f0;
                        border-radius: 12px;
                        padding: 16px;
                        margin-bottom: 20px;
                        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
                    }
                    .web-manager-card h3 { margin: 0 0 10px 0; color: #1e293b; font-size: 1.1rem; display:flex; align-items:center; gap:8px;}
                    .web-field { font-size: 0.9rem; color: #475569; margin-bottom: 6px; }
                    .web-field strong { color: #1e293b; }
                    .web-actions { margin-top: 15px; display: flex; gap: 10px; flex-wrap: wrap; }
                    .btn-small { padding: 6px 12px; font-size: 0.85rem; border-radius: 6px; cursor: pointer; border: none; font-weight: 500; }
                    .btn-primary { background: var(--color-primary); color: white; }
                    .btn-outline { background: white; border: 1px solid #cbd5e1; color: #475569; }
                    .btn-danger { background: #fee2e2; color: #ef4444; }
                    
                    .dir-status-box { padding: 10px; border-radius: 8px; font-size: 0.9rem; margin-top:10px; font-weight: 600; display:flex; align-items:center; gap:8px;}
                    .connection-disconnected { background: #fee2e2; color: #ef4444; border: 1px solid #fca5a5; }
                    .connection-connected { background: #dcfce7; color: #10b981; border: 1px solid #86efac; }
                    .news-manage-list { margin-top: 10px; background: #f8fafc; border-radius: 8px; border: 1px solid #e2e8f0; overflow:hidden;}
                    .news-manage-item { display:flex; padding: 12px; border-bottom: 1px solid #e2e8f0; align-items:center; justify-content:space-between; gap:10px;}
                    .news-manage-item:last-child { border-bottom: none; }
                    .news-manage-info { flex: 1; }
                    .news-manage-info h4 { margin:0 0 4px 0; font-size:0.9rem; color:#0f172a; display:-webkit-box; -webkit-line-clamp:1; -webkit-box-orient:vertical; overflow:hidden; }
                    .news-manage-info p { margin:0; font-size:0.8rem; color:#64748b; }
                    .password-reveal { background: #f1f5f9; padding: 4px 8px; border-radius: 4px; font-family: monospace; cursor:pointer; }
                    
                    .notification-banner {
                        background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2);
                        color: #10b981; padding: 10px 14px; border-radius: 8px; font-size: 0.85rem;
                        margin-bottom: 12px;
                    }
                `;
                document.head.appendChild(style);
            }

            renderWebHubUI(content);

            overlay.classList.add('open');
            drawer.classList.add('open');
            document.body.style.overflow = 'hidden';
        }

        function renderWebHubUI(content) {
            let html = `<div class="web-manager-wrapper">`;
            html += `<div id="webSyncNotification" style="display: none;" class="notification-banner"></div>`;
            
            html += `<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                        <p style="margin:0; font-size:0.9rem; color:#64748b;">Administra accesos y carpetas locales.</p>
                        <button class="btn-small btn-primary" onclick="promptNewProject()">+ Nuevo Proyecto</button>
                     </div>`;

            webProjects.forEach(proj => {
                html += `
                <div class="web-manager-card" id="card-${proj.id}">
                    <h3>🌐 ${proj.name}</h3>
                    <div class="web-field"><strong>URL:</strong> <a href="${proj.url}" target="_blank" style="color:var(--color-primary)">${proj.url}</a></div>
                    <div class="web-field"><strong>Hosting:</strong> ${proj.hosting}</div>
                    <div class="web-field"><strong>Usuario:</strong> ${proj.username || '-'}</div>
                    <div class="web-field"><strong>Clave:</strong> <span class="password-reveal" onclick="togglePassword(this, '${proj.password}')">•••••••• (Ver)</span></div>
                    
                    <div class="web-actions">
                        <button class="btn-small btn-outline" onclick="editProject('${proj.id}')">Editar</button>
                        <button class="btn-small btn-danger" onclick="deleteProject('${proj.id}')">Eliminar</button>
                    </div>

                    ${proj.hasAuraNews ? renderAuraNewsSection(proj.id) : ''}
                </div>`;
            });

            html += `</div>`;
            content.innerHTML = html;
            
            // Check statuses asynchronously
            webProjects.forEach(proj => {
                if (proj.hasAuraNews) {
                    checkProjectFolderStatus(proj.id);
                }
            });
        }

        function renderAuraNewsSection(id) {
            return `
            <div style="margin-top: 20px; border-top: 1px solid #e2e8f0; padding-top: 15px;">
                <h4 style="margin:0 0 10px 0; font-size:0.95rem; color:#1e293b;">📰 Sincronización de Noticias (Aura)</h4>
                <div id="status-${id}" class="dir-status-box connection-disconnected">
                    <span>🔴 Buscando carpeta local...</span>
                </div>
                <div class="web-actions">
                    <button id="btn-link-${id}" class="btn-small btn-primary" onclick="linkProjectFolder('${id}')">Vincular Carpeta</button>
                </div>
                
                <div class="news-manage-list" id="news-list-${id}" style="display:none; margin-top:15px;">
                    <p style="color: var(--text-dim); font-size: 0.85rem; text-align: center; padding: 20px;">Cargando artículos...</p>
                </div>
            </div>`;
        }

        function togglePassword(element, pwd) {
            if (element.textContent.includes('••••••••')) {
                element.textContent = pwd || '(vacío)';
            } else {
                element.textContent = '•••••••• (Ver)';
            }
        }

        function promptNewProject() {
            const name = prompt("Nombre del Proyecto Web:");
            if (!name) return;
            const url = prompt("URL del sitio:");
            const hosting = prompt("Plataforma de Hosting (ej: Vercel):");
            const username = prompt("Usuario de acceso:");
            const password = prompt("Contraseña:");
            const hasAuraNews = confirm("¿Habilitar módulo de noticias sincronizado con Aura para esta web?");
            
            const newProj = {
                id: 'proj_' + Date.now(),
                name, url, hosting, username, password, hasAuraNews
            };
            webProjects.push(newProj);
            saveWebProjects();
            renderWebHubUI(document.getElementById('drawer-content'));
        }

        function editProject(id) {
            const p = webProjects.find(x => x.id === id);
            if (!p) return;
            const pwd = prompt("Nueva contraseña (deja vacío para no cambiar):", p.password);
            if (pwd !== null) {
                p.password = pwd;
                saveWebProjects();
                renderWebHubUI(document.getElementById('drawer-content'));
            }
        }

        function deleteProject(id) {
            if(confirm("¿Seguro que quieres eliminar este proyecto del Hub?")) {
                webProjects = webProjects.filter(x => x.id !== id);
                saveWebProjects();
                renderWebHubUI(document.getElementById('drawer-content'));
            }
        }

        // --- FS API Logic ---
        const DB_NAME = "RicardoHubDB";
        function getDB() {
            return new Promise((resolve, reject) => {
                const request = indexedDB.open(DB_NAME, 2);
                request.onupgradeneeded = e => {
                    const db = e.target.result;
                    if(!db.objectStoreNames.contains('directories')) {
                        db.createObjectStore('directories');
                    }
                };
                request.onsuccess = e => resolve(e.target.result);
                request.onerror = e => reject(e.target.error);
            });
        }

        async function getDirectoryHandle(id) {
            try {
                const db = await getDB();
                return new Promise((resolve, reject) => {
                    const t = db.transaction('directories', 'readonly');
                    const store = t.objectStore('directories');
                    const req = store.get(id);
                    req.onsuccess = () => resolve(req.result);
                    req.onerror = () => reject(req.error);
                });
            } catch(e) { return null; }
        }

        async function saveDirectoryHandle(id, handle) {
            try {
                const db = await getDB();
                const t = db.transaction('directories', 'readwrite');
                t.objectStore('directories').put(handle, id);
            } catch(e) { console.error(e); }
        }

        async function unlinkProjectFolder(id) {
            try {
                const db = await getDB();
                const t = db.transaction('directories', 'readwrite');
                t.objectStore('directories').delete(id);
                activeProjectHandle = null;
                activeProjectId = null;
                showWebSyncNotification("🔴 Carpeta desvinculada.");
                checkProjectFolderStatus(id);
            } catch(e) {}
        }

        async function checkProjectFolderStatus(id) {
            const statusBox = document.getElementById('status-' + id);
            const linkBtn = document.getElementById('btn-link-' + id);
            const newsList = document.getElementById('news-list-' + id);
            if(!statusBox) return;

            const handle = await getDirectoryHandle(id);
            if (!handle) {
                statusBox.className = "dir-status-box connection-disconnected";
                statusBox.innerHTML = '<span>🔴 No Vinculado</span>';
                linkBtn.textContent = "Vincular Carpeta";
                linkBtn.style.display = "inline-block";
                linkBtn.onclick = () => linkProjectFolder(id);
                newsList.style.display = "none";
                return;
            }

            try {
                const perm = await handle.queryPermission({ mode: 'readwrite' });
                if (perm === 'granted') {
                    statusBox.className = "dir-status-box connection-connected";
                    statusBox.innerHTML = '<span>🟢 Conectado: ' + handle.name + '</span>';
                    linkBtn.textContent = "Desvincular";
                    linkBtn.onclick = () => unlinkProjectFolder(id);
                    linkBtn.className = "btn-small btn-danger";
                    newsList.style.display = "block";
                    activeProjectHandle = handle;
                    activeProjectId = id;
                    renderProjectNewsList(id);
                } else {
                    statusBox.className = "dir-status-box connection-disconnected";
                    statusBox.innerHTML = '<span>🟡 Requiere Permisos de Navegador</span>';
                    linkBtn.textContent = "Autorizar Acceso";
                    linkBtn.onclick = async () => {
                        if ((await handle.requestPermission({ mode: 'readwrite' })) === 'granted') {
                            showWebSyncNotification("🟢 Permisos concedidos.");
                            checkProjectFolderStatus(id);
                        }
                    };
                }
            } catch(e) {
                unlinkProjectFolder(id);
            }
        }

        async function linkProjectFolder(id) {
            try {
                const handle = await window.showDirectoryPicker();
                // Validate if it has js folder inside (basic validation)
                try {
                    await handle.getDirectoryHandle('js');
                } catch(e) {
                    showWebSyncNotification("⚠️ La carpeta no parece ser un proyecto web válido (falta carpeta js/).", true);
                }
                const perm = await handle.queryPermission({ mode: 'readwrite' });
                if(perm === 'prompt') await handle.requestPermission({ mode: 'readwrite' });
                await saveDirectoryHandle(id, handle);
                showWebSyncNotification("🟢 Carpeta vinculada exitosamente.");
                checkProjectFolderStatus(id);
            } catch(e) {
                console.log("Picker cancelled");
            }
        }

        function renderProjectNewsList(id) {
            const list = document.getElementById('news-list-' + id);
            if(!list) return;

            let publishedIds = [];
            try {
                publishedIds = JSON.parse(localStorage.getItem('router_web_published_news') || '[117, 118, 119]');
            } catch(e) { publishedIds = [117, 118, 119]; }

            const newsItems = bitacoraData.filter(item => item.tag === "Noticias");
            
            if(newsItems.length === 0) {
                list.innerHTML = '<p style="padding:15px;text-align:center;color:#64748b;">No hay noticias creadas por Aura aún.</p>';
                return;
            }

            let html = '';
            newsItems.forEach(item => {
                const isPub = publishedIds.includes(item.id);
                html += `
                <div class="news-manage-item">
                    <div class="news-manage-info">
                        <h4>${item.title}</h4>
                        <p>${item.date} | ${isPub ? '<strong style="color:#10b981;">Publicado</strong>' : 'Borrador'}</p>
                    </div>
                    <button class="btn-small ${isPub ? 'btn-danger' : 'btn-primary'}" onclick="toggleNewsPublish(${item.id}, '${id}')">
                        ${isPub ? 'Ocultar' : 'Publicar'}
                    </button>
                </div>`;
            });
            list.innerHTML = html;
        }

        async function toggleNewsPublish(newsId, projectId) {
            let publishedIds = [];
            try {
                publishedIds = JSON.parse(localStorage.getItem('router_web_published_news') || '[117, 118, 119]');
            } catch(e) { publishedIds = [117, 118, 119]; }

            if (publishedIds.includes(newsId)) {
                publishedIds = publishedIds.filter(id => id !== newsId);
            } else {
                publishedIds.unshift(newsId);
                if (publishedIds.length > 3) publishedIds = publishedIds.slice(0, 3);
            }

            try { localStorage.setItem('router_web_published_news', JSON.stringify(publishedIds)); } catch(e){}
            renderProjectNewsList(projectId);
            await syncProjectNewsToFileSystem(projectId);
        }

        async function syncProjectNewsToFileSystem(projectId) {
            if (activeProjectId !== projectId || !activeProjectHandle) return;
            
            const handle = activeProjectHandle;
            const permission = await handle.queryPermission({ mode: 'readwrite' });
            if (permission !== 'granted') return;

            try {
                let publishedIds = JSON.parse(localStorage.getItem('router_web_published_news') || '[117, 118, 119]');
                const newsItems = bitacoraData.filter(item => item.tag === "Noticias");
                
                const activeNewsList = [];
                publishedIds.forEach(id => {
                    const article = newsItems.find(item => item.id === id);
                    if (article) activeNewsList.push({
                        id: article.id, date: article.date, title: article.title,
                        desc: article.desc, image: article.image, content: article.content
                    });
                });

                const jsDirHandle = await handle.getDirectoryHandle('js', { create: true });
                const fileHandle = await jsDirHandle.getFileHandle('news-data.js', { create: true });
                const writable = await fileHandle.createWritable();
                const content = `// Archivo generado automáticamente por Ricardo AI System. NO EDITAR DIRECTAMENTE.\nconst ROUTER_NEWS_DATA = ${JSON.stringify(activeNewsList, null, 2)};\n`;
                await writable.write(content);
                await writable.close();
                showWebSyncNotification("⚡ Sincronización exitosa: Sitio web local actualizado.");
            } catch (e) {
                console.error(e);
                showWebSyncNotification("⚠️ Error al escribir el archivo local news-data.js", true);
            }
        }

        function showWebSyncNotification(msg, isWarning = false) {
            const banner = document.getElementById('webSyncNotification');
            if (!banner) return;
            banner.style.display = 'block';
            banner.textContent = msg;
            if (isWarning) { banner.style.background = 'rgba(245,158,11,0.1)'; banner.style.color = '#f59e0b'; }
            else if (msg.includes('Error') || msg.includes('desvinculada')) { banner.style.background = 'rgba(239,68,68,0.1)'; banner.style.color = '#ef4444'; }
            else { banner.style.background = 'rgba(16,185,129,0.1)'; banner.style.color = '#10b981'; }
            setTimeout(() => { if(banner) banner.style.display='none'; }, 4000);
        }

        // Expose functions
        window.openWebManager = openWebManager;
        window.togglePassword = togglePassword;
        window.promptNewProject = promptNewProject;
        window.editProject = editProject;
        window.deleteProject = deleteProject;
        window.linkProjectFolder = linkProjectFolder;
        window.unlinkProjectFolder = unlinkProjectFolder;
        window.toggleNewsPublish = toggleNewsPublish;
"""

pattern = re.compile(re.escape(start_marker) + r".*?" + re.escape(end_marker), re.DOTALL)
new_content = pattern.sub(new_module + "\n        " + end_marker, content)

with open('/Users/ricardomarimodinger/.gemini/antigravity/scratch/ricardo-ai-system/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated index.html successfully.")
