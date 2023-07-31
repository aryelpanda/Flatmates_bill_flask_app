# Generates a pdf telling each flat mate how much money he ows in bills .
# This is the flask implementation dor the pdf bill generator
# Every page has its own class
from fpdf import FPDF
import webbrowser
from flat import Bill, FlatMate
from reports import PdfReport


def flatmate_input():

    name = input("Provide a flatmate name: ")
    days_in_house = int(input("How many days he stayed at the house?: "))
    new_flatmate = FlatMate(name, days_in_house)
    return new_flatmate


def bill_input():

    amount = int(input("Please enter the bill amount:"))
    period = input("Please enter the bill period: ")
    new_bill = Bill(amount, period)
    return new_bill


def main():

    flatmate_1 = flatmate_input()
    flatmate_2 = flatmate_input()
    the_bill = bill_input()
    # print(f"Jhon pays: {john.pays(the_bill, flatmate2=marry)}")
    # print(f"Marry pays: {marry.pays(the_bill, flatmate2=john)}")

    pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
    pdf_report.generate(flatmate1=flatmate_1,
                        flatmate2=flatmate_2, bill=the_bill)


if __name__ == "__main__":

    main()
