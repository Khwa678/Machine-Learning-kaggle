from flask import Flask, render_template, request, redirect

app = Flask(__name__)
expenses = []

@app.route('/')
def home():
    return render_template("index.html", expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    date = request.form['date']
    category = request.form['category']
    description = request.form['description']
    amount = float(request.form['amount'])

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_expense(index):
    if 0 <= index < len(expenses):
        expenses.pop(index)
    return redirect('/')

# TOTAL EXPENSE PAGE
@app.route('/total')
def total_expense():
    total = sum(e["amount"] for e in expenses)
    return render_template("total.html", total=total)

if __name__ == "__main__":
    app.run(debug=True)
