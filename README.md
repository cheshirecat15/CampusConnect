# CampusConnect  
*A Community-Aware Student Collaboration Engine*

---

## 📌 Problem Statement

As a **2nd-year university student**, I experienced a recurring problem on campus:  
despite being surrounded by many students, it is often difficult to find peers who are **equally ambitious**, **academically aligned**, or **interested in collaborative activities** such as hackathons, group studies, or research projects.

Most connections happen randomly or within limited social circles, which leads to:
- missed collaboration opportunities  
- uneven exposure to motivated peers  
- isolated interest groups  

This project aims to address that gap by **systematically connecting students based on shared academic interests, goals, and activities**, fostering a **healthy, competitive, and collaborative university environment**.

---

## 🎯 Project Objective

**CampusConnect** is a data science–driven system that:
- models student academic profiles,
- discovers natural collaboration communities,
- and recommends meaningful peer connections  
without relying on social networking features.

The focus is on **academic compatibility**, not social popularity.

---

## 🧠 High-Level System Overview

The system works as a pipeline:

Student Profiles  
↓  
Feature Engineering (Vectors)  
↓  
Cosine Similarity  
↓  
Similarity Graph (NetworkX)  
↓  
Community Detection using Louvain  
↓  
Community-Aware Recommendations  


Each stage builds upon the previous one to transform raw student data into structured, explainable recommendations.

---

## ⚙️ How the System Works (High Level)

1. **Student Profiling**  
   Each student is represented using structured attributes such as:
   - academic domains (e.g., AI/ML, Cybersecurity)
   - clubs / chapters
   - goals (research, hackathons, startups, etc.)
   - year of study  

2. **Vector Representation**  
   These attributes are converted into fixed-length numerical vectors using binary and one-hot encoding.

3. **Similarity Measurement**  
   Cosine similarity is computed between normalized student vectors to measure alignment based on direction rather than magnitude.

4. **Graph Construction**  
   Students are modeled as nodes in a graph, where edges represent meaningful similarity scores above a defined threshold.

5. **Community Detection**  
   The Louvain algorithm is applied to discover natural student communities based on graph structure.

6. **Recommendation Engine**  
   For each student:
   - top collaborators are recommended from the same community
   - one optional cross-community “bridge” recommendation is added to encourage interdisciplinary interaction

All recommendations are **explainable**, based on shared domains, clubs, or goals.

---
  
### Example: Student S1

Detected Community:
- AI / ML / Data-focused students

Top Recommendations:
- S5 — shared domains (AI/ML, Data Science), same club (AIS)
- S4 — shared AI/ML interest, hackathon-oriented
- S7 — cross-community bridge with AI + cybersecurity overlap

---

## 🧪 Techniques Used

- **NumPy**  
  Vector operations, normalization, similarity computation

- **Cosine Similarity**  
  To measure alignment between student profiles independent of scale

- **Graph Modeling (NetworkX)**  
  To represent students as nodes and similarities as weighted edges

- **Louvain Community Detection**  
  For unsupervised discovery of student communities

- **Rule-Based Recommendation Logic**  
  Community-aware ranking with similarity-based prioritization

---

## 🤔 Why These Choices Were Made

### Why Cosine Similarity?
- Student profiles vary in size and sparsity
- Cosine similarity focuses on **direction (interests)** rather than **quantity**
- Commonly used in recommendation systems and information retrieval

### Why Graph-Based Modeling?
- Student relationships are inherently relational
- Graphs allow analysis of:
  - community structure
  - connectivity
  - bridge students
- Enables explainable clustering instead of opaque ML models

### Why Louvain for Community Detection?
- Fully unsupervised (no predefined number of communities)
- Works well with weighted graphs
- Optimizes modularity, leading to meaningful, interpretable groups

### Why Not a Social Network?
- Avoids popularity bias
- Reduces noise and social pressure
- Keeps focus on academic collaboration

---

## ⚖️ Ethical & Design Considerations

- No personal data beyond academic interests is used
- No ranking of “better” or “worse” students
- Communities are descriptive, not prescriptive
- Cross-community recommendations help reduce academic silos

---

## 🚧 Limitations

- Uses **synthetic data** (no real student deployment yet)
- Assumes accurate self-reported interests
- Small datasets may lead to unstable communities
- No temporal dynamics (interests assumed static)
- No real-time feedback loop or validation metrics

These limitations are acknowledged and documented as part of the design.

---

## 🔮 Future Work

- Real student onboarding with consent
- Feedback-based recommendation refinement
- Dynamic interest updates over time
- Lightweight API layer (FastAPI)
- Visualization of student communities
- Fairness-aware weighting to prevent silos

---

## 📚 Key Takeaway

This project demonstrates how **data science, graph theory, and unsupervised learning** can be combined to model real-world academic collaboration — turning an abstract social problem into a structured, explainable system.

---

## 👩‍💻 Author

**Rijuta Ghosh**
2nd Year B.Tech Computer Science Student  
