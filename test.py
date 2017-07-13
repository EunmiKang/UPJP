# -*-coding:utf-8 -*-
# Author : Kali-KM
# Blog : kali-km.tistory.com

import os, sys, optparse, time


class YarCrate:
    def GetFileList(self, DirPath):
        res = []
        for root, dirs, files in os.walk(DirPath):
            rootpath = os.path.join(os.path.abspath(DirPath), root)
            for file in files:
                filepath = os.path.join(rootpath, file)
                res.append(filepath)
        return res

    def GetStrings(self, Dirpath):
        Filelist = self.GetFileList(Dirpath)
        print "[+] Get Strgins..."
        for file in Filelist:
            command = 'strings.exe -q -n 3 ' + file + '>>GenDB.db'
            os.system(command)
        self.DB_Update()
        return

    def DB_Update(self):
        offset = 0
        o = open('GenDB.tmp', 'wb')
        while True:
            with open('GenDB.db', 'rb') as f:
                f.seek(offset)
                buf = f.read(0x2000000)
            if not len(buf): break

            arr = buf.split('\n')
            arr = list(set(arr))

            for i in arr: o.write(str(i) + '\n')
            offset += len(buf)
        o.close()
        os.remove('GenDB.db')
        os.rename("GenDB.tmp", "GenDB.db")

    def CompareFile(self, Comp):
        print "[+] ing..."
        command = 'strings.exe -q -n 3 ' + Comp
        bufs = os.popen(command).read()
        buf_arr = bufs.split('\n')
        buf_arr = list(set(buf_arr))

        with open('GenDB.db', 'r') as f:
            while True:
                data = f.read(0x2000000)
                if not data: break
                read_arr = data.split('\n')

                for text in read_arr:
                    try:
                        buf_arr.remove(text)
                    except ValueError:
                        pass
                        # 반환되는 결과가 \xff와 같은 형태일 수도 있으며, Unicode일 수도 있음
                        # 따라서 Rule 생성 시 이에 대하여 신경써야함
        print "[+] Result"
        print buf_arr
        return


def main():
    print "\n[+] Kali-KM's GenCreater. kali-km.tistory.com"
    usage = "[+] Usage : Python %Prog [-d DirPath] or [-c CompareFile] or [-u]"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('-d', '--dirpath', dest='DirPath', help='specifies a directory where the files')
    parser.add_option('-c', '--compare', dest='Comp', help='specify a compare file')

    (options, args) = parser.parse_args()

    if (not options.DirPath and not options.Comp) or (options.DirPath and options.Comp):
        print parser.usage
        sys.exit(0)

    Gen = YarCrate()
    if options.DirPath:
        Gen.GetStrings(options.DirPath)
        sys.exit(0)

    elif options.Comp:
        Gen.CompareFile(options.Comp)
        sys.exit(0)

    return


if __name__ == '__main__':
    main()