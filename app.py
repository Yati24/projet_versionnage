from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cle_secrete_projet_vacances'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vacances.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# --- db ---
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('albums', lazy=True))

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)
    album = db.relationship('Album', backref=db.backref('photos', lazy=True))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- routes ---

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(username=request.form.get('username'), password=request.form.get('password'))
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    albums = Album.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', albums=albums)

@app.route('/create_album', methods=['POST'])
@login_required
def create_album():
    name = request.form.get('name')
    if name:
        db.session.add(Album(name=name, user_id=current_user.id))
        db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/delete_album/<int:id>')
@login_required
def delete_album(id):
    album = Album.query.get(id)
    if album.user_id == current_user.id:
        db.session.delete(album)
        db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form.get('username')).first()
        if user and user.password == request.form.get('password'):
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/album/<int:id>', methods=['GET', 'POST'])
@login_required
def view_album(id):
    album = Album.query.get_or_404(id)
    if request.method == 'POST':
        f = request.files['photo']
        if f:
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            db.session.add(Photo(filename=filename, album_id=album.id))
            db.session.commit()
    return render_template('album.html', album=album)

@app.route('/delete_photo/<int:id>')
@login_required
def delete_photo(id):
    photo = Photo.query.get(id)
    if photo.album.user_id == current_user.id:
        db.session.delete(photo)
        db.session.commit()
        return redirect(url_for('view_album', id=photo.album_id))
    return "Interdit"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)