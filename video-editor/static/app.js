// --- State ---
let files = [];
let sessionId = null;
let segments = [];
let currentAudio = null;
let currentStyle = '';
let keywords = [];
let highlights = [];

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
const progressArea = document.getElementById('progress-area');
const progressFill = document.getElementById('progress-fill');
const progressText = document.getElementById('progress-text');
const previewPlayer = document.getElementById('preview-player');
const previewVideo = document.getElementById('preview-video');
const previewLabel = document.getElementById('preview-label');
const tabRough = document.getElementById('tab-rough');
const tabJudy = document.getElementById('tab-judy');
const keywordsArea = document.getElementById('keywords-area');
const keywordsList = document.getElementById('keywords-list');

// --- Toast ---
function showToast(msg, duration) {
    duration = duration || 2000;
    toast.textContent = msg;
    toast.style.display = 'block';
    setTimeout(function () { toast.style.display = 'none'; }, duration);
}

// --- Format time ---
function fmtTime(s) {
    var m = Math.floor(s / 60);
    var sec = Math.floor(s % 60);
    return m + ':' + String(sec).padStart(2, '0');
}

// --- Sound effects ---
var audioCtx = null;

function initAudio() {
    if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
}

function playSuccessSound() {
    initAudio();
    var now = audioCtx.currentTime;
    [523.25, 659.25].forEach(function (freq, i) {
        var osc = audioCtx.createOscillator();
        var gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.value = freq;
        gain.gain.setValueAtTime(0.15, now + i * 0.12);
        gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.12 + 0.35);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now + i * 0.12);
        osc.stop(now + i * 0.12 + 0.35);
    });
}

function playErrorSound() {
    initAudio();
    var now = audioCtx.currentTime;
    var osc = audioCtx.createOscillator();
    var gain = audioCtx.createGain();
    osc.type = 'square';
    osc.frequency.value = 150;
    gain.gain.setValueAtTime(0.08, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start(now);
    osc.stop(now + 0.3);
}

function playToggleSound() {
    initAudio();
    var now = audioCtx.currentTime;
    var osc = audioCtx.createOscillator();
    var gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.value = 660;
    gain.gain.setValueAtTime(0.04, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.06);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start(now);
    osc.stop(now + 0.06);
}

// --- Similarity slider ---
similaritySlider.addEventListener('input', function () {
    similarityValue.textContent = similaritySlider.value + '%';
});

// --- Mode tabs ---
tabRough.addEventListener('click', function () {
    if (currentStyle === '') return;
    currentStyle = '';
    tabRough.classList.add('active');
    tabJudy.classList.remove('active');
    keywordsArea.style.display = 'none';
    keywords = [];
    highlights = [];
});
tabJudy.addEventListener('click', function () {
    if (currentStyle === 'judy') return;
    currentStyle = 'judy';
    tabJudy.classList.add('active');
    tabRough.classList.remove('active');
    // Update settings to Judy defaults
    document.getElementById('silence-threshold').value = '0.3';
    similaritySlider.value = '55';
    similarityValue.textContent = '55%';
    document.getElementById('filler-words').value = '嗯,呃,啊,哦,啧,就是,那个,就是说,然后呢,对吧,说白了,其实吧,你懂吧,怎么样,这个';
});

// --- File upload / drag-drop ---
dropZone.addEventListener('click', function () { fileInput.click(); });
fileInput.addEventListener('change', function (e) { addFiles(e.target.files); });

dropZone.addEventListener('dragover', function (e) {
    e.preventDefault();
    dropZone.classList.add('dragover');
});
dropZone.addEventListener('dragleave', function () {
    dropZone.classList.remove('dragover');
});
dropZone.addEventListener('drop', function (e) {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    addFiles(e.dataTransfer.files);
});

function addFiles(newFiles) {
    for (var i = 0; i < newFiles.length; i++) {
        var f = newFiles[i];
        if (!f.type.startsWith('video/')) continue;
        files.push({
            name: f.name,
            duration: null,
            url: URL.createObjectURL(f),
            file: f
        });
    }
    if (files.length > 0) settings.style.display = 'block';
    renderFileList();
}

function renderFileList() {
    fileList.innerHTML = files.map(function (f, i) {
        return '<li class="file-item" draggable="true" data-index="' + i + '">' +
            '<span class="handle">≡</span>' +
            '<span class="name">' + f.name + '</span>' +
            '<span class="dur">' + (f.duration ? f.duration + 's' : '') + '</span>' +
            '<button class="btn-play" data-index="' + i + '">▶</button>' +
            '<button class="btn-sm" data-index="' + i + '">✕</button>' +
            '</li>';
    }).join('');

    analyzeBtn.disabled = files.length === 0;

    fileList.querySelectorAll('.file-item').forEach(function (item) {
        item.addEventListener('dragstart', handleDragStart);
        item.addEventListener('dragover', handleDragOver);
        item.addEventListener('dragleave', handleDragLeave);
        item.addEventListener('drop', handleDrop);
        item.addEventListener('dragend', handleDragEnd);
    });

    fileList.querySelectorAll('.btn-play').forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            e.stopPropagation();
            var idx = parseInt(btn.dataset.index);
            var f = files[idx];
            if (currentAudio) { currentAudio.pause(); currentAudio = null; }
            if (f.url) { currentAudio = new Audio(f.url); currentAudio.play(); }
        });
    });

    fileList.querySelectorAll('.btn-sm').forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            e.stopPropagation();
            var idx = parseInt(btn.dataset.index);
            if (currentAudio) { currentAudio.pause(); currentAudio = null; }
            files.splice(idx, 1);
            if (files.length === 0) settings.style.display = 'none';
            renderFileList();
        });
    });
}

