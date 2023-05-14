from flet import *

def main(page:Page):
	page.scroll = "auto"
	# REMOVE PADDING IN SCREEN
	page.padding = 0 
	page.spacing = 0

	# NOW I CREATE 3 CONTAINER red, blue yellow
	ct = Column([
		Container(
		bgcolor="red200",
		alignment=alignment.center,
		height=page.window_height,
		content=Text("Page One",size=30,color="white"),
		# NOW FOR ACTIVATE YOU SCROLL TO CONTAINER HERE
		# ADD KEY 
		key="one"


			),
		Container(
		bgcolor="blue200",
		alignment=alignment.center,
		height=page.window_height,
		content=Text("Page two",size=30,color="white"),
		key="two"

			),
		Container(
		bgcolor="yellow200",
		alignment=alignment.center,
		height=page.window_height,
		content=Text("Page three",size=30,color="white"),
		key="three"
			),
		

		],
		# ENABLE SCROLL IN COLUMN
		scroll="auto"
		)

	# NOW CREATE 3 BUTTON NAVIGATION FOR MOVE BETWEEN SCREEN

	page.overlay.append(
		Container(
			height=160,
			bgcolor="white",
			margin=margin.only(top=150,
				left=page.window_width-60
				),
			border_radius=30,
			padding=10,
			content=Column([
				IconButton(icon="home",
					icon_color="red",

				# AND NOW IF YOU CLICK BUTTON HERE
				# YOU WILL NAVIGAATION TO CONTAINER YOU 
				# SELECT KEY
			on_click=lambda _:ct.scroll_to(key="one",duration=1000)

					),
				IconButton(icon="favorite",
					icon_color="purple",
			on_click=lambda _:ct.scroll_to(key="two",duration=1000)

					),
				IconButton(icon="arrow_circle_up",
					icon_color="orange",
					
			on_click=lambda _:ct.scroll_to(key="three",duration=1000)

			),
				

				])
			)

		)


	page.add(ct)

flet.app(target=main)
	