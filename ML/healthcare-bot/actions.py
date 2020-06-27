# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

import json
import requests

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionFormInfo(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_info"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ['ulcers_on_tongue', 'spotting_ urination', 'anxiety', 'cold_hands_and_feets',
        'patches_in_throat' ,'irregular_sugar_level' ,'sunken_eyes' ,'dehydration',
        'pain_behind_the_eyes', 'yellow_urine' ,'acute_liver_failure',
        'fluid_overload' ,'runny_nose' ,'weakness_in_limbs' ,'pain_in_anal_region',
        'swollen_blood_vessels' ,'extra_marital_contacts' ,'knee_pain',
        'movement_stiffness' ,'spinning_movements' ,'weakness_of_one_body_side',
        'foul_smell_of urine' ,'passage_of_gases', 'belly_pain',
        'dischromic _patches', 'watering_from_eyes' ,'mucoid_sputum' ,'rusty_sputum',
        'lack_of_concentration' ,'visual_disturbances',
        'history_of_alcohol_consumption' ,'blood_in_sputum' ,'pus_filled_pimples',
        'silver_like_dusting' ,'blister']


    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:
        

        #dispatcher.utter_message(template="utter_submit")
        ''' get the data and store them''' 
        ulcers_on_tongue_value = tracker.get_slot("ulcers_on_tongue")
        spotting_urination_value = tracker.get_slot("spotting_ urination")
        anxiety_value = tracker.get_slot("anxiety")
        cold_hands_and_feets_value = tracker.get_slot("cold_hands_and_feets")
        patches_in_throat_value = tracker.get_slot("patches_in_throat")
        irregular_sugar_level_value = tracker.get_slot("irregular_sugar_level")
        sunken_eyes_value = tracker.get_slot("sunken_eyes")
        dehydration_value = tracker.get_slot("dehydration")
        pain_behind_the_eyes_value = tracker.get_slot("pain_behind_the_eyes")
        yellow_urine_value = tracker.get_slot("yellow_urine")
        acute_liver_failure_value = tracker.get_slot("acute_liver_failure")
        fluid_overload_value = tracker.get_slot("fluid_overload")
        runny_nose_value = tracker.get_slot("runny_nose")
        weakness_in_limbs_value = tracker.get_slot("weakness_in_limbs")
        pain_in_anal_region_value = tracker.get_slot("pain_in_anal_region")
        swollen_blood_vessels_value = tracker.get_slot("swollen_blood_vessels")
        extra_marital_contacts_value = tracker.get_slot("extra_marital_contacts")
        knee_pain_value = tracker.get_slot("knee_pain")
        movement_stiffness_value = tracker.get_slot("movement_stiffness")
        spinning_movements_value = tracker.get_slot("spinning_movements")
        weakness_of_one_body_side_value = tracker.get_slot("weakness_of_one_body_side")
        foul_smell_ofurine_value = tracker.get_slot("foul_smell_of urine")
        passage_of_gases_value = tracker.get_slot("passage_of_gases")
        belly_pain_value = tracker.get_slot("belly_pain")
        dischromic_patches_value = tracker.get_slot("dischromic _patches")
        watering_from_eyes_value = tracker.get_slot("watering_from_eyes")
        mucoid_sputum_value = tracker.get_slot("mucoid_sputum")
        rusty_sputum_value = tracker.get_slot("rusty_sputum")
        lack_of_concentration_value = tracker.get_slot("lack_of_concentration")
        visual_disturbances_value = tracker.get_slot("visual_disturbances")
        history_of_alcohol_consumption_value = tracker.get_slot("history_of_alcohol_consumption")
        blood_in_sputum_value = tracker.get_slot("blood_in_sputum")
        pus_filled_pimples_value = tracker.get_slot("pus_filled_pimples")
        silver_like_dusting_value = tracker.get_slot("silver_like_dusting")
        blister_value = tracker.get_slot("blister")
    

        form_info_values = [ulcers_on_tongue_value, spotting_urination_value, anxiety_value, cold_hands_and_feets_value,
        patches_in_throat_value ,irregular_sugar_level_value ,sunken_eyes_value ,dehydration_value,
        pain_behind_the_eyes_value, yellow_urine_value ,acute_liver_failure_value,
        fluid_overload_value ,runny_nose_value ,weakness_in_limbs_value ,pain_in_anal_region_value,
        swollen_blood_vessels_value ,extra_marital_contacts_value ,knee_pain_value,
        movement_stiffness_value ,spinning_movements_value ,weakness_of_one_body_side_value,
        foul_smell_ofurine_value ,passage_of_gases_value, belly_pain_value,
        dischromic_patches_value, watering_from_eyes_value ,mucoid_sputum_value ,rusty_sputum_value,
        lack_of_concentration_value , visual_disturbances_value ,
        history_of_alcohol_consumption_value , blood_in_sputum_value , pus_filled_pimples_value ,
        silver_like_dusting_value , blister_value]

        mapping = {True:1 , False:0}
        mapped_values = [mapping[x] for x in form_info_values] 

        form_info_keys = ['ulcers_on_tongue', 'spotting_ urination', 'anxiety', 'cold_hands_and_feets',
        'patches_in_throat' ,'irregular_sugar_level' ,'sunken_eyes' ,'dehydration',
        'pain_behind_the_eyes', 'yellow_urine' ,'acute_liver_failure',
        'fluid_overload' ,'runny_nose' ,'weakness_in_limbs' ,'pain_in_anal_region',
        'swollen_blood_vessels' ,'extra_marital_contacts' ,'knee_pain',
        'movement_stiffness' ,'spinning_movements' ,'weakness_of_one_body_side',
        'foul_smell_of urine' ,'passage_of_gases', 'belly_pain',
        'dischromic _patches', 'watering_from_eyes' ,'mucoid_sputum' ,'rusty_sputum',
        'lack_of_concentration' ,'visual_disturbances',
        'history_of_alcohol_consumption' ,'blood_in_sputum' ,'pus_filled_pimples',
        'silver_like_dusting' ,'blister']

        #payload
        form_info_dict = dict(zip(form_info_keys, mapped_values))
        #form_info = json.dumps(form_info_dict)
        r = requests.post("http://127.0.0.1:12345/predict", json=form_info_dict)
        content = r.text
        con_dict = json.loads(content)
        conStr = str(con_dict['prediction'])
        dispatcher.utter_message("You most probably have", conStr)
        return []    

    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "ulcers_on_tongue": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)]
            ,
            "spotting_ urination": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],

            "anxiety": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],

            "cold_hands_and_feets": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],

            "patches_in_throat": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "irregular_sugar_level": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "sunken_eyes": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "dehydration": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "pain_behind_the_eyes": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "yellow_urine": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "acute_liver_failure": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "fluid_overload": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "runny_nose": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "weakness_in_limbs": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "pain_in_anal_region": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "swollen_blood_vessels": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "extra_marital_contacts": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "knee_pain": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "movement_stiffness": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "spinning_movements": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            "spotting_ urination": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "weakness_of_one_body_side": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],
            
            "foul_smell_of urine": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],

            "passage_of_gases": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],

            "belly_pain": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],

            "dischromic _patches": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],

            "watering_from_eyes": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],

            "mucoid_sputum": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],

            "rusty_sputum": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],

            "lack_of_concentration": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],


            "visual_disturbances": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],


            "history_of_alcohol_consumption": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],

            "blood_in_sputum": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],

            "pus_filled_pimples": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],

             "silver_like_dusting": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)],

             "blister": [self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)]
            
        }

