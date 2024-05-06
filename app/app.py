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
		# construct
		super().__init__()
		self.items = self.convert_to_gui_item(jsi_mini.itemList())

		# window setting
		self.title("JSI-mini Demo")
		self.geometry("800x600")

		# header setting
		self.header = self.create_header_frame()

		# main setting
		self.current_main_frame_index = 0
		self.item_frames = [self.create_main_frame(item) for item in self.items]

		# footer setting
		self.footer = tk.Frame(self)
		self.btn_prev = tk.Button(self.footer, text="＜ 前の項目", command=self.go_prev_item_frame)
		self.btn_prev.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
		self.btn_next = tk.Button(self.footer, text="次の項目 ＞", command=self.go_next_item_frame)
		self.btn_next.grid(row=0, column=1, sticky="ew", padx=5, pady=10)
		self.footer.pack(side="bottom", fill="x")
		self.footer.grid_columnconfigure(0, weight=1)
		self.footer.grid_columnconfigure(1, weight=1)

		self.update_main_frame()
		self.update_footer

	# headerを生成する
	def create_header_frame(self) -> tk.Frame:
		header = tk.Frame(self)
		tk.Label(header, text="JSI-mini Demo", font=("Helvetica", 20)).pack()
		return header

	# 動的に検査項目のframeを生成する
	def create_main_frame(self, item: GUIItem) -> tk.Frame:
		frame = tk.Frame(self, borderwidth=2, relief="ridge")
		tk.Label(frame, text=f"No {item.number}", font=("Helvetica", 12)).pack(anchor="w", padx=5, pady=5)

		label = tk.Label(frame, text=f"{item.title}", wraplength=450)
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
			tk.Radiobutton(frame, text=text, variable=item.selected, value=value, font=("Helvetica", 10)).pack(anchor="w")
		return frame

	# 描画されている検査項目のframeを更新する
	def update_main_frame(self):
		# 先にframe全体をを初期化して、重複表示されないようにする
		self.disable_main_frame()

		# 対象のframeを描画する
		self.item_frames[self.current_main_frame_index].pack()
		self.update_footer()

	# 検査項目のframeを非表示にする
	def disable_main_frame(self):
		for frame in self.item_frames:
			# 対象のframeを一時的にwindowsから削除する
			# Windowに描画されていないというだけで、メモリ上にframeは残っている
			frame.pack_forget()

	# footerを生成する
	def create_footer_frame(self) -> tk.Frame:
		footer = tk.Frame(self)
		btn_prev = tk.Button(footer, text="＜ 前の項目", command=self.go_prev_item_frame)
		btn_prev.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
		btn_next = tk.Button(footer, text="次の項目 ＞", command=self.go_next_item_frame)
		btn_next.grid(row=0, column=1, sticky="ew", padx=5, pady=10)
		return footer

	# footerを更新する
	def update_footer(self):
		# 最初の検査項目の場合、前の項目ボタンを無効化する
		if self.current_main_frame_index == 0:
			self.btn_prev.config(state="disabled")
		else:
			self.btn_prev.config(state="normal")
		
		# 最後の検査項目の場合、次の項目ボタンの内容を変更する
		if self.current_main_frame_index == len(self.items) - 1:
			self.btn_next.config(text="診断する", command=self.show_result)
		else:
			self.btn_next.config(text="次の項目 ＞", command=self.go_next_item_frame)

	# footerを非表示にする
	def disable_footer(self):
		self.footer.pack_forget()

	# 次の検査項目のframeを表示する
	def go_next_item_frame(self):
		# listのindexを超過しないように循環させる
		self.current_main_frame_index = (self.current_main_frame_index + 1) % len(self.items)
		self.update_main_frame()

	# 前の検査項目のframeを表示する
	def go_prev_item_frame(self):
		# listのindexを超過しないように循環させる
		self.current_main_frame_index = (self.current_main_frame_index - 1) % len(self.items)
		self.update_main_frame()

	# 検査結果を表示する
	def show_result(self):
		# 余計なframeを非表示にする
		self.disable_main_frame()
		self.disable_footer()
	
	# jsi_mini.ItemのリストをGUIItemのリストに変換する
	def convert_to_gui_item(self, items: list[jsi_mini.Item]) -> list[GUIItem]:
		r = []
		for i in items:
			gi = GUIItem(i.number, i.title, i.type)
			gi.selected = tk.IntVar()
			gi.selected.set(0)
			r.append(gi)
		return r
