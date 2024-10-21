import speedtest

def test_network_speed():
    # Create a Speedtest object
    test = speedtest.Speedtest()

    print("Fetching the best server...")
    test.get_best_server()  # Selects the best server based on ping

    # Measure download speed
    download_speed = test.download()
    download_speed = round(download_speed / 10**6, 2)  # Convert to Mbps
    print(f"Download Speed: {download_speed} Mbps")

    # Measure upload speed
    upload_speed = test.upload()
    upload_speed = round(upload_speed / 10**6, 2)  # Convert to Mbps
    print(f"Upload Speed: {upload_speed} Mbps")

    # Measure ping time
    ping_result = test.results.ping
    print(f"Ping: {ping_result} ms")

# Run the speed test
test_network_speed()
