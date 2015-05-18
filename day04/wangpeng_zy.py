log = open('accesslog')

log_dict = {}
for i in log:
    line = i.split()
    ip = line[0]
    url = line[6]
    status = line[8]
    if ip in log_dict:
        if url in log_dict[ip]:
            log_dict[ip][url][status] = log_dict[ip][url].get(status,0) + 1
        else:
            log_dict[ip][url] = {status:1}
    else:
        log_dict[ip] = {url:{status:1}}
print log_dict

