import webbrowser
from fpdf import FPDF
from flat import Bill, FlatMate
import os


class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates such as thier names.their due amount and the peroid of the bill
    """

    def __init__(self, filename) -> None:
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
        my_pdf = FPDF(orientation='P', unit='pt',
                      format='A4')  # defoult parameters
        my_pdf.add_page()  # creates a page in the pdf

        # add icon
        my_pdf.image("files/house.png", w=30, h=30)
        # add some text
        my_pdf.set_font(family='Times', size=24, style='B')
        my_pdf.cell(w=530, h=60, txt="Flatemates Bill",
                    border=1, align='C', ln=1)

        # Insert period lavel and value
        my_pdf.cell(w=80, h=40, txt="Period", border=0)
        my_pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)
        my_pdf.set_font(family='Times', size=18)
        # Insert name and due amount if the first flatmate
        my_pdf.cell(w=80, h=40, txt=flatmate1.name, border=0)
        my_pdf.cell(w=150, h=40, txt=flatmate1_pay, border=0, ln=1)
        # Insert name and due amount if the second  flatmate
        my_pdf.cell(w=80, h=40, txt=flatmate2.name, border=0)
        my_pdf.cell(w=150, h=40, txt=flatmate2_pay, border=0, ln=1)

        os.chdir("files")

        my_pdf.output(self.filename)

        webbrowser.open(self.filename)
