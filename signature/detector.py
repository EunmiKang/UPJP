import yara

class Detector(object):

    def ruleMatchFile(targetFilePath):
        rule_path = r".\ruleFile_dir\yara_rule.yar"  #rule file path 입력

        try:
            tFile = open(targetFilePath, "rb")
            fileData = tFile.read()
            print("file data :", fileData)

            compiledRules = yara.compile(filepath=rule_path)    #rule 파일 compile
            rule_match_result = compiledRules.match(data=fileData)

        except Exception as e:
            print(e)
            return

        print("결과 :", rule_match_result)

def main(_):
    return

if __name__ == "__main__":
    main()
  # flags.StartMain(main)