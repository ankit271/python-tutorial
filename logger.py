import os
import datetime
    
def logMessage(message):
    try:
        current_date = datetime.datetime.now()
        year  = current_date.year
        month = current_date.strftime("%B")
        
        if not os.path.exists('error'):
            os.mkdir('error')
            
        if not os.path.exists(f"error/{year}/{month}"):
            os.makedirs(f"error/{year}/{month}")
        
        if not os.path.exists(f"error/{year}/{month}/log_{current_date.date()}.txt"):
            with open(f"error/{year}/{month}/log_{current_date.date()}.txt", 'w') as log_file:
                log_file.write(f"{current_date} - {message}\n")
        else:
            with open(f"error/{year}/{month}/log_{current_date.date()}.txt", 'a') as log_file:
                log_file.write(f"{current_date} - {message}\n")
        
    except Exception as e:
        print("An error occurred while writing to the log file:", e)
    

