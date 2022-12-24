from flask import render_template, request, redirect, flash
from flask import Flask
import os

# import calculate_phi_pn function
from column_capacity_simple import calculate_phi_pn

application = Flask(__name__)
application.secret_key = os.urandom(24)


@application.route("/")
def home():
    return render_template("index.html")

@application.route("/", methods=['POST'])
def enter_information():
    if request.method == 'POST':
        moment_of_inertia = request.form.get('moment_of_inertia')
        section_area = request.form.get('section_area')
        k_l = request.form.get('k_l')
        steel_modulus_of_elasticity = request.form.get('steel_modulus_of_elasticity')
        f_y = request.form.get('steel_yield_stress')
        
        # check whether all inputs are entered
        check_inputs = all([moment_of_inertia, section_area, k_l, steel_modulus_of_elasticity, f_y])

        # check_inputs is true, call for the calculate_phi_pn function
        if check_inputs:
            phi_pn = calculate_phi_pn(float(moment_of_inertia), float(section_area), float(k_l), float(steel_modulus_of_elasticity), float(f_y))
        
            output = "Design Axial Capacity of the Column is: " + str(phi_pn) + " kips"

            # we can use flash to show the output on the same page 
            flash(output)
            return redirect(request.url)
        
        # if input(s) are missing
        else:

            flash('Please fill all of the boxes.')
            return redirect(request.url)

if __name__ == "__main__":
    application.run(debug=True)