import flask
import pickle
import pandas as pd
import xgboost as xgb
import os
# Use pickle to load in the pre-trained model
with open(f'./deploy/model_4.pkl', 'rb') as f:
    model = pickle.load(f)
with open(f'./deploy/mean_var_4.pkl', 'rb') as f:
    mean_var = pickle.load(f)
if not os.path.exists("./deploy/count.pkl"):
    visitor_count=0
    with open(f"./deploy/count.pkl","wb") as f:
        pickle.dump(visitor_count, f)

with open(f"./deploy/count.pkl","rb") as f:
    visitor_count=pickle.load(f)
# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    global visitor_count
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html', visitor_count=visitor_count))
    
    if flask.request.method == 'POST':
        # Extract the input
        L = (float(flask.request.form['L'])-mean_var[0][0])/(mean_var[0][1])
        LDH = (float(flask.request.form['LDH'])-mean_var[1][0])/(mean_var[1][1])
        CRP = (float(flask.request.form['CRP'])-mean_var[2][0])/(mean_var[2][1])
        N = (float(flask.request.form['N'])-mean_var[3][0])/(mean_var[3][1])

        # Make DataFrame for model
        input_variables = pd.DataFrame([[L,LDH, CRP,N]],
                                       columns=['Laboratory_test_L','Laboratory_test_LDH_(U/L)' , 'Laboratory_test_CRP_(mg/L)',"Laboratory_test_N"],
                                       dtype=float,
                                       index=['input'])

        # Get the model's prediction
        prediction = model.predict_proba(input_variables)[0][1]
        # print(model.predict_proba(input_variables))
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        visitor_count+=1
        with open(f"./count.pkl", "wb") as f:
            pickle.dump(visitor_count, f)
        return flask.render_template('main.html',
                                     original_input={
                                                    'L':flask.request.form['L'],
                                                     'LDH':flask.request.form['LDH'],
                                                     'CRP':flask.request.form['CRP'],
                                                     'N':flask.request.form['N']
                                                     },
                                     result=prediction,
                                     visitor_count=visitor_count
                                     )

if __name__ == '__main__':
    app.run()