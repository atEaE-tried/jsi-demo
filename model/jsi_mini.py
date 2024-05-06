from enum import Enum

# 検索項目
class Item:

	# Constructor
	def __init__(self, number: int, title: str, type: Enum):
		self._number = number
		self._title = title
		self._type = type
		self._assessment = AssessmentPoint.UNKNOWN

	# number getter
	@property
	def number(self):
		return self._number

	# title getter
	@property
	def title(self):
		return self._title
	
	# type getter
	@property
	def type(self):
		return self._type
	
	# assessment getter
	@property
	def assessment(self):
		return self._assessment

	# assessment setter
	@assessment.setter
	def assessment(self, assessment: Enum):
		self._assessment = assessment


# 感覚属性（検査項目が属する属性を表す）
class SensoryType(Enum):
	A = 1     # A系列: 感覚探求
	B = 2     # B系列: 感覚過敏
	AB = 3    # AB系列: 感覚探求と感覚過敏の両方
	OTHER = 4 # その他

# 評価ポイント
class AssessmentPoint(Enum):
	NONE = 0        # まったくない　
	VERYRARELY = 1  # ごくたまにある
	SOMETIMES = 2   # 時々ある
	FREQUENTLY = 3  # 頻繁にある
	ALWAYS = 4      # いつもある
	NOTAPPLY = 5    # 質問項目にあてはまらない。（例えば、項目内容が、お子さんの状態に合わない等）
	UNKNOWN = 6     # わからない。（例えば、項目内容を、これまで経験したことがない等）

# 検査項目リストA系列: 感覚探求を合算する
def sumSensorySearch(list: list[Item]) -> int:
	sum = 0
	for item in list:
		if item.type == SensoryType.A or item.type == SensoryType.AB:
			# A系列の評価ポイントを合計する
            # ただし、「まったくない」、「質問項目にあてはまらない」、「わからない」は合算する必要がないので無視
			if item.assessment != AssessmentPoint.NONE and item.assessment != AssessmentPoint.NOTAPPLY and item.assessment != AssessmentPoint.UNKNOWN:
				sum += item.assessment.value
	return sum

# 検査項目リストB系列: 感覚過敏を合算する
def sumSensoryHypersensitivity(list: list[Item]) -> int:
	sum = 0
	for item in list:
		if item.type == SensoryType.B or item.type == SensoryType.AB:
			# A系列の評価ポイントを合計する
            # ただし、「まったくない」、「質問項目にあてはまらない」、「わからない」は合算する必要がないので無視
			if item.assessment != AssessmentPoint.NONE and item.assessment != AssessmentPoint.NOTAPPLY and item.assessment != AssessmentPoint.UNKNOWN:
				sum += item.assessment.value
	return sum

# 検査項目リストその他: その他の評価ポイントを合算する
def sumOther(list: list[Item]) -> int:
	sum = 0
	for item in list:
		if item.type == SensoryType.OTHER:
			# その他の評価ポイントを合計する
			# ただし、「まったくない」、「質問項目にあてはまらない」、「わからない」は合算する必要がないので無視
			if item.assessment != AssessmentPoint.NONE and item.assessment != AssessmentPoint.NOTAPPLY and item.assessment != AssessmentPoint.UNKNOWN:
				sum += item.assessment.value
	return sum

# 検査項目リストA系列: 感覚探求を判定する
def decisionSensorySearch(sum: int):
	if sum <= 4:
		return CONST_DECISION_GREEN
	if sum > 4 and sum <= 8:
		return CONST_DECISION_YELLOW
	if sum > 8:
		return CONST_DECISION_RED

# 検査項目リストB系列: 感覚過敏を判定する
def decisionSensoryHypersensitivity(sum: int):
	if sum <= 3:
		return CONST_DECISION_GREEN
	if sum > 3 and sum <= 6:
		return CONST_DECISION_YELLOW
	if sum > 6:
		return CONST_DECISION_RED

# 検査項目リスト全体: 全体の評価ポイントを判定する
def decisionTotal(sum: int):
	if sum <= 10:
		return CONST_DECISION_GREEN
	if sum > 10 and sum <= 17:
		return CONST_DECISION_YELLOW
	if sum > 17:
		return CONST_DECISION_RED

CONST_DECISION_GREEN = "GREEN"
CONST_DECISION_YELLOW = "YELLOW"
CONST_DECISION_RED = "RED"

# 検索項目リストを返却する
def itemList():
	r = [
		Item(1, "滑り台など、滑る遊具を怖がる", SensoryType.B),
		Item(2, "非常に長い間、自分一人であるいは遊具に乗ってぐるぐる回転することを好む", SensoryType.A),
		Item(3, "粘土、水、泥、砂などの遊びを他の子供よりも過度に好む", SensoryType.A),
		Item(4, "粘土、水、泥、砂などの遊びを嫌がる", SensoryType.B),
		Item(5, "手でなんでも触ってまわる", SensoryType.A),
		Item(6, "抱かれたり、手を握られたりすることを嫌う", SensoryType.B),
		Item(7, "洗面・洗髪・散髪・歯磨き・爪切り・耳かき等を嫌がる", SensoryType.B),
		Item(8, "そばに人が近づくと、すっと逃げる", SensoryType.B),
		Item(9, "呼びかけても、振り向かないことがある", SensoryType.OTHER),
		Item(10,"理由もなく周囲をうろうろしたり、動き回ったりしている事が多い", SensoryType.A),
		Item(11,"いろいろな物が見えると、気が散りやすくなる", SensoryType.OTHER),
		Item(12,"座っている時や遊んでいる時に、繰り返し頭を振ったり体全体を揺らす等の癖がみられる", SensoryType.A),
		Item(13,"つま先歩きをすることが多い", SensoryType.AB),
		Item(14,"固い物（食物以外）を口に入れ、噛んでいることがある", SensoryType.A),
		Item(15,"偏食がある", SensoryType.B),
		Item(16,"特定の音に非常に過敏な反応をする", SensoryType.B),
		Item(17,"回転物（車のタイヤの回転、換気扇、扇風機など）を見つめることを好む", SensoryType.A),
		Item(18,"転びやすかったり、簡単にバランスを崩しやすい", SensoryType.OTHER),
		Item(19,"体がぐにゃぐにゃしていて、椅子から簡単にずり落ちそうな座り方をしている", SensoryType.OTHER),
		Item(20,"風船や動物などを、そっと握ることができず、握り方の加減がわからない", SensoryType.OTHER),
	]
	return r