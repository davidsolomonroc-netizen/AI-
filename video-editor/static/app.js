// --- State ---
let files = [];
let sessionId = null;
let segments = [];
let currentAudio = null;

// --- DOM refs ---
const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const fileList = document.getElementById('file-list');
const settings = document.getElementById('settings');
const analyzeBtn = document.getElementById('analyze-btn');
const analyzeStatus = document.getElementById('analyze-status');
const reviewSection = document.getElementById('review-section');
const segmentList = document.getElementById('segment-list');
const keepTime = document.getElementById('keep-time');
const cutTime = document.getElementById('cut-time');
const totalTime = document.getElementById('total-time');
const exportBtn = document.getElementById('export-btn');
const exportStatus = document.getElementById('export-status');
const similaritySlider = document.getElementById('similarity-threshold');
const similarityValue = document.getElementById('similarity-value');
const toast = document.getElementById('toast');

// --- Toast ---
function showToast(msg, duration = 2000) {
    toast.textContent = msg;
    toast.style.display = 'block';
    setTimeout(() => toast.style.display = 'none', duration);
}

// --- Format time ---
function fmtTime(s) {
    const m = Math.floor(s / 60);
    const sec = Math.floor(s % 60);
    return `${m}:${sec.toString().padStart(2, '0')}`;
}

// --- Similarity slider ---
similaritySlider.addEventListener('input', () => {
    similarityValue.textContent = similaritySlider.value + '%';
});

// --- File upload / drag-drop ---
dropZone.addEventListener('click', () => fileInput.click());
fileInput.addEventListener('change', (e) => addFiles(e.target.files));

dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});
dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragover'));
dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    addFiles(e.dataTransfer.files);
});

function addFiles(newFiles) {
    for (const f of newFiles) {
        if (!f.type.startsWith('video/')) continue;
        files.push({
            name: f.name,
            duration: null,
            url: URL.createObjectURL(f),
            file: f,
        });
    }
    if (files.length > 0) settings.style.display = 'block';
    renderFileList();
}

function renderFileList() {
    fileList.innerHTML = files.map((f, i) => `
        <li class="file-item" draggable="true" data-index="${i}">
            <span class="handle">≡</span>
            <span class="name">${f.name}</span>
            <span class="dur">${f.duration ? f.duration + 's' : ''}</span>
            <button class="btn-play" data-index="${i}">▶</button>
            <button class="btn-sm" data-index="${i}">✕</button>
        </li>
    `).join('');

    analyzeBtn.disabled = files.length === 0;

    fileList.querySelectorAll('.file-item').forEach(item => {
        item.addEventListener('dragstart', handleDragStart);
        item.addEventListener('dragover', handleDragOver);
        item.addEventListener('dragleave', handleDragLeave);
        item.addEventListener('drop', handleDrop);
        item.addEventListener('dragend', handleDragEnd);
    });

    fileList.querySelectorAll('.btn-play').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const idx = parseInt(btn.dataset.index);
            const f = files[idx];
            if (currentAudio) { currentAudio.pause(); currentAudio = null; }
            if (f.url) {
                currentAudio = new Audio(f.url);
                currentAudio.play();
            }
        });
    });

    fileList.querySelectorAll('.btn-sm').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const idx = parseInt(btn.dataset.index);
            if (currentAudio) { currentAudio.pause(); currentAudio = null; }
            files.splice(idx, 1);
            if (files.length === 0) settings.style.display = 'none';
            renderFileList();
        });
    });
}

// --- Drag and drop sorting ---
let dragSrcIndex = null;

function handleDragStart(e) {
    dragSrcIndex = parseInt(this.dataset.index);
    this.classList.add('dragging');
    e.dataTransfer.effectAllowed = 'move';
}

function handleDragOver(e) {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
    this.classList.add('drag-over');
}

function handleDragLeave() {
    this.classList.remove('drag-over');
}

function handleDrop(e) {
    e.preventDefault();
    this.classList.remove('drag-over');
    const targetIdx = parseInt(this.dataset.index);
    if (dragSrcIndex !== null && dragSrcIndex !== targetIdx) {
        const [moved] = files.splice(dragSrcIndex, 1);
        files.splice(targetIdx, 0, moved);
        renderFileList();
    }
}

function handleDragEnd() {
    this.classList.remove('dragging');
    fileList.querySelectorAll('.file-item').forEach(el => el.classList.remove('drag-over'));
    dragSrcIndex = null;
}

// --- Upload to server ---
async function uploadFiles() {
    const formData = new FormData();
    for (const f of files) {
        formData.append('files', f.file);
    }
    const resp = await fetch('/api/upload', { method: 'POST', body: formData });
    if (!resp.ok) throw new Error('Upload failed');
    const data = await resp.json();
    sessionId = data.session_id;
    return data;
}

// --- Upload to server ---
async function uploadFiles() {
    const formData = new FormData();
    for (const f of files) {
        formData.append('files', f.file);
    }
    const resp = await fetch('/api/upload', { method: 'POST', body: formData });
    if (!resp.ok) throw new Error('Upload failed');
    const data = await resp.json();
    sessionId = data.session_id;
    return data;
}

// --- Progress bar ---
const progressArea = document.getElementById('progress-area');
const progressFill = document.getElementById('progress-fill');
const progressText = document.getElementById('progress-text');

function showProgress(msg, pct) {
    progressArea.style.display = 'block';
    progressText.textContent = msg;
    if (pct !== undefined) {
        progressFill.style.width = (pct * 100) + '%';
    }
}

function hideProgress() {
    progressArea.style.display = 'none';
    progressFill.style.width = '0%';
}

// --- Analyze (SSE stream) ---
analyzeBtn.addEventListener('click', async () => {
    try {
        analyzeBtn.disabled = true;
        analyzeStatus.textContent = '正在上传...';

        await uploadFiles();
        analyzeStatus.textContent = '';
        showProgress('准备分析...', 0);

        const formData = new FormData();
        formData.append('session_id', sessionId);
        formData.append('file_order', JSON.stringify(files.map(f => f.name)));
        formData.append('silence_threshold', document.getElementById('silence-threshold').value);
        formData.append('similarity_threshold', similaritySlider.value / 100);
        formData.append('filler_words', document.getElementById('filler-words').value);

        const resp = await fetch('/api/analyze', { method: 'POST', body: formData });
        if (!resp.ok) {
            const err = await resp.json();
            throw new Error(err.detail || 'Analysis failed');
        }

        // Read SSE stream
        const reader = resp.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            buffer += decoder.decode(value, { stream: true });
            const lines = buffer.split('\n');
            buffer = lines.pop() || '';

            for (const line of lines) {
                if (line.startsWith('data: ')) {
                    const event = JSON.parse(line.slice(6));

                    if (event.step === 'concat') {
                        showProgress(event.message, 0.02);
                    } else if (event.step === 'transcribe') {
                        showProgress(event.message, 0.05 + event.progress * 0.85);
                    } else if (event.step === 'detect') {
                        showProgress(event.message, 0.92);
                    } else if (event.step === 'done') {
                        showProgress('分析完成', 1);
                        segments = event.segments;
                        renderSegments();
                        setTimeout(hideProgress, 800);
                        reviewSection.style.display = 'block';
                        reviewSection.scrollIntoView({ behavior: 'smooth' });
                        analyzeStatus.textContent = '分析完成';
                    }
                }
            }
        }

        analyzeBtn.disabled = false;
    } catch (err) {
        hideProgress();
        analyzeStatus.textContent = '错误: ' + err.message;
        analyzeBtn.disabled = false;
    }
});

// --- Render segments ---
function renderSegments() {
    let keepTotal = 0, cutTotal = 0;

    segmentList.innerHTML = segments.map(seg => {
        const dur = seg.end - seg.start;
        if (seg.action === 'keep') keepTotal += dur;
        else cutTotal += dur;

        return `
            <li class="segment-item ${seg.action}" data-index="${seg.index}">
                <span class="seg-time">${fmtTime(seg.start)} - ${fmtTime(seg.end)}</span>
                <span class="seg-text" title="${escapeHtml(seg.text)}">${escapeHtml(seg.text) || '[静音]'}</span>
                ${seg.reason ? `<span class="seg-reason">${escapeHtml(seg.reason)}</span>` : ''}
                <label class="toggle">
                    <input type="checkbox" ${seg.action === 'keep' ? 'checked' : ''} data-index="${seg.index}">
                    <span class="slider"></span>
                </label>
            </li>
        `;
    }).join('');

    keepTime.textContent = fmtTime(keepTotal);
    cutTime.textContent = fmtTime(cutTotal);
    totalTime.textContent = fmtTime(keepTotal + cutTotal);

    segmentList.querySelectorAll('input[type=checkbox]').forEach(cb => {
        cb.addEventListener('change', () => {
            const idx = parseInt(cb.dataset.index);
            segments[idx].action = cb.checked ? 'keep' : 'cut';
            updateStats();
            const item = cb.closest('.segment-item');
            item.classList.toggle('keep', cb.checked);
            item.classList.toggle('cut', !cb.checked);
        });
    });
}

function updateStats() {
    let keepTotal = 0, cutTotal = 0;
    for (const seg of segments) {
        const dur = seg.end - seg.start;
        if (seg.action === 'keep') keepTotal += dur;
        else cutTotal += dur;
    }
    keepTime.textContent = fmtTime(keepTotal);
    cutTime.textContent = fmtTime(cutTotal);
}

function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

// --- Export ---
exportBtn.addEventListener('click', async () => {
    try {
        exportBtn.disabled = true;
        exportStatus.textContent = '正在导出...';

        const keepIntervals = segments
            .filter(s => s.action === 'keep')
            .map(s => [s.start, s.end]);

        const formData = new FormData();
        formData.append('session_id', sessionId);
        formData.append('keep_intervals', JSON.stringify(keepIntervals));

        const resp = await fetch('/api/export', { method: 'POST', body: formData });
        if (!resp.ok) {
            const err = await resp.json();
            throw new Error(err.detail || 'Export failed');
        }

        const blob = await resp.blob();
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'output.mp4';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);

        exportStatus.textContent = '导出完成';
        exportBtn.disabled = false;
        showToast('视频已导出');
    } catch (err) {
        exportStatus.textContent = '错误: ' + err.message;
        exportBtn.disabled = false;
    }
});
