import tkinter as tk

# Frameを継承したLandingPageクラス
class LandingPage(tk.Frame):
	# initialize
	def __init__(self, parent):
		super().__init__(parent)

		label = tk.Label(self, text="JSI-mini Demo", font=("Helvetica", 16))
		label.pack()

		start_button = tk.Button(self, text="開 始", command=lambda: parent.show("AssessmentPage"))
