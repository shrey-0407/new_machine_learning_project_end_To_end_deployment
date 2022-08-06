from distutils.log import error
import os,sys
import logging
from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():

    try:
        raise Exception("We are testing exception")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("WE ARE TESTING LOGGONG MODULE")
        
    return "CI CD PIPELINE HAS BEEN ESTABLISHED"


if __name__=="__main__":
    app.run(debug=True)