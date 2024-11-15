import paramiko

# Remote machine details
command = sys.argv[1]
hostname = sys.argv[2]  # Remote machine's IP address
username = sys.argv[3]
password = sys.argv[4]
sudo_password = sys.argv[5]


def run_sudo_command():
    try:
        # Create an SSH client and connect
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password)

        # Execute the command with sudo
        command_with_sudo = f"echo {sudo_password} | sudo -S {command}"
        stdin, stdout, stderr = client.exec_command(command_with_sudo)

        # Capture output and errors
        output = stdout.read().decode()
        error = stderr.read().decode()

        # Print results
        if output:
            print("Command Output:\n", output)
        if error:
            print("Command Error:\n", error)

    except Exception as e:
        print(f"Failed to connect or execute command: {e}")

    finally:
        # Close the SSH connection if the client exists
        try:
            client.close()
        except NameError:
            pass

# Run the function
run_sudo_command()
