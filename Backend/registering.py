from optparse import BadOptionError
from xml.dom import NotFoundErr
from datetime import datetime
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()


scac_codes = {
    'OOCL': 'OOLU',
    'ZIM': 'ZIMU',
    'Wan Hai': 'WHLC',
    'Maersk': 'MAEU',
    'CNC': '11DX',
    'Dongjin': '11PG',
    'Heung-A': '11QU',
    'Jin Jiang': '11WJ',
    'Interasia': '12AT',
    'Hai Hua': '12GE',
    'Sinotrans': '12IH',
    'SITC': '12PD',
    'Misheng': '13CQ',
    'T.S.': '13DF',
    'Pan Continental': '15AC',
    'Nirint': '32GH',
    'ACL': 'ACLU',
    'Admiral Container': 'ADMU',
    'AC Container': 'ALRB',
    'ANL': 'ANNU',
    'Alianca': 'ANRM',
    'APL': 'APLU',
    'Arkas': 'ARKU',
    'Blue Anchor America': 'BANQ',
    'Sunmarine': 'BAXU',
    'Bee': 'BELC',
    'Avana BALAJI': 'BLJU',
    'BLPL singapore': 'BLZU',
    'BMC': 'BMSU',
    'BNSF': 'BNLS',
    'BAL': 'BURU',
    'Blue World': 'BWLE',
    'Blue Water': 'BWLU',
    'CAMELLIA': 'CAKU',
    'Crowley': 'CAMN',
    'China Navigation': 'CHVW',
    'CK': 'CKLU',
    'CMA CGM': 'CMDU',
    'COSCO': 'COSU',
    'Cosiarma': 'CRAU',
    'Containerships': 'CSHP',
    'CULINES': 'CULU',
    'DAL': 'DAYU',
    'Damco': 'DMCQ',
    'DSV': 'DSVF',
    'Dachser': 'DTRA',
    'Econship': 'ECNU',
    'ECU': 'ECUW',
    'Evergreen': 'EGLV',
    'Emkay': 'EMKU',
    'Ethiopian': 'ESLU',
    'Emirates': 'ESPU',
    'Eukor': 'EUKO',
    'Expeditors': 'EXPO',
    'FESCO': 'FESO',
    'Tarros': 'GETU',
    'Grimaldi': 'GRIU',
    'Gold Star': 'GSLU',
    'Hyundai': 'HDMU',
    'Hillebrand': 'HGLU',
    'Hapag-Lloyd': 'HLCU',
    'JAS': 'JASO',
    'KN': 'KHNN',
    'Kambara': 'KKCL',
    'K line': 'KKLU',
    'Korea': 'KMTU',
    'Leschaco': 'LEHO',
    'Ignazio': 'LMCU',
    'Laurel': 'LNLU',
    'MLL': 'MAEI',
    'MATS': 'MATS',
    'Carpenters': 'MBFU',
    'MacAndrews': 'MCAW',
    'Sealand': 'MCCQ',
    'MELL': 'MEXU',
    'Maritime Marfret': 'MFTU',
    'Marguisa': 'MGSU',
    'MOL': 'MOLU',
    'MSC': 'MSCU',
    'Maxicon': 'MXCU',
    'Nippon': 'NEDF',
    'Nile Dutch': 'NIDU',
    'Namsung': 'NSRU',
    'NYK': 'NYKS',
    'ONE': 'ONEY',
    'Orient Star': 'OSTI',
    'Odyssey': 'OYLT',
    'Pan Asia': 'PALU',
    'PIL': 'PCIU',
    'Dong Young': 'PCSL',
    'NPDL': 'PDLU',
    'Perma': 'PMLU',
    'Pan Ocea': 'POBU',
    'Pasha Hawaii': 'PSHI',
    'QNL': 'QNLU',
    'RCL': 'REGU',
    'Romocean': 'ROMO',
    'Safmarine': 'SAFM',
    'SCI': 'SCIU',
    'Sealand Americas': 'SEAU',
    'Seino Logix Co': 'SEIN',
    'DB Schenker': 'SHKK',
    'SHAL': 'SHKU',
    'Shipco': 'SHPT',
    'Samudera': 'SIKU',
    'Sarjak': 'SJKU',
    'Sinokor': 'SKLU',
    'SML': 'SMLM',
    'STC': 'SNTU',
    'SPIL': 'SPNU',
    'Route Planner': 'SRRP',
    'SETH': 'SSPH',
    'Hamburg': 'SUDU',
    'Transfar': 'TJFH',
    'Trans Asia': 'TLXU',
    'TOTE': 'TOTE',
    'Turkon': 'TRKU',
    'Tropical': 'TSCW',
    'Transvision': 'TVSU',
    'VAS': 'VMLU',
    'WDS': 'WDSB',
    'WEC': 'WECU',
    'Wallenius Wilhelmsen': 'WLWH',
    'Westwood': 'WWSU',
    'Yusen': 'YASV',
    'Yang Ming': 'YMLU'
}
VFC_API_KEY = os.getenv("VFC_API_KEY")

