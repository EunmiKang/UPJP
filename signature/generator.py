import optparse
import os
import sys


class Gen(object):

    def __init__(self):
        self.extractor = Extractor()

    def addWhiteList(self, path, db='GenDB.db'):
        # insert db
        self.extractor.extractStringsWithDB(path, db)

    def compareFile(self, path, db='GenDB.db'):

        buf_arr = self.extractor.extractMalPattern(path, db)

        return buf_arr

    def CreateYara(self):

        raise NotImplementedError


class Extractor(object):
    """Base class for signature extractors."""

    def __init__(self, path=None):
        # self.path = path or []
        return

    def extractStrings(self, path):
        """Extracts interesting signatures from a given file.
        
        Args:
          path: 
        
        Returns:
          A list of extracted signatures (as strings).
        """
        print("[+] Get Strings...")
        command = 'string.exe -n 3 ' + path
        bufs = os.popen(command).read()
        buf_arr = bufs.split('\n')
        buf_arr = list(set(buf_arr))

        print("[+} Result")
        print(buf_arr)
        return buf_arr

    def extractStringsWithDB(self, path, db):
        """Extracts interesting paths from a given path And Inserts to db.
        
        Args:
          path: 
        
        Returns:
          A list of extracted paths (as strings).
        """
        files = getFileList(path)
        print("[+] Get Strings...")
        for file in files:
            command = 'strings.exe -n 3 ' + file + '>>' + db
            os.system(command)

    def extractMalPattern(self, path, db):

        print("[+] Get Strings...")
        command = 'string.exe -n 3 ' + path
        bufs = os.popen(command).read()
        buf_arr = bufs.split('\n')
        buf_arr = list(set(buf_arr))

        with open(db, 'r') as f:
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
        print("[+} Result")
        print(buf_arr)
        return buf_arr

    def extract_(self, path):

        raise NotImplementedError()


def getFileList(path):
    res = []
    for root, dirs, files in os.walk(path):
        rootpath = os.path.join(os.path.abspath(path), root)
        for file in files:
            filepath = os.path.join(rootpath, file)
            res.append(filepath)
    return res

    # def DB_Update(self):
    #     offset = 0
    #     o = open('GenDB.tmp', 'wb')
    #     while True:
    #         with open('GenDB.db', 'rb') as f:
    #             f.seek(offset)
    #             buf = f.read(0x2000000)
    #         if not len(buf): break
    #
    #         arr = buf.split('\n')
    #         arr = list(set(arr))
    #
    #         for i in arr: o.write(str(i) + '\n')
    #         offset += len(buf)
    #     o.close()
    #     os.remove('GenDB.db')
    #     os.rename("GenDB.tmp", "GenDB.db")

def main(_):
    return

if __name__ == "__main__":
    main()
  # flags.StartMain(main)