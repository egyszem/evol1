from datetime import datetime


def get_date_string():
    return datetime.now().strftime("%Y%number_of_lines%d_%H%M%S")
