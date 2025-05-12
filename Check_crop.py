import tkinter as tk
from tkinter import ttk
import joblib
import numpy as np

# Load the trained SVM model
model = joblib.load("SVM.joblib")

# Define state mapping for encoding
state_mapping = {
    "Andaman and Nicobar": 0, "Andhra Pradesh": 1, "Assam": 2,
    "Chattisgarh": 3, "Goa": 4, "Gujarat": 5, "Haryana": 6, "Himachal Pradesh": 7,
    "Jammu and Kashmir": 8, "Karnataka": 9, "Kerala": 10, "Madhya Pradesh": 11,
    "Maharashtra": 12, "Manipur": 13, "Meghalaya": 14, "Nagaland": 15,
    "Odisha": 16, "Pondicherry": 17, "Punjab": 18, "Rajasthan": 19,
    "Tamil Nadu": 20, "Telangana": 21, "Tripura": 22, "Uttar Pradesh": 23,
    "Uttrakhand": 24, "West Bengal": 25
}

# Define crop labels and their respective organic fertilizers
crop_fertilizers = {
    "Apple": "Compost, Cow manure", "Banana": "Vermicompost, Green manure", "Blackgram": "Farmyard manure, Compost",
    "ChickPea": "Biofertilizers, Cow dung manure", "Coconut": "Neem cake, Poultry manure", "Coffee": "Bone meal, Green manure",
    "Cotton": "Farmyard manure, Vermicompost", "Grapes": "Compost, Poultry manure", "Jute": "Bio-compost, Organic mulches",
    "Mango": "Cow dung, Neem cake", "MothBeans": "Green manure, Compost", "MungBean": "Biofertilizers, Compost",
    "Orange": "Vermicompost, Bone meal", "KidneyBeans": "Cow manure, Compost", "Lentil": "Farmyard manure, Neem cake",
    "Maize": "Compost, Vermicompost", "Papaya": "Cow dung, Biofertilizers", "PigeonPeas": "Compost, Green manure",
    "Pomgranate": "Farmyard manure, Bone meal", "Rice": "Organic compost, Green manure", "Watermelon": "Neem cake, Poultry manure",
    "Muskmelon": "Farmyard manure, Green manure"
}

# Predict function
def predict_crop():
    try:
        features = np.array([
            float(entry_n.get()), float(entry_p.get()), float(entry_k.get()),
            float(entry_temp.get()), float(entry_humidity.get()), float(entry_ph.get()),
            float(entry_rainfall.get()), state_mapping.get(state_var.get(), 26)
        ]).reshape(1, -1)
        prediction = model.predict(features)
        crop_name = prediction[0]
        crop_result.set(crop_name)
        fertilizer_result.set(crop_fertilizers.get(crop_name, "No recommendation available"))
    except ValueError:
        crop_result.set("Invalid Input")
        fertilizer_result.set("")

# Create the main Tkinter window
root = tk.Tk()
root.title("Crop and Soil Prediction System")
root.geometry("900x600")
root.configure(bg="lightblue")

# Title Label
title_label = tk.Label(root, text="Crop and Soil Prediction System", font=('Helvetica', 20, 'bold'), bg='lightblue')
title_label.pack(pady=10)

# Input Fields
frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=10)

labels = ["N", "P", "K", "Temperature", "Humidity", "pH", "Rainfall", "State"]
entries = []

for i, label in enumerate(labels):
    tk.Label(frame, text=label, font=("Arial", 12), bg="lightblue").grid(row=i, column=0, pady=5, padx=10, sticky='w')
    if label == "State":
        state_var = tk.StringVar()
        state_menu = ttk.Combobox(frame, textvariable=state_var, values=list(state_mapping.keys()), width=20)
        state_menu.grid(row=i, column=1, pady=5, padx=10)
    else:
        entry = tk.Entry(frame, width=25)
        entry.grid(row=i, column=1, pady=5, padx=10)
        entries.append(entry)

entry_n, entry_p, entry_k, entry_temp, entry_humidity, entry_ph, entry_rainfall = entries

# Predict Button
crop_result = tk.StringVar()
fertilizer_result = tk.StringVar()
predict_button = tk.Button(root, text="Predict Crop", command=predict_crop, font=("Arial", 14), bg="green", fg="white")
predict_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, textvariable=crop_result, font=('Arial', 16, 'bold'), bg='lightblue', fg='red')
result_label.pack(pady=10)

# Fertilizer Recommendation
fertilizer_label = tk.Label(root, text="Recommended Organic Fertilizers:", font=('Arial', 14, 'bold'), bg='lightblue', fg='black')
fertilizer_label.pack(pady=5)
fertilizer_result_label = tk.Label(root, textvariable=fertilizer_result, font=('Arial', 12), bg='lightblue', fg='darkgreen')
fertilizer_result_label.pack(pady=5)

root.mainloop()
