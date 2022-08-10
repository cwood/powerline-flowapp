from powerline.lib.shell import asrun


def flowapp(pl):
    status_delimiter = '-~`/='
    ascript = '''
        tell application "System Events"
            set process_list to (name of every process)
        end tell

        if process_list contains "Flow" then
            tell application "Flow"
                set flow_status to "" & getTime & "{0}" & getPhase
                return flow_status
            end tell
        else
            return "not running"
        end if
    '''.format(status_delimiter)

    flow = asrun(pl, ascript)
    if not asrun:
        return None

    if flow == "not running":
        return None

    flow_time = flow.split(status_delimiter)

    return [{
        "contents": "{phase} | {time}".format(
            phase=flow_time[1], time=flow_time[0]),
        "highlight_groups": ["flowapp"],
        "divider_highlight_group": "flowapp:divider",
    }]
