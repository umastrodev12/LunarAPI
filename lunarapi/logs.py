import os


LOGS = os.path.expanduser('~/.lunarclient/offline/multiver/logs/latest.log')

def monitoring():
    with open(LOGS, encoding="UTF-8") as log:
        log.seek(0, 2)
        while True:
            line = log.readline()

            if "[CHAT]" in line:
                print(f"[💬] {line.strip()}")


def startLogs():
    print("Starting Lunar Client Script Logs...")

    monitoring()