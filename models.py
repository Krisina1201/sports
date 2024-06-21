from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///sports.db')
Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Sport(Base):
    __tablename__ = 'sports'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Athlete(Base):
    __tablename__ = 'athletes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    weight = Column(Float)
    height = Column(Float)
    country_id = Column(Integer, ForeignKey('countries.id'))
    sport_id = Column(Integer, ForeignKey('sports.id'))
    country = relationship('Country', backref='athletes')
    sport = relationship('Sport', backref='athletes')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# def import_data(file_path):
#     # Импортируем данные из файла
#     with open(file_path, 'r') as file:
#         data = file.readlines()
#     for line in data:
#         name, age, weight, height, country, sport = line.strip().split(',')
#         country_obj = session.query(Country).filter_by(name=country).first()
#         if not country_obj:
#             country_obj = Country(name=country)
#             session.add(country_obj)
#         sport_obj = session.query(Sport).filter_by(name=sport).first()
#         if not sport_obj:
#             sport_obj = Sport(name=sport)
#             session.add(sport_obj)
#         athlete = Athlete(name=name, age=int(age), weight=float(weight), height=float(height), country=country_obj, sport=sport_obj)
#         session.add(athlete)
#     session.commit()

def get_unique_countries():
    return [country for country in session.query(Country.name).distinct().all()]

def get_unique_sports():
    return [sport for sport in session.query(Sport.name).distinct().all()]

def get_athletes_by_country(country_name):
    if isinstance(country_name, tuple):
        country_name = country_name
    country = session.query(Country).filter(Country.name == country_name).first()
    return country.athletes if country else []

def get_athletes_by_sport(sport_name):
    sport = session.query(Sport).filter(Sport.name == sport_name).first()
    return sport.athletes

def get_athletes_by_country_and_sport(country_name, sport_name):
    country = session.query(Country).filter_by(name=country_name).first()
    sport = session.query(Sport).filter_by(name=sport_name).first()
    return session.query(Athlete).filter_by(country=country, sport=sport).all()

def add_athlete(name, age, weight, height, country_name, sport_name):
    country = session.query(Country).filter_by(name=country_name).first()
    sport = session.query(Sport).filter_by(name=sport_name).first()
    athlete = Athlete(name=name, age=int(age), weight=float(weight), height=float(height), country=country, sport=sport)
    session.add(athlete)
    session.commit()

def delete_athlete(id):
    athlete = session.query(Athlete).filter_by(id=id).first()
    if athlete:
        session.delete(athlete)
        session.commit()

def update_athlete(id, name, age, weight, height):
    athlete = session.query(Athlete).filter_by(id=id).first()
    if athlete:
        athlete.name = name
        athlete.age = int(age)
        athlete.weight = float(weight)
        athlete.height = float(height)
        session.commit()

def get_all_athletes():
    return session.query(Athlete).all()

def filter_athletes(countries, sports):
    query = session.query(Athlete)
    if countries:
        query = query.join(Athlete.country).filter(Country.name.in_(countries))
    if sports:
        query = query.join(Athlete.sport).filter(Sport.name.in_(sports))
    return query.all()


def import_data():
    countries = [
        "USA", "Canada", "Mexico", "Brazil", "Argentina", "China", "Japan", "South Korea", "Germany", "France", "UK", "Italy", "Spain", "Australia", "Russia", "India", "South Africa", "Egypt", "Turkey", "Poland"
    ]

    sports = [
        "Ice Hockey", "Basketball", "Football", "Baseball", "Soccer", "Tennis", "Volleyball", "Rugby", "Cricket", "Golf", "Boxing", "Wrestling", "Swimming", "Cycling", "Athletics", "Gymnastics", "Rowing", "Sailing", "Equestrian"
    ]

    athletes = [
        ("John Smith", 25, 80.0, 180.0, "USA", "Ice Hockey"),
        ("Jane Doe", 28, 65.0, 170.0, "Canada", "Basketball"),
        ("Maria Rodriguez", 22, 60.0, 165.0, "Mexico", "Football"),
        ("Pedro Silva", 30, 90.0, 190.0, "Brazil", "Soccer"),
        ("Luis Sanchez", 26, 75.0, 175.0, "Argentina", "Tennis"),
        ("Li Wei", 29, 70.0, 185.0, "China", "Volleyball"),
        ("Yui Nakamura", 24, 58.0, 160.0, "Japan", "Rugby"),
        ("Ji-Hoon Kim", 27, 85.0, 195.0, "South Korea", "Cricket"),
        ("Hans Müller", 31, 95.0, 200.0, "Germany", "Golf"),
        ("Pierre Dupont", 25, 80.0, 180.0, "France", "Boxing"),
        ("Emily Wilson", 26, 60.0, 165.0, "UK", "Wrestling"),
        ("Gianni Bianchi", 28, 75.0, 175.0, "Italy", "Swimming"),
        ("Carlos Garcia", 29, 90.0, 190.0, "Spain", "Cycling"),
        ("Mia Lee", 24, 55.0, 155.0, "Australia", "Athletics"),
        ("Sergei Petrov", 30, 100.0, 205.0, "Russia", "Gymnastics"),
        ("Rahul Patel", 27, 70.0, 170.0, "India", "Rowing"),
        ("Themba Moyo", 25, 85.0, 185.0, "South Africa", "Sailing"),
        ("Amr Ali", 26, 75.0, 175.0, "Egypt", "Equestrian"),
        ("Fatma Yılmaz", 28, 60.0, 165.0, "Turkey", "Ice Hockey"),
        ("Katarzyna Kowalska", 29, 65.0, 170.0, "Poland", "Basketball"),
    ]

    for country in countries:
        country_obj = session.query(Country).filter_by(name=country).first()
        if not country_obj:
            country_obj = Country(name=country)
            session.add(country_obj)

    for sport in sports:
        sport_obj = session.query(Sport).filter_by(name=sport).first()
        if not sport_obj:
            sport_obj = Sport(name=sport)
            session.add(sport_obj)

    for athlete in athletes:
        name, age, weight, height, country_name, sport_name = athlete
        country_obj = session.query(Country).filter_by(name=country_name).first()
        sport_obj = session.query(Sport).filter_by(name=sport_name).first()
        athlete_obj = Athlete(name=name, age=age, weight=weight, height=height, country=country_obj, sport=sport_obj)
        session.add(athlete_obj)

    session.commit()

import_data()
