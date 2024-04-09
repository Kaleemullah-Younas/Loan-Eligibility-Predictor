# 🏦 BANK LOAN PREDICTOR

The Bank Loan Prediction Model utilizes machine learning algorithms to predict loan eligibility based on user-provided financial and personal data. Deployed using Streamlit, the application offers an intuitive interface for users to input their information and receive instant loan approval predictions.

## Preview

![Loan Prediction Model Preview](loan_predictor.gif)

## Working of the Project

The **Bank Loan Prediction Model** is designed to assist individuals in determining their eligibility for a bank loan by analyzing various factors such as income, credit score, employment status, and property area.

### Data Collection and Preprocessing

1. **Dataset:** Utilized a comprehensive dataset containing historical loan application data, including attributes such as applicant income, credit score, and loan status.

2. **Feature Engineering:** Preprocessed the data by handling missing values, encoding categorical variables, and scaling numerical features to prepare it for model training.

### Machine Learning Model

3. **Model Selection:** Employed a Support Vector Machine (SVM) classifier to train the loan prediction model due to its ability to handle non-linear decision boundaries and high-dimensional feature spaces.

4. **Model Training:** Trained the SVM model on the preprocessed dataset to learn patterns and relationships between input features and loan approval decisions.

### User Interaction

5. **Streamlit Interface:** Developed an interactive user interface using Streamlit, allowing users to input their financial and personal information and receive real-time loan approval predictions.

6. **Loan Prediction:** Upon user submission, the application processes the input data using the trained SVM model to predict whether the user is likely to be approved for a bank loan.

### Visualizations

7. **Prediction Display:** Visualized the loan approval prediction along with relevant details such as applicant name, account number, and loan outcome.

8. **User-Friendly UI:** Designed an intuitive interface with clear input fields and informative output displays to enhance user experience and understanding.

This project aims to simplify the loan application process for individuals by providing them with instant feedback on their loan eligibility, thereby facilitating informed financial decisions.

## How to Run the Project

Follow these steps to set up and run the project locally:

1. **Clone the Repository:**
   Clone this repository to your local machine.

    ```bash
    git clone https://github.com/drstrange102/Loan-Eligibility-Predictor.git
    ```

2. **Install Dependencies:**
   Install Python 3.10 and all additional dependencies listed in the requirements.txt file.

    ```bash
    pip install -r ./requirements.txt
    ```

3. **Run the Streamlit App:**
   Open a terminal and navigate to the project directory. Then, run the Streamlit app.

    ```bash
    streamlit run app.py
    ```

The Streamlit app will be hosted on `localhost:8501`.

## Contribute:

Contributions from the developer community are welcome to enhance and refine the Bank Loan Prediction Model. You can contribute by forking the repository, submitting issues, and creating pull requests to improve the project's functionality and user experience.🎬✨
