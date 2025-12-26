# 🚀 Advanced Modular Scraper

A professional, modular Python web scraper designed for clean and efficient data extraction. This project focuses on maintainability and ease of use for developers and data enthusiasts.

---

## 🛠️ Features

- **Modular Architecture**: Clean separation between the scraping engine and the main execution flow.
- **Interactive CLI**: Dynamic user input for custom URLs directly from the terminal.
- **Data Persistence**: Automatically exports extracted data into structured **JSON** files for further analysis.
- **Error Handling**: Basic protection against common connection issues and timeouts.

---

## 📦 Project Structure

- `main.py`: The entry point that handles user interaction and the main loop.
- `src/scraper_logic.py`: The core engine containing the BeautifulSoup logic and data parsing functions.
- `requirements.txt`: Contains all necessary Python dependencies (Requests, BeautifulSoup4).

---

## 🚀 Getting Started

### 1. Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/1joepie1/advanced-web-scraper.git
cd advanced-web-scraper
```

2. Environment Setup (Optional but Recommended)
Create a virtual environment to keep your dependencies organized:

```python -m venv venv```

# On Windows:
```venv\Scripts\activate```

# On macOS/Linux:
```source venv/bin/activate```

3. Install Dependencies
Install the required Python libraries using pip:
```pip install -r requirements.txt```
5. Usage
Launch the scraper and follow the on-screen prompts to start extracting data:

```python main.py```



🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project
Create your Feature Branch (```git checkout -b feature/AmazingFeature```)
Commit your Changes (```git commit -m 'Add some AmazingFeature'```)
Push to the Branch (```git push origin feature/AmazingFeature```)
Open a Pull Request


⚖️ License
Distributed under the MIT License. This means you are free to use, modify, and distribute the software for any purpose.
