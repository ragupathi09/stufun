import pandas as pd
from datetime import datetime

# Sample new hospital record
new_record = {
    'patient_id': 'P123456',
    'name': 'Jane Doe',
    'dob': '1990-04-15',
    'admission_date': datetime.now().strftime('%Y-%m-%d'),
    'diagnosis': 'Pneumonia',
    'doctor': 'Dr. Smith'
}

# Convert to DataFrame
new_df = pd.DataFrame([new_record])

# Append to existing CSV file
new_df.to_csv('hospital_records.csv', mode='a', header=False, index=False)

print("Record added successfully.")
