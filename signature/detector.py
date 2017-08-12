import yara

class Detector(object):

    """
    악성코드 여부를 검사하려는 파일과
    정의해놓은 yara rule을 matching 시킨 결과 return
    """
    def ruleMatchFile(targetFilePath):

        rule_path = r".\ruleFile_dir\yara_rule.yar"  #rule file path 입력
        result_message = ""

        try:
            tFile = open(targetFilePath, "rb")
            fileData = tFile.read()
            print("file data :", fileData)

            compiledRules = yara.compile(filepath=rule_path)    #rule 파일 compile
            rule_match_result = compiledRules.match(data=fileData)

            print("결과 :", rule_match_result)
            if len(rule_match_result) > 0:
                targetFilePath += "\n"
                result_message += targetFilePath
                for i in rule_match_result:
                    print(i, " ")

            return result_message

        except Exception as e:
            print(e)
            return

        print("결과 :", rule_match_result)

def main(_):
    return

if __name__ == "__main__":
    main()
  # flags.StartMain(main)