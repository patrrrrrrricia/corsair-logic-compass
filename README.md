# Pirate's Treasure Compass

## 💻 Overview
A sophisticated navigation and route-planning ecosystem designed for maritime exploration. Built with **Django 5.2**, this application allows users to orchestrate complex treasure hunts by linking nautical instructions into a recursive chain. Beyond simple data entry, the system features a **recursive route engine** that calculates cumulative distance and risk factors from any point in the journey.

---

## 🤍 Tech Stack
* **Backend:** Python 3.10+, **Django 5.2** (MVT Architecture)
* **Frontend:** HTML5, **Bootstrap 5**, Custom CSS3 with purple gradients
* **Database:** Relational modeling with **OneToOne recursive relationships**
* **Styling:** Custom glassmorphism effects and UI components

![Python](https://img.shields.io/badge/python-3.10+-%23FF69B4.svg?style=for-the-badge&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/django-5.2-%23FFB6C1.svg?style=for-the-badge&logo=django&logoColor=black)

![HTML5](https://img.shields.io/badge/HTML5-%234F4F4F.svg?style=for-the-badge&logo=html5&logoColor=white) ![Bootstrap 5](https://img.shields.io/badge/Bootstrap_5-%234F4F4F.svg?style=for-the-badge&logo=bootstrap&logoColor=white) ![CSS3](https://img.shields.io/badge/Custom_CSS3-%234F4F4F.svg?style=for-the-badge&logo=css3&logoColor=white)

![Relational Modeling](https://img.shields.io/badge/Relational_Modeling-%23333333.svg?style=for-the-badge&logo=diagrams.net&logoColor=white) ![Glassmorphism](https://img.shields.io/badge/Glassmorphism_UI-%23333333.svg?style=for-the-badge&logo=glassdoor&logoColor=white)

---

## 🎀 Core Functionality
* **Recursive Route Linking:** Every instruction can be connected to its predecessor using a `OneToOneField`, creating a unique, traceable path back to the starting point.
* **Smart Route Analytics:** * **Cumulative Distance:** Automatically calculates the total nautical miles from the start to the current instruction.
    * **Risk Assessment:** Computes the average risk level (`0-100`) and provides safety warnings based on the route's difficulty.
* **Direction Visualization:** Dynamic SVG rendering based on nautical directions (North, South-East, etc.).
* **Advanced Theming:** A bespoke UI featuring deep purple gradients (`#5e1c9c` to `#d0aeec`) and polished Bootstrap components.

---

## 📂 Project Structure
The application follows a clean, layered Django structure:
* **`models.py`**: Defines the `Instruction` entity with recursive linking and direction choices.
* **`views.py`**: Contains the logic for route backtracking and statistical summaries.
* **`style.css`**: Custom styles for the "Pirate" aesthetic, including card gradients and hover effects.
* **`templates/`**: Responsive Django templates for index and detail views.

---

## Getting Started

Follow these instructions to set up the environment and launch the Pirate's Compass locally:

```bash
# Clone the repository
git clone [https://github.com/patrrrrrrricia/corsair-logic-compass.git](https://github.com/patrrrrrrricia/corsair-logic-compass.git)
cd corsair-logic-compass

# Create and activate a virtual environment
python -m venv venv

# Activate the environment
# On Windows: venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate

#Install the Django framework using the Python package manager:
pip install django

#Apply migrations to create the database structure
python manage.py migrate

#Start the local development engine
python manage.py runserver

The application will be available at: https://www.google.com/search?q=http://127.0.0.1:8000

```

© 2025 Glitter Geeks Coderun | Developed by [**𝐅𝐥𝐨𝐫𝐞𝐚𝐧 𝐄𝐦𝐢𝐥𝐢𝐚-𝐀𝐥𝐞𝐱𝐚𝐧𝐝𝐫𝐚**](https://github.com/Emily-f2510), [**𝐋𝐞𝐨𝐧𝐭𝐞 𝐏𝐚𝐭𝐫𝐢𝐜𝐢𝐚-𝐌𝐢𝐫𝐚𝐛𝐞𝐥𝐚**](https://github.com/patrrrrrrricia), [**𝐋𝐮𝐩𝐚𝐧𝐜𝐮 𝐆𝐚𝐛𝐫𝐢𝐞𝐥𝐚-𝐕𝐚𝐥𝐞𝐧𝐭𝐢𝐧𝐚**](https://github.com/gabrielalupancu)




