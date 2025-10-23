import ffmpeg
import time

# 録音時間（秒）
duration = 11 #10に設定したら音声ファイルが秒数を切り上げてしまい9秒と表示されてしまったので11秒に設定しました
# 出力ファイル名
output_file = 'python-audio-output.wav'

try:
    print(f"{duration}秒間、マイクからの録音を開始します...")
    # FFmpegコマンドを実行
    #   - macOS: 'avfoundation'
    # -i <入力デバイス名>: デバイス名を指定
    (
        ffmpeg
        .input(':0', format='avfoundation', t=duration) # macOSの例
        .output(output_file, acodec='pcm_s16le', ar='44100', ac=1)
        .run(overwrite_output=True)
    )
    print(f"録音が完了しました。")

except ffmpeg.Error as e:
    print(f"エラーが発生しました: {e.stderr.decode()}")
except Exception as e:
    print(f"予期せぬエラー: {e}")