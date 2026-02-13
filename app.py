from flask import Flask, jsonify, render_template, request, redirect 
from pymavlink import  mavutil
from dronekit import connect, Command, LocationGlobalRelative, VehicleMode
import math
import time

app = Flask(__name__)