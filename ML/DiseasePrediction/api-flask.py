from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np

app = Flask(__name__)


def preprocess(json_data):
    
    data = json_data['queryResult']['outputContexts'][1]['parameters']
    new_data = {}
    features_names = ["ulcers_on_tongue", "spotting_urination", "anxiety", "cold_hands_and_feets",
        "patches_in_throat" ,"irregular_sugar_level" ,"sunken_eyes" ,"dehydration",
        "pain_behind_the_eyes", "yellow_urine" ,"acute_liver_failure",
        "fluid_overload" ,"runny_nose" ,"weakness_in_limbs" ,"pain_in_anal_region",
        "swollen_blood_vessels" ,"extra_marital_contacts" ,"knee_pain",
        "movement_stiffness" ,"spinning_movements" ,"weakness_of_one_body_side",
        "foul_smell_ofurine" ,"passage_of_gases", "belly_pain",
        "dischromic_patches", "watering_from_eyes" ,"mucoid_sputum" ,"rusty_sputum",
        "lack_of_concentration" ,"visual_disturbances",
        "history_of_alcohol_consumption" ,"blood_in_sputum" ,"pus_filled_pimples",
        "silver_like_dusting" ,"blister"]
        #get specific feature names/parameters
    for key, value in data.items():
        if key in features_names:
            new_data[key] = value
    #print(new_data)    

    ordered_data = {k: new_data[k] for k in features_names}
    ordered_data_values = list(ordered_data.values())
    mapping = {"yes":1 , "no":0}
    mapped_values = [mapping[x] for x in ordered_data_values] 
    form_info_dict = dict(zip(features_names, mapped_values))
    return form_info_dict


@app.route('/predict', methods=['POST']) # Your API endpoint URL would consist /predict
def predict():
    if mnb:
        try:
            data = request.get_json()
            #print(data)
            preprocess_data = preprocess(data)
            query = pd.get_dummies(pd.DataFrame(preprocess_data, index=[0]))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(mnb.predict(query))
            prediction = str(prediction)
            #return jsonify({'prediction': prediction})
            return jsonify({ "fulfillmentMessages": [{"text": {"text": [prediction]}}]})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')


if __name__ == '__main__':
    
    port = 80 # If you don't provide any port then the port will be set to 12345
    mnb = joblib.load('final_model.pkl') # Load "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load('model_columns.pkl') # Load "model_columns.pkl"
    print ('Model columns loaded')
    app.run(port=port, debug=True,ssl_context='adhoc')


