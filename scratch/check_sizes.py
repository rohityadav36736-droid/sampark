import struct
import glob
import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_image_size(fname):
    with open(fname, 'rb') as f:
        data = f.read(30)
        if data[:8] == b'\x89PNG\r\n\x1a\n':
            w, h = struct.unpack('>LL', data[16:24])
            return w, h, 'PNG'
        elif data[:2] == b'\xff\xd8':
            f.seek(0)
            f.read(2)
            b = f.read(1)
            try:
                while (b and b != b''):
                    while (b != b'\xff'): b = f.read(1)
                    while (b == b'\xff'): b = f.read(1)
                    if (b >= b'\xc0' and b <= b'\xc3'):
                        f.read(3)
                        h, w = struct.unpack('>HH', f.read(4))
                        break
                    else:
                        f.read(int(struct.unpack('>H', f.read(2))[0])-2)
                    b = f.read(1)
                return w, h, 'JPEG'
            except:
                return None
    return None

for path in sorted(glob.glob('assets/images/*.*')):
    sz = get_image_size(path)
    if sz:
        w, h, fmt = sz
        print(f"{path}: {w}x{h} (aspect {w/h:.2f}) [{fmt}]")
