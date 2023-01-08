from flask import Flask,request
from pymongo import MongoClient

app=Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
hospital_database = client['bed_management']
hospital_collection = hospital_database['hospital_details']

patient_database = client['bed_management']
patient_collection = patient_database['patient_details']

@app.route("/data_insertion", methods=['post'])
def patient_data():
    try:
        input_json = request.get_json()
        patient_collection.insert_one(input_json)
        print(input_json)
        hospital_idno=input_json['hospital_idno']
        print(hospital_idno)
        response = list(hospital_collection.find({"hospital_idno": hospital_idno}, {"_id": 0}))

        response1 = (response[0]['hospital_vaccancy']) - 1
        print(response1)
        data1 = {"hospital_idno": hospital_idno}
        data_to_update = {"$set": {"hospital_vaccancy": response1}}
        hospital_collection.update_one(filter=data1, update=data_to_update)
        return {'message': "successfully inserted",'data':response}

    except Exception as e:
        print(f"Error : {str(e)}")
        return {'status': " Sorry No vaccancy beds available"}


@app.route("/hospital_data_insertion", methods=['post'])
def hospital_data():
    try:
        input_json = request.get_json()
        hospital_collection.insert_one(input_json)
        print(input_json)
        return {'status': "successfully inserted",'data2':input_json}

    except Exception as e:
        print(f"Error : {str(e)}")
        return {'status': " invallid"}

@app.route("/find_patient", methods=['post'])
def patient_info():
    try:
        input_json = request.get_json()
        print(input_json)
        hospitalid=input_json['hospital_idno']
        patient_total_info = list(patient_collection.find({'hospital_idno': hospitalid}, {"_id": 0}))
        print(patient_total_info)
        for patient_data in patient_total_info:
            print(patient_data['patient_name'])
        return {'status': "SUCCESSFULLY GET THE DETAILS OF THE PATIENT",'data2':patient_data}

    except Exception as e:
        print(f"Error : {str(e)}")
        return {'status': "PATIENT NOT FOUND"}



@app.route("/list_patient_data", methods=['post'])
def patient_information_data():
    try:
        input_json = request.get_json()
        print(input_json)
        hospitalid = input_json['hospital_idno']
        patient_total_info = list(patient_collection.find({'hospital_idno': hospitalid}, {"_id": 0}))
        for hospital_info_data in patient_total_info:
            print(hospital_info_data)
        patient_hospital_id = patient_total_info[0]["hospital_idno"]
        print(patient_hospital_id)
        hospital_total_info = list(hospital_collection.find({"hospital_idno": hospitalid}, {"_id": 0}))
        print(hospital_total_info)
        for patient_info_data in patient_total_info:
            print(patient_info_data)
        hospital_name_id = hospital_total_info[0]["hospital_idno"]
        print(hospital_name_id)
        if hospital_name_id == patient_hospital_id:
            print(hospital_total_info[0]["hospital_name"])

        return {'status': "SUCCESSFULLY got the hospital_info oh patient",'data4':print(hospital_total_info[0]["hospital_name"])}
    except Exception as e:
        print(f"Error : {str(e)}")
        return {'status': "PATIENT NOT FOUND"}

@app.route("/remove_data", methods=['post'])
def delete_patient_info():
    input_json = request.get_json()
    print(input_json)
    patient_id = input_json['patient_id']
    patient_total_info = list(patient_collection.find({'patient_id': patient_id}, {"_id": 0}))
    print(patient_total_info)
    patient_hospital_info=patient_total_info[0]['hospital_idno']
    print(patient_hospital_info)
    deleting_patient_data = patient_collection.delete_one({"patient_id": patient_id})
    print(deleting_patient_data)
    hospital_data_of_patient= list(hospital_collection.find({"hospital_idno": patient_hospital_info}, {"_id": 0}))
    print(hospital_data_of_patient)
    response1 = (hospital_data_of_patient[0]['hospital_vaccancy']) + 1
    print(response1)
    data1 = {"hospital_idno": patient_hospital_info}
    data_to_update = {"$set": {"hospital_vaccancy": response1}}
    hospital_collection.update_one(filter=data1, update=data_to_update)





    return "success"






if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5555)
