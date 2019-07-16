# extract_pe_file
여러 종류의 파일이 있을 때, (hwp, pdf, exe 등등) windows 실행파일인 PE(Portable Excutable) 파일만을 추출해 내는 간단한 소스코드입니다.


사용방법
1. FILE_PATH에 파일의 전체 경로를 입력합니다.
2. extract_pe 함수를 호출시킵니다.
3. print("This file is exactly PE") 부분을 자신이 필요한 방법으로 알맞게 수정합니다.

참고 : MZ (0x4D 0x5A) PE (0x50 0x45 0x00 0x00)      
32bit machine = 0x4C 0x01    64bit machine = 0x64 0x86   (PE 뒤에 있는 2bytes 를 보면 됩니다.)