// --- Drag and drop sorting ---
var dragSrcIndex = null;

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
function handleDragLeave() { this.classList.remove('drag-over'); }
function handleDrop(e) {
    e.preventDefault();
    this.classList.remove('drag-over');
    var targetIdx = parseInt(this.dataset.index);
    if (dragSrcIndex !== null && dragSrcIndex !== targetIdx) {
        var moved = files.splice(dragSrcIndex, 1)[0];
        files.splice(targetIdx, 0, moved);
        renderFileList();
    }
}
function handleDragEnd() {
    this.classList.remove('dragging');
    fileList.querySelectorAll('.file-item').forEach(function (el) { el.classList.remove('drag-over'); });
    dragSrcIndex = null;
}

// --- Progress bar ---
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

// --- Upload to server ---
function uploadFiles() {
    var formData = new FormData();
    for (var i = 0; i < files.length; i++) {
        formData.append('files', files[i].file);
    }
    return fetch('/api/upload', { method: 'POST', body: formData })
        .then(function (resp) {
            if (!resp.ok) throw new Error('Upload failed');
            return resp.json();
        })
        .then(function (data) {
            sessionId = data.session_id;
            return data;
        });
}

// --- Analyze (SSE) ---
analyzeBtn.addEventListener('click', function () {
    analyzeBtn.disabled = true;
    analyzeStatus.textContent = '正在上传...';
    showProgress('上传中...', 0.01);

    uploadFiles().then(function () {
        analyzeStatus.textContent = '';
        showProgress('开始分析...', 0.03);

        var formData = new FormData();
        formData.append('session_id', sessionId);
        formData.append('file_order', JSON.stringify(files.map(function (f) { return f.name; })));
        formData.append('silence_threshold', document.getElementById('silence-threshold').value);
        formData.append('similarity_threshold', similaritySlider.value / 100);
        formData.append('filler_words', document.getElementById('filler-words').value);
        if (currentStyle) {
            formData.append('style', currentStyle);
        }

        return fetch('/api/analyze', { method: 'POST', body: formData });
    }).then(function (resp) {
        if (!resp.ok) {
            return resp.json().then(function (err) {
                throw new Error(err.detail || 'Analysis failed');
            });
        }

        var reader = resp.body.getReader();
        var decoder = new TextDecoder();
        var buffer = '';

        function read() {
            return reader.read().then(function (result) {
                if (result.done) return;

                buffer += decoder.decode(result.value, { stream: true });
                var lines = buffer.split('\n');
                buffer = lines.pop() || '';

                for (var i = 0; i < lines.length; i++) {
                    var line = lines[i];
                    if (line.indexOf('data: ') === 0) {
                        var event = JSON.parse(line.slice(6));
                        handleSSE(event);
                    }
                }
                return read();
            });
        }
        return read();
    }).then(function () {
        analyzeBtn.disabled = false;
    }).catch(function (err) {
        hideProgress();
        analyzeStatus.textContent = '错误: ' + err.message;
        analyzeBtn.disabled = false;
        playErrorSound();
    });
});

