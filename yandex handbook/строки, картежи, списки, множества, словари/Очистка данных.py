while log := input():
    if log.endswith("@@@"):
        continue
    log = log.lstrip("##")
    print(log)