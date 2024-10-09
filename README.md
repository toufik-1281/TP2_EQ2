# TP2_EQ2 Exercice 1
import sys

import sqlite3

from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QTableView, QLineEdit, QHBoxLayout,

                             QFormLayout)

from PyQt6.QtSql import QSqlDatabase, QSqlTableModel

from PyQt6.QtCore import Qt


class CarnetAdresse(QWidget):

    def 
__init__
(
self
):

        super().
__init__
()

        
self
.setWindowTitle(
'Carnet d
\'
Adresses'
)

        
self
.resize(800, 600)

        # Layout principal

        
self
.layout = QVBoxLayout()

        # Bouton d'initialisation de la base de données

        
self
.init_button = QPushButton(
'Initialiser la base de données'
)

        
self
.init_button.clicked.connect(
self
.init_db)

        
self
.layout.addWidget(
self
.init_button)

        # TableView pour afficher les contacts

        
self
.table_view = QTableView()

        
self
.layout.addWidget(
self
.table_view)

        # Formulaire d'ajout de contact

        
self
.form_layout = QFormLayout()

        
self
.nom_input = QLineEdit()

        
self
.professionnel_input = QLineEdit()

        
self
.portable_input = QLineEdit()

        
self
.personnel_input = QLineEdit()

        
self
.email_input = QLineEdit()

        
self
.form_layout.addRow(
"Nom"
, 
self
.nom_input)

        
self
.form_layout.addRow(
"Professionnel"
, 
self
.professionnel_input)

        
self
.form_layout.addRow(
"Portable"
, 
self
.portable_input)

        
self
.form_layout.addRow(
"Personnel"
, 
self
.personnel_input)

        
self
.form_layout.addRow(
"E-mail"
, 
self
.email_input)

        # Ajouter les boutons pour gérer les contacts

        
self
.button_layout = QHBoxLayout()

        
self
.add_button = QPushButton(
'Ajouter'
)

        
self
.update_button = QPushButton(
'Modifier'
)

        
self
.delete_button = QPushButton(
'Supprimer'
)

        
self
.add_button.clicked.connect(
self
.add_contact)

        
self
.update_button.clicked.connect(
self
.update_contact)

        
self
.delete_button.clicked.connect(
self
.delete_contact)

        
self
.button_layout.addWidget(
self
.add_button)

        
self
.button_layout.addWidget(
self
.update_button)

        
self
.button_layout.addWidget(
self
.delete_button)

        
self
.layout.addLayout(
self
.form_layout)

        
self
.layout.addLayout(
self
.button_layout)

        # Configurer la base de données et le modèle

        
self
.db = None

        
self
.model = None

        
self
.setLayout(
self
.layout)

    def init_db(
self
):

        
self
.db = QSqlDatabase.addDatabase(
'QSQLITE'
)

        
self
.db.setDatabaseName(
'carnet_adresse.db'
)

        if not 
self
.db.open():

            print(
"Erreur : Impossible d'ouvrir la base de données."
)

            return

        query = QSqlDatabase.exec_(
"""CREATE TABLE IF NOT EXISTS contacts (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nom TEXT NOT NULL,

            professionnel TEXT,

            portable TEXT,

            personnel TEXT,

            email TEXT)"""
)

        if query.isActive():

            print(
"Base de données initialisée avec succès !"
)

        
self
.load_data()

    def load_data(
self
):

        
self
.model = QSqlTableModel(
self
, 
self
.db)

        
self
.model.setTable(
'contacts'
)

        
self
.model.select()

        
self
.table_view.setModel(
self
.model)

    def add_contact(
self
):

        query = QSqlDatabase.exec_(
f"""INSERT INTO contacts (nom, professionnel, portable, personnel, email) VALUES (

            '
{
self
.nom_input.text()}
',

            '
{
self
.professionnel_input.text()}
',

            '
{
self
.portable_input.text()}
',

            '
{
self
.personnel_input.text()}
',

            '
{
self
.email_input.text()}
'

        )"""
)

        if query.isActive():

            
self
.model.select()  # Refresh the model to show the new data

    def update_contact(
self
):

        # Logique pour modifier un contact sélectionné

        pass

    def delete_contact(
self
):

        # Logique pour supprimer un contact sélectionné

        pass


if __name__ == 
'__main__'
:

    app = QApplication(sys.argv)

    window = CarnetAdresse()

    window.show()

    sys.exit(app.exec())