function handleSSE(event) {
    if (event.step === 'concat') {
        showProgress(event.message, 0.05);
    } else if (event.step === 'transcribe') {
        showProgress(event.message, 0.05 + event.progress * 0.85);
    } else if (event.step === 'detect') {
        showProgress(event.message, 0.92);
    } else if (event.step === 'done') {
        showProgress('分析完成', 1);
        segments = event.segments;
        keywords = event.keywords || [];
        highlights = event.highlights || [];
        renderKeywords();
        renderSegments();
        setTimeout(function () { hideProgress(); }, 1000);
        reviewSection.style.display = 'block';
        reviewSection.scrollIntoView({ behavior: 'smooth' });
        analyzeStatus.textContent = '分析完成';
        playSuccessSound();
    }
}

function renderKeywords() {
    if (currentStyle !== 'judy' || keywords.length === 0) {
        keywordsArea.style.display = 'none';
        return;
    }
    keywordsArea.style.display = 'block';
    keywordsList.innerHTML = keywords.map(function (kw) {
        return '<span class="kw-tag">' + escapeHtml(kw) + '</span>';
    }).join('');
}

// --- Render segments ---
function renderSegments() {
    var keepTotal = 0, cutTotal = 0;

    segmentList.innerHTML = segments.map(function (seg) {
        var dur = seg.end - seg.start;
        if (seg.action === 'keep') keepTotal += dur;
        else cutTotal += dur;

        return '<li class="segment-item ' + seg.action + '" data-index="' + seg.index + '">' +
            '<span class="seg-time">' + fmtTime(seg.start) + ' - ' + fmtTime(seg.end) + '</span>' +
            '<span class="seg-text" title="' + escapeHtml(seg.text) + '">' + (escapeHtml(seg.text) || '[静音]') + '</span>' +
            (seg.reason ? '<span class="seg-reason">' + escapeHtml(seg.reason) + '</span>' : '') +
            '<label class="toggle">' +
            '<input type="checkbox" ' + (seg.action === 'keep' ? 'checked' : '') + ' data-index="' + seg.index + '">' +
            '<span class="slider"></span>' +
            '</label>' +
            '</li>';
    }).join('');

    keepTime.textContent = fmtTime(keepTotal);
    cutTime.textContent = fmtTime(cutTotal);
    totalTime.textContent = fmtTime(keepTotal + cutTotal);

    segmentList.querySelectorAll('input[type=checkbox]').forEach(function (cb) {
        cb.addEventListener('change', function () {
            var idx = parseInt(cb.dataset.index);
            segments[idx].action = cb.checked ? 'keep' : 'cut';
            updateStats();
            var item = cb.closest('.segment-item');
            item.classList.toggle('keep', cb.checked);
            item.classList.toggle('cut', !cb.checked);
            playToggleSound();
        });
    });

    segmentList.querySelectorAll('.segment-item').forEach(function (item) {
        item.addEventListener('click', function (e) {
            if (e.target.tagName === 'INPUT') return;
            var idx = parseInt(item.dataset.index);
            var seg = segments[idx];

            previewVideo.src = '/api/video/' + sessionId;
            previewPlayer.style.display = 'block';
            previewLabel.textContent = fmtTime(seg.start) + ' ~ ' + fmtTime(seg.end) + ' — ' + (seg.text || '[静音]');
            previewVideo.currentTime = seg.start;
            previewVideo.play();

            var stopAt = seg.end;
            function checkTime() {
                if (previewVideo.currentTime >= stopAt) {
                    previewVideo.pause();
                    previewVideo.removeEventListener('timeupdate', checkTime);
                }
            }
            previewVideo.removeEventListener('timeupdate', checkTime);
            previewVideo.addEventListener('timeupdate', checkTime);
        });
    });
}

