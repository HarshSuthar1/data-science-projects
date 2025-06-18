import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Load & preprocess data
qual_df = pd.read_csv('Data/F1_2025_QualifyingResults.csv')
race_df = pd.read_csv('Data/F1_2025_RaceResults.csv')

# Replace non-finishers with a dummy position
race_df['Position'].replace(['DQ', 'NC'], 21, inplace=True)
qual_df['Position'].replace('NC', 0, inplace=True)

# Convert to numeric
race_df['Position'] = pd.to_numeric(race_df['Position'])
race_df['Points'] = pd.to_numeric(race_df['Points'])
qual_df['Position'] = pd.to_numeric(qual_df['Position'])

# Convert times
time_cols = ['Q1', 'Q2', 'Q3']
for col in time_cols:
    qual_df[col] = pd.to_timedelta('00:' + qual_df[col], errors='coerce')
    qual_df[col] = pd.to_numeric(qual_df[col], errors='coerce')

race_df['Fastest Lap Time'] = pd.to_timedelta('00:' + race_df['Fastest Lap Time'], errors='coerce')
race_df['Fastest Lap Time'] = pd.to_numeric(race_df['Fastest Lap Time'], errors='coerce')

# 2. Create Result label: Gain, Same, Loss
def comparing(race_pos, qual_pos):
    if qual_pos > race_pos:
        return 'Gain'
    elif qual_pos == race_pos:
        return 'Same'
    else:
        return 'Loss'

race_df['Result'] = race_df.apply(lambda x: comparing(x['Position'], x['Starting Grid']), axis=1)

# 3. Merge datasets
merged_df = qual_df.merge(race_df[['No', 'Track', 'Result']], on=['No', 'Track'])

# 4. Select features and target
X = merged_df.drop(columns=['Result'])
y = merged_df['Result']

# 5. Encode categorical columns
categorical_cols = ['Track', 'Driver', 'Team']
encoder = OrdinalEncoder()
X[categorical_cols] = encoder.fit_transform(X[categorical_cols])

# 6. Fill missing values
X.fillna(0, inplace=True)

# 7. Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 8. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 9. Train model
model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# 10. Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
