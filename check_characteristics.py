import os
import struct

# FILE_PATH = r'/home/seclab/Documents/meseum_data/virussign'
FILE_PATH = r'/home/seclab/Documents/meseum_data/virusshare_only_pe_32_two'
characteristics_set = set()
# final_n + 3 + 19

def check_characteristics(file_path):
    with open(file_path, 'rb') as f:
        data = f.read(2)
        if hex(data[0]) == hex(0x4D) and hex(data[1]) == hex(0x5A):
            # print("This file is MZ")
            f.seek(0)
            data = f.read()
            # print(hex(data[60]), hex(data[61]), hex(data[62]), hex(data[63]))  # pe
            # little endian
            n1 = hex(data[63]).split('0x')[1].rjust(2, '0')
            n2 = hex(data[62]).split('0x')[1].rjust(2, '0')
            n3 = hex(data[61]).split('0x')[1].rjust(2, '0')
            n4 = hex(data[60]).split('0x')[1].rjust(2, '0')
            final_n = int(n1 + n2 + n3 + n4, 16)
            # print(data[final_n:final_n + 2])
            if hex(data[final_n]) == hex(0x50) and hex(data[final_n + 1]) == hex(0x45) and hex(data[final_n + 2]) == hex(0x00) and hex(data[final_n + 3]) == hex(0x00):
                if hex(data[final_n + 3 + 21]) == hex(0x0B) and hex(data[final_n + 3 + 22]) == hex(0x01):
                    num = data[final_n+3+19:final_n+3+21]
                    num = int.from_bytes(num, byteorder='little', signed=False)
                    # 0x2000 -> DLL, 0x0002 -> File is a executable
                    if (num & 0x2000) == 0x2000:
                        return "File is a DLL"
                    return "This file is not DLL"


if __name__ == '__main__':
    for _path, _dir, files in os.walk(FILE_PATH):
        if not _dir:
            for file_name in files:
                full_file_name = os.path.join(_path, file_name)
                print(check_characteristics(full_file_name))
