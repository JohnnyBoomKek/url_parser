import django_tables2 as tables


class LinkTable(tables.Table):
    url = tables.Column()
    domain = tables.Column()
    create_date = tables.Column()
    update_date = tables.Column()
    country = tables.Column()
    idDead = tables.Column()

class UrlTable(tables.Table):
    url = tables.Column()

