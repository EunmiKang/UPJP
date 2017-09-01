import argparse
import os
import sys

class Generater(object):

    def extractStrings(self, path):
        """Extracts interesting signatures from a given path.
        
        Args:
          path: target directory or files
        
        Returns:
          A list of extracted signatures (as strings).
        """
        print("[+] Get Strings...")
        command = 'strings.exe -n 3 ' + path
        bufs = os.popen(command).read()
        buf_arr = bufs.split('\n')
        buf_arr = list(set(buf_arr))

        print("[+} Result")
        print(buf_arr)
        return buf_arr

    def extractStringsWithDB(self, path, db='GenDB.db'):
        """Extracts interesting signatures from a given path and Inserts to db.

        This method extracts string from files in path and Store at local database

        Args:
          path: target directory or files
          db: A path of database
        
        Returns:
          None
        """
        files = getFileList(path)
        print(files)
        print("[+] Get Strings...")
        for file in files:
            command = 'strings.exe -n 3 ' + file + '>>' + db
            os.system(command)
            
        self.DB_Update()

    def extractMalPattern(self, path, db='GenDB.db'):
        """Extracts interesting signatures from a given path.

         This method extracts string from file in path and compare with whilelist database

        Args:
            path: target file
            db: A path of database

        Returns:
             A list of extracted signatures (as strings).
        """
        files = getFileList(path)
        print(files)
        print("[+] Get Strings...")
        for file in files:
            # o = open(file+'_pattern.txt', 'wb')
            command = 'strings.exe -n 3 ' + file + '>>' + file+'.txt'
            os.system(command)
            self.DB_Update(file+'.txt')
            # bufs = os.popen(command, 'r').read()
            # buf_arr = bufs.split(b'\n')
            # buf_arr = list(set(buf_arr))
            # for i in buf_arr: o.write(i + b'\n')
            #
            # with open(db, 'rb') as f:
            #     while True:
            #         data = f.read(0x2000000)
            #         if not data:
            #             for i in buf_arr: o.write(i + b'\n')
            #             break
            #         read_arr = data.split(b'\n')
            #
            #         for text in read_arr:
            #             try:
            #                 buf_arr.remove(text)
            #             except ValueError:
            #                 pass

        # print("[+} Result")
        # print(buf_arr)
        # return buf_arr

    def DB_Update(self, db='GenDB.db'):
        """Removing redundency from a whitelist database

        """
        offset=0
        o = open(db+'.tmp', 'wb')
        while True:
            with open(db, 'rb') as f:
                f.seek(offset)
                buf = f.read(0x2000000)
                print(buf)
            if not len(buf): break

            arr = buf.split(b'\n')
            arr = list(set(arr))

            for i in arr: o.write(i + b'\n')
            offset += len(buf)
        
        o.close()
        os.remove(db)
        os.rename(db+'.tmp', db)


def getFileList(path):
    res = []
    for root, dirs, files in os.walk(path):
        rootpath = os.path.join(os.path.abspath(path), root)
        for file in files:
            filepath = os.path.join(rootpath, file)
            res.append(filepath)
    return res

def main():
    print("\n[+] Kali-KM's GenCreater. kali-km.tistory.com")
    usage = "[+] Usage : Python %Prog [-d DirPath] or [-c CompareFile] or [-u]"
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument('-d', '--dirpath', help='specifies a directory where the files')
    parser.add_argument('-c', '--compare', help='specify a compare file')
    args = parser.parse_args()
    if (not args.dirpath and not args.compare) or (args.dirpath and args.compare):
        print(parser.usage)
        sys.exit(0)

    gen = Generater()
    if args.dirpath:
        gen.addWhiteList(args.dirpath)
        sys.exit(0)

    elif args.compare:
        gen.compareFile(args.compare)
        sys.exit(0)

    return

if __name__ == "__main__":
    main()
