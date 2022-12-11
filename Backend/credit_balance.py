import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


def credit_balance(FILE_PATH):
    CREDITS_BALANCE_API_KEY = '6d41e361d93ce1e92e5caea93036a3ed76c1c8c0'
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    FILE_PATH_errorlog = f"{FILE_PATH}/API Output Files/Error Log.xlsx"
    SHEET_NAME_errorlog = 'Sheet1'

    # FILE_PATH_creditbalance = f"{FILE_PATH}/API Output Files/Credit Balance.xlsx"
    # SHEET_NAME_creditbalance = 'Sheet1'

    df_error_log = pd.read_excel(FILE_PATH_errorlog, sheet_name=SHEET_NAME_errorlog)

    # df = pd.read_excel(FILE_PATH_creditbalance, sheet_name=SHEET_NAME_creditbalance)

    try:
        url = 'https://services.marinetraffic.com/api/exportcredits/' + CREDITS_BALANCE_API_KEY +"/protocol:jsono"
        response = requests.get(url, verify=False)
        response_json = response.json()

        print(response_json)
        if response.status_code == 200:
            #print(response_json)
            #print(response.status_code)
            response_credits = response_json[0]
            
            balance = response_credits['CREDIT_BALANCE']
            # balance = response_credits['LAST_CHARGED']
            print(balance)
            
            response_json_dict = response_json[0]
            response_json_dict.update({'Modified Date': now})
            #print(response_json_dict)
            df = pd.DataFrame(response_json_dict , index=[0])
            
            df.to_excel(f"{FILE_PATH}/API Output Files/Credit Balance.xlsx", index=False)

            return balance
            
        else: 
                       
            error_response_dict = {
                                    'status': 'error',
                                    'code': response_json['errors'][0]['code'],
                                    'message':response_json['errors'][0]['detail'],
                                    'Time': now, 
                                    'MBL':"Generated when balance checking, no MBL",
                                    'ShipmentID':"Generated when balance checking, no shipment ID"
                                 }

            print(error_response_dict)    
            df_error_log = df_error_log.append(error_response_dict, ignore_index=True)
            # df_creditbalance = df_creditbalance.append(error_response_dict, ignore_index=True)

            print(df_error_log)
            df_error_log.to_excel(f"{FILE_PATH}/API Output Files/Error Log.xlsx", index=False)
           
            # raise ValueError('SERVICE KEY NOT FOUND')

    except Exception as e:
        pass
        
    

# if __name__ == '__main__':
#     credit_balance("C:/Users/User/MAS Holdings (Pvt) Ltd/Logistics DA Project - Documents/General")
