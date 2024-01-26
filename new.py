import re
import long_responses as long

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        prob = message_probability(message, list_of_words, single_response, required_words)
        highest_prob_list[bot_response] = prob

    # Responses -----------------------------------------
    response('Hello There!', ['hello', 'hi', 'sup', 'hey', 'heyo', 'howdy', 'hola'], single_response=True)
    response('My name is ASN, Nice to meet you:)', ['your', 'name'], required_words=['name'])
    response('2*2 is 4',['2*2'], required_words=['2*2'])
    response(long.Q_Chick, ['how', 'to', 'take', 'care', ' of', 'a', 'baby', 'chicken'], required_words=['baby', 'care', 'chick'])
    response("I'm doing fine, and you?", ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Thank You!', ['I', 'like', 'this', 'bot'], required_words=['like', 'bot'])
    response(long.R_Eating, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Testing the response system
while True:
    print('ASN Bot: ' + get_response(input('You: ')))
