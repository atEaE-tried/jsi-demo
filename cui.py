from datetime import datetime
from model import jsi_mini

def main():
	# 検査項目を表示してユーザーへの入力を促す
	list = jsi_mini.itemList()
	for item in list:
		show_item(item)
		show_assessment_select()
		item.assessment = get_user_input()
		print ("-------------------")

	# 検査結果を表示する
	show_result(list)	

# 検索項目を表示する
def show_item(item: jsi_mini.Item):
	print("")
	print("No: {}".format(item.number))
	print(item.title)

# 評価ポイントの詳細を表示する
def show_assessment_select():
	print("")
	print("0: まったくない")
	print("1: ごくたまにある")
	print("2: 時々ある")
	print("3: 頻繁にある")
	print("4: いつもある")
	print("5: 質問項目にあてはまらない。（例えば、項目内容が、お子さんの状態に合わない等）")
	print("6: わからない。（例えば、項目内容を、これまで経験したことがない等）")

# 検査結果を表示する
def show_result(list:list[jsi_mini.Item]):
	# ヘッダー情報を表示してあげる
	print("")
	print("【検査結果】")
	now = datetime.now()
	print("検査日: {}".format(now.strftime("%Y年%m月%d日")))
	print("")

	# 検査結果の表示
	sumSensorSearch = jsi_mini.sumSensorySearch(list)
	show_assessment_decision("A系列:感覚探求", sumSensorSearch, jsi_mini.decisionSensorySearch(sumSensorSearch))
	
	sumSensorHypersensitivity = jsi_mini.sumSensoryHypersensitivity(list)
	show_assessment_decision("B系列:感覚過敏", sumSensorHypersensitivity, jsi_mini.decisionSensoryHypersensitivity(sumSensorHypersensitivity))
	
	total = sumSensorSearch + sumSensorHypersensitivity + jsi_mini.sumOther(list)
	show_assessment_decision("総合評価（全項目合計点）", total, jsi_mini.decisionTotal(total))

# 評価結果を表示する
def show_assessment_decision(title: str, point: int, decision: str):
	print("{}: {} 【{}】".format(title, point, decision))


# ユーザーからの入力を取得する
def get_user_input() -> jsi_mini.AssessmentPoint:
	userInput = -1

	# 0-6の入力を受け付ける　それ以外は再入力させる
	while True:
		try:
			userInput = int(input("-> "))
		except ValueError:
			userInput = -1
		
		if userInput < 0 or userInput > 6:
			print("0-6の数字を入力してください")
		else:
			break
	
	return convert_user_input_for_assessment_point(userInput)

# ユーザー入力を評価ポイントに変換する
def convert_user_input_for_assessment_point(userInput: int) -> jsi_mini.AssessmentPoint:
	if userInput == 0:
		return jsi_mini.AssessmentPoint.NONE
	elif userInput == 1:
		return jsi_mini.AssessmentPoint.VERYRARELY
	elif userInput == 2:
		return jsi_mini.AssessmentPoint.SOMETIMES
	elif userInput == 3:
		return jsi_mini.AssessmentPoint.FREQUENTLY
	elif userInput == 4:
		return jsi_mini.AssessmentPoint.ALWAYS
	elif userInput == 5:
		return jsi_mini.AssessmentPoint.NOTAPPLY
	elif userInput == 6:
		return jsi_mini.AssessmentPoint.UNKNOWN

if __name__ == "__main__":
	main()