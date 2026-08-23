import csv

with open("servers.csv", "r", newline="", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    required_columns = {
        "hostname",
        "environment",
        "port"
    }

    actual_columns = set(reader.fieldnames or [])

    missing = required_columns - actual_columns

    if missing:
        raise ValueError(
            f"Missing columns: {missing}"
        )

    for server in reader:

        try:
            port = int(server["port"])
        except ValueError:
            print(
                f"Invalid port for {server['hostname']}"
            )
            continue

        if not 1 <= port <= 65535:
            print(
                f"Invalid port for {server['hostname']}: {port}"
            )