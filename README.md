# 📚 Book Recommendation System

A simple **Machine Learning based Book Recommendation System** built using **Python** and **K-Nearest Neighbors (KNN)**.
It suggests similar books based on user rating patterns.

---

## 🚀 Features

* 📖 Recommend books based on user input
* 🤝 Uses collaborative filtering (user-book interactions)
* ⚡ Fast similarity search using sparse matrix
* 🧠 Built with Scikit-learn KNN model
* 📊 Works on custom datasets (books, users, ratings)

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* SciPy

---

## 📂 Dataset

The project uses 3 CSV files:

### 1. `book.csv`

Contains book details:

* Title
* Author
* Genre
* Year
* ISBN
* Pages
* Language
* Summary

### 2. `user.csv`

Contains user information:

* user_id
* location
* age

### 3. `ratings.csv`

Contains user-book interactions:

* userid
* ISBN
* rating (1–10)

---

## ⚙️ How It Works

1. **Data Preprocessing**

   * Filter active users (more than 4 ratings)
   * Merge books and ratings data
   * Remove less popular books

2. **Pivot Table Creation**

   * Rows → Books
   * Columns → Users
   * Values → Ratings

3. **Sparse Matrix Conversion**

   * Convert pivot table to sparse matrix for efficiency

4. **Model Training**

   * Use KNN (Nearest Neighbors) to learn similarity

5. **Recommendation**

   * Input a book name
   * System returns similar books

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install pandas numpy scikit-learn scipy
```

### 2. Run the program

```bash
python bookRecomenderSystem.py
```

### 3. Enter a book name

```
Enter book name: The Echoes of Silence
```

### 4. Get recommendations 🎉

---

## 📸 Example Output

```
Recommended Books:

Beyond the Event Horizon
Quantum Drift
Starlight Rebellion
Neon Shadows
Fragments of Tomorrow
```

---

## ⚠️ Notes

* Book name must match exactly (case-sensitive)
* Ensure datasets are not empty
* Ratings dataset must be sufficiently large

---

## 🔮 Future Improvements

* 🔍 Fuzzy search (partial book names)
* 🌐 Web UI using Streamlit / Flask
* ⭐ Personalized recommendations
* 📈 Popularity-based filtering

---

## 👨‍💻 Author

**Akshit Bisht**

---

## ⭐ Contribute

Feel free to fork this repo and improve it!

---

## 📜 License

This project is open-source and free to use.
