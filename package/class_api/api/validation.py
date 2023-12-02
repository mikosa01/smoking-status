from marshmallow import Schema, fields, ValidationError, validates_schema

import typing as t 
import json 

class InvalidInputError(Exception):
    """Invalid model input"""

# SYNTAX_ERROR_FIELD_MAP = {
#     'height(cm)' : "height_cm",
#     'weight(kg)' : 'weight_kg', 
#     'waist(cm)' :  "waist_cm", 
#     'eyesight(left)' : 'eyesight_left',
#     'eyesight(right)' : 'eyesight_right',
#     'hearing(left)' : 'hearing_left', 
#     'hearing(right)' : 'hearing_right',
#     'fasting blood sugar' : 'fasting_blood_sugar', 
#     'Urine protein' : 'Urine_protein', 
#     'serum creatinine' : 'serum_ceratintine',
#     'dental caries' : 'dental_caries'
# }

class SmokingDataRequestSchema(Schema):
    id = fields.Integer()
    age = fields.Integer()
    height_cm = fields.Integer(data_key='height_cm')
    weight_kg = fields.Integer(data_key='weight_kg')
    waist_cm = fields.Integer(data_key='waist_cm')
    eyesight_left = fields.Integer(data_key='eyesight_left')
    eyesight_right = fields.Integer(data_key='eyesight_right')
    hearing_left = fields.Integer(data_key='hearing_left')
    hearing_right = fields.Integer(data_key='hearing_right')
    systolic = fields.Integer()
    diastolic = fields.Integer()  # Renamed relaxation to diastolic for clarity
    fasting_blood_sugar = fields.Integer(data_key='fasting_blood_sugar')
    cholesterol = fields.Integer()  # Renamed Cholesterol to cholesterol
    triglyceride = fields.Integer()
    hdl = fields.Integer()  # Renamed HDL to hdl
    ldl = fields.Integer()  # Renamed LDL to ldl
    hemoglobin = fields.Integer()
    urine_protein = fields.Integer(data_key='urine_protein')  # Renamed Urine_protein to urine_protein
    serum_creatinine = fields.Integer(data_key='serum_creatinine')
    ast = fields.Integer(data_key='AST')  # Renamed AST to ast
    alt = fields.Integer(data_key='ALT')  # Renamed ALT to alt
    gtp = fields.Integer()
    dental_caries = fields.Integer(data_key='dental_caries')
    smoking = fields.Integer()


@validates_schema
def validate_inputs(input_data, **kwargs):
    for data_point in input_data:
        height_cm = data_point.get('height_cm')
        if height_cm is not None and height_cm < 0:
            raise ValidationError('Height cannot be negative.')


# class SmokingDataRequestSchema(Schema): 
#     id = fields.Integer()
#     age = fields.Integer()
#     height_cm = fields.Integer(data_key = 'height(cm)')
#     weight_kg = fields.Integer(data_key = 'weight(kg)')
#     waist_cm = fields.Integer(data_key = 'waist(cm)')
#     eyesight_left = fields.Integer(data_key = 'eyesight(left)')
#     eyesight_right = fields.Integer(data_key = 'eyesight(right)')
#     hearing_left = fields.Integer(data_key='hearing(left)')
#     hearing_right = fields.Integer(data_key='hearing(right)')
#     systolic = fields.Integer()
#     relaxation = fields.Integer()
#     fasting_blood_sugar = fields.Integer(data_key = 'fasting blood sugar' )
#     Cholesterol = fields.Integer()
#     triglyceride = fields.Integer()
#     HDL = fields.Integer()
#     LDL = fields.Integer()
#     hemoglobin = fields.Integer()
#     Urine_protein  = fields.Integer(data_key = 'Urine protein' )
#     serum_creatinine = fields.Integer(data_key = 'serum creatinine' )
#     AST = fields.Integer()
#     ALT = fields.Integer()
#     Gtp = fields.Integer()
#     dental_caries = fields.Integer(data_key = 'dental caries')
#     smoking = fields.Integer()



# @validates_schema
# def validate_inputs(input_data, **kwargs):
#     # if not isinstance(input_data, list):
#     #     raise ValidationError('Input data should be a list of dictionaries.')

#     for data_point in input_data:
#         height_cm = data_point.get('height_cm')
#         if height_cm is not None and height_cm < 0:
#             raise ValidationError('Height cannot be negative.')

# @validates_schema
# def validate_inputs(input_data, **kwargs:None):
#     height_cm = input_data.get('height_cm')
#     if height_cm is not None and height_cm < 0:
#         raise ValidationError('Height cannot be negative.')

# def _filter_error_rows(errors:dict, 
#                        validate_input: t.List[dict]
#                        ) -> t.List[dict]:
#     indexes = errors.keys()

#     for index in sorted(indexes, reverse=True): 
#         del validate_input[index]
#     return validate_input

# def validate_inputs(input_data): 
#     schema = SmokingDataRequestSchema( many= True)

#     for dict in input_data:
#         for key, value in SYNTAX_ERROR_FIELD_MAP.items():
#             dict[value] = dict[key]
#             del dict[key]

#     errors= None
#     try:
#         schema.load(input_data)
#     except ValidationError as exc: 
#         errors = exc.messages

#     for dict in input_data: 
#         for key, value in  SYNTAX_ERROR_FIELD_MAP.items(): 
#             dict[key] = dict[value]
#             del dict[value]

#     if errors: 
#         validated_input = _filter_error_rows(errors= errors, validate_input=input_data)
#     else: 
#         validated_input = input_data
#     return validated_input, errors