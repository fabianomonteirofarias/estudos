from tkinter import *
from tkinter import tix, ttk, messagebox
from tkcalendar import Calendar, DateEntry

from aula031.controllers.Funcs import Funcs
from aula031.controllers.Relatorios import Relatorios
from aula031.controllers.Validadores import Validadores
from aula031.view.GradientFrame import GradientFrame
from controllers.PlaceHolder import EntryPlaceHold

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image

import sqlite3
