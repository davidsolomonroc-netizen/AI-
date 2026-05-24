# tests/test_processor.py
import subprocess
import sys
sys.path.insert(0, ".")
from processor import get_duration


def test_get_duration_real_video():
    """用 FFmpeg 生成一个 3 秒的测试视频，验证 get_duration 返回 ~3.0"""
    # 生成测试视频：3 秒黑屏 + 静音
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi",
        "-i", "color=c=black:s=320x240:d=3",
        "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
        "-shortest", "-t", "3",
        "/tmp/test_3s.mp4"
    ], check=True, capture_output=True)

    duration = get_duration("/tmp/test_3s.mp4")
    assert 2.8 <= duration <= 3.2, f"Expected ~3.0s, got {duration}"


def test_concat_two_videos():
    """拼接两个 2s 视频，验证输出时长 ~4s"""
    # 生成 video1: 2s
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi",
        "-i", "color=c=red:s=320x240:d=2",
        "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
        "-shortest", "-t", "2",
        "/tmp/test_red.mp4"
    ], check=True, capture_output=True)
    # 生成 video2: 2s
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi",
        "-i", "color=c=blue:s=320x240:d=2",
        "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
        "-shortest", "-t", "2",
        "/tmp/test_blue.mp4"
    ], check=True, capture_output=True)

    from processor import concat_videos
    concat_videos(["/tmp/test_red.mp4", "/tmp/test_blue.mp4"], "/tmp/test_concat.mp4")
    dur = get_duration("/tmp/test_concat.mp4")
    assert 3.8 <= dur <= 4.2, f"Expected ~4s, got {dur}"


def test_extract_single_segment():
    """裁剪 3s 视频的 1.0-2.0 段，验证输出 ~1s"""
    from processor import extract_segments
    extract_segments("/tmp/test_3s.mp4", [(1.0, 2.0)], "/tmp/test_trimmed.mp4")
    dur = get_duration("/tmp/test_trimmed.mp4")
    assert 0.8 <= dur <= 1.2, f"Expected ~1s, got {dur}"


def test_extract_two_segments():
    """裁剪两段 1s，验证输出 ~2s"""
    from processor import extract_segments
    extract_segments("/tmp/test_3s.mp4", [(0.5, 1.5), (2.0, 3.0)], "/tmp/test_two_trim.mp4")
    dur = get_duration("/tmp/test_two_trim.mp4")
    assert 1.8 <= dur <= 2.2, f"Expected ~2s, got {dur}"
