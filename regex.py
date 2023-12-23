import re


class LogParser:
    def __init__(self, log_message):
        self.log_message = log_message
        self.log_pattern = re.compile(r'''
            \[
            (?P<timestamp>[\d/: AMPM]+)\s+
            TYPE=(?P<type>\w+)\s+
            USER=(?P<user>(?P<nt>[\w]+)\s+(?P<authority_system>[\w\\]+))\s+
            COMP=(?P<comp>\w+)\s+
            SORC=(?P<sorc>\w+)\s+
            CATG=(?P<catg>\w+)\s+
            EVID=(?P<evid>\d+)\s+
            MESG=(?P<mesg>.+?)
            ]
        ''', re.VERBOSE)

    def parse_log_message(self):
        match = self.log_pattern.search(self.log_message)

        if match:
            timestamp = match.group('timestamp')
            log_type = match.group('type')
            user = match.group('user')
            comp = match.group('comp')
            sorc = match.group('sorc')
            catg = match.group('catg')
            evid = match.group('evid')
            mesg = match.group('mesg')

            print(f"Timestamp: {timestamp}")
            print(f"Type: {log_type}")
            print(f"User: {user}")
            print(f"Comp: {comp}")
            print(f"Sorc: {sorc}")
            print(f"Catg: {catg}")
            print(f"EVID: {evid}")
            print(f"Mesg: {mesg}")
        else:
            print("No match found.")


if __name__ == "__main__":
    # Example usage:
    log_message_example = ("[6/18/2007 2:36 PM TYPE=Information USER=NT AUTHORITY\SYSTEM COMP=DBSERVER \
                           SORC=MSSQLSERVER CATG=Logon EVID=17055 \
                           MESG=18453 : Login succeeded for user ''NT AUTHORITY\SYSTEM''.]")
    log_parser = LogParser(log_message_example)
    log_parser.parse_log_message()
