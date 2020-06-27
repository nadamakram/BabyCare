## prdict disease happy path
*greet 
  - utter_greet

*imply_disease{"disease":"allergy", "symptom":"sneezing"}
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}

*thank
  - utter_goodbye




## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
