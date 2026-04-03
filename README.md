# Pirate's Treasure Compass

## 💻 Overview
A sophisticated navigation and route-planning ecosystem designed for maritime exploration. Built with **Django 5.2**, this application allows users to orchestrate complex treasure hunts by linking nautical instructions into a recursive chain. Beyond simple data entry, the system features a **recursive route engine** that calculates cumulative distance and risk factors from any point in the journey.

---

## 🤍 Tech Stack
* **Backend:** Python 3.10+, **Django 5.2** (MVT Architecture)
* **Frontend:** HTML5, **Bootstrap 5**, Custom CSS3 with purple gradients
* **Database:** Relational modeling with **OneToOne recursive relationships**
* **Styling:** Custom glassmorphism effects and UI components

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

© 2025 Glitter Geeks Coderun | Developed by [**𝐋𝐞𝐨𝐧𝐭𝐞 𝐏𝐚𝐭𝐫𝐢𝐜𝐢𝐚-𝐌𝐢𝐫𝐚𝐛𝐞𝐥𝐚**](https://github.com/patrrrrrrricia) 
