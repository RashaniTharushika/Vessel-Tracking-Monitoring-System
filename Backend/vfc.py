from datetime import datetime
from optparse import BadOptionError
from xml.dom import NotFoundErr
import pandas as pd
import requests
import os.path
from openpyxl import load_workbook
from other import Shipment_status_dict
from dotenv import load_dotenv

load_dotenv()

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# def fill_nan(filepath, sheet_name='Sheet1'):
#     dataframe = pd.read_excel(filepath, sheet_name=sheet_name)
#
#     for column in dataframe.columns:
#         dataframe[column].fillna("Not Found", inplace=True)
#
#     book = load_workbook(filepath)
#     writer = pd.ExcelWriter(filepath, engine='openpyxl')
#     writer.book = book
#
#     writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
#
#     dataframe.to_excel(writer, sheet_name=sheet_name, index=False)
#
#     writer.close()


def vfc(FILE_PATH):
    Shipment_status_dict = {1: 'Booked',
                            2: 'Collected from Shipper',
                            3: 'Not arrived at Port of Load',
                            4: 'Waiting at Port of Load',
                            5: 'Shipped on board',
                            6: 'Underway',
                            7: 'Underway to a Transhipment Port (to be added soon)',
                            8: 'Arrival at Transhipment Port (to be added soon)',
                            9: 'Waiting at Transhipment Port',
                            10: 'Shipped on board at Transhipment Port',
                            11: 'Arrived at Port or Discharge',
                            12: 'Waiting at Destination Port',
                            13: 'Left the Destination Port',
                            14: 'Shipment Completed'}

    # input_file = "C:/Users/sachinkaa/OneDrive - MAS Holdings (Pvt) Ltd (1)/General/Master file - Input file - Documents/General"
    # output_file = "C:/Users/sachinkaa/OneDrive - MAS Holdings (Pvt) Ltd (1)/General/API Output Files - Documents/General/API Output Files"

    FILE_PATH_master = f"{FILE_PATH}/Master file - Input file/Master File.xlsx"
    SHEET_NAME_master = 'Master File_To be Daily updated'
    PORT_ID = 1272

    FILE_PATH_register = f"{FILE_PATH}/Master file - Register info/MT register.xlsx"
    SHEET_NAME_register = 'Sheet1'

    FILE_PATH_errorlog = f"{FILE_PATH}/API Output Files/Error Log.xlsx"
    SHEET_NAME_errorlog = 'Sheet1'

    VFC_API_KEY = os.getenv("VFC_API_KEY")

    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    df_master = pd.read_excel(FILE_PATH_master, sheet_name=SHEET_NAME_master)

    df_master = df_master.loc[df_master['Need Registering Yes/No?'] == 'Yes']

    df_master = df_master[~pd.isnull(df_master['MBL NO'])]

    df_register = pd.read_excel(FILE_PATH_register, sheet_name=SHEET_NAME_register)
    df_error_log = pd.read_excel(FILE_PATH_errorlog, sheet_name=SHEET_NAME_errorlog)
    print(df_master)
    #  print(type(df_master['Shipment ID']))

    df_register.drop(['Vessel Name', 'Voyage'], axis=1, inplace=True)

    df_master.index = range(len(df_master.index))
    df_master_1 = pd.merge(df_master, df_register, on='MBL NO', how='inner')

    # df_master = df_master[~pd.isnull(df_master['Shipment ID'])]

    print(df_master)
    df_VFC = df_master_1.reindex(
        columns=[*df_master_1.columns.tolist(),
                 #  'Shipment Id',
                 'SCAC',
                 'Carrier.1',
                 'Transport Document ID',
                 'Transport Document Type',
                 'Shipment Status',
                 'Origin Port',
                 'Origin Port Name',
                 'Origin Port Unlocode',
                 'Origin Port Country',
                 'Origin Port Local TimeOffset',
                 'Origin Port Predictive Departure Utc',
                 'Origin Port Actual Departure Utc',
                 'Final Port Id',
                 'Final Port Name',
                 'Final Port Unlocode',
                 'Final Port Country',
                 'Final Port Local TimeOffset',
                 'Final Port Predictive Arrival Utc',
                 'Final Port Predictive Arrival Utc Last',
                 'Final Port Actual Arrival Utc',
                 'Final Port Anchorage Actual Arrival Utc',
                 'Final Port Terminal Actual Arrival Utc',
                 'Final Port Terminal Actual Arrival Name',
                 'Vessel Name',
                 'Vessel IMO Number',
                 'Vessel ShipID',
                 'Carrier Voyage Number',
                 'Next Port Name',
                 'Next Port ID',
                 'Next Port Unlocoded',
                 'Next Port DistanceToGo',
                 'Next PortPredictiveArrival',
                 'Web View URL',
                 'Modified Date Time'
                 ],
        fill_value=None)

    df_events = pd.DataFrame(
        columns=['Event ID', 'Event Type Description', 'Event Category', 'Event Date Time', 'Event Status',
                 'Carrier Voyage Number', 'Vessel', 'Location', 'MBL Number'])

    ship_name_dict = {}
    port_name_dict = {}
    tracked_ships = 0

    for i in range(0, len(df_master)):
        try:
            MBL = df_VFC.iloc[i, 2]

            shipmentId = str(df_register[df_register['MBL NO'] == df_master.iloc[i, 2]]['Shipment ID']).split()[1]
            # shipmentId = df_register.iloc[i, 1]

            url = "https://services.marinetraffic.com/api/vfcshipment/" + VFC_API_KEY + "/shipmentId:" + shipmentId + "/protocol:jsono"

            response = requests.get(url, verify=False)
            json_response = response.json()
            # print(json_response)

            if response.status_code == 400:
                json_response['Time'] = now
                json_response['MBL'] = MBL
                json_response['ShipmentID'] = shipmentId

                df_error_log = df_error_log.append(json_response, ignore_index=True)

                raise BadOptionError

            if response.status_code == 404:
                json_response['Time'] = now
                json_response['MBL'] = MBL
                json_response['ShipmentID'] = shipmentId

                df_error_log = df_error_log.append(json_response, ignore_index=True)

                raise NotFoundErr

            if response.status_code == 500:
                json_response['Time'] = now
                json_response['MBL'] = MBL
                json_response['ShipmentID'] = shipmentId

                df_error_log = df_error_log.append(json_response, ignore_index=True)
                raise SystemError

            if response.status_code == 200:
                response_VFC = json_response

                #  Opening JSON 
                # filef= open('C:/Users/User/Desktop/Vessel Tracking Outputs/YM CONTINUITY Vessel/2022_08_22_9.30 AM - YM.json')  

                # response_VFC.get(= json.load(filef)

                # shipmentId = response_VFC.get('shipmentId')
                scac = response_VFC.get('scac')
                carrier = response_VFC.get('carrier')
                transportDocumentID = response_VFC.get('transportDocumentId')
                transportDocumentType = response_VFC.get('transportDocumentType')
                shipmentStatus = response_VFC.get('shipmentStatus')
                originPort = response_VFC.get('originPortId')
                originPortName = response_VFC.get('originPortName')
                originPortUnlocode = response_VFC.get('originPortUnlocode')
                originPortCountry = response_VFC.get('originPortCountry')
                originPortLocalTimeOffset = response_VFC.get('originPortLocalTimeOffset')
                originPortPredictiveDepartureUtc = response_VFC.get('originPortPredictiveDepartureUtc')
                originPortActualDepartureUtc = response_VFC.get('originPortActualDepartureUtc')
                finalPortId = response_VFC.get('finalPortId')
                finalPortName = response_VFC.get('finalPortName')
                finalPortUnlocode = response_VFC.get('finalPortUnlocode')
                finalPortCountry = response_VFC.get('finalPortCountry')
                finalPortLocalTimeOffset = response_VFC.get('finalPortLocalTimeOffset')
                finalPortPredictiveArrivalUtc = response_VFC.get('finalPortPredictiveArrivalUtc')
                finalPortPredictiveArrivalUtcLast = response_VFC.get('finalPortPredictiveArrivalUtcLast')
                finalPortActualArrivalUtc = response_VFC.get('finalPortActualArrivalUtc')
                finalPortAnchorageActualArrivalUtc = response_VFC.get('finalPortAnchorageActualArrivalUtc')
                finalPortTerminalActualArrivalUtc = response_VFC.get('finalPortTerminalActualArrivalUtc')
                finalPortTerminalActualArrivalName = response_VFC.get('finalPortTerminalActualArrivalName')
                vesselName = response_VFC.get('vesselName')
                vesselIMONumber = response_VFC.get('vesselIMONumber')
                vesselShipID = response_VFC.get('vesselShipId')
                carrierVoyageNumber = response_VFC.get('currentCarrierVoyageNumber')
                nextPortName = response_VFC.get('nextPortName')
                nextPortID = response_VFC.get('nextPortId')
                nextPortUnlocoded = response_VFC.get('nextPortUnlocode')
                nextPortDistanceToGo = response_VFC.get('nextPortDistanceToGo')
                nextPortPredictiveArrival = response_VFC.get('nextPortPredictiveArrivalUtc')
                webViewURL = response_VFC.get('webViewUrl')

                # df_VFC.iloc[i, 12] = shipmentId
                df_VFC.iloc[i, 17] = scac
                df_VFC.iloc[i, 18] = carrier
                df_VFC.iloc[i, 19] = transportDocumentID
                df_VFC.iloc[i, 20] = transportDocumentType
                df_VFC.iloc[i, 21] = Shipment_status_dict[shipmentStatus]
                df_VFC.iloc[i, 22] = originPort
                df_VFC.iloc[i, 23] = originPortName
                df_VFC.iloc[i, 24] = originPortUnlocode
                df_VFC.iloc[i, 25] = originPortCountry
                df_VFC.iloc[i, 26] = originPortLocalTimeOffset
                df_VFC.iloc[i, 27] = originPortPredictiveDepartureUtc
                df_VFC.iloc[i, 28] = originPortActualDepartureUtc
                df_VFC.iloc[i, 29] = finalPortId
                df_VFC.iloc[i, 30] = finalPortName
                df_VFC.iloc[i, 31] = finalPortUnlocode
                df_VFC.iloc[i, 32] = finalPortCountry
                df_VFC.iloc[i, 33] = finalPortLocalTimeOffset
                df_VFC.iloc[i, 34] = finalPortPredictiveArrivalUtc
                df_VFC.iloc[i, 35] = finalPortPredictiveArrivalUtcLast
                df_VFC.iloc[i, 36] = finalPortActualArrivalUtc
                df_VFC.iloc[i, 37] = finalPortAnchorageActualArrivalUtc
                df_VFC.iloc[i, 38] = finalPortTerminalActualArrivalUtc
                df_VFC.iloc[i, 39] = finalPortTerminalActualArrivalName
                df_VFC.iloc[i, 40] = vesselName
                df_VFC.iloc[i, 41] = vesselIMONumber
                df_VFC.iloc[i, 42] = vesselShipID
                df_VFC.iloc[i, 43] = carrierVoyageNumber
                df_VFC.iloc[i, 44] = nextPortName
                df_VFC.iloc[i, 45] = nextPortID
                df_VFC.iloc[i, 46] = nextPortUnlocoded
                df_VFC.iloc[i, 47] = nextPortDistanceToGo
                df_VFC.iloc[i, 48] = nextPortPredictiveArrival
                df_VFC.iloc[i, 49] = webViewURL
                df_VFC.iloc[i, 50] = datetime.now()
                print('**********')
                # print(list(df_VFC.columns.values))
                transportationPlan = response_VFC['transportationPlan']

                transportLegs = transportationPlan['transportLegs']
                print('**********')
                print(type(transportLegs))

                if len(transportLegs) >= 1:
                    locations = transportationPlan['locations']

                    df_transportleg = pd.DataFrame(transportLegs)
                    # df_transportleg["MBL NO"] = df_master.iloc[i,2]
                    df_transportleg["Depature Location Name"] = 0
                    df_transportleg["Depature Location Country"] = 0
                    df_transportleg["Depature Latitude"] = 0
                    df_transportleg["Depature Longitude"] = 0

                    df_transportleg["Arrival Location Name"] = 0
                    df_transportleg["Arrival Location Country"] = 0
                    df_transportleg["Arrival Latitude"] = 0
                    df_transportleg["Arrival Longitude"] = 0

                    # df_transportleg2 = pd.DataFrame(locations)

                    for k in range(len(df_transportleg)):

                        # print("len",len(df_transportleg))   
                        # print(df_transportleg.iloc[i,3]["portId"])  

                        for j in range(len(locations)):

                            if df_transportleg.iloc[k, 3]['portId'] == locations[j]['portId']:
                                # print("match",i,j)    
                                locationName = locations[j]["locationName"]

                                locationCountry = locations[j]["locationCountry"]
                                lat = locations[j]["lat"]
                                lon = locations[j]["lon"]

                                df_transportleg.iloc[k, 11] = locationName
                                df_transportleg.iloc[k, 12] = locationCountry
                                df_transportleg.iloc[k, 13] = lat
                                df_transportleg.iloc[k, 14] = lon
                                # df_transportleg.iloc[k, 15] = df_master.iloc[i,2]                              
                                # print(df_master.iloc[i,2])
                            # print(df_transportleg.iloc[i,6]["portId"]) 
                            if df_transportleg.iloc[k, 6]['portId'] == locations[j]['portId']:
                                locationName = locations[j]["locationName"]

                                # print("locationName", locationName)
                                locationCountry = locations[j]["locationCountry"]
                                lat = locations[j]["lat"]
                                lon = locations[j]["lon"]

                                df_transportleg.iloc[k, 15] = locationName
                                df_transportleg.iloc[k, 16] = locationCountry
                                df_transportleg.iloc[k, 17] = lat
                                df_transportleg.iloc[k, 18] = lon

                                if not "MBL_NO" in df_transportleg.columns:
                                    df_transportleg["MBL_NO"] = None
                                    # df_transportleg.iloc[k, 20] = df_master.iloc[i,2] 

                                # else:
                                #     df_transportleg["MBL_NO"] = None

                                df_transportleg.iloc[k, 19] = df_master.iloc[i, 2]
                                # df_transportleg.ioloc[k, 20] =

                                # df_transportleg.iloc[i,19] = datetime.now()

                                df_transportleg.to_excel(f"{FILE_PATH}/API Output Files/Transport_Leg_Static.xlsx",
                                                         index=False)

                                # df_final = pd.read_excel("C:/Users/User/Desktop/Logistic script/API Output Files/Transport_Leg.xlsx")
                                # frames = [df_final,df_VFC]
                                # Full_df = pd.concat(frames,axis=0)
                                # Full_df.to_excel('C:/Users/User/Desktop/Logistic script/API Output Files/Transport_Leg.xlsx', index=False)

                events = transportationPlan['events']
                for event in events:
                    new_row = {'Event ID': event['eventId'],
                               'Event Type Description': event['eventTypeDescription'],
                               'Event Category': event['eventCategory'],
                               'Event Date Time': event['eventDatetime'],
                               'Event Status': event['eventStatus'],
                               'Carrier Voyage Number': event['carrierVoyageNumber'],
                               'Vessel': event['vessel']['shipId'],
                               'Location': event['location']['portId'],
                               'MBL Number': df_master.iloc[i, 2]}

                    df_events = df_events.append(new_row, ignore_index=True)
                    # frames = [df_events,pd.DataFrame(new_row)]
                    # df_events = pd.concat(frames,axis=0)

                vessels = transportationPlan['vessels']
                for vessel in vessels:
                    ship_name_dict[vessel['shipId']] = vessel['vesselName']

                locations = transportationPlan['locations']
                for location in locations:
                    port_name_dict[location['portId']] = location['locationName']
            tracked_ships = tracked_ships + 1

        except ConnectionError as e:
            message = str(e)

            error_code = 'Other error - code not generated'

            json_response['Time'] = now
            json_response['MBL'] = 'mbl_number'
            json_response['ShipmentID'] = shipmentId

            df_error_log = df_error_log.append(json_response, ignore_index=True)
            raise ConnectionError('INCORRECT CALL-CHECK PARAMETERS')

        except Exception as e:
            print(e)
            pass

    event_status_dict = {'ACT': 'Actual',
                         'PLN': 'Planned'}

    # df_events['Event Status'].map(event_status_dict).fillna(df_events['Event Status'])
    df_events['Event Status'].replace(event_status_dict, inplace=True)
    df_events['Vessel'].replace(ship_name_dict, inplace=True)
    df_events['Location'].replace(port_name_dict, inplace=True)

    df_events.to_excel(f"{FILE_PATH}/API Output Files/Events_Stat.xlsx", index=False)

    # df_final = pd.read_excel("C:/Users/User/Desktop/Logistic script/API Output Files/Events.xlsx")
    # frames = [df_final,df_VFC]
    # Full_df = pd.concat(frames,axis=0)
    # Full_df.to_excel('C:/Users/User/Desktop/Logistic script/API Output Files/Events.xlsx', index=False)

    df_VFC.to_excel(f"{FILE_PATH}/API Output Files/VFC_Static.xlsx", index=False)

    if os.path.exists(f"{FILE_PATH}/API Output Files/VFC.xlsx"):
        df_final = pd.read_excel(f"{FILE_PATH}/API Output Files/VFC.xlsx", sheet_name='Sheet1')
        df_final = df_final.append(df_VFC, ignore_index=True)
        df_final.to_excel(f'{FILE_PATH}/API Output Files/VFC.xlsx', index=False)
    else:
        df_VFC.to_excel(f'{FILE_PATH}/API Output Files/VFC.xlsx', index=False)

    # df_final = pd.read_excel("C:/Users/User/Desktop/Logistic script/API Output Files/VFC.xlsx")
    # frames = [df_final,df_VFC]
    # Full_df = pd.concat(frames,axis=0)
    # Full_df.to_excel('C:/Users/User/Desktop/Logistic script/API Output Files/VFC.xlsx', index=False)

    # Fill Nan and blank values
    # fill_nan(f'{FILE_PATH}/API Output Files/Transport_Leg_Static.xlsx')
    # fill_nan(f"{FILE_PATH}/API Output Files/VFC_Static.xlsx")
    # fill_nan(f'{FILE_PATH}/API Output Files/Events_Stat.xlsx')
    df_error_log.to_excel(f"{FILE_PATH}/API Output Files/Error Log.xlsx", index=False)
    print('COMPLETE')
    return tracked_ships

# if __name__ == "__main__":
# vfc(r"C:\Users\ASUS\MAS Holdings (Pvt) Ltd\Logistics DA Project - Documents\General")
