import csv

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

expenses = []
incomes = []

# Load expenses and incomes from CSV files
with open('expenses.csv', 'r') as f:
    reader = csv.DictReader(f)
    expenses = [row for row in reader]

with open('incomes.csv', 'r') as f:
    reader = csv.DictReader(f)
    incomes = [row for row in reader]







@app.route('/')
def index():
    return render_template('index.html')


@app.get('/incomesexpenses')
def get_income_and_expenses():
    global expenses
    global incomes
    with open('expenses.csv', 'r') as f:
        reader = csv.DictReader(f)
        expenses = []
        for row in reader:
            print(row)
            expenses.append({"name" : row["name"], "date" : row["date"], "amount" : row["amount"]})


    with open('incomes.csv', 'r') as f:
        reader = csv.DictReader(f)
        incomes = []
        for row in reader:
            incomes.append({"name" : row["name"], "date" : row["date"], "amount" : row["amount"]})

    return {"income": incomes,"expense" :  expenses}


@app.post("/incomes")
def add_income():

    print("add income called")
    try :
    
        name = request.form.get('name')
        date = request.form.get('date')
        amount = request.form.get('amount')
        income_array = [name, date, amount ]
        with open('incomes.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(income_array)
            csvfile.close()

    except:
        return "error occured"
     
    return "Successfully added expense"




@app.post("/expenses")
def add_expense():
    print("add expense called")
    try : 
        name = request.form.get('name')
        date = request.form.get('date')
        amount = request.form.get('amount')
        expense_array = [name, date, amount ]

        print(expense_array)

        with open('expenses.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(expense_array)
            csvfile.close()
    except:
        return "Some Error occurred"

    return "Expenses added successfully"



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)