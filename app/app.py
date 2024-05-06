import tkinter as tk
from model import jsi_mini

# GUI用にItemクラスを継承したGUI専用のItemクラス
class GUIItem(jsi_mini.Item):
	def __init__(self, number, title, type):
		super().__init__(number, title, type)

	# selected getter
	# radio buttonの選択状態を保持する変数
	# 排他制御をするためにtk.IntVarが必要
	@property
	def selected(self)-> tk.IntVar:
		return self._selected
	
	# selected setter
	@selected.setter
	def selected(self, selected: tk.IntVar):
		self._selected = selected

# Tkを継承したAppクラス
class JSIApp(tk.Tk):

	# initialize
	def __init__(self):
		# window setting
		super().__init__()
		self.title("JSI-mini Demo")
		self.geometry("800x600")

		header = tk.Frame(self)
		tk.Label(header, text="JSI-mini Demo", font=("Helvetica", 20)).pack()
		header.pack()

		# construct
		self.items = self.convert_to_gui_item(jsi_mini.itemList())
		self.current_index = 0
		self.item_frames = [self.create_item_frame(item) for item in self.items]

		self.btn_prev = tk.Button(self, text="Prev", command=self.go_prev_item_frame)
		self.btn_prev.pack(side="bottom", fill="x")

		self.btn_next = tk.Button(self, text="Next", command=self.go_next_item_frame)
		self.btn_next.pack(side="bottom", fill="x")

		self.update_item_frame()

	# 動的に検査項目のframeを生成する
	def create_item_frame(self, item: GUIItem) -> tk.Frame:
		frame = tk.Frame(self, borderwidth=2, relief="ridge")	
		label = tk.Label(frame, text=f"Item {item.number}: {item.title}", wraplength=300)
		label.pack(expand=True, fill="both", padx=20, pady=20)

		# radio buttonを生成する
		for text, value in [
			("0: まったくない", 0), 
			("1: ごくたまにある", 1), 
			("2: 時々ある", 2),
			("3: 頻繁にある", 3),
			("4: いつもある", 4),
			("5: 質問項目にあてはまらない。（例えば、項目内容が、お子さんの状態に合わない等）", 5),
			("6: わからない。（例えば、項目内容を、これまで経験したことがない等）", 6),
		]:
			tk.Radiobutton(frame, text=text, variable=item.selected, value=value).pack(anchor="w")
		return frame

	# 描画されている検査項目のframeを更新する
	def update_item_frame(self):
		for frame in self.item_frames:
			# 対象のframeを一時的にwindowsから削除する
			# Windowに描画されていないというだけで、メモリ上にframeは残っている
			frame.pack_forget()

		# 対象のframeを描画する
		# 先にframeを初期化しているので、重複表示はされないはず
		self.item_frames[self.current_index].pack()

	# 次の検査項目のframeを表示する
	def go_next_item_frame(self):
		# listのindexを超過しないように循環させる
		self.current_index = (self.current_index + 1) % len(self.items)
		self.update_item_frame()

	def go_prev_item_frame(self):
		# listのindexを超過しないように循環させる
		self.current_index = (self.current_index - 1) % len(self.items)
		self.update_item_frame()
	
	def convert_to_gui_item(self, items: list[jsi_mini.Item]) -> list[GUIItem]:
		r = []
		for i in items:
			gi = GUIItem(i.number, i.title, i.type)
			gi.selected = tk.IntVar()
			gi.selected.set(0)
			r.append(gi)
		return r
