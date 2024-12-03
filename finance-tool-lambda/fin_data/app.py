import json
from common_utils import send_email
from data_utlis import generate_bakery_network_data, analyze_industry_performance, format_analysis_to_string

# Generate sample data
df = generate_bakery_network_data()

def lambda_handler(event, context):
    agent = event['agent']
    actionGroup = event['actionGroup']
    function = event['function']
    parameters = {param['name']: param['value'] for param in event.get('parameters', [])}

    response_body = ""
    
    if function == 'send_email':
        subject = parameters.get('subject')
        html_body = parameters.get('html_body')
        if html_body and subject:
            response_body = str(send_email(subject, html_body))
        else:
            response_body = "Error: Missing subject or html_body parameter"
    elif function == 'analyze_industry_performance':
        industry = parameters.get('industry')
        date_from = parameters.get('date_from')
        date_to = parameters.get('date_to')
        if industry and date_from and date_to:
            data_res = analyze_industry_performance(
               df, 
                industry=industry,
                date_range=(date_from, date_to)
            )
            print(format_analysis_to_string(data_res))
            response_body = json.dumps(data_res, indent=2, default=str)
        else:
            response_body = "Error: Missing industry or date_from or date_to parameter"
    elif function == 'analyze_all_performance':
        data_res = analyze_industry_performance(df)
        print(format_analysis_to_string(data_res))
        response_body = json.dumps(data_res, indent=2, default=str)
    else:
        response_body = f"Unknown function: {function}"

    responseBody = {
        "TEXT": {
            "body": response_body
        }
    }
    
    action_response = {
        'actionGroup': actionGroup,
        'function': function,
        'functionResponse': {
            'responseBody': responseBody
        }
    }
    
    function_response = {'response': action_response, 'messageVersion': event['messageVersion']}
    # print(f"Response: {json.dumps(function_response)}")
    return function_response