### Relacionamento 1:1
=> Pode ser configurado em qualquer view, desde que seja declarado o nome `models.OneToOneField()` **em apenas uma view**
### Relacionamento 1:N
=> **Só pode ser configurado na view responsável pelo N na relação**, onde é utilizado o nome `models.foreignKey()` adereçando a sua respectiva view na variável "related_name"
- Exemplo: `tabela1 = ManyToManyField("tabela2.nomeclasse", on_delete=models.CASCADE,  related_name="ingredients")`
### Relacionamento N:N
=> Pode ser configurado de ambos os lados, mas **em apenas uma view** utilizando o comando `models.ManyToManyField()`.

-