function updateStats() {
    var keepTotal = 0, cutTotal = 0;
    for (var i = 0; i < segments.length; i++) {
        var dur = segments[i].end - segments[i].start;
        if (segments[i].action === 'keep') keepTotal += dur;
        else cutTotal += dur;
    }
    keepTime.textContent = fmtTime(keepTotal);
    cutTime.textContent = fmtTime(cutTotal);
}

function escapeHtml(str) {
    var div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

// --- Export ---
exportBtn.addEventListener('click', function () {
    exportBtn.disabled = true;
    exportStatus.textContent = '';
    showProgress('准备导出...', 0.01);

    var keepIntervals = segments
        .filter(function (s) { return s.action === 'keep'; })
        .map(function (s) { return [s.start, s.end]; });

    var formData = new FormData();
    formData.append('session_id', sessionId);
    formData.append('keep_intervals', JSON.stringify(keepIntervals));
    if (currentStyle === 'judy' && highlights.length > 0) {
        formData.append('highlights', JSON.stringify(highlights));
    }

    fetch('/api/export', { method: 'POST', body: formData })
        .then(function (resp) {
            if (!resp.ok) {
                return resp.json().then(function (err) {
                    throw new Error(err.detail || 'Export failed');
                });
            }

            var reader = resp.body.getReader();
            var decoder = new TextDecoder();
            var buffer = '';

            function read() {
                return reader.read().then(function (result) {
                    if (result.done) return;

                    buffer += decoder.decode(result.value, { stream: true });
                    var lines = buffer.split('\n');
                    buffer = lines.pop() || '';

                    for (var i = 0; i < lines.length; i++) {
                        var line = lines[i];
                        if (line.indexOf('data: ') === 0) {
                            var event = JSON.parse(line.slice(6));
                            handleExportSSE(event);
                        }
                    }
                    return read();
                });
            }
            return read();
        })
        .catch(function (err) {
            hideProgress();
            exportStatus.textContent = '错误: ' + err.message;
            exportBtn.disabled = false;
            playErrorSound();
        });
});

function handleExportSSE(event) {
    if (event.step === 'prepare') {
        showProgress(event.message, 0.05);
    } else if (event.step === 'processing') {
        showProgress(event.message, 0.05 + event.progress * 0.9);
    } else if (event.step === 'done') {
        showProgress(event.message + '，开始下载...', 1);

        fetch(event.download_url)
            .then(function (resp) { return resp.blob(); })
            .then(function (blob) {
                var url = URL.createObjectURL(blob);
                var a = document.createElement('a');
                a.href = url;
                a.download = 'output.mp4';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
                hideProgress();
                exportStatus.textContent = '导出完成';
                exportBtn.disabled = false;
                showToast('视频已导出');
                playSuccessSound();
            })
            .catch(function (err) {
                hideProgress();
                exportStatus.textContent = '下载错误: ' + err.message;
                exportBtn.disabled = false;
                playErrorSound();
            });
    }
}
