#!/usr/bin/env python
from app import create_app, db
from app.models import User

if __name__ == '__main__':
    app = create_app('development')
    # Flask suporta multiples aplicacions a la vegada
    # el block with indica a quina aplicacio s'ha de referir cada
    # instancia (per exemple db).
    with app.app_context():
        db.create_all()
        if User.query.filter_by(username='john').first() is None:
            User.register('john', 'cat')
    app.run()
