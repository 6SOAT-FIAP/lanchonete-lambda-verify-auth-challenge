# Acionador lambda para verificar resposta do desafio de autenticação

def lambda_handler(event, context):
    
    expected_answer = event['request']['privateChallengeParameters']['secretCode']
    
    if event['request']['challengeAnswer'] == expected_answer:
        event['response']['answerCorrect'] = True
    else:
        event['response']['answerCorrect'] = False
        
    return event