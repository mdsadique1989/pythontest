import speedtest

def speed_test():
    test = speedtest.Speedtest()  # Initialize speedtest

    print("Testing download speed...")
    download_speed = test.download() / 8  # Convert to Bytes (MBps)
    download_speed_MBps = round(download_speed / 10**6, 2)
    print(f"Download Speed: {download_speed_MBps} MBps")

    print("Testing upload speed...")
    upload_speed = test.upload() / 8  # Convert to Bytes (MBps)
    upload_speed_MBps = round(upload_speed / 10**6, 2)
    print(f"Upload Speed: {upload_speed_MBps} MBps")

    ping = test.results.ping
    print(f"Ping Time: {ping} ms")

# Run the speed test
speed_test()
