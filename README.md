# Foodlabs

This is a simple application

## Explaining the relationship implementation into Django models

### Relationship 1:1
=> Pode ser configurado em qualquer view, desde que seja declarado o nome `models.OneToOneField()` **em apenas uma view**

### Relationship 1:N
=> **Só pode ser configurado na view responsável pelo N na relação**, onde é utilizado o nome `models.foreignKey()` adereçando a sua respectiva view na variável "related_name"
- Example: `table1 = ManyToManyField("tabela2.nomeclasse", on_delete=models.CASCADE,  related_name="ingredients")`

### Relationship N:N
=> Pode ser configurado de ambos os lados, mas **em apenas uma view** utilizando o comando `models.ManyToManyField()`.



## Main commands to manage API:
### Commands to execute API:
Create the python virtual environment (the second `venv` can be which name you want, altough the convention is to name as `venv` as well).

```bash
python -m venv venv
```
#### Activate python virtual environment
```bash
venv/Scripts/Activate
```
#### Install the requirements for the application
```bash
pip install -r requirements.txt
```
#### Execute the command to run the server
```bash
python manage.py runserver
```
#### After change the database migrations
```bash
python manage.py makemigrations
```
#### Commit the migrations into the database

```bash
python manage.py migrate
```
#### clean the local database, if necessary:

```bash
python manage.py flush
```
