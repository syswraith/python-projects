import sys

input_text = sys.stdin.read()
output_text = ''
lines = input_text.splitlines()

def editor(line):
    line = line.strip()
    if line.startswith("#include"): return (''.join(line.split(' ')) + '\n')
    elif line.startswith("using"): return (line)
    elif line.startswith('int') or line.startswith('string') or line.startswith('float') or line.startswith('double') or line.startswith('char') or line.startswith('bool') or line.startswith('long') or line.startswith('short') or line.startswith('unsigned'): return (line)
    elif line.startswith('return'): return (line)
    else: return ''.join(line.split(' '))

for line in lines:
    output_text += editor(line)

print(output_text)
