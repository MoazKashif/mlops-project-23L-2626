# MLOps Assignment 1: Version Control & Machine Learning Workflow

**Student Name:** Chaudary Moaz Kashif
**Student ID / Roll No:** 23L-2626
**Repository:** `mlops-project-23L-2626`

---

## 📌 Project Overview

This repository contains **MLOps Assignment 1**, focused on establishing a reproducible machine learning workflow using modern **version control and project organization practices**.

The project demonstrates how to structure a machine learning repository by maintaining a clear separation between:

* Source code
* Raw datasets
* Trained machine learning models
* Project dependencies
* Version control configuration

The repository also follows MLOps best practices by preventing large datasets and serialized model artifacts from being tracked by Git through an appropriately configured `.gitignore` file.

---

## 🎯 Objectives

The primary objectives of this assignment are to:

* Establish a clean and reproducible ML project structure.
* Implement a machine learning training pipeline.
* Manage source code using Git and GitHub.
* Demonstrate feature preprocessing and scaling.
* Maintain separate branches for different development tasks.
* Practice Git merge and conflict resolution.
* Prevent large datasets and model artifacts from being committed to version control.
* Document the complete workflow for reproducibility.

---

## 📁 Repository Structure

```text
mlops-project-23L-2626/
│
├── data/
│   └── dataset.csv
│
├── src/
│   └── train_23L-2626.py
│
├── model/
│   └── model_23L-2626.pkl
│
├── .gitignore
├── requirements.txt
└── README.md
```

### Directory & File Description

| File / Directory     | Description                                                           |
| -------------------- | --------------------------------------------------------------------- |
| `data/`              | Contains the raw machine learning dataset.                            |
| `src/`               | Contains the project's source code.                                   |
| `train_23L-2626.py`  | Performs data preprocessing, model training, and model serialization. |
| `model/`             | Stores generated trained model artifacts locally.                     |
| `model_23L-2626.pkl` | Serialized trained machine learning model.                            |
| `.gitignore`         | Prevents datasets and model artifacts from being tracked by Git.      |
| `requirements.txt`   | Contains the Python dependencies required to run the project.         |
| `README.md`          | Project documentation and setup instructions.                         |

> **Note:** The `data/` directory and generated model artifacts are intentionally excluded from Git tracking according to the project's MLOps artifact-management strategy.

---

## ⚙️ Environment Setup

Follow the steps below to reproduce the project environment locally.

### 1. Clone the Repository

```bash
git clone https://github.com/MoazKashif/mlops-project-23L-2626.git
cd mlops-project-23L-2626
```

### 2. Create a Virtual Environment

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Upgrade `pip` and install the required packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🚀 Running the Training Pipeline

Once the environment is configured and the required dataset is available, run the training script:

```bash
python src/train_23L-2626.py
```

The script performs the required preprocessing and machine learning operations before saving the trained model as a serialized `.pkl` file.

### Expected Output

```text
Loading dataset for Student ID: 23L-2626...
Model successfully trained and saved to model/model_23L-2626.pkl
```

After successful execution, the trained model should be available at:

```text
model/model_23L-2626.pkl
```

---

## 🛡️ MLOps Artifact Management

A key objective of this assignment is to demonstrate proper handling of machine learning artifacts.

The following files/directories are excluded from Git tracking:

```text
data/
model/*.pkl
```

### Why?

Raw datasets and serialized machine learning models can become large and should generally not be committed directly to a Git repository.

Keeping these artifacts outside Git:

* Reduces repository size.
* Improves Git performance.
* Prevents unnecessary binary files from being versioned.
* Keeps source-code version control clean.
* Follows standard MLOps project organization principles.

### Verify Git Tracking

To verify the repository status:

```bash
git status
```

You can also inspect the configured ignore rules using:

```bash
cat .gitignore
```

---

## 🌿 Git Workflow & Branch Strategy

The project follows a feature-based Git workflow to demonstrate controlled development and version management.

### Main Branch

```text
main
```

The `main` branch contains the stable and production-ready version of the project.

### Feature Branches

#### Preprocessing

```text
feature-preprocessing-23L-2626
```

This branch was used to implement and evaluate data preprocessing techniques, including feature scaling with:

```python
StandardScaler
```

#### Hyperparameter / Scaling Evaluation

```text
feature-tuning-23L-2626
```

This branch was used to evaluate alternative feature-scaling approaches, including:

```python
MinMaxScaler
```

### Branch Workflow

The general development workflow is:

```text
main
 │
 ├── feature-preprocessing-23L-2626
 │
 └── feature-tuning-23L-2626
```

Changes are developed and tested within feature branches before being merged into the main branch.

---

## 🔀 Merge Conflict Resolution

As part of the version-control workflow, merge conflicts were intentionally handled during development.

Conflicts were resolved at the **line level using Visual Studio Code's built-in merge-conflict resolution tools**.

The resolution process involved:

1. Identifying conflicting sections.
2. Reviewing changes from both branches.
3. Selecting or combining the appropriate changes.
4. Removing Git conflict markers.
5. Testing the resulting code.
6. Committing the resolved changes.

Typical Git conflict markers include:

```text
<<<<<<< HEAD
Current branch changes
=======
Incoming branch changes
>>>>>>> feature-branch
```

After resolving the conflict, the changes were staged and committed normally.

---

## 🔄 Reproducibility Workflow

The project can be reproduced using the following workflow:

```text
Clone Repository
       │
       ▼
Create Virtual Environment
       │
       ▼
Install Dependencies
       │
       ▼
Load Dataset
       │
       ▼
Preprocess Data
       │
       ▼
Train Machine Learning Model
       │
       ▼
Serialize Model
       │
       ▼
Save Model Artifact
```

This structure ensures that the training pipeline can be executed consistently on another machine with the required dependencies and dataset.

---

## 🧰 Technologies Used

| Technology             | Purpose                                   |
| ---------------------- | ----------------------------------------- |
| **Python**             | Machine learning pipeline implementation  |
| **Git**                | Version control                           |
| **GitHub**             | Remote repository and collaboration       |
| **Visual Studio Code** | Development and merge-conflict resolution |
| **scikit-learn**       | Data preprocessing and machine learning   |
| **Pickle**             | Model serialization                       |

---

## 📋 MLOps Practices Demonstrated

This assignment demonstrates the following fundamental MLOps concepts:

* ✅ Version control with Git
* ✅ Remote repository management with GitHub
* ✅ Feature-based branching
* ✅ Merge and conflict resolution
* ✅ Reproducible environment setup
* ✅ Dependency management
* ✅ Data and source-code separation
* ✅ Model artifact management
* ✅ `.gitignore` configuration
* ✅ Machine learning pipeline documentation

---

## 👨‍🎓 Student Information

| Field                    | Information              |
| ------------------------ | ------------------------ |
| **Student Name**         | Chaudary Moaz Kashif     |
| **Student ID / Roll No** | 23L-2626                 |
| **Assignment**           | MLOps Assignment 1       |
| **Repository**           | `mlops-project-23L-2626` |

---

## 📄 License

This project was developed as part of an academic MLOps assignment.
