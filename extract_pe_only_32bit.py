import os
import shutil

FILE_PATH = r'/home/seclab/Documents/meseum_data/virusshare'
MOVE_PATH = r'/home/seclab/Documents/meseum_data/virusshare_only_pe'

def extract_pe(file_path):
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
                    return True
            return False

if __name__ == '__main__':
    for _path, _dir, _files in os.walk(FILE_PATH):
        if not _dir:
            for file_name in _files:
                fp = os.path.join(_path, file_name)
                try:
                    if extract_pe(fp):
                        file_name = file_name.split('_')[1]+'.vir'
                        target_path = os.path.join(MOVE_PATH, file_name)
                        shutil.copy2(fp, target_path)
                        print("FINISHED!!!! {} to {}".format(fp, target_path))
                except Exception as e:
                    print(e)