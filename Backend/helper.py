import pandas as pd
import os.path
from datetime import datetime,timedelta, date


def input_form_data(params, FILE_PATH):

    plant = params['plant']
    if plant != 'INTIMATES':
        FILE_PATH = FILE_PATH + "/" + plant

    FileUpdatedDate = params['FileUpdatedDate']
    RecordUpdatedDate = params['RecordUpdatedDate']
    MBL = params['MBL']
    VESSEL = params['VESSEL']
    Carrier = params['Carrier']
    pol = params['pol']
    etd = params['etd']
    etaToCMB = params['etaToCMB']
    NeedRegistering = params['NeedRegistering']
    TrackingCommonMBL = params['TrackingCommonMBL']
    MMSI = params['MMSI']
    Voyage = params['Voyage']
    HBL = params['HBL']
    ShipmentType = params['ShipmentType']


    FileUpdatedDate = datetime.fromisoformat(FileUpdatedDate) + timedelta(days=1)
    RecordUpdatedDate = datetime.fromisoformat(RecordUpdatedDate) + timedelta(days=1)
    etd = datetime.fromisoformat(etd) + timedelta(days=1)
    etaToCMB = datetime.fromisoformat(etaToCMB) + timedelta(days=1)

    df = pd.DataFrame(columns=['File Updated Date by Logistic Team',
                               'Record Updated Date by Logistic Team',
                               'MBL NO',
                               'VESSEL',
                               'Carrier',
                               'POL',
                               'ETD ',
                               'ETA to CMB',
                               'Need Registering Yes/No?',
                               'Tracking Common MBL ',
                               'MMSI',
                               'Voyage',
                               'HBL',
                               'Shipment Type'])



    for hbl in HBL:
        data = {
            'File Updated Date by Logistic Team': FileUpdatedDate,
            'Record Updated Date by Logistic Team': RecordUpdatedDate,
            'MBL NO': MBL,
            'VESSEL': VESSEL,
            'Carrier': Carrier,
            'POL': pol,
            'ETD ': etd,
            'ETA to CMB': etaToCMB,
            'Need Registering Yes/No?': NeedRegistering,
            'Tracking Common MBL ': TrackingCommonMBL,
            'MMSI': MMSI,
            'Voyage': Voyage,
            'HBL': hbl,
            'Shipment Type': ShipmentType
        }

        df = df.append(data, ignore_index=True)

    if os.path.exists(f"{FILE_PATH}/Master file - Input file/Master File - Test.xlsx"):
        df_final = pd.read_excel(f"{FILE_PATH}/Master file - Input file/Master File - Test.xlsx", sheet_name='Master File_To be Daily updated')
        df_final = df_final.append(df, ignore_index=True)
        df_final.to_excel(f'{FILE_PATH}/Master file - Input file/Master File - Test.xlsx', sheet_name='Master File_To be Daily updated', index=False)
    else:
        df.to_excel(f'{FILE_PATH}/Master file - Input file/Master File - Test.xlsx', sheet_name='Master File_To be Daily updated', index=False)

    return "Success", len(df)


def get_view(params, FILE_PATH):

    plant = params['plant']
    if plant != 'INTIMATES':
        FILE_PATH = FILE_PATH + "/" + plant

    FILE_PATH_master = f"{FILE_PATH}/Master file - Input file/Master File.xlsx"
    SHEET_NAME_master = 'Master File_To be Daily updated'

    df_master = pd.read_excel(FILE_PATH_master, sheet_name=SHEET_NAME_master, engine="openpyxl")

    data = df_master.to_json(orient = 'records')

    return data
