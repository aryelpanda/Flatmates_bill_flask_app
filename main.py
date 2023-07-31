from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat
from waitress import serve
app = Flask(__name__)  # initiate the flask app class, central object
# app.config['DEBUG'] = True

# each page recives its own class


class HomePage(MethodView):

    def get(self):
        # adding html to style the page,flask recognizes the "templates" folder and uses the index
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        # we pass the variable so html recognizes it
        return render_template('bill_form_page.html', billform=bill_form)


class ResultsPage(MethodView):
    def post(self):  # post is needed to post the data

        billform = BillForm(request.form)
        # conect the amoutn widget to this variavle
        # we use the "billform" to get the data from the widgets
        the_bill = flat.Bill(float(billform.amount.data),
                             billform.period.data)  # create the bill
        flatmate1 = flat.FlatMate(
            billform.name1.data, float(billform.days_in_house1.data))
        flatmate2 = flat.FlatMate(
            billform.name2.data, float(billform.days_in_house2.data))

        rounded_amount1 = round(flatmate1.pays(the_bill, flatmate2), 2)
        rounded_amount2 = round(flatmate2.pays(the_bill, flatmate1), 2)
        # in the return statment we tell flask witch html page we would like to show, and we send the variavles we want to display also.
        return render_template('results.html', name1=flatmate1.name, amount1=rounded_amount1, name2=flatmate2.name, amount2=rounded_amount2)


class BillForm(Form):
    # create input box recivess the amount
    amount = StringField("Bill amount: ", default=4000)
    period = StringField("Bill period: ", default="October")

    name1 = StringField("First flatmate: ", default="Ariel")
    days_in_house1 = StringField("Days in the house: ", default=30)

    name2 = StringField("Second flatmate", default="Shiran")
    days_in_house2 = StringField("Days in the house: ", default=45)

    button = SubmitField("Calculate")


if __name__ == "__main__":
    # How the urls are going to look of every page
    app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
    app.add_url_rule('/bill', view_func=BillFormPage.as_view
                     ('bill_form_page'))
    app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))
    serve(app, host='localhost', port=8080)
    app.run()
