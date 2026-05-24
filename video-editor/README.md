# 口播视频自动剪辑工具

自动去除口播视频中的语气词、空白停顿和重复段落。

## 环境要求

- Python 3.10+
- FFmpeg (安装: `brew install ffmpeg`)
- 16GB+ 内存 (Whisper large-v3 模型需要)

## 安装

```bash
cd video-editor
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

首次运行时 faster-whisper 会自动下载 large-v3 模型 (~3GB)。

## 使用

```bash
cd video-editor
source .venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000
```

打开浏览器访问 `http://localhost:8000`

## 工作流程

1. 上传多段手机录制的口播视频
2. 拖拽调整视频顺序
3. 点击"开始分析" → 自动语音识别 + 检测
4. 在确认编辑界面手动调整保留/删除的片段
5. 点击"导出视频" → 下载成品

## 检测项目

| 检测 | 说明 | 默认 |
|------|------|------|
| 语气词 | 匹配预定义中文语气词列表 | 嗯、啊、就是、那个... |
| 空白停顿 | 词间间隔超过阈值 | 0.8 秒 |
| 重复段落 | 相邻句相似度超过阈值 | 70% |

## 技术栈

- FastAPI (Web 后端)
- faster-whisper large-v3 (中文语音识别)
- FFmpeg (视频拼接裁剪)
- 全部本地运行，不上传云端
