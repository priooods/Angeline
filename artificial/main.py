import json
import command as cmd

_config = open('./config.json')
_config = json.load(_config)
cmd._run_command(_config['angeline']['production'])

