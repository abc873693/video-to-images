
# ffmpeg -i rtsp://@192.168.100.10/h264/ch1/main/av_stream -r 15 2019-10-03_113920.mp4
mkdir -p records
ffmpeg -rtsp_transport tcp -reorder_queue_size 8000 -i $1 -r 25 -map 0 -f segment -segment_time 600 -reset_timestamps 1 -strftime 1 "./records/%Y-%m-%d_%H-%M-%S.mp4"