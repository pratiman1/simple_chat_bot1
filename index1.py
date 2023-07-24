import re
import long_responses as long


def message_probability(user_message, recong_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # counts how many words are present in each predined message
    for word in user_message:
        if word in recong_words:
            message_certainty += 1
    # calculating the percentage of recogonside words in a user mesage
    percentage = float(message_certainty) / float(len(recong_words))

    # check that the required words are in string
    for word in required_words:
        if word in user_message:
            has_required_words = False
            break
    # must either the required word or single respone
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_message(message):
    highest_prop_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]): # simplifies respone creation / add it to the dict
        nonlocal highest_prop_list  # nonlocal is a fuction where we can use out side the fuction
        # bot_re is a key  method call message_pro
        highest_prop_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # respons 
    response('Hello', ['hello', 'hi', 'hey', ], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)       #reuired-word is used when u used strong key word
    response('I\'m doing fine and you?', ['how', 'are', 'you', 'doing'], required_words=['How'])
    response('You\'re welcome', ['thank', 'thankyou'], single_response=True)
    response('Thank you ', ['i', 'love', 'kg', 'codding'], required_words=['kg', 'coding'])

    # long response
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prop_list, key=highest_prop_list.get)
    # print(highest_prop_list)
    # print(f"best match={best_match} | score :{highest_prop_list[best_match]}")
    return long.unknown() if highest_prop_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_message(split_message)
    return response


while True:
    print('Bot: ' + get_response(input('You: ')))
