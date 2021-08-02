def font(size: int):
    return ("Courier New", size)


main_table = {
    "headings": ["idx", "url"],
    "size": (300, 30),
    "auto_size_columns": False,
    "font": font(11),
    "col_widths": [6, 70],
    "justification": "left",
    "text_color": "#000000",
    "alternating_row_color": "#ffffff",
}

price_text = {"font": font(11)}
price_input = {
    "size": (6, 1),
    "font": font(15),
    "justification": "right",
}
keyword_text = {"font": font(11)}
keyword = {
    "size": (12, 1),
    "font": font(15),
}
log = {
    "size": (40, 10),
    "border_width": 2,
    "autoscroll": True,
    "auto_refresh": True,
    "font": font(11),
}
