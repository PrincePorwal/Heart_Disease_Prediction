# Heart Disease Prediction System

This system allows you to predict heart disease using a trained machine learning model. Follow these steps to use the prediction system:

## Getting Started

1. **Open the Notebook**: Start by opening the Jupyter Notebook, which contains the code for training and saving the heart disease prediction model.

2. **Run All Cells**: Execute all the cells in the notebook. You can do this by clicking on "Cell" in the menu and selecting "Run All" or by pressing `Shift + Enter` for each cell.

## Download Files

3. **Download the Pickle File**: After running all the cells, the notebook will generate or load a machine learning model and save it as a pickle file. Download this file from the appropriate cell in the notebook.

4. **Download the `main.py` File**: You'll also need a Python script named `main.py` for running the Streamlit application. Download this file from the github where you found the notebook.

## Setup and Execution

5. **Put Both Files in the Same Folder**: Place both the downloaded pickle file (from step 3) and the `main.py` file (from step 4) in the same directory or folder. This is essential as the Streamlit application requires access to the trained model.

6. **Run the Streamlit Application**: Open your terminal or command prompt, navigate to the folder where you placed the pickle and `main.py` files, and run the following command:

   ```bash
   python -m streamlit run main.py
