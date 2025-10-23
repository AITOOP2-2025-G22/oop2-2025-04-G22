import ffmpeg
import time

# 録音時間（秒）
duration = 10

try:
    print(f"{duration}秒間、マイクからの録音を開始します...")
    # FFmpegコマンドを実行
    #   - macOS: 'avfoundation'
    # -i <入力デバイス名>: デバイス名を指定
    (
        ffmpeg
        .input(':0', format='avfoundation', t=duration) # macOSの例
        .run(overwrite_output=True)
    )
    print(f"録音が完了しました。")

except ffmpeg.Error as e:
    print(f"エラーが発生しました: {e.stderr.decode()}")
except Exception as e:
    print(f"予期せぬエラー: {e}")