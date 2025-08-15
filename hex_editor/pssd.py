import argparse

parser = argparse.ArgumentParser('pssd')
parser.add_argument('-o', '--offset', type=int, default=16, help='Hex offset')
parser.add_argument('-f', '--filename', type=str, help='File name', required=True)
args = parser.parse_args()

class Hex_editor:
    def __init__(self, args):
        self.offset = args.offset
        self.filename = args.filename

    def run(self) -> str:
        offset_counter = 0
        result = ''
        with open(self.filename, 'rb') as file:
            file_data = file.read()
            while offset_counter < len(file_data):
                chunk = file_data[offset_counter:offset_counter + self.offset]
                hex_output = [f'{b:02x}' for b in chunk]
                ascii_part = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in chunk)
                result += f"{offset_counter:08x}  {' '.join(hex_output):<{self.offset*3}}  {ascii_part}\n"
                offset_counter += self.offset
        return result

editor = Hex_editor(args)
print(editor.run(), end='')

