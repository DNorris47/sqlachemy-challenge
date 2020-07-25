mport numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/<start>/<end>

       
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation"""
    # Query all preciptiation
    results = session.query(measurement.date, measurement.prcp).filter(measurement.date >= "2016-08-23").all
    dict1 = list(np.ravel(results1))

    
    # dict1 = {}
    # for temps  in results1:
    #     temps_dict = {}
    #     temps_dict[date] = meausrement.date
    #     temps_dict[tobs] = measurement.tobs
    #     dict1.append(temps_dict)                 

    return jsonify(dict1)
    session.close()


@app.route("/api/v1.0/stations")
def stations():
    
    session = Session(engine)

    results2 = session.query(Station.station, Station.name).all()

    sec_dict = list(np.ravel(results2))
    dict2 = []
    for ttl_stations in results2:
        station_dict["station"] = Station.station
        station_dict["name"] = Station.name
        dict2.append(station_dict)

      
    return jsonify(dict2)  
    session.close()

     @app.route("/api/v1.0/tobs")
def tobs():
    
    session = Session(engine)

    results3 = session.query(measurement.date, measurement.tobs).all()

    temps_dict = list(np.ravel(results3))

    dict3 = []
    for ttl_stations in results3:
        station_dict["station"] = Station.station
        station_dict["name"] = Station.name
        dict3.append(station_dict)

      
    return jsonify(dict3)  
    session.close()
    

    return jsonify(temp_dict)


if __name__ == '__main__':
    app.run(debug=True)
