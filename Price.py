import json
from collections import OrderedDict

def PriceSetting():
    with open('Input-Fees-JSON.json') as input_file:                #Reading the JSON file
        Input_data = json.load(input_file)
        #print(Input_data)
        fees_details = list(Input_data['fees'])
        Output=OrderedDict()
        Output = {'Pricing':[]}                                      
        #kill=[]
        default_daily_price =[]                                      #list for calculating default_daily_price
        for item in fees_details:
        
            if item['type']=='FLAT FEE' and item['category']=='CLEANING' and item['restriction']=='MANDATORY' :
                Output['cleaning_fee'] = item['amount']
            if item['name']=='Guest Fee' and item['multiplier']=='NIGHT' and item['restriction']=='MANDATORY':
                Output['guests_included'] = item['baseUnitMin']
                Output['price_per_person'] = item['amount']
            if  item['type']=='FLAT FEE' :
                if item['restriction']=='MANDATORY' and item['multiplier']=='STAY' and item['name']=='Linen & Towel Fee: $70 Per Stay':
                    Output['Pricing'].append({'standard_fees_type':'PASS_THROUGH_LINEN_FEE','standard_fees_amount':item['amount']*1000000,'standard_fees_amount_type':'flat'})
                    default_daily_price.append(item['amount'])
                elif item['category']=='ACTIVITY' and item['name']=='Resort Fee':
                    Output['Pricing'].append({'standard_fees_type':'PASS_THROUGH_RESORT','standard_fees_amount':item['amount']*1000000,'standard_fees_amount_type':'flat'})
                    default_daily_price.append(item['amount'])
                elif item['category']=='ADMIN' and item['name']=='Community Fee: $125 Per Stay':
                    Output['Pricing'].append({'standard_fees_type':'PASS_THROUGH_COMMUNITY_FEE','standard_fees_amount':item['amount']*1000000,'standard_fees_amount_type':'flat'})
                    default_daily_price.append(item['amount'])
                elif item['name']=='$100 Flat Management Fee' and item['category']=='ADMIN':
                    Output['Pricing'].append({'standard_fees_type':'PASS_THROUGH_COMMUNITY_FEE','standard_fees_amount':item['amount']*1000000,'standard_fees_amount_type':'flat'})
                    default_daily_price.append(item['amount'])
                    
            Output['default_daily_price'] = sum(default_daily_price) 
        
        print(Output)
        try:
            with open("Output-Fees.json","w") as fp:
                json.dump(Output, fp)
        except:
            print('Error while creating output file')
        


if __name__ == "__main__":
    PriceSetting();
