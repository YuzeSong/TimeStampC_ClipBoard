from datetime import datetime
import clipboard

def run():
    now = datetime.now() # current date and time

    date_time = now.strftime("%H:%M:%S %Y/%m/%d")
    clipboard.copy(date_time) 	
