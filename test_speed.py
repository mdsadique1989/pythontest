import network_speed as st

def Speed_Test():
    test = st.Speedtest()  # Correct class initialization

    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)  # Fixed syntax issue
    print("Download speed in Mbps:", down_speed)

    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print("Upload speed in Mbps:", up_speed)

    ping = test.results.ping
    print("Ping:", ping)

Speed_Test()
