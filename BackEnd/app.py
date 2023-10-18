from flask import Flask, render_template, request, jsonify, flash
import random, data_analysis, ml_model
app = Flask(__name__)