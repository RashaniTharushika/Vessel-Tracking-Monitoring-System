import pandas as pd
import os.path
from datetime import datetime,timedelta, date
import json


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

    if os.path.exists(f"{FILE_PATH}/Master file - Input file/Master File.xlsx"):
        df_final = pd.read_excel(f"{FILE_PATH}/Master file - Input file/Master File.xlsx", sheet_name='Master File_To be Daily updated')
        df_final = df_final.append(df, ignore_index=True)
        df_final.to_excel(f'{FILE_PATH}/Master file - Input file/Master File.xlsx', sheet_name='Master File_To be Daily updated', index=False)
    else:
        df.to_excel(f'{FILE_PATH}/Master file - Input file/Master File.xlsx', sheet_name='Master File_To be Daily updated', index=False)

    return "Success", len(df)


def get_view(params, FILE_PATH):

    plant = params['plant']
    if plant != 'INTIMATES':
        FILE_PATH = FILE_PATH + "/" + plant

    FILE_PATH_master = f"{FILE_PATH}/Master file - Input file/Master File.xlsx"
    SHEET_NAME_master = 'Master File_To be Daily updated'

    df_master = pd.read_excel(FILE_PATH_master, sheet_name=SHEET_NAME_master, engine="openpyxl")

    # data = df_master.to_json(orient = 'records')
    data = []

    for i in range(len(df_master)):
        row = {
            'File Updated Date by Logistic Team': str(df_master.loc[i, "File Updated Date by Logistic Team"]).split(" ")[0],
            'Record Updated Date by Logistic Team': str(df_master.loc[i, "Record Updated Date by Logistic Team"]).split(" ")[0],
            'MBL NO': df_master.loc[i, "MBL NO"],
            'VESSEL': df_master.loc[i, "VESSEL"],
            'Carrier': df_master.loc[i, "Carrier"],
            'POL': df_master.loc[i, "POL"],
            'ETD ': str(df_master.loc[i, "ETD "]).split(" ")[0],
            'ETA to CMB': str(df_master.loc[i, "ETA to CMB"]).split(" ")[0],
            'Need Registering Yes/No?': df_master.loc[i, "Need Registering Yes/No?"],
            'Tracking Common MBL ': df_master.loc[i, "Tracking Common MBL "],
            'Refered CN no': df_master.loc[i, "Refered CN no"],
            'MMSI': df_master.loc[i, "MMSI"],
            'Voyage': df_master.loc[i, "Voyage"],
            'HBL': df_master.loc[i, "HBL"],
            'Shipment Type': df_master.loc[i, "Shipment Type"]
        }

        data.append(row)

    return json.dumps(data)


def update(params, FILE_PATH):
    plant = params['plant']
    hbl = params['HBL']

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
    ShipmentType = params['ShipmentType']

    try:
        FILE_PATH_master = f"{FILE_PATH}/Master file - Input file/Master File.xlsx"
        SHEET_NAME_master = 'Master File_To be Daily updated'

        df_master = pd.read_excel(FILE_PATH_master, sheet_name=SHEET_NAME_master, engine="openpyxl")

        idx = df_master.index[df_master['HBL'] == hbl][0]
        df_master.iloc[idx, 0] = FileUpdatedDate
        df_master.iloc[idx, 1] = RecordUpdatedDate
        df_master.iloc[idx, 2] = MBL
        df_master.iloc[idx, 3] = VESSEL
        df_master.iloc[idx, 4] = Carrier
        df_master.iloc[idx, 5] = pol
        df_master.iloc[idx, 6] = etd
        df_master.iloc[idx, 7] = etaToCMB
        df_master.iloc[idx, 8] = NeedRegistering
        df_master.iloc[idx, 9] = TrackingCommonMBL
        df_master.iloc[idx, 11] = MMSI
        df_master.iloc[idx, 12] = Voyage
        df_master.iloc[idx, 14] = ShipmentType

        df_master.to_excel(f'{FILE_PATH}/Master file - Input file/Master File.xlsx', sheet_name='Master File_To be Daily updated', index=False)

        return "Success"
    except:
        return "Failed"


def delete(params, FILE_PATH):
    plant = params['plant']
    hbl = plant['HBL']
    if plant != 'INTIMATES':
        FILE_PATH = FILE_PATH + "/" + plant

    try:
        FILE_PATH_master = f"{FILE_PATH}/Master file - Input file/Master File.xlsx"
        SHEET_NAME_master = 'Master File_To be Daily updated'

        df_master = pd.read_excel(FILE_PATH_master, sheet_name=SHEET_NAME_master, engine="openpyxl")

        idx = df_master.index[df_master['HBL'] == hbl][0]

        df_master.drop(idx, axis=0, inplace=True)
        df_master.reset_index(drop=True, inplace=True)

        df_master.to_excel(f'{FILE_PATH}/Master file - Input file/Master File.xlsx', sheet_name='Master File_To be Daily updated', index=False)

        return "Success"
    except:
        return "Failed"
