🌱 Soil Classification and Crop Prediction with Fertilizer Recommendation

This project uses machine learning and image processing techniques to classify soil types based on their characteristics and recommend the most suitable crops. Additionally, it suggests appropriate fertilizers for the predicted crops, helping farmers make informed decisions and increase productivity.

🔍 Features
  •	📊 Soil Classification: Classifies soil into categories like clay, sandy, loamy, etc., using a CNN (Convolutional Neural Network) model.
  •	🌾 Crop Prediction: Recommends crops based on soil type, temperature, humidity, pH, and rainfall data.
  •	💊 Fertilizer Recommendation: Suggests the best fertilizers for the predicted crop and current soil condition.
  •	📷 Image Input (Optional): Accepts soil images for visual classification (if enabled).
  •	📈 User-Friendly Interface: Simple and intuitive interface for entering soil data and getting instant recommendations.

🛠️ Technologies Used
   •	Python
   •	TensorFlow / Keras (for CNN)
   •	Pandas, NumPy (data processing)
   •	Scikit-learn (for ML model comparison)
   •	Matplotlib / Seaborn (visualizations)
   •	Flask or Streamlit (for deployment – optional)
  •	Jupyter Notebook

📂 Dataset
   •	Soil and crop datasets collected from [Kaggle/UCI/Open Government Data] 
       https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset,         
       https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset.
   •	Custom-labeled soil images for CNN training (optional) 

📌 How It Works
  1.	Data Collection & Preprocessing – Soil and crop datasets are cleaned and normalized.
  2.	Model Training – A CNN is trained on soil images; ML models like Decision Tree, Random Forest, and SVM are tested for crop prediction.
  3.	Prediction Pipeline – Given user inputs (e.g., soil pH, NPK values), the system predicts the best crop and suggests fertilizers.
  4.	Visualization – Graphs and charts are used to represent predictions and model performance.

🚀 Getting Started
Clone the repository:
git clone https://github.com/yourusername/soil-crop-prediction.git
cd soil-crop-prediction

Install dependencies:
pip install -r requirements.txt

Run the model / UI:
python app.py

📸 Screenshots
![login](https://github.com/user-attachments/assets/f0509f38-ccf0-4f25-b894-680fa3e3be33)
![reg](https://github.com/user-attachments/assets/18f300b1-264e-4250-ace7-bc0da2b89a43)
![soil](https://github.com/user-attachments/assets/fd969f87-d4a0-4550-bfc0-8a093c6f7b41)
![final](https://github.com/user-attachments/assets/095fd9b4-95c1-45db-92a8-c9f0d85a049a)



🤝 Contributions
Contributions are welcome! Please feel free to fork the repository and submit pull requests.


