from flask import Flask, request, render_template, redirect, url_for, jsonify, abort

import forms
from forms import CarsForm
from sql_service import SqlService


app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"
service = SqlService("sqlite.db")

@app.route("/api/v1/sql_service/", methods=["GET"])
def create_cars():
    service.main()
    car_list = service.select_all()
    print(car_list)

    return jsonify({'cars': car_list}),

@app.route('/')
def homepage():
    service.main()
    car_list = service.select_all()
    car_model = forms.CarsForm()
    return render_template("cars_homepage.html", cars=car_list, car_model=car_model)


@app.route('/cars/', methods=["GET", "POST"])
def car_list():
    if request.method == "POST":
        service.add_car(request.form['marka'], request.form['model'], request.form['rocznik'],
                        request.form['kolor'], request.form['moc'], False)

    car_list = service.select_all()
    car_model = forms.CarsForm()
    return render_template("cars_homepage.html", cars=car_list, car_model=car_model)

@app.route("/cars/<int:car_id>", methods=["GET"])
def get_car(car_id):
    car = service.get_car(car_id)
    car_model={"id": car[0], "marka": car[1], "model": car[2], "rocznik": car[3], "kolor": car[4], "moc": car[5],
     "czy_bezwypadkowy": False}
    form = CarsForm(data=car_model)
    if not car:
        abort(404)
    print(form.id)
    return render_template("cars_id.html", form=form, car_id = car_id)

@app.route("/update_car/<int:id>", methods=["POST"])
def update_car(id):
    service.update_car(id, request.form['marka'], request.form['model'], request.form['rocznik'],
                    request.form['kolor'], request.form['moc'], False)
    return redirect('/');

@app.route("/delete_car/<int:id>", methods=["POST"])
def delete_car(id):
    service.delete_car(id)
    return redirect('/');


if __name__ == "__main__":
    app.run(debug=True)

