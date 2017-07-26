
import sys

import logging

from PyQt5.QtWidgets import QApplication

from gui.client_ui import *

# def main():
#     print("\n[+] Kali-KM's GenCreater. kali-km.tistory.com")
#     usage = "[+] Usage : Python %Prog [-d DirPath] or [-c CompareFile] or [-u]"
#     parser = optparse.OptionParser(usage=usage)
#     parser.add_option('-d', '--dirpath', dest='DirPath', help='specifies a directory where the files')
#     parser.add_option('-c', '--compare', dest='Comp', help='specify a compare file')
#
#     (options, args) = parser.parse_args()
#
#     if (not options.DirPath and not options.Comp) or (options.DirPath and options.Comp):
#         print(parser.usage)
#         sys.exit(0)
#
#     Gen = YarCrate()
#     if options.DirPath:
#         Gen.GetStrings(options.DirPath)
#         sys.exit(0)
#
#     elif options.Comp:
#         Gen.CompareFile(options.Comp)
#         sys.exit(0)
#
#     return

class App(Main):

    def __init__(self):
        super().__init__()

def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
