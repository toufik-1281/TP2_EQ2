import sqlite3

def init_db():
    conn = sqlite3.connect('gestion_projets.db')
    cursor = conn.cursor()

    # Créer la table pour les projets
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS projets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        description TEXT,
        date_debut TEXT,
        date_fin TEXT,
        statut TEXT
    )''')

    # Créer la table pour les tâches
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS taches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_projet INTEGER,
        nom_tache TEXT NOT NULL,
        description_tache TEXT,
        date_echeance TEXT,
        priorite INTEGER,
        statut TEXT,
        FOREIGN KEY(id_projet) REFERENCES projets(id)
    )''')

    conn.commit()
    conn.close()

# Initialisation de la base de données
init_db()

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem

class GestionProjet(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion de Projets")
        self.setGeometry(200, 100, 800, 600)

        # Layout principal
        layout = QVBoxLayout()

        # Tableau pour afficher les projets
        self.project_table = QTableWidget()
        self.project_table.setColumnCount(4)
        self.project_table.setHorizontalHeaderLabels(["Nom", "Description", "Date Début", "Statut"])
        layout.addWidget(self.project_table)

        # Bouton pour ajouter un projet
        add_project_btn = QPushButton("Ajouter Projet")
        add_project_btn.clicked.connect(self.add_project)
        layout.addWidget(add_project_btn)

        self.setLayout(layout)
        self.load_projects()

    def load_projects(self):
        # Charger les projets depuis la base de données
        conn = sqlite3.connect('gestion_projets.db')
        cursor = conn.cursor()

        cursor.execute("SELECT nom, description, date_debut, statut FROM projets")
        projects = cursor.fetchall()

        self.project_table.setRowCount(0)  # Réinitialiser les lignes

        for row_num, project in enumerate(projects):
            self.project_table.insertRow(row_num)
            for col_num, data in enumerate(project):
                self.project_table.setItem(row_num, col_num, QTableWidgetItem(str(data)))

        conn.close()

    def add_project(self):
        # Fonction pour ajouter un projet (à compléter)
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GestionProjet()
    window.show()
    sys.exit(app.exec())