def registering(FILE_PATH, params):

    FILE_PATH_All_register = f'{FILE_PATH}/All - register.xlsx'
    SHEET_NAME_All_register = 'Sheet1'

    PLANT = params['plant']

    if PLANT != 'INTIMATES':
        FILE_PATH = FILE_PATH + "/" + PLANT

    FILE_PATH_master = f"{FILE_PATH}/Master file - Input file/Master File.xlsx"
    SHEET_NAME_master = 'Master File_To be Daily updated'

    FILE_PATH_register = f"{FILE_PATH}/Master file - Register info/MT register.xlsx"
    SHEET_NAME_register = 'Sheet1'

    FILE_PATH_errorlog = f"{FILE_PATH}/API Output Files/Error Log.xlsx"
    SHEET_NAME_errorlog = 'Sheet1'

    tdType = "BL"
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    reg_df = pd.read_excel(FILE_PATH_All_register, sheet_name=SHEET_NAME_All_register, engine="openpyxl")

    df_master = pd.read_excel(FILE_PATH_master, sheet_name=SHEET_NAME_master, engine="openpyxl")

    df_register = pd.read_excel(FILE_PATH_register, sheet_name=SHEET_NAME_register, engine="openpyxl")
    # filter the MBL's need regitering & which has not regestered/shipment ID not generated
    # - This to be regesterd by button click

    df_error_log = pd.read_excel(FILE_PATH_errorlog, sheet_name=SHEET_NAME_errorlog, engine="openpyxl")

    register = df_master.loc[(df_master['Need Registering Yes/No?'] == 'Yes')]
    register = register.reset_index(drop=True)

    register = register.loc[register['MBL NO'] != 'MBL NOT GENERATED']

    register2 = pd.merge(register, df_register, on=['MBL NO'], how="outer", indicator=True)
    register2 = register2[register2['_merge'] == 'left_only']

    print(register2)
    registered = 0
    for i in range(0, len(register2)):
        try:
            registered = registered + 1
            # carrier_name
            carrier_name = register2.iloc[i, 4]

            # mbl_number
            mbl_number = register2.iloc[i, 2]

            vessel_name = register2.iloc[i, 3]

            voyage = register2.iloc[i, 12]

            mid_reg_df = reg_df.loc[(reg_df['Vessel Name'] == vessel_name)]
            mid_reg_df = mid_reg_df[mid_reg_df['Voyage'] == voyage]

            if len(mid_reg_df) > 0:
                df_register = df_register.append(mid_reg_df[0], ignore_index=True)
                df_register.to_excel(f"{FILE_PATH}/Master file - Register info/MT register.xlsx", index=False)
                continue

            print(mbl_number)
            # check whether not filled (Null) or selected 'Not Found' option
            if pd.isnull(carrier_name) or carrier_name == 'Not Found':
                print(
                    "Carrier name is not filled(empty) or User has not update the carrier name. Please select a carrier")
                pass

            elif pd.isnull(mbl_number) or mbl_number == 'Not Found':
                print(
                    "MBL number is not filled(empty) or User has not update the MBL number. Please input the MBL number")
                pass

            elif carrier_name not in scac_codes:
                print("Not supported SCAC code. Please check the carrier name")
                pass


            else:
                # scac code
                scac_code = scac_codes[carrier_name]

                # url = "https://services.marinetraffic.com/api/vfcsubscribe/" +VFC_API_KEY +"/scac:" + scac_code + "/tdId/" + str(mbl_number) + "/tdType" + tdType + "/protocol:jsono"
                # suresh
                url = "https://services.marinetraffic.com/api/vfcsubscribe/" + VFC_API_KEY + "?scac=" + scac_code + "&tdId=" + str(
                    mbl_number) + "&tdType=" + tdType
                # /vfcsubscribe/75493a4cfdf0814961fe2d12519d5bc66690077e?scac=MAEU&tdId=ABCD421911263977&tdType=BL
                print(url)

                response = requests.get(url, verify=False)
                json_response = response.json()

                print(json_response)
                print("response", response.status_code)

                if response.status_code == 400:
                    json_response['Time'] = now
                    json_response['MBL'] = mbl_number
                    json_response['ShipmentID'] = 'Generated when regestering, no shipment ID'

                    df_error_log = df_error_log.append(json_response, ignore_index=True)

                    raise BadOptionError

                if response.status_code == 401:
                    json_response['Time'] = now
                    json_response['MBL'] = mbl_number
                    json_response['ShipmentID'] = 'Generated when regestering, no shipment ID'

                    df_error_log = df_error_log.append(json_response, ignore_index=True)

                    raise ValueError('SERVICE KEY NOT FOUND')

                if response.status_code == 404:
                    json_response['Time'] = now
                    json_response['MBL'] = mbl_number
                    json_response['ShipmentID'] = 'Generated when regestering, no shipment ID'

                    df_error_log = df_error_log.append(json_response, ignore_index=True)

                    raise NotFoundErr

                if response.status_code == 500:
                    json_response['Time'] = now
                    json_response['MBL'] = mbl_number
                    json_response['ShipmentID'] = 'Generated when regestering, no shipment ID'

                    df_error_log = df_error_log.append(json_response, ignore_index=True)

                    raise SystemError

                if response.status_code == 200:
                    response_VFC = json_response

                    print(response_VFC)
                    shipmentId = response_VFC['subscription']['shipmentId']

                    new_row = {'MBL NO': mbl_number, 'Shipment ID': shipmentId, 'Vessel Name': vessel_name, 'Voyage': voyage, 'Registered date time': datetime.now()}
                    # append row to the dataframe
                    df_register = df_register.append(new_row, ignore_index=True)
                    df_register.to_excel(f"{FILE_PATH}/Master file - Register info/MT register.xlsx", index=False)

                    reg_df = reg_df.append(new_row, ignore_index=True)
                    reg_df.to_excel(FILE_PATH_All_register, index=False)

        except ConnectionError as e:
            message = str(e)

            error_code = 'Other error - code not generated'

            json_response['Time'] = now
            json_response['MBL'] = mbl_number
            json_response['ShipmentID'] = 'Generated when regestering, no shipment ID'

            df_error_log = df_error_log.append(json_response, ignore_index=True)

    df_error_log.to_excel(f"{FILE_PATH}/API Output Files/Error Log.xlsx", index=False)

    return registered


# registering(r"C:\Users\ASUS\MAS Holdings (Pvt) Ltd\Logistics DA Project - Documents\General", None)
