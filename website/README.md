# Suraj Dattatray Ghadage — Portfolio Website

A modern, responsive, recruiter-ready personal portfolio website for **Suraj Dattatray Ghadage**, a Computer Science undergraduate specializing in **Data Analytics** and **Full-Stack Software Development**.

Built strictly in accordance with [`portfolio-website-build-brief.md`](portfolio-website-build-brief.md) and [`Suraj_Ghadage_Resume.pdf`](assets/Suraj_Ghadage_Resume.pdf).

---

## 🌟 Live Demo & Preview
- **Local:** Open `index.html` in any modern web browser or start a static server.
- **GitHub Pages:** `https://<username>.github.io/<repo-name>/`

---

## 🛠️ Tech Stack & Architecture

| Layer | Technology | Purpose |
|---|---|---|
| **Markup** | HTML5 (Semantic) | Accessible, SEO-optimized, zero build dependencies |
| **Styling** | Modular CSS3 | Custom properties design system, Grid & Flexbox, dark theme |
| **Behavior** | Vanilla JavaScript (ES6+) | Sticky nav, scroll spy, smooth scroll, form validation, copy-to-clipboard |
| **Typography** | Google Fonts | `Space Grotesk` (Headings) + `Inter` (Body copy) |
| **Icons** | Font Awesome 6 CDN | Crisp vector icons for skills, contact, and navigation |
| **Assets** | Custom Vector SVGs | Monogram avatar, favicon, and bespoke project visual diagrams |
| **Form Handling** | Formspree API | Asynchronous contact form submissions with seamless `mailto:` fallback |

---

## 📂 Project Structure

```
portfolio-website/
├── index.html                   # Main single-page semantic HTML structure
├── css/
│   └── styles.css               # Design system, CSS variables, responsive breakpoints
├── js/
│   └── script.js                # Mobile nav, IntersectionObserver, scroll spy, toast
├── assets/
│   ├── Suraj_Ghadage_Resume.pdf # Source resume PDF for one-click recruiter download
│   ├── icons/
│   │   └── favicon.svg          # SG monogram SVG favicon
│   ├── images/
│   │   ├── pimage.png           # Professional profile headshot portrait
│   │   ├── suraj-monogram.svg   # High-resolution circular SVG monogram avatar
│   │   ├── cyber-crime-analytics.svg     # Dashboard visual for Cyber Crime project
│   │   ├── statistical-crime-trend.svg   # Regression chart visual for Crime Modeler
│   │   ├── car-price-prediction.svg      # ML regression visual for Car Price model
│   │   └── movie-recommender-system.svg  # NLP similarity visual for Movie Recommender
│   └── notebooks/
│       ├── car.ipynb            # Jupyter notebook for Car Price Prediction
│       └── new.ipynb            # Jupyter notebook for Movie Recommendation System
├── car.ipynb                    # Machine learning regression & EDA notebook
├── new.ipynb                    # NLP & Content-based movie recommender notebook
├── portfolio-website-build-brief.md      # Specification and content guidelines
└── README.md                    # Project documentation
```

---

## 🎯 Sections & Content Fidelity

Every fact, technical skill, and experience bullet is faithfully derived from `Suraj_Ghadage_Resume.pdf`:

1. **Sticky Header & Nav:** Brand monogram, quick jump navigation, resume download button, and mobile hamburger drawer.
2. **Hero / Landing:** Prominent name typography, dynamic tagline, internship badge, Class of 2027 indicator, and CTA buttons.
3. **About Me:** Verbatim executive summary, academic timeline at Willingdon College (Shivaji University), and core competencies.
4. **Technical Skills:** 5 distinct resume categories:
   - *Programming Languages* (Python, Java, C#, C++, SQL, HTML5, CSS3, JavaScript)
   - *Analytics & BI Tools* (Power BI, DAX, Advanced Excel, Power Query, Pivot Tables, VLOOKUP, EDA)
   - *Libraries & Frameworks* (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
   - *Database Systems* (MySQL, RDBMS, SQL Query Optimization)
   - *Core Competencies* (Statistical Analysis, Data Visualization, OOP, Data Structures)
5. **Professional Experience:** Softspara Software & Data Analyst Intern with all 4 responsibility bullets.
6. **Key Projects:**
   - *Cyber Crime Analytics System* (EDA pipeline, Power BI dashboards, threat models)
   - *Statistical Crime Trend & Pattern Modeler* (Longitudinal trend regression, hypothesis testing)
   - *Used Car Price Prediction & Valuation Model* (`car.ipynb` — Random Forest & OLS Regression, R² & MAE benchmarks, vehicle feature EDA)
   - *Content-Based Movie Recommendation Engine* (`new.ipynb` — TF-IDF Vectorization, Cosine Similarity matrix, difflib fuzzy query ranking)
7. **Education:** Bachelor of Computer Science (BCS) — Willingdon College, Sangli (Shivaji University, Kolhapur) — Expected 2027.
8. **Contact:** Interactive form, one-click copy buttons for email (`surajghadage1206@gmail.com`) and phone (`+91 9456160255`), social links, and resume download.
9. **Footer:** Quick links, social icons, copyright notice, and smooth Back-to-Top trigger.

---

## 🚀 How to Run Locally

### Option 1: Direct File
Simply double-click `index.html` in your file explorer to open it in Chrome, Edge, Safari, or Firefox.

### Option 2: Python HTTP Server
```bash
python -m http.server 8000
```
Then navigate to `http://localhost:8000` in your web browser.

### Option 3: VS Code Live Server
Right click `index.html` and select **"Open with Live Server"**.

---

## 🌐 Deployment to GitHub Pages

1. Initialize git (if not already done):
   ```bash
   git init
   git add .
   git commit -m "feat: complete portfolio website build for Suraj Ghadage"
   ```
2. Push to GitHub:
   ```bash
   git remote add origin https://github.com/<username>/portfolio-website.git
   git branch -M main
   git push -u origin main
   ```
3. Enable GitHub Pages:
   - Go to **Settings > Pages** on your GitHub repository.
   - Set Source to `Deploy from a branch` -> `main` / `root` -> **Save**.
   - Your live website will be published in seconds!

---

## 📄 License & Ownership
© 2026 Suraj Dattatray Ghadage. All rights reserved.
