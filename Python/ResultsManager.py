from Python.ResultData import ResultData


class ResultsManager:
    def __init__(self, controller):
        self.controller = controller
        self.testData = ResultData()

    def getTestResult(self):
        isHateSpeechBool = self.controller.isHateSpeech()
        isLGBTQIASpeechBool = self.controller.isLGBTQIASpeech()
        if isHateSpeechBool and isLGBTQIASpeechBool:
            return 'LGBT_hate_speech'
        elif isHateSpeechBool:
            return 'hate_speech'
        elif isLGBTQIASpeechBool:
            return 'LGBT_non_hate_speech'
        else:
            return 'non_hate_speech'

    def calcTestResults(self, num):
        targets = []
        results = []
        texts = []
        indexes = []
        hate_speech_count = 0
        non_hate_speech_count = 0
        testData = self.testData.getTestData()

        totalCount = 0
        testResults = self.testData.getResults()
        for result in testResults:
            if len(result) > 0:
                if result[1] == '-' or result[2] == '-':
                    break
                totalCount += 1
        count = 0
        progress = 0
        min_index = totalCount
        max_index = totalCount + num
        for data in testData:
            if min_index <= count < max_index:
                if data[1] == 'LGBT_hate_speech':
                    if hate_speech_count < num / 2:
                        hate_speech_count += 1
                    elif non_hate_speech_count >= num / 2:
                        hate_speech_count += 1
                    else:
                        continue
                elif data[1] == 'non_hate_speech':
                    if non_hate_speech_count < num / 2:
                        non_hate_speech_count += 1
                    elif hate_speech_count >= num / 2:
                        non_hate_speech_count += 1
                    else:
                        continue
                else:
                    continue
                self.controller.newText(data[0])
                result = self.getTestResult()
                targets.append(data[1])
                results.append(result)
                indexes.append(count)
                texts.append(self.controller.text)
                progress += 1
                if progress < 250:
                    if progress % 10 == 0:
                        print(progress)
                else:
                    if progress % 50 == 0:
                        print(progress)
            count += 1
        if len(targets) > 0:
            self.testData.addResults(targets, results, texts, indexes)

    def getCorrectLGBTTestResults(self):
        correctLGBTHateSpeech = 0
        correctHateSpeech = 0
        correctLGBT = 0
        totalLGBTHateSpeech = 0
        false_hate_speech = 0
        false_lgbtqia = 0
        false_lgbt_hate_speech = 0
        correctPositiveSpeech = 0
        totalPositiveSpeech = 0
        results = self.testData.getResults()
        for result in results:
            if len(result) > 0:
                if result[1] == '-' or result[2] == '-':
                    continue
                if result[1] == 'LGBT_hate_speech':
                    if result[2] == 'LGBT_hate_speech':
                        correctLGBTHateSpeech += 1
                        correctLGBT += 1
                        correctHateSpeech += 1
                    elif result[2] == 'hate_speech':
                        correctHateSpeech += 1
                    elif result[2] == 'LGBT_non_hate_speech':
                        correctLGBT += 1
                    totalLGBTHateSpeech += 1
                if result[1] == 'non_hate_speech':
                    if result[2] == 'non_hate_speech':
                        correctPositiveSpeech += 1
                    elif result[2] == 'LGBT_hate_speech':
                        false_lgbt_hate_speech += 1
                        false_hate_speech += 1
                        false_lgbtqia += 1
                    elif result[2] == 'hate_speech':
                        false_hate_speech += 1
                    elif result[2] == 'LGBT_non_hate_speech':
                        false_lgbtqia += 1
                    totalPositiveSpeech += 1

        print('Number of test results = ' + str(totalLGBTHateSpeech + totalPositiveSpeech))

        hate_speech_precision = 0
        if correctHateSpeech > 0 or false_hate_speech > 0:
            hate_speech_precision = correctHateSpeech / (correctHateSpeech + false_hate_speech)
        hate_speech_recall = 0
        if correctHateSpeech > 0 or totalLGBTHateSpeech > 0:
            hate_speech_recall = correctHateSpeech / totalLGBTHateSpeech
        print('')
        print('Hate Speech: ')
        print('Precision = ' + str(hate_speech_precision))
        print('Recall = ' + str(hate_speech_recall))

        lgbtqia_recall = 0
        if correctLGBT > 0 or totalLGBTHateSpeech > 0:
            lgbtqia_recall = correctLGBT / totalLGBTHateSpeech
        print('')
        print('LGBTQIA+: ')
        print('Recall = ' + str(lgbtqia_recall))

        lgbtqia_hate_speech_precision = 0
        if correctLGBTHateSpeech > 0 or false_lgbt_hate_speech > 0:
            lgbtqia_hate_speech_precision = correctLGBTHateSpeech / (correctLGBTHateSpeech + false_lgbt_hate_speech)
        lgbtqia_hate_speech_recall = 0
        if correctLGBTHateSpeech > 0 or totalLGBTHateSpeech > 0:
            lgbtqia_hate_speech_recall = correctLGBTHateSpeech / totalLGBTHateSpeech
        print('')
        print('LGBTQIA+ Hate Speech: ')
        print('Precision = ' + str(lgbtqia_hate_speech_precision))
        print('Recall = ' + str(lgbtqia_hate_speech_recall))

    def resetResults(self):
        self.testData.resetResults()
