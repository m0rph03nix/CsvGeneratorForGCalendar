# Génère un calendrier CSV pour google, à partir des planning de 5A de CPE Lyon		

:warning: Certaines parties sont un peu sales... ce script est un outil pour faire de l'administratif plus vite, pas une vitrine de développement !

## Comment l'utiliser ?
- Dans GCalendarCpeGenerator.py, modifier la portion suivante:
```python
    def __init__(self):
        wb = load_workbook(filename='Planning_ROS_1920_v1h.xlsx') # file to open
        self.ws = wb.active

        # Date cell of the first day
        self.start_cell = 'B4'

        # End cell of the last event
        self.end_cell = 'AB21'

        # Legend of the events to consider
        self.legend_range = self.ws['AI4':'AI12']

        # Columns to skip
        self.skip = ['T', 'U']

```
- Si vous n'avez pas openpyxl, installez le (avec pip3)
- Lancez GCalendarCpeGenerator.py avec python 3.7 
- Vérifiez que le fichier PlanningCPE.csv a bien été généré
- Créez un nouvel agenda sous google calendar
- Importez y le fichier PlanningCPE.csv 


## Formalisme du fichier excel
- Le premier mot de l'évènement doit correspondre au premier mot d'un des modules en légende
- Le regex '//' permet de séparer 2 évènements sur la même tranche horaire
- Si 2 créneaux avec le même texte se suivent dans une même demi-journée ils seront fusionnées (ex: 8h-10h et 10h15-12h15 --> 8h-12h15)
- Les cellules fusionnées ne sont pas interprêtées (seul la cellule en haut à gauche contient l'information de la cellule)
- Les couleurs et commentaires ne sont pas pris en compte



