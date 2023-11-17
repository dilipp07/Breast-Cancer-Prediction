from flask import Flask,request,render_template,jsonify
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
from src.exception import CustomException
import os
import sys

application=Flask(__name__)

app=application



@app.route('/')
def home_page():
    try:
        return render_template('index.html')
    except Exception as e:
        raise CustomException(e,sys)

@app.route('/predict',methods=['GET','POST'])


def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:

        data=CustomData(
            radius_mean =float (request.form.get('radius_mean')),
            texture_mean =float (request.form.get('texture_mean')),
            smoothness_mean =float (request.form.get('smoothness_mean')),
            compactness_mean =float (request.form.get('compactness_mean')),
            concavity_mean =float (request.form.get('concavity_mean')),
            concave_points_mean =float (request.form.get('concave_points_mean')),
            symmetry_mean =float (request.form.get('symmetry_mean')),
            fractal_dimension_mean =float (request.form.get('fractal_dimension_mean')),
            radius_se =float (request.form.get('radius_se')),
            texture_se =float (request.form.get('texture_se')),
            perimeter_se =float (request.form.get('perimeter_se')),
            area_se =float (request.form.get('area_se')),
            smoothness_se =float (request.form.get('smoothness_se')),
            compactness_se =float (request.form.get('compactness_se')),
            concavity_se =float (request.form.get('concavity_se')),
            concave_points_se =float (request.form.get('concave_points_se')),
            symmetry_se =float (request.form.get('symmetry_se')),
            fractal_dimension_se =float (request.form.get('fractal_dimension_se')),
            texture_worst =float (request.form.get('texture_worst')),
            smoothness_worst =float (request.form.get('smoothness_worst')),
            compactness_worst =float (request.form.get('compactness_worst')),
            concavity_worst =float (request.form.get('concavity_worst')),
            concave_points_worst =float (request.form.get('concave_points_worst')),
            symmetry_worst =float (request.form.get('symmetry_worst')),
            fractal_dimension_worst =float (request.form.get('fractal_dimension_worst'))
            

        )
        final_new_data=data.get_data_as_dataframe()
        print(final_new_data)
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        # results=round(pred[0],2)

        return render_template('result.html',final_result=pred)






if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)